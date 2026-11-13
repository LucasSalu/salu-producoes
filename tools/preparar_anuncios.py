# -*- coding: utf-8 -*-
"""Prepara os criativos da Meta nos formatos de feed (1080x1350) e story (1080x1920)."""
import os
import sys

from PIL import Image, ImageFilter, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
OUT = os.path.join(BASE, "selecao", "anuncios")
os.makedirs(OUT, exist_ok=True)

ARTES = {
    "arte1": r"C:\Users\PC\.dsh\attachments\v1\objects\95\95e2384c934b5a8260edbd3b8ee0264d609c27ac0b9dff58b8e3cdc86a545e79",
    "arte2": r"C:\Users\PC\.dsh\attachments\v1\objects\19\19ab1eca9d267186dfb6c3c87e19f5f8125062bce5e21defe91484e27ce9479d",
}


def compose(src: str, w: int, h: int, dst: str) -> None:
    im = Image.open(src).convert("RGB")
    ratio_src = im.width / im.height
    ratio_dst = w / h

    if abs(ratio_src - ratio_dst) < 0.02:
        # proporção praticamente igual: só recorta/preenche
        out = ImageOps.fit(im, (w, h), Image.LANCZOS)
    else:
        # fundo desfocado preenchendo a tela
        bg = ImageOps.fit(im, (w, h), Image.LANCZOS)
        bg = bg.filter(ImageFilter.GaussianBlur(48))
        dark = Image.new("RGB", (w, h), (10, 10, 11))
        bg = Image.blend(bg, dark, 0.55)

        fg = im.copy()
        fg.thumbnail((w, h), Image.LANCZOS)
        x = (w - fg.width) // 2
        y = (h - fg.height) // 2
        bg.paste(fg, (x, y))
        out = bg

    out.save(dst, "PNG", optimize=True)
    print(os.path.basename(dst), "->", out.size, os.path.getsize(dst) // 1024, "KB")


for nome, caminho in ARTES.items():
    if not os.path.exists(caminho):
        print("FALTANDO:", caminho)
        continue
    im = Image.open(caminho)
    print(nome, "origem:", im.size)
    compose(caminho, 1080, 1350, os.path.join(OUT, f"{nome}-feed.png"))
    compose(caminho, 1080, 1920, os.path.join(OUT, f"{nome}-story.png"))

print("\nPasta:", OUT)
