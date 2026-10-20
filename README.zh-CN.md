# git-gui 多语言包

**让 Git GUI 说你的语言：85 个语言/区域，Windows 一键安装。**

[English](README.md) · [发布指南](GITHUB-发布指南.md)

![License](https://img.shields.io/badge/license-GPL--2.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey)
![Locales](https://img.shields.io/badge/locales-85-brightgreen)

Git GUI（git-gui）自带的翻译很少。本项目提供 **85 个 locale 的 .msg 文件**，以及一个会自动识别新版/旧版 Git 目录的一键安装器。

适合不想改 Tcl、不想编译、也不想自己找 msgs 目录的人。

## 预览

| 简体中文 | Français | العربية |
|:---:|:---:|:---:|
| <img src="docs/screenshot-zh.png" width="280"> | <img src="docs/screenshot-fr.png" width="280"> | <img src="docs/screenshot-ar.png" width="280"> |

## 特点

- **85 个语言/区域**：81 种语言 + 中文/葡萄牙语/挪威语区域变体。
- **一键安装**：自动 UAC 提权，先备份，再复制全部 .msg。
- **新旧目录都支持**：ucrt64、mingw64、mingw32、usr、share，以及自定义 Git 路径。
- **支持拖放**：Git 根目录、msgs 目录、git-gui lib 目录都可以直接拖到 bat 上。
- **无运行时依赖**：纯 Tcl msgcat 文件，git-gui 原生加载。
- **自动质量检查**：占位符、Tcl 转义、脚本混入、往返解析。

## 安装

**先看 [INSTALL.md](INSTALL.md)，有 12 种语言的安装说明：** English · 简体中文 · 繁體中文 · Español · Français · Deutsch · Português · Русский · 日本語 · 한국어 · العربية · हिन्दी

1. 下载 Release 里的压缩包并解压，不要在压缩包里直接运行。
2. 双击 **install-all-languages.bat**，Windows 询问时点“是”。
3. 重新打开 Git GUI，它会跟随 Windows 显示语言。

**安装所有语言.bat** 只是同一个安装器的中文别名。

如果 UAC 被拒绝，右键 bat，选择“以管理员身份运行”。

支持路径：

| 版本 | 目录 |
|---|---|
| Git for Windows 2.4x+（UCRT64） | ucrt64\share\git-gui\lib\msgs |
| 旧版 Git for Windows（MinGW-w64） | mingw64\share\git-gui\lib\msgs |
| 旧版 32 位 Git | mingw32\share\git-gui\lib\msgs |
| MSYS2 | usr\share\git-gui\lib\msgs |
| 自定义/便携版 | <Git 根目录>\...\share\git-gui\lib\msgs |

每次安装会在目标旁边创建 msgs_backup_<随机数>。

## 强制语言

默认跟随 Windows 显示语言。测试或强制：

    set LANG=fr
    git gui

Git Bash：

    LANG=fr git gui

完整语言列表见 [语言覆盖与质量.md](语言覆盖与质量.md)，逐语言加载结果见 [语言加载验证.md](语言加载验证.md)。

## 质量

- 官方人工：14 种
- DeepL + 术语表：27 种
- Bing + 术语表：40 种
- 区域变体：4 种

低资源语言（my、lo、yo 等）仍有机翻痕迹，欢迎母语者提交修正。

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

GPL-2.0。翻译文件来自 git-gui / Git 翻译源，遵循 GPL-2.0。

## 致谢

git-gui 与 Git 上游译者、Git for Windows、DeepL、Microsoft Bing，以及所有帮忙校对语言的人。
