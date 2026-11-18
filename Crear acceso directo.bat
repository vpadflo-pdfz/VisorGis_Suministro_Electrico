@echo off
setlocal EnableExtensions
rem ---------------------------------------------------------------------------
rem  Crea en el Escritorio el acceso directo "Visor Suministros Electricos"
rem  con el icono del rayo. Doble clic y listo (no instala nada).
rem  El icono se copia a %LOCALAPPDATA% para que no dependa de la carpeta de red.
rem ---------------------------------------------------------------------------
set "DIR=%~dp0"
set "ICODIR=%LOCALAPPDATA%\VisorGIS_Suministros"
if not exist "%ICODIR%" mkdir "%ICODIR%"
copy /y "%DIR%icono_electrico.ico" "%ICODIR%\icono_electrico.ico" >nul

powershell -NoProfile -ExecutionPolicy Bypass -Command "$d=[Environment]::GetFolderPath('Desktop'); $s=(New-Object -ComObject WScript.Shell).CreateShortcut((Join-Path $d 'Visor Suministros Electricos.lnk')); $s.TargetPath=($env:DIR + 'Abrir visor.bat'); $s.WorkingDirectory=$env:DIR; $s.IconLocation=($env:ICODIR + '\icono_electrico.ico'); $s.WindowStyle=7; $s.Description='Visor GIS de suministros electricos'; $s.Save()"

if errorlevel 1 (
  echo No se pudo crear el acceso directo.
) else (
  echo Listo: acceso directo "Visor Suministros Electricos" creado en el Escritorio.
)
timeout /t 4 >nul
