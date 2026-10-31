# -*- coding: utf-8 -*-
"""Gera a imagem de compartilhamento (Open Graph) 1200x630 a partir da foto do hero."""
import os

from PIL import Image, ImageOps

BASE = r"C:\dev\deepseek\salu_producoes"
SRC = os.path.join(BASE, "public", "fotos", "070-1600.webp")
DST = os.path.join(BASE, "public", "og-image.jpg")

with Image.open(SRC) as im:
    im = im.convert("RGB")
    og = ImageOps.fit(im, (1200, 630), Image.LANCZOS)
    og.save(DST, quality=88, optimize=True, progressive=True)

print("OG gerado:", DST, os.path.getsize(DST) // 1024, "KB")
