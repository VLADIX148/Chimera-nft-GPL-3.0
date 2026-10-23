# Anonymous

Chimera NFT / eblanNFT — exteraGram plugin for managing Telegram collectible
gifts (NFT), username/fragment info cards and related utilities. Fully
deobfuscated and built offline: the runtime package is embedded as plain
base64 inside the plugin bootstrap and does not depend on any external
licensing/update server.

Licensed under **GPL-3.0-or-later** (see [LICENSE](LICENSE)).

## Layout

| Path | What |
|---|---|
| `builds/Chimera NFT-1.1.2-3.11-release.eaf` | original release archive (as shipped) |
| `builds/Chimera NFT-1.1.2-3.11-release-OPEN.eaf` | runtime embedded unencrypted |
| `builds/Chimera NFT-1.1.2-3.11-release-OFFLINE.eaf` | recommended build: no server dependency at all |
| `source/chimeranft_runtime_open_source/` | runtime sources (`plugin.py` is the entry point) |
| `source/eblannft_dex_source.py` | legacy eblanNFT source |
| `originals/eblannft_dex.plugin` | legacy plugin archive |
| `tools/build_open.py` | rebuilds the OFFLINE `.eaf` from sources |

## Rebuild

```
python tools\build_open.py
```

Edit `source/chimeranft_runtime_open_source/*.py`, then run the builder — it
repacks the runtime, re-stamps the payload SHA-256 and re-reads the offline
seed fragments into the bootstrap, producing a fresh
`builds/Chimera NFT-1.1.2-3.11-release-OFFLINE.eaf`.

## Installation

Copy any `*.eaf` build into the exteraGram plugins folder (or open it via the
plugin loader). The OFFLINE build requires no network except Telegram itself.
