#!/usr/bin/env python3
"""Comprueba que las fotos del shapefile existen en las carpetas de fotos.

Uso:
    python comprobar_fotos.py data/puntos.zip

Lee config.js (campos y carpetas) y dice, punto por punto, qué fotos faltan
y qué fotos de las carpetas no están enlazadas a ningún punto.
"""
import io, re, struct, sys, zipfile, unicodedata
from pathlib import Path

def leer_dbf(zip_path):
    z = zipfile.ZipFile(zip_path)
    nombre = lambda ext: next(n for n in z.namelist() if n.lower().endswith(ext))
    d = z.read(nombre(".dbf"))
    try: enc = z.read(nombre(".cpg")).decode().strip() or "latin1"
    except StopIteration: enc = "latin1"
    try: "x".encode(enc)
    except LookupError: enc = "cp1252" if "1252" in enc else "latin1"
    n, hl, rl = struct.unpack("<I", d[4:8])[0], struct.unpack("<H", d[8:10])[0], struct.unpack("<H", d[10:12])[0]
    campos, o = [], 32
    while d[o] != 13:
        campos.append((d[o:o+11].split(b"\0")[0].decode(enc, "replace"), d[o+16])); o += 32
    filas = []
    for i in range(n):
        r, p, fila = d[hl+i*rl:hl+(i+1)*rl], 1, {}
        for nm, l in campos:
            fila[nm] = r[p:p+l].decode(enc, "replace").strip(); p += l
        filas.append(fila)
    return filas

def leer_config():
    c = Path(__file__).with_name("config.js").read_text(encoding="utf-8")
    titulo = re.search(r'campoTitulo:\s*"([^"]+)"', c).group(1)
    fotos = re.findall(r'campo:\s*"([^"]+)",\s*carpeta:\s*"([^"]+)"', c)
    return titulo, fotos

def clave(s):
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"\.[^.]+$", "", s.replace("\\", "/").split("/")[-1])

def main(zip_path):
    base = Path(__file__).parent
    titulo, grupos = leer_config()
    filas = leer_dbf(zip_path)
    print(f"{len(filas)} puntos\n")
    faltan = 0
    for campo, carpeta in grupos:
        dirp = base / carpeta
        existentes = {clave(f.name) for f in dirp.glob("*.jpg") if f.parent == dirp} if dirp.exists() else set()
        usadas = set()
        for i, f in enumerate(filas, 1):
            for nom in filter(None, re.split(r"[;|]", f.get(campo, ""))):
                k = clave(nom.strip()); usadas.add(k)
                if k not in existentes:
                    faltan += 1
                    print(f"FALTA  [{campo}] punto {i} ({f.get(titulo,'?')}): {nom.strip()}")
        sobran = sorted(existentes - usadas)
        print(f"\n{carpeta}: {len(existentes)} fotos en carpeta, {len(usadas)} enlazadas")
        for s in sobran: print(f"  sin enlazar: {s}")
        print()
    print("TODO OK" if not faltan else f"{faltan} fotos enlazadas que no se encuentran")

if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
