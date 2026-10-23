# Copyright (C) 2026 Anonymous
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Chimera NFT offline builder.
#
# Rebuilds Chimera-NFT-1.1.2-...-OFFLINE.eaf from the original release .eaf plus
# the runtime sources in source/chimeranft_runtime_open_source/.
#
# What the builder does:
#   1. decrypts the runtime payload from the original loader (seed = client XOR server,
#      key = HMAC-SHA256(seed, "ChimeraNFT:PAYLOAD:v3"), HMAC-CTR),
#   2. repacks the runtime zip from source/chimeranft_runtime_open_source/,
#   3. patches loader.py: plaintext payload (no server), per-build seed embedded
#      offline (_SEED_SERVER_MODE = 0, fragments/mask), new payload sha256,
#   4. verifies the result end-to-end (sha, seed, no-network payload load).
#
# Usage: python build_open.py          (from anywhere; paths are relative to the project root)

import io
import os
import re
import base64
import zipfile
import hashlib
import hmac as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "source", "chimeranft_runtime_open_source")
ORIG_EAF = os.path.join(ROOT, "builds", "Chimera NFT-1.1.2-3.11-release.eaf")
OUT_EAF = os.path.join(ROOT, "builds", "Chimera NFT-1.1.2-3.11-release-OFFLINE.eaf")

CLIENT_SHARE = bytes.fromhex("baf6bf600da16c672ae5a714954d8fab02f6d24a679ce62630126db38ae3a451")
SERVER_SHARE = bytes.fromhex("9d570471e27e77d8097bc7b478839a77c81db91ed608e933af58532cdab6c1fc")
SEED = bytes(a ^ b for a, b in zip(CLIENT_SHARE, SERVER_SHARE))
SEED_EXPECTED_HEX = SEED.hex()

RUNTIME_FILES = ["__init__.py", "legacy_gifts.py", "plugin.py", "sync_client.py", "updater.py"]


def read_loader():
    with zipfile.ZipFile(ORIG_EAF) as z:
        return z.read("chimeranft/src/loader.py").decode("utf-8", "replace")


def decrypt_original_runtime(loader, sha):
    b64 = re.search(r'_PAYLOAD_B64\s*=\s*"""(.*?)"""', loader, re.S).group(1)
    blob = base64.b64decode(b64.strip().replace("\n", ""))
    key = H.new(SEED, b"ChimeraNFT:PAYLOAD:v3", hashlib.sha256).digest()
    nonce, ct = blob[:12], blob[44:]
    plain = bytearray()
    for counter, pos in enumerate(range(0, len(ct), 32)):
        ks = H.new(key, nonce + counter.to_bytes(8, "big"), hashlib.sha256).digest()
        plain.extend(b ^ ks[j] for j, b in enumerate(ct[pos:pos + 32]))
    plain = bytes(plain)
    if hashlib.sha256(plain).hexdigest() != sha:
        raise RuntimeError("original payload decryption failed")
    return plain


def build_runtime_zip():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("chimeranft_runtime/", "")
        for name in RUNTIME_FILES:
            with open(os.path.join(SRC_DIR, name), "rb") as f:
                zf.writestr("chimeranft_runtime/" + name, f.read())
    return buf.getvalue()


def patch_loader(loader, old_sha, runtime_zip):
    b64 = base64.b64encode(runtime_zip).decode()
    new_loader = loader.replace(
        '_PAYLOAD_SHA256 = "%s"' % old_sha, '_PAYLOAD_SHA256 = "%s"' % hashlib.sha256(runtime_zip).hexdigest()
    )
    new_loader = re.sub(
        r'(_PAYLOAD_B64\s*=\s*""")(.*?)(""")',
        lambda m: m.group(1) + b64 + m.group(3),
        new_loader,
        count=1,
        flags=re.S,
    )
    # offline seed
    frag3, frag1, frag0, frag2 = (
        SEED[0:8].hex(), SEED[8:16].hex(), SEED[16:24].hex(), SEED[24:32].hex()
    )
    new_loader = new_loader.replace('_SEED_SERVER_MODE = int("1")', '_SEED_SERVER_MODE = int("0")')
    new_loader = re.sub(r'_SEED_FRAG_3 = "[0-9a-f]+"', '_SEED_FRAG_3 = "%s"' % frag3, new_loader, count=1)
    new_loader = re.sub(r'_SEED_FRAG_1 = "[0-9a-f]+"', '_SEED_FRAG_1 = "%s"' % frag1, new_loader, count=1)
    new_loader = re.sub(r'_SEED_FRAG_0 = "[0-9a-f]+"', '_SEED_FRAG_0 = "%s"' % frag0, new_loader, count=1)
    new_loader = re.sub(r'_SEED_FRAG_2 = "[0-9a-f]+"', '_SEED_FRAG_2 = "%s"' % frag2, new_loader, count=1)
    new_loader = re.sub(r'_SEED_MASK = "[0-9a-f]+"', '_SEED_MASK = "%s"' % ("00" * 32), new_loader, count=1)
    return new_loader


def verify(out_path):
    with zipfile.ZipFile(out_path) as z:
        loader = z.read("chimeranft/src/loader.py").decode("utf-8", "replace")
    dump = base64.b64decode(re.search(r'_PAYLOAD_B64\s*=\s*"""(.*?)"""', loader, re.S).group(1))
    assert hashlib.sha256(dump).hexdigest() == re.search(
        r'_PAYLOAD_SHA256\s*=\s*"([0-9a-f]{64})"', loader
    ).group(1), "payload sha mismatch"
    assert re.search(r'_SEED_SERVER_MODE = int\("0"\)', loader), "server mode not disabled"
    frags = [re.search(r'_SEED_FRAG_%s = "([0-9a-f]+)"' % x, loader).group(1) for x in (3, 1, 0, 2)]
    mask = re.search(r'_SEED_MASK = "([0-9a-f]+)"', loader).group(1)
    seed = bytes(a ^ b for a, b in zip(b"".join(bytes.fromhex(f) for f in frags), bytes.fromhex(mask)))
    assert seed == SEED, "offline seed mismatch"
    rt = zipfile.ZipFile(io.BytesIO(dump))
    assert rt.read("chimeranft_runtime/plugin.py"), "runtime missing plugin.py"
    assert '"enabled": False' in rt.read("chimeranft_runtime/plugin.py").decode("utf-8"), "sync patch lost"
    assert '_UPDATE_BASE_URL_DEFAULT = ""' in rt.read("chimeranft_runtime/updater.py").decode("utf-8"), "updater patch lost"
    return len(dump), len(frags[0]) * 4 + len(frags)


def main():
    loader = read_loader()
    old_sha = re.search(r'_PAYLOAD_SHA256\s*=\s*"([0-9a-f]{64})"', loader).group(1)
    decrypt_original_runtime(loader, old_sha)  # sanity only
    runtime_zip = build_runtime_zip()
    new_loader = patch_loader(loader, old_sha, runtime_zip)
    assert b64decode_ok(new_loader)
    with zipfile.ZipFile(ORIG_EAF) as zin, zipfile.ZipFile(OUT_EAF, "w") as out:
        for info in zin.infolist():
            data = new_loader.encode("utf-8") if info.filename == "chimeranft/src/loader.py" else zin.read(info)
            ni = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            ni.compress_type = info.compress_type
            ni.external_attr = info.external_attr
            out.writestr(ni, data)
    payload_len, frag_bytes = verify(OUT_EAF)
    print("OFFLINE build:", OUT_EAF, os.path.getsize(OUT_EAF), "bytes")
    print("runtime zip  :", payload_len, "bytes")
    print("offline seed :", SEED_EXPECTED_HEX, "(fragments", frag_bytes, "B + zeros mask)")
    print("checks       : sha OK | mode=0 | seeds OK | sync off | updater empty")


def b64decode_ok(loader):
    return re.search(r'_PAYLOAD_B64\s*=\s*"""(.*?)"""', loader, re.S) is not None


if __name__ == "__main__":
    main()
