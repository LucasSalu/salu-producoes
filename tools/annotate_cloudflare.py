# -*- coding: utf-8 -*-
"""Marca na captura do painel os dois caminhos para criar o projeto Pages."""
from PIL import Image, ImageDraw, ImageFont

SRC = r"C:\Users\PC\.dsh\attachments\v1\objects\37\37910c13abb64140dda87920020af52ae3471a2d460127c299480fbdd6dd4bc8"
DST = r"C:\dev\deepseek\salu_producoes\selecao\cloudflare-passo.png"

im = Image.open(SRC).convert("RGB")
draw = ImageDraw.Draw(im)

try:
    font = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 22)
except Exception:  # noqa: BLE001
    font = ImageFont.load_default()

RED = (255, 80, 60)
WHITE = (255, 255, 255)

# 1) Menu lateral: Compute
draw.rectangle([12, 296, 240, 336], outline=RED, width=4)
draw.ellipse([10, 268, 46, 304], fill=RED)
draw.text((21, 273), "1", font=font, fill=WHITE)

# 2) Botao "Create app"
draw.rectangle([600, 682, 714, 728], outline=RED, width=4)
draw.ellipse([598, 654, 634, 690], fill=RED)
draw.text((609, 659), "2", font=font, fill=WHITE)

im.save(DST)
print("ok", DST, im.size)
