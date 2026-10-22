@echo off
setlocal EnableExtensions EnableDelayedExpansion
echo ============================================
echo  git-gui + gitk Multilingual Pack
echo  Installing 85 language files for Git GUI
echo  and 85 language files for gitk
echo ============================================
echo.
fltmc >nul 2>&1
if errorlevel 1 (
    echo Requesting administrator privileges...
    set "SELF=%~f0"
    set "SELFARG=%~1"
    set "PSCMD=Start-Process -FilePath $env:SELF -Verb RunAs"
    if defined SELFARG set "PSCMD=Start-Process -FilePath $env:SELF -ArgumentList $env:SELFARG -Verb RunAs"
    powershell -NoProfile -ExecutionPolicy Bypass -Command "!PSCMD!"
    exit /b 0
)
title git-gui language pack installer

set "SOURCE=%~dp0msgs"
set "GITKSOURCE=%~dp0gitk\msgs"

set "HAVEGUI=0"
set "HAVEGITK=0"
dir /b "%SOURCE%\*.msg" >nul 2>&1
if not errorlevel 1 set "HAVEGUI=1"
dir /b "%GITKSOURCE%\*.msg" >nul 2>&1
if not errorlevel 1 set "HAVEGITK=1"

if "%HAVEGUI%%HAVEGITK%"=="00" (
    echo [ERROR] No message folders were found next to this script:
    echo         "%SOURCE%"
    echo         "%GITKSOURCE%"
    goto :fail
)

set "GITROOT="
set "DIRECT_TARGET="
set "INSTALLED=0"
set "WRITE_FAIL=0"

if not "%~1"=="" (
    call :resolve_target "%~1"
    if errorlevel 1 goto :fail
    if defined DIRECT_TARGET goto :install_direct
    goto :find_targets
)

rem ---------- 1) locate git.exe ----------
set "GITEXE="
for /f "delims=" %%G in ('where git 2^>nul') do (
    set "GITEXE=%%~fG"
    goto :have_git
)
:have_git
if defined GITEXE (
    call :derive_root
    if defined GITROOT goto :find_targets
)

rem ---------- 2) common locations ----------
if not defined GITROOT if exist "%ProgramFiles%\Git\cmd\git.exe" set "GITROOT=%ProgramFiles%\Git"
if not defined GITROOT if exist "%ProgramFiles%\Git\bin\git.exe" set "GITROOT=%ProgramFiles%\Git"
if not defined GITROOT if exist "%ProgramFiles%\Git\mingw64\bin\git.exe" set "GITROOT=%ProgramFiles%\Git"
if not defined GITROOT if exist "%ProgramFiles%\Git\ucrt64\bin\git.exe" set "GITROOT=%ProgramFiles%\Git"
if not defined GITROOT if exist "%ProgramFiles(x86)%\Git\cmd\git.exe" set "GITROOT=%ProgramFiles(x86)%\Git"
if not defined GITROOT if exist "%LocalAppData%\Programs\Git\cmd\git.exe" set "GITROOT=%LocalAppData%\Programs\Git"
if not defined GITROOT if exist "%USERPROFILE%\PortableGit\cmd\git.exe" set "GITROOT=%USERPROFILE%\PortableGit"
if not defined GITROOT if exist "%USERPROFILE%\scoop\apps\git\current\cmd\git.exe" set "GITROOT=%USERPROFILE%\scoop\apps\git\current"
if not defined GITROOT if exist "C:\Git\cmd\git.exe" set "GITROOT=C:\Git"
if defined GITROOT goto :find_targets

rem ---------- 3) ask the user ----------
echo.
echo Could not find Git automatically.
echo Enter the Git installation folder, for example:
echo     C:\Program Files\Git
echo     D:\PortableGit
echo.
echo Tip: you can also drag the Git folder onto this .bat file.
echo.
set /p "GITROOT=Git folder: "
if not defined GITROOT goto :fail
call :resolve_target "!GITROOT!"
if errorlevel 1 goto :fail
if defined DIRECT_TARGET goto :install_direct

:find_targets
set "INSTALLED=0"
set "GITKINSTALLED=0"
set "WRITE_FAIL=0"

if "%HAVEGUI%"=="1" (
    for %%P in (
        "ucrt64\share\git-gui\lib\msgs"
        "mingw64\share\git-gui\lib\msgs"
        "mingw32\share\git-gui\lib\msgs"
        "usr\share\git-gui\lib\msgs"
        "share\git-gui\lib\msgs"
    ) do (
        if exist "!GITROOT!\%%~P" call :install "%SOURCE%" "!GITROOT!\%%~P"
    )

    rem Some installs have lib but no msgs yet. Create it next to about.tcl.
    for %%P in (
        "ucrt64\share\git-gui\lib"
        "mingw64\share\git-gui\lib"
        "mingw32\share\git-gui\lib"
        "usr\share\git-gui\lib"
        "share\git-gui\lib"
    ) do (
        if exist "!GITROOT!\%%~P\about.tcl" if not exist "!GITROOT!\%%~P\msgs" (
            mkdir "!GITROOT!\%%~P\msgs" >nul 2>&1
            call :install "%SOURCE%" "!GITROOT!\%%~P\msgs"
        )
    )
)

if "%HAVEGITK%"=="1" (
    rem gitk ships as <prefix>\bin\gitk and reads <prefix>\share\gitk\lib\msgs.
    for %%P in ("ucrt64" "mingw64" "mingw32" "usr") do (
        if exist "!GITROOT!\%%~P\bin\gitk" (
            if not exist "!GITROOT!\%%~P\share\gitk\lib\msgs" mkdir "!GITROOT!\%%~P\share\gitk\lib\msgs" >nul 2>&1
            if exist "!GITROOT!\%%~P\share\gitk\lib\msgs" call :install "%GITKSOURCE%" "!GITROOT!\%%~P\share\gitk\lib\msgs"
        )
    )
    for %%P in ("ucrt64" "mingw64" "mingw32" "usr") do (
        if not exist "!GITROOT!\%%~P\bin\gitk" if exist "!GITROOT!\%%~P\share\gitk\lib" (
            if not exist "!GITROOT!\%%~P\share\gitk\lib\msgs" mkdir "!GITROOT!\%%~P\share\gitk\lib\msgs" >nul 2>&1
            if exist "!GITROOT!\%%~P\share\gitk\lib\msgs" call :install "%GITKSOURCE%" "!GITROOT!\%%~P\share\gitk\lib\msgs"
        )
    )
    if exist "!GITROOT!\share\gitk\lib" (
        if not exist "!GITROOT!\share\gitk\lib\msgs" mkdir "!GITROOT!\share\gitk\lib\msgs" >nul 2>&1
        if exist "!GITROOT!\share\gitk\lib\msgs" call :install "%GITKSOURCE%" "!GITROOT!\share\gitk\lib\msgs"
    )
)

if %INSTALLED%==0 if %GITKINSTALLED%==0 (
    if "%WRITE_FAIL%"=="1" (
        echo.
        echo [ERROR] Permission denied. Right-click this .bat and choose "Run as administrator".
    ) else (
        echo.
        echo [ERROR] No git-gui or gitk message folder was found under:
        echo         "!GITROOT!"
        echo.
        echo Checked:
        echo   ucrt64\share\git-gui\lib\msgs
        echo   mingw64\share\git-gui\lib\msgs
        echo   mingw32\share\git-gui\lib\msgs
        echo   usr\share\git-gui\lib\msgs
        echo   share\git-gui\lib\msgs
        echo   ucrt64\share\gitk\lib\msgs
        echo   mingw64\share\gitk\lib\msgs
        echo   mingw32\share\gitk\lib\msgs
        echo   usr\share\gitk\lib\msgs
        echo   share\gitk\lib\msgs
        echo.
        echo Drag the Git root folder onto this script, or pass it as the first argument.
    )
    goto :fail
)

echo.
echo Done. git-gui: %INSTALLED% folder^(s^), gitk: %GITKINSTALLED% folder^(s^).
echo Both tools follow the Windows display language automatically.
echo To force a language, run:  set LANG=fr  ^&^&  git gui
echo.
pause
exit /b 0

:install_direct
set "DIRECT_SOURCE=%SOURCE%"
echo "!DIRECT_TARGET!" | find /i "\gitk\lib" >nul 2>&1
if not errorlevel 1 set "DIRECT_SOURCE=%GITKSOURCE%"
call :install "%DIRECT_SOURCE%" "%DIRECT_TARGET%"
if errorlevel 1 goto :fail
echo.
echo Done. Installed into "%DIRECT_TARGET%".
pause
exit /b 0

rem ============================================================
rem :resolve_target  <folder>
rem Accepts a Git root, a ...\git-gui\lib folder, or a msgs folder.
rem ============================================================
:resolve_target
set "ROOT=%~1"
for %%R in ("%ROOT%") do set "ROOT=%%~fR"
if not exist "%ROOT%\" (
    echo [ERROR] Folder not found: "%ROOT%"
    exit /b 1
)
dir /b "%ROOT%\*.msg" >nul 2>&1
if not errorlevel 1 (
    set "DIRECT_TARGET=%ROOT%"
    exit /b 0
)
if exist "%ROOT%\about.tcl" (
    if not exist "%ROOT%\msgs" mkdir "%ROOT%\msgs" >nul 2>&1
    set "DIRECT_TARGET=%ROOT%\msgs"
    exit /b 0
)
rem A gitk lib folder: ...\share\gitk\lib  ->  ...\share\gitk\lib\msgs
echo "%ROOT%" | find /i "\gitk\lib" >nul 2>&1
if not errorlevel 1 (
    if not exist "%ROOT%\msgs" mkdir "%ROOT%\msgs" >nul 2>&1
    set "DIRECT_TARGET=%ROOT%\msgs"
    exit /b 0
)
set "GITROOT=%ROOT%"
if not exist "%GITROOT%\cmd\git.exe" if not exist "%GITROOT%\bin\git.exe" if not exist "%GITROOT%\ucrt64\bin\git.exe" if not exist "%GITROOT%\mingw64\bin\git.exe" (
    echo [WARN] git.exe was not found under "%GITROOT%".
    echo        Continuing and checking the known git-gui layouts.
)
exit /b 0

rem ============================================================
rem :derive_root  - from git --exec-path, or from where git
rem ============================================================
:derive_root
set "GITROOT="
set "EXECPATH="
for /f "delims=" %%E in ('git --exec-path 2^>nul') do set "EXECPATH=%%~E"
if defined EXECPATH (
    for %%R in ("!EXECPATH!\..\..\..") do set "CAND=%%~fR"
    if exist "!CAND!\cmd\git.exe" set "GITROOT=!CAND!"
    if exist "!CAND!\mingw64\bin\git.exe" set "GITROOT=!CAND!"
    if exist "!CAND!\ucrt64\bin\git.exe" set "GITROOT=!CAND!"
    if exist "!CAND!\usr\bin\git.exe" set "GITROOT=!CAND!"
)
if defined GITROOT exit /b 0

for %%D in ("%GITEXE%") do set "GITBIN=%%~dpD"
for %%R in ("!GITBIN!..") do set "CAND=%%~fR"
if exist "!CAND!\cmd\git.exe" (
    set "GITROOT=!CAND!"
    exit /b 0
)
for %%B in ("!CAND!") do set "CANDNAME=%%~nxB"
if /i not "!CANDNAME!"=="mingw64" if /i not "!CANDNAME!"=="ucrt64" if /i not "!CANDNAME!"=="mingw32" if /i not "!CANDNAME!"=="usr" (
    if exist "!CAND!\bin\git.exe" (
        set "GITROOT=!CAND!"
        exit /b 0
    )
)
for %%R in ("!GITBIN!..\..") do set "CAND=%%~fR"
if exist "!CAND!\cmd\git.exe" (
    set "GITROOT=!CAND!"
    exit /b 0
)
if exist "!CAND!\ucrt64\bin\git.exe" (
    set "GITROOT=!CAND!"
    exit /b 0
)
if exist "!CAND!\mingw64\bin\git.exe" (
    set "GITROOT=!CAND!"
    exit /b 0
)
exit /b 0

rem ============================================================
rem :install  <source msgs folder>  <target msgs folder>
rem ============================================================
:install
set "SRCDIR=%~1"
set "TARGET=%~2"
if not exist "%TARGET%\" (
    echo [ERROR] Target folder not found: "%TARGET%"
    exit /b 1
)

copy /y nul "%TARGET%\.write_test" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Cannot write to "%TARGET%".
    echo         Right-click this .bat and choose "Run as administrator".
    set "WRITE_FAIL=1"
    exit /b 1
)
del "%TARGET%\.write_test" >nul 2>&1

for %%B in ("%TARGET%\..") do set "PARENT=%%~fB"
set "BACKUP=%PARENT%\msgs_backup_%RANDOM%%RANDOM%"
dir /b "%TARGET%\*.msg" >nul 2>&1
if not errorlevel 1 (
    mkdir "%BACKUP%" >nul 2>&1
    xcopy "%TARGET%\*.msg" "%BACKUP%\" /y /i >nul 2>&1
    echo [BACKUP] "%BACKUP%"
)

xcopy "%SRCDIR%\*.msg" "%TARGET%\" /y /i >nul
if errorlevel 1 (
    echo [ERROR] Copy failed to "%TARGET%".
    exit /b 1
)

set "COUNT=0"
for /f %%C in ('dir /b "%TARGET%\*.msg" 2^>nul ^| find /c /v ""') do set "COUNT=%%C"
echo "!TARGET!" | find /i "\gitk\lib" >nul 2>&1
if errorlevel 1 (
    set /a INSTALLED+=1
) else (
    set /a GITKINSTALLED+=1
)
echo [OK] "%TARGET%"  -  %COUNT% .msg files
exit /b 0

:fail
echo.
echo Installation failed.
pause
exit /b 1
