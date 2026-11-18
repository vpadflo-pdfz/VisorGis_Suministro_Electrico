@echo off
setlocal EnableExtensions
rem ---------------------------------------------------------------------------
rem  Abre el visor como una APLICACION (ventana propia, sin barra de direcciones
rem  ni pestanas) usando el Edge o Chrome que ya tiene Windows. No instala nada.
rem  Funciona desde cualquier carpeta: USB, disco local o carpeta de red.
rem ---------------------------------------------------------------------------
set "P=%~dp0index.html"
set "P=%P:\=/%"
set "P=%P: =%20%"
if "%P:~0,2%"=="//" (set "URL=file:%P%") else (set "URL=file:///%P%")

for %%B in (
  "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
  "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
  "%ProgramFiles%\Google\Chrome\Application\chrome.exe"
  "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
) do (
  if exist %%B (
    start "" %%B --app="%URL%" --window-size=1400,850
    exit /b 0
  )
)

rem Sin Edge ni Chrome: se abre con el navegador predeterminado
start "" "%~dp0index.html"
