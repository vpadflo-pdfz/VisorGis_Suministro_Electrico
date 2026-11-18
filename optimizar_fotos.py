#!/usr/bin/env python3
"""Reduce las fotos para la web.

Uso:
    python optimizar_fotos.py CARPETA_ORIGINAL CARPETA_DESTINO

Ejemplo (fachadas):
    python optimizar_fotos.py "C:\\GIS\\FOTOS\\FOTOS SUMINISTROS AGUA\\FOTOS FACHADAS" fotos/fachadas

Genera por cada foto:
    DESTINO/NOMBRE.jpg        (máx. 1600 px, calidad 80)  -> al ampliar
    DESTINO/mini/NOMBRE.jpg   (máx.  320 px)              -> en el popup
Solo procesa las fotos nuevas o modificadas, así que puedes volver a ejecutarlo.
Requiere:  pip install pillow
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

EXT = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".heic"}
GRANDE, MINI = 1600, 320

def procesar(src, dst, lado, calidad):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)      # respeta la rotación del móvil
        im = im.convert("RGB")
        im.thumbnail((lado, lado), Image.LANCZOS)
        im.save(dst, "JPEG", quality=calidad, optimize=True, progressive=True)

def main(origen, destino):
    origen, destino = Path(origen), Path(destino)
    (destino / "mini").mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted(origen.iterdir()):
        if f.suffix.lower() not in EXT:
            continue
        g, m = destino / (f.stem + ".jpg"), destino / "mini" / (f.stem + ".jpg")
        if g.exists() and m.exists() and g.stat().st_mtime >= f.stat().st_mtime:
            continue
        try:
            procesar(f, g, GRANDE, 80)
            procesar(f, m, MINI, 75)
            print(f"{f.name}: {f.stat().st_size/1e6:.1f} MB -> {g.stat().st_size/1e3:.0f} KB")
            n += 1
        except Exception as e:
            print(f"ERROR {f.name}: {e}")
    print(f"{n} fotos procesadas")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
