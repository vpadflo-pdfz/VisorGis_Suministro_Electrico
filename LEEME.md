# Visor GIS - Suministros eléctricos (Gran Canaria)

Mismo visor que "Abasto" con los datos de `2027_Suministros_electricos_REGCAN95` (527 puntos).

## Manual de uso
`docs/Manual_de_uso_Visor_Suministros_Electricos.pdf` (para los usuarios). Fuente editable: `docs/manual/manual.html` (+ capturas en `docs/manual/img/`).

## Abrir
- Doble clic en `index.html` (necesita internet para el mapa y la ortofoto GRAFCAN), o
- `Abrir visor.bat` (Windows): ventana propia con Edge/Chrome, sin instalar nada.
Es portable: la carpeta se puede copiar a un USB o a una carpeta de red.
Icono: rayo amarillo sobre azul (colores del Cabildo). `icono_electrico.svg` es el de los puntos y la pestaña; la ventana de `Abrir visor.bat` lo usa también.
Para un acceso directo en el Escritorio con el icono: doble clic en `Crear acceso directo.bat` (no instala nada; crea "Visor Suministros Electricos" en el Escritorio).

## Publicar en internet
Arrastra la carpeta a https://app.netlify.com/drop

## Actualizar los datos
1. Exporta la capa a shapefile y comprime `.shp .shx .dbf .prj .cpg` como `data/puntos.zip`
   (los ficheros dentro del zip pueden llamarse como quieras).
2. `python generar_puntos_js.py` (actualiza `data/puntos.js`, necesario para abrir con doble clic).

## Informe del suministro
Selecciona un punto y pulsa **Informe del suministro (datos + fotos)** en el panel lateral: se abre una hoja con los datos
y las 5 fotos. Botón **Imprimir / Guardar PDF** (elige "Guardar como PDF" en la impresora). Esc o **Cerrar** para volver al mapa.
Los nombres de los campos y los campos que no salen se cambian en `config.js` (`etiquetas`, `ocultarInforme`).

## Fotos (sin instalar nada)
El shapefile enlaza 5 fotos por punto (Vista aérea, Fachada, Armario fachada, Armario medida, Equipo medida).
El visor las lee directamente de la carpeta de red, con el MISMO nombre de archivo que figura en el shapefile
(la ruta `Z:\\...` se ignora; solo cuenta el nombre). No hay que copiar ni convertir fotos.

- Carpeta: `\\srvdatosCabildo\servInstala\06_GIS\_SUMINISTROS_ELECTRICOS\FOTOS`
- En `config.js`: `servidorFotos: "file://srvdatosCabildo/servInstala/06_GIS/_SUMINISTROS_ELECTRICOS/FOTOS/"`
- Abre el visor con `Abrir visor.bat` o doble clic en `index.html` (como archivo; hace falta tener acceso a la carpeta de red).
- Si una foto no existe, el panel muestra "No disponible". Tolera el espacio tras `_` y mayúsculas/minúsculas (Windows).
- Si publicas el visor en internet (Netlify) las fotos de red NO se verán: un navegador no deja a una web leer carpetas locales.

Alternativas (opcionales): un servidor web (`servidorFotos: "http://servidor:8081/"`; incluido `servidor_fotos.py`, requiere Python),
o carpetas `fotos/` junto al visor como en Abasto (`servidorFotos: ""`, fotos generadas con `optimizar_fotos.py`).

## Configuración
Todo en `config.js`: WMS, campos del popup, filtros, fotos, icono, logo, vista inicial.
