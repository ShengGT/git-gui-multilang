# git-gui + gitk 多语言包

**让 Git GUI 和 gitk 说你的语言：85 个语言/区域，Windows 一键安装。**

[English](README.md) · [发布指南](GITHUB-发布指南.md)

![License](https://img.shields.io/badge/license-GPL--2.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey)
![Locales](https://img.shields.io/badge/locales-85-brightgreen)

Git GUI（git-gui）和 gitk 自带的翻译很少。本项目为两套界面各提供 **85 个 locale 的 .msg 文件**（`msgs/` 给 Git GUI，`gitk/msgs/` 给 gitk），以及一个会自动识别新版/旧版 Git 目录的一键安装器。

适合不想改 Tcl、不想编译、也不想自己找 msgs 目录的人。

## 预览

| 简体中文 | Français | العربية |
|:---:|:---:|:---:|
| <img src="docs/screenshot-zh.png" width="280"> | <img src="docs/screenshot-fr.png" width="280"> | <img src="docs/screenshot-ar.png" width="280"> |

## 特点

- **85 个语言/区域**：81 种语言 + 中文/葡萄牙语/挪威语区域变体。
- **git-gui + gitk 双引擎**：`msgs/` 给 Git GUI，`gitk/msgs/` 给 gitk，同一个安装器一起装。
- **一键安装**：自动 UAC 提权，先备份，再复制全部 .msg。
- **新旧目录都支持**：ucrt64、mingw64、mingw32、usr、share，以及自定义 Git 路径。
- **支持拖放**：Git 根目录、msgs 目录、git-gui / gitk lib 目录都可以直接拖到 bat 上。
- **无运行时依赖**：纯 Tcl msgcat 文件，Git GUI 与 gitk 原生加载。
- **自动质量检查**：占位符、Tcl 转义、脚本混入、往返解析。

## 安装

**先看 [INSTALL.md](INSTALL.md)，有 12 种语言的安装说明：** English · 简体中文 · 繁體中文 · Español · Français · Deutsch · Português · Русский · 日本語 · 한국어 · العربية · हिन्दी

1. 下载 Release 里的压缩包并解压，不要在压缩包里直接运行。
2. 双击 **install-all-languages.bat**，Windows 询问时点“是”。
3. 重新打开 Git GUI 和 gitk，它们会跟随 Windows 显示语言。


如果 UAC 被拒绝，右键 bat，选择“以管理员身份运行”。

支持路径：

| 版本 | 目录 |
|---|---|
| Git for Windows 2.4x+（UCRT64） | ucrt64\share\git-gui\lib\msgs |
| 旧版 Git for Windows（MinGW-w64） | mingw64\share\git-gui\lib\msgs |
| 旧版 32 位 Git | mingw32\share\git-gui\lib\msgs |
| MSYS2 | usr\share\git-gui\lib\msgs |
| 自定义/便携版 | <Git 根目录>\...\share\git-gui\lib\msgs |

gitk 使用同样的规则，只是目录名换成 `gitk`：

| 版本 | 目录 |
|---|---|
| Git for Windows 2.4x+（UCRT64） | ucrt64\share\gitk\lib\msgs |
| 旧版 Git for Windows（MinGW-w64） | mingw64\share\gitk\lib\msgs |
| 旧版 32 位 Git | mingw32\share\gitk\lib\msgs |
| MSYS2 | usr\share\gitk\lib\msgs |

gitk 只从 `<前缀>\share\gitk\lib\msgs` 读取译文（`<前缀>` 是 `bin\gitk` 的上一级）。目录不存在时安装器会自动创建。

每次安装会在目标旁边创建 msgs_backup_<随机数>（git-gui 与 gitk 各自备份）。

## 强制语言

默认跟随 Windows 显示语言。测试或强制：

    set LANG=fr
    git gui

Git Bash：

    LANG=fr git gui

完整 git-gui 语言列表见 [语言覆盖与质量.md](语言覆盖与质量.md)，逐语言加载结果见 [语言加载验证.md](语言加载验证.md)，gitk 进度见 [gitk/translation-status.md](gitk/translation-status.md)。

## gitk 翻译

gitk 与 Git GUI 是两套独立的 msgcat 目录，本仓库同时提供：

    gitk/source_strings.json     从 gitk 源码抽取的 316 条原文（按索引）
    gitk/translations/xx.json    每种语言的译文表（索引 -> 译文）
    gitk/msgs/xx.msg             生成的 Tcl msgcat 目录文件
    gitk/translation-status.md   逐语言进度表

进度：**85/85 全部完成**，每种语言 316/316 条。简体中文（zh_cn）逐条人工翻译；繁体中文（zh_tw、zh_hk）由 OpenCC 从 zh_cn 派生；新加坡中文（zh_sg）复用 zh_cn；其余 81 种为 AI 逐条翻译并保持 316 条完整覆盖。修改译文只需编辑 `gitk/translations/xx.json` 后执行：

    python tools/build_gitk_msgs.py build xx

未翻译的条目在生成的 .msg 中以 `##` 注释保留，方便逐条补全。

## 质量

- 官方人工：14 种
- DeepL + 术语表：27 种
- Bing + 术语表：40 种
- 区域变体：4 种
- gitk：85/85 全部完成（316/316 条）；中文 4 种为人工/OpenCC 派生，其余 81 种为 AI 逐条翻译

低资源语言（my、lo、yo 等）仍有机翻痕迹，欢迎母语者提交修正。

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

GPL-2.0。翻译文件来自 git-gui / Git 翻译源，遵循 GPL-2.0。

## 致谢

git-gui 与 Git 上游译者、Git for Windows、DeepL、Microsoft Bing，以及所有帮忙校对语言的人。
