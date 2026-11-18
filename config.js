// ====== CONFIGURACIÓN: es lo único que tienes que tocar ======
const CONFIG = {
  titulo: "Suministros eléctricos",   // título de la pestaña del navegador
  logo: "logo.png",                      // archivo en esta carpeta. Vacío = sin logo
  googleApiKey: "",                      // opcional: clave Google Maps (vacío = mapa base CARTO)

  // WMS (pon aquí tu URL y capas; deja url vacío para ocultarlo)
  wms: {
    url: "https://idecan1.grafcan.es/ServicioWMS/OrtoUrb",
    capas: "OU",
    nombre: "Ortofoto urbana GRAFCAN",
    activa: true,
    formato: "image/jpeg",
    opacidad: 1
  },

  // Puntos: zip con .shp/.shx/.dbf/.prj/.cpg (se reproyecta solo a partir del .prj: REGCAN95 UTM 28N)
  puntos: "data/puntos.zip",
  iconoPuntos: "icono_electrico.svg",
  nombrePuntos: "Suministros eléctricos",
  vialesActivos: false,

  campoTitulo: "ENTIDAD",        // título del popup
  campoSubtitulo: "MUNICIPIO",   // línea bajo el título en el panel lateral

  // ORIGEN DE LAS FOTOS: carpeta (o servidor) donde están, con el MISMO nombre de archivo que figura
  // en el shapefile (la ruta Z:\\... se ignora; solo cuenta el nombre). No hay que copiar ni convertir nada.
  // Carpeta de red (sin instalar nada; abrir el visor con "Abrir visor.bat" o index.html):
  //     \\srvdatosCabildo\servInstala\06_GIS\_SUMINISTROS_ELECTRICOS\FOTOS   ->  file://srvdatosCabildo/servInstala/...
  // Servidor web: "http://servidor:8081/".  Vacío = carpetas fotos/ junto al visor (como en el visor Abasto).
  servidorFotos: "file://srvdatosCabildo/servInstala/06_GIS/_SUMINISTROS_ELECTRICOS/FOTOS/",

  // Fotos: en el shapefile solo importa el NOMBRE del archivo (la ruta Z:\... se ignora).
  // Se buscan en fotos/<NOMBRE>.jpg (y fotos/mini/<NOMBRE>.jpg) -> las genera optimizar_fotos.py
  fotos: [
    { campo: "VISTA_AER",  carpeta: "fotos/", etiqueta: "Vista aérea" },
    { campo: "FACHADA",    carpeta: "fotos/", etiqueta: "Fachada" },
    { campo: "ARM_FACH",   carpeta: "fotos/", etiqueta: "Armario en fachada" },
    { campo: "ARM_MEDIDA", carpeta: "fotos/", etiqueta: "Armario de medida" },
    { campo: "EQ_MEDIDA",  carpeta: "fotos/", etiqueta: "Equipo de medida" }
  ],

  // Campos que NO se muestran en el popup
  ocultar: ["X", "Y", "LONGITUD", "LATITUD", "COORD_UTM", "NUM_FOTOS", "GOOGLE_MAP"],

  // Nombres legibles de los campos en el informe (los que no estén aquí salen con su nombre del shapefile)
  etiquetas: {
    NUM: "Nº", ENTIDAD: "Entidad", MUNICIPIO: "Municipio", DIRECCION: "Dirección", CUPS: "CUPS",
    NUM_CONT: "Nº de contador", TIPO_CONT: "Tipo de contador", TARIFA: "Tarifa", POT_CONTR: "Potencia contratada",
    ULT_REV: "Última revisión", LOTE: "Lote", OBSERVAC: "Observaciones"
  },
  // Campos que NO salen en el informe (por defecto, los mismos de "ocultar")
  ocultarInforme: ["X", "Y", "LONGITUD", "LATITUD", "COORD_UTM", "NUM_FOTOS", "GOOGLE_MAP"],

  // Campos por los que se puede filtrar (menús desplegables)
  filtros: ["ENTIDAD", "MUNICIPIO", "TARIFA", "TIPO_CONT"],

  centro: [28.1, -15.43],
  zoom: 11,
  zoomMax: 21,
  zoomAlBuscar: 16
};
