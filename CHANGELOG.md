# Changelog

## 1.1.0 — 2026-10-22

- Added gitk catalogs (`gitk/msgs/`, 85 files, 316 strings each).
- Source strings are extracted from the installed gitk script, so catalogs track the current version.
- Rebuilt Simplified Chinese from the legacy hand-made file: 40 new strings added, 41 obsolete ones dropped.
- Traditional Chinese (zh_tw, zh_hk) derived from zh_cn; Singapore Chinese (zh_sg) reuses zh_cn.
- New gitk translations: ja, ko, de, fr, es, it, nl, pl, pt_br, pt, ru, tr, vi.
- Completed the remaining 68 locales, so all 85 catalogs now carry 316/316 strings.
- pt_pt derived from pt_br, sr_latn transliterated from sr, no derived from nb, hr derived from sr_latn.
- Installer now installs gitk catalogs into `<prefix>\share\gitk\lib\msgs` for ucrt64, mingw64, mingw32 and usr, creating the folder when needed; it also handles the root-level share layout.
- New tooling: `tools/po_tools.py`, `tools/build_gitk_msgs.py`, `tools/derive_zh.py`, `tools/init_gitk_tables.py`.
- Added `gitk/translation-status.md` progress table.

## 1.0.0 — 2026-10-20

- First public release.
- 85 locales: 81 languages plus 4 regional variants.
- One-click Windows installer with UAC elevation and backup.
- Auto-detects ucrt64, mingw64, mingw32, usr and custom Git roots.
- Fixed legacy CMD parsing and path-detection bugs.
- Single universal installer: install-all-languages.bat.
- Legacy Chinese-named aliases removed.
- Verified all 85 locales through Tcl msgcat.
- Screenshots for Simplified Chinese, French and Arabic.
