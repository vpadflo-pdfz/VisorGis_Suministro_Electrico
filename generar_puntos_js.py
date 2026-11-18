#!/usr/bin/env python3
"""Genera data/puntos.js a partir de data/puntos.zip.

Sirve para que el visor funcione también abriendo index.html con doble clic
(sin servidor). Ejecútalo cada vez que cambies data/puntos.zip:

    python generar_puntos_js.py
"""
import base64
from pathlib import Path
d = Path(__file__).parent / "data"
b64 = base64.b64encode((d / "puntos.zip").read_bytes()).decode()
(d / "puntos.js").write_text(f'window.PUNTOS_B64="{b64}";\n', encoding="ascii")
print(f"data/puntos.js generado ({len(b64)//1024} KB)")
