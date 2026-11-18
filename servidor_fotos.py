#!/usr/bin/env python3
"""Servidor local de fotos para el visor.

Sirve una carpeta con las fotos tal cual (mismo nombre que en el shapefile).
No distingue mayusculas/minusculas ni el espacio tras "_" en los nombres.

Uso:
    python servidor_fotos.py "RUTA\\FOTOS" [puerto]      (puerto por defecto: 8081)
Ejemplo:
    python servidor_fotos.py "\\\\srvdatosCabildo\\servInstala\\06_GIS\\_SUMINISTROS_ELECTRICOS\\FOTOS"

Luego, en config.js:  servidorFotos: "http://localhost:8081/"
(si lo ejecutas en otro equipo de la red: "http://NOMBRE-O-IP:8081/")
"""
import sys, os, re, urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

RAIZ = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "fotos")
PUERTO = int(sys.argv[2]) if len(sys.argv) > 2 else 8081
clave = lambda s: re.sub(r"_\s+", "_", s).lower()
indice = {}

def indexar():
    indice.clear()
    for n in os.listdir(RAIZ):
        indice.setdefault(clave(n), n)

class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=RAIZ, **k)
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")   # el visor se abre desde file:// u otro sitio
        self.send_header("Cache-Control", "max-age=300")
        super().end_headers()
    def translate_path(self, path):
        n = urllib.parse.unquote(urllib.parse.urlsplit(path).path).lstrip("/")
        if n and not os.path.exists(os.path.join(RAIZ, n)):
            if clave(n) not in indice: indexar()
            n = indice.get(clave(n), n)
        return os.path.join(RAIZ, n)
    def list_directory(self, path):
        self.send_error(403)   # sin listado de carpeta
    def log_message(self, f, *a): pass

if __name__ == "__main__":
    if not os.path.isdir(RAIZ): sys.exit("No existe la carpeta: " + RAIZ)
    indexar()
    print(f"Sirviendo {len(indice)} archivos de {RAIZ}\nhttp://localhost:{PUERTO}/   (Ctrl+C para parar)")
    ThreadingHTTPServer(("0.0.0.0", PUERTO), H).serve_forever()
