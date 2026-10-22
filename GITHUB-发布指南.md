# 发布到 GitHub：名称、描述与步骤

本仓库当前是 **git-gui + gitk 多语言包 v1.1.0**：git-gui 和 gitk 各 85 个 locale，共 170 个 `.msg` 文件，安装器一次装好两套。

## 1. 当前仓库信息

- 仓库：<https://github.com/ShengGT/git-gui-multilang>
- 默认分支：`main`
- 安装入口：`install-all-languages.bat`（唯一安装器，旧的 `汉化脚本.bat` 已移除）
- 发布包：`git-gui-multilang-v1.1.0.zip`
- 目标 tag：`v1.1.0`
- 许可证：GPL-2.0

## 2. About 描述（直接粘贴）

英文（推荐）：

    85-language localization pack for Git GUI (git-gui) and gitk on Windows. One-click installer, auto-detects ucrt64/mingw64 paths, backups included. 85 locales for each tool.

中文：

    Git GUI（git-gui）与 gitk 85 语言本地化包。Windows 一键安装，自动识别 ucrt64/mingw64 目录，安装前备份；两套界面各 85 个语言文件。

## 3. Topics（标签）

复制到 GitHub 仓库的 Topics：

    git
    git-gui
    gitk
    git-gui-localization
    localization
    i18n
    translation
    multilingual
    language-pack
    windows
    tcl
    msgcat

## 4. v1.1.0 Release 模板

Tag：`v1.1.0`

Title：`v1.1.0 — gitk catalogs, 85 locales for Git GUI and gitk`

Notes：

    Second public release.

    - Added gitk catalogs: 85 locales, 316 of 316 strings each
    - Git GUI catalogs remain at 85 locales, 608 strings each
    - One installer installs both: msgs/ for git-gui, gitk/msgs/ for gitk
    - Installer creates <prefix>\share\gitk\lib\msgs and backs up old catalogs
    - Supports ucrt64, mingw64, mingw32, usr, share and custom Git roots
    - Rebuilt Simplified Chinese gitk catalog from the legacy hand-made file
    - Traditional Chinese (zh_tw, zh_hk) derived from zh_cn; Singapore Chinese (zh_sg) reuses zh_cn
    - Added build/validate tooling: tools/po_tools.py, tools/build_gitk_msgs.py, tools/validate_gitk.py
    - INSTALL.md updated for the combined installer

    Assets: attach git-gui-multilang-v1.1.0.zip

## 5. 发布步骤

1. 在本地确认安装器可用：双击 `install-all-languages.bat`，应显示 git-gui 与 gitk 各安装了多少个目录。
2. 提交并推送代码：

       git add .
       git commit -m "Release v1.1.0: gitk catalogs for 85 locales"
       git push origin main

3. 创建并推送 tag：

       git tag -a v1.1.0 -m "v1.1.0: gitk catalogs, 85 locales"
       git push origin v1.1.0

4. 打开 GitHub 仓库 → **Releases** → **Draft a new release**：
   - 选择 tag `v1.1.0`；
   - Title 和 Notes 用上面的模板；
   - 上传 `git-gui-multilang-v1.1.0.zip` 作为附件；
   - 发布。

5. 在 **Settings → Social preview** 上传 `docs/screenshot-zh.png` 或 `docs/screenshot-fr.png`。

## 6. 发布包里放什么

只放用户运行所需文件，不要把开发脚本和缓存打进去：

    msgs/                        85 个 git-gui .msg
    gitk/msgs/                   85 个 gitk .msg
    install-all-languages.bat    唯一安装器
    INSTALL.md                   12 语言安装说明
    README.md / README.zh-CN.md
    CHANGELOG.md
    LICENSE
    CONTRIBUTING.md
    语言覆盖与质量.md
    语言加载验证.md
    docs/                        截图

`tools/`、`gitk/translations/`、`gitk/source_strings.json` 留在 Git 仓库里供维护者使用，不必放进发布包。

## 7. 注意事项

- 通过 SSH 只能 push 代码和 tag，**不能上传 Release 附件**。上传附件要么用浏览器，要么配置 `GH_TOKEN` 后用 GitHub API。
- `.gitignore` 已忽略 `*.zip`、`work/`、`msgs_backup_*/`、`__pycache__/`，发布包不会误提交。
- 发布前跑一遍 `python tools/validate_gitk.py`，应为 `85 catalogs checked, 0 problem(s)`。
- 安装器会修改 `C:\Program Files\Git`，测试前先确认已有备份；真实安装会生成 `msgs_backup_<随机数>`。
- 翻译文件来自 git-gui / Git 上游 GPL-2.0 翻译源，仓库保持 GPL-2.0。
