# -*- coding: utf-8 -*-
"""Gera as versoes WebP da foto do bloco 'Sobre' (DSC01544, preto e branco)."""
import os
import sys

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
SRC = os.path.join(BASE, "melhores fotos", "DSC01544.jpg")
OUT = os.path.join(BASE, "public", "fotos")

WIDTHS = (480, 960, 1365)

with Image.open(SRC) as img:
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    print("origem:", w, "x", h)
    for target in WIDTHS:
        if target > w:
            continue
        nh = round(h * target / w)
        resized = img.resize((target, nh), Image.LANCZOS)
        name = f"sobre-bw-{target}.webp"
        resized.save(os.path.join(OUT, name), "WEBP", quality=82, method=6)
        print("gerado:", name, os.path.getsize(os.path.join(OUT, name)) // 1024, "KB")
