@echo off
rem Arranca el servidor local de fotos. Cambia la ruta por la carpeta con las fotos.
set "FOTOS=Z:\06_GIS\_SUMINISTROS_ELECTRICOS\FOTOS"
if not "%~1"=="" set "FOTOS=%~1"
cd /d "%~dp0"
python servidor_fotos.py "%FOTOS%" 8081
pause
