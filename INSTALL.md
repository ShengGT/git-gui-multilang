# How to install / 安装方法 / Instalación

**Choose your language / 选择语言 / Elige tu idioma:**

[English](#english) · [简体中文](#简体中文) · [繁體中文](#繁體中文) · [Español](#español) · [Français](#français) · [Deutsch](#deutsch) · [Português](#português) · [Русский](#русский) · [日本語](#日本語) · [한국어](#한국어) · [العربية](#العربية) · [हिन्दी](#हिन्दी)

The installer copies 85 language files into your Git GUI folder, makes a backup first, and asks for administrator rights only because Git is usually installed under C:\Program Files.

安装器会把 85 个语言文件复制到 Git GUI 目录，先备份，再提权；提权只是因为 Git 通常装在 C:\Program Files。

---

## English

1. Download the latest release ZIP: **git-gui-多语言包.zip**.
2. Extract it. Do not run the .bat from inside the ZIP.
3. Double-click **install-all-languages.bat**. Click **Yes** when Windows asks for administrator rights.
4. Restart Git GUI. It follows your Windows display language automatically.

The installer finds Git by itself, supports ucrt64 / mingw64 / mingw32 / usr and custom folders, and creates a backup before copying.

To force a language:

    set LANG=fr
    git gui

If it fails:

- UAC denied: right-click the .bat and choose **Run as administrator**.
- Git not found: drag the Git root folder onto the .bat.
- Still English: check that ...\git-gui\lib\msgs contains 85 .msg files.

---

## 简体中文

1. 下载 Release 里的 **git-gui-多语言包.zip**。
2. 解压。不要在压缩包里直接双击运行。
3. 双击 **install-all-languages.bat**，Windows 询问时点 **“是”**。
4. 重新打开 Git GUI，默认跟随 Windows 显示语言。

安装器会自动找 Git，支持 ucrt64 / mingw64 / mingw32 / usr 和自定义目录，复制前会备份。

强制指定语言：

    set LANG=fr
    git gui

失败时：

- UAC 被拒绝：右键 bat，选择 **以管理员身份运行**。
- 找不到 Git：把 Git 根目录拖到 bat 上。
- 仍是英文：检查 ...\git-gui\lib\msgs 是否有 85 个 .msg 文件。

---

## 繁體中文

1. 下載 Release 裡的 **git-gui-多語言包.zip**。
2. 解壓縮。不要在壓縮檔裡直接執行。
3. 雙擊 **install-all-languages.bat**，Windows 詢問時按 **「是」**。
4. 重新開啟 Git GUI，預設跟隨 Windows 顯示語言。

安裝器會自動尋找 Git，支援 ucrt64 / mingw64 / mingw32 / usr 與自訂資料夾，複製前會備份。

強制指定語言：

    set LANG=zh_TW
    git gui

失敗時：

- UAC 被拒絕：右鍵 bat，選擇 **以系統管理員身分執行**。
- 找不到 Git：把 Git 根目錄拖到 bat 上。
- 仍是英文：檢查 ...\git-gui\lib\msgs 是否有 85 個 .msg 檔案。

---

## Español

1. Descarga el ZIP de la última release: **git-gui-多语言包.zip**.
2. Extráelo. No ejecutes el .bat desde dentro del ZIP.
3. Haz doble clic en **install-all-languages.bat**. Pulsa **Sí** cuando Windows pida permisos de administrador.
4. Reinicia Git GUI. Usará automáticamente el idioma de Windows.

El instalador encuentra Git solo, admite ucrt64 / mingw64 / mingw32 / usr y carpetas personalizadas, y crea una copia de seguridad antes de copiar.

Para forzar un idioma:

    set LANG=es
    git gui

Si falla:

- UAC denegado: clic derecho en el .bat y elige **Ejecutar como administrador**.
- No encuentra Git: arrastra la carpeta raíz de Git sobre el .bat.
- Sigue en inglés: comprueba que ...\git-gui\lib\msgs tenga 85 archivos .msg.

---

## Français

1. Téléchargez le ZIP de la dernière release : **git-gui-多语言包.zip**.
2. Extrayez-le. Ne lancez pas le .bat depuis l'intérieur du ZIP.
3. Double-cliquez sur **install-all-languages.bat**. Cliquez sur **Oui** quand Windows demande les droits d'administrateur.
4. Redémarrez Git GUI. Il suit automatiquement la langue d'affichage de Windows.

L'installateur trouve Git tout seul, gère ucrt64 / mingw64 / mingw32 / usr et les dossiers personnalisés, et crée une sauvegarde avant de copier.

Pour forcer une langue :

    set LANG=fr
    git gui

En cas d'échec :

- UAC refusé : clic droit sur le .bat, puis **Exécuter en tant qu'administrateur**.
- Git introuvable : glissez le dossier racine de Git sur le .bat.
- Toujours en anglais : vérifiez que ...\git-gui\lib\msgs contient 85 fichiers .msg.

---

## Deutsch

1. Lade das ZIP der neuesten Release herunter: **git-gui-多语言包.zip**.
2. Entpacke es. Starte die .bat nicht direkt aus dem ZIP.
3. Doppelklicke auf **install-all-languages.bat**. Klicke auf **Ja**, wenn Windows Administratorrechte anfragt.
4. Starte Git GUI neu. Es übernimmt automatisch die Windows-Anzeigesprache.

Der Installer findet Git selbst, unterstützt ucrt64 / mingw64 / mingw32 / usr und eigene Ordner und legt vor dem Kopieren eine Sicherung an.

Sprache erzwingen:

    set LANG=de
    git gui

Wenn es nicht klappt:

- UAC abgelehnt: Rechtsklick auf die .bat, dann **Als Administrator ausführen**.
- Git nicht gefunden: den Git-Stammordner auf die .bat ziehen.
- Immer noch Englisch: prüfe, ob ...\git-gui\lib\msgs 85 .msg-Dateien enthält.

---

## Português

1. Baixe o ZIP da release mais recente: **git-gui-多语言包.zip**.
2. Extraia. Não execute o .bat de dentro do ZIP.
3. Dê um duplo clique em **install-all-languages.bat**. Clique em **Sim** quando o Windows pedir permissões de administrador.
4. Reinicie o Git GUI. Ele segue automaticamente o idioma do Windows.

O instalador encontra o Git sozinho, suporta ucrt64 / mingw64 / mingw32 / usr e pastas personalizadas, e cria um backup antes de copiar.

Para forçar um idioma:

    set LANG=pt_BR
    git gui

Se falhar:

- UAC negado: clique com o botão direito no .bat e escolha **Executar como administrador**.
- Git não encontrado: arraste a pasta raiz do Git para o .bat.
- Continua em inglês: verifique se ...\git-gui\lib\msgs tem 85 arquivos .msg.

---

## Русский

1. Скачайте ZIP последнего релиза: **git-gui-多语言包.zip**.
2. Распакуйте. Не запускайте .bat изнутри ZIP.
3. Дважды щёлкните **install-all-languages.bat**. Нажмите **Да**, когда Windows запросит права администратора.
4. Перезапустите Git GUI. Он автоматически использует язык Windows.

Установщик сам находит Git, поддерживает ucrt64 / mingw64 / mingw32 / usr и произвольные папки, создаёт резервную копию перед копированием.

Принудительно задать язык:

    set LANG=ru
    git gui

Если не получилось:

- UAC отклонён: щёлкните .bat правой кнопкой и выберите **Запуск от имени администратора**.
- Git не найден: перетащите корневую папку Git на .bat.
- Остаётся английский: проверьте, что в ...\git-gui\lib\msgs есть 85 файлов .msg.

---

## 日本語

1. 最新リリースの **git-gui-多语言包.zip** をダウンロードします。
2. 解凍します。ZIP の中から .bat を直接実行しないでください。
3. **install-all-languages.bat** をダブルクリックします。Windows の管理者権限の確認では **「はい」** を選びます。
4. Git GUI を再起動します。Windows の表示言語が自動で使われます。

インストーラーは Git を自動検出し、ucrt64 / mingw64 / mingw32 / usr とカスタムフォルダーに対応します。コピー前にバックアップも作成します。

言語を強制する場合：

    set LANG=ja
    git gui

うまくいかない場合：

- UAC を拒否した：.bat を右クリックして **管理者として実行**。
- Git が見つからない：Git のルートフォルダーを .bat にドラッグ。
- 英語のまま：...\git-gui\lib\msgs に 85 個の .msg ファイルがあるか確認。

---

## 한국어

1. 최신 릴리스의 **git-gui-多语言包.zip**을 다운로드합니다.
2. 압축을 풉니다. ZIP 안에서 .bat을 직접 실행하지 마세요.
3. **install-all-languages.bat**을 더블클릭합니다. Windows가 관리자 권한을 물으면 **예**를 선택합니다.
4. Git GUI를 다시 시작합니다. Windows 표시 언어를 자동으로 따릅니다.

설치 프로그램은 Git을 자동으로 찾고 ucrt64 / mingw64 / mingw32 / usr 및 사용자 지정 폴더를 지원하며, 복사 전에 백업을 만듭니다.

언어를 강제로 지정하려면:

    set LANG=ko
    git gui

실패할 경우:

- UAC를 거부한 경우: .bat을 마우스 오른쪽 버튼으로 클릭하고 **관리자 권한으로 실행**을 선택합니다.
- Git을 찾지 못하는 경우: Git 루트 폴더를 .bat 위로 끌어다 놓습니다.
- 계속 영어로 나오는 경우: ...\git-gui\lib\msgs에 85개의 .msg 파일이 있는지 확인합니다.

---

## العربية

1. نزّل ملف ZIP من أحدث إصدار: **git-gui-多语言包.zip**.
2. استخرجه. لا تشغّل ملف .bat من داخل ZIP.
3. انقر نقرًا مزدوجًا على **install-all-languages.bat**. اختر **نعم** عندما يطلب Windows صلاحيات المسؤول.
4. أعد تشغيل Git GUI. سيستخدم لغة عرض Windows تلقائيًا.

يبحث المثبّت عن Git بنفسه، ويدعم ucrt64 / mingw64 / mingw32 / usr والمجلدات المخصصة، وينشئ نسخة احتياطية قبل النسخ.

لفرض لغة معينة:

    set LANG=ar
    git gui

إذا فشل التثبيت:

- رفضت UAC: انقر بزر الفأرة الأيمن على ملف .bat واختر **التشغيل كمسؤول**.
- لم يتم العثور على Git: اسحب مجلد Git الجذر إلى ملف .bat.
- ما زال بالإنجليزية: تحقق من وجود 85 ملف .msg داخل ...\git-gui\lib\msgs.

---

## हिन्दी

1. नवीनतम रिलीज़ की **git-gui-多语言包.zip** डाउनलोड करें।
2. इसे एक्सट्रैक्ट करें। ZIP के अंदर से .bat न चलाएँ।
3. **install-all-languages.bat** पर डबल-क्लिक करें। Windows प्रशासक अधिकार माँगे तो **हाँ** चुनें।
4. Git GUI को फिर से खोलें। यह Windows की डिस्प्ले भाषा अपने आप ले लेगा।

इंस्टॉलर Git को स्वयं ढूँढता है, ucrt64 / mingw64 / mingw32 / usr और कस्टम फ़ोल्डर सपोर्ट करता है, और कॉपी करने से पहले बैकअप बनाता है।

भाषा ज़बरदस्ती चुनने के लिए:

    set LANG=hi
    git gui

अगर काम न करे:

- UAC अस्वीकार हुआ: .bat पर राइट-क्लिक करें और **Run as administrator** चुनें।
- Git नहीं मिला: Git का रूट फ़ोल्डर .bat पर खींचकर छोड़ें।
- अंग्रेज़ी ही दिख रही है: जाँचें कि ...\git-gui\lib\msgs में 85 .msg फ़ाइलें हैं।

---

## Need help?

Open an issue with:

- your Windows version;
- your Git version (git --version);
- the exact path of your msgs folder;
- a screenshot of the installer window.

帮助 / Ayuda / Aide / Hilfe / Ajuda / Помощь / ヘルプ / 도움말 / مساعدة / सहायता
