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

## Fotos desde un servidor local
El shapefile enlaza 5 fotos por punto (Vista aérea, Fachada, Armario fachada, Armario medida, Equipo medida).
El visor las pide a un servidor con el MISMO nombre de archivo que figura en el shapefile
(la ruta `Z:\\...` se ignora; solo cuenta el nombre, con su extensión).

1. Arranca el servidor con la carpeta de fotos (necesita Python):
       python servidor_fotos.py "Z:\06_GIS\_SUMINISTROS_ELECTRICOS\FOTOS" 8081
   o doble clic en `Servidor fotos.bat` (edita la ruta dentro).
2. En `config.js`: `servidorFotos: "http://localhost:8081/"`
   (si el servidor está en otro equipo de la red: `"http://NOMBRE-O-IP:8081/"`).
3. Abre el visor. Si una foto no existe, el panel muestra "No disponible".

- El servidor no distingue mayúsculas/minúsculas ni el espacio tras `_` (`_ Armario_fachada` = `_Armario_fachada`).
- Sirve cualquier servidor web (IIS, nginx...) que exponga la carpeta con cabecera CORS `Access-Control-Allow-Origin: *`.
- Si publicas el visor en https (Netlify), el navegador bloquea fotos de un servidor http que no sea localhost.
  Para uso en red local, abre el visor con `Abrir visor.bat` / `index.html`.
- Sin servidor: deja `servidorFotos: ""` y usa carpetas (`fotos/`) generadas con `optimizar_fotos.py`.

## Configuración
Todo en `config.js`: WMS, campos del popup, filtros, fotos, icono, logo, vista inicial.
