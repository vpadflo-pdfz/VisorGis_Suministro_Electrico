# Visor GIS - Suministros eléctricos (Gran Canaria)

Mismo visor que "Abasto" con los datos de `2027_Suministros_electricos_REGCAN95` (527 puntos).

## Abrir
- Doble clic en `index.html` (necesita internet para el mapa y la ortofoto GRAFCAN), o
- `Abrir visor.bat` (Windows): ventana propia con Edge/Chrome, sin instalar nada.
Es portable: la carpeta se puede copiar a un USB o a una carpeta de red.

## Publicar en internet
Arrastra la carpeta a https://app.netlify.com/drop

## Actualizar los datos
1. Exporta la capa a shapefile y comprime `.shp .shx .dbf .prj .cpg` como `data/puntos.zip`
   (los ficheros dentro del zip pueden llamarse como quieras).
2. `python generar_puntos_js.py` (actualiza `data/puntos.js`, necesario para abrir con doble clic).

## Fotos (opcional)
El shapefile enlaza 5 fotos por punto (Vista aérea, Fachada, Armario fachada, Armario medida, Equipo medida).
Las fotos NO están incluidas: mientras no existan, el panel muestra "No disponible".
    pip install pillow
    python optimizar_fotos.py "RUTA\FOTOS" fotos
    python comprobar_fotos.py data/puntos.zip

## Configuración
Todo en `config.js`: WMS, campos del popup, filtros, fotos, icono, logo, vista inicial.
