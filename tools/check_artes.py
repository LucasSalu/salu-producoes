# -*- coding: utf-8 -*-
"""Valida as artes geradas: overflow de texto, cores esperadas e foto na banda do story."""
import os
import sys

import numpy as np
from PIL import Image, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
FONTS = os.path.join(BASE, "tools", "fonts")
ARTES = os.path.join(BASE, "selecao", "artes")


def playfair(size, weight=500):
    f = ImageFont.truetype(os.path.join(FONTS, "PlayfairDisplay.ttf"), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:  # noqa: BLE001
        pass
    return f


def script(size):
    return ImageFont.truetype(os.path.join(FONTS, "GreatVibes-Regular.ttf"), size)


def sans(size):
    return ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", size)


pf_test = ImageFont.truetype(os.path.join(FONTS, "PlayfairDisplay.ttf"), 100)
print("eixos variaveis:", pf_test.get_variation_axes())

print("\n=== larguras de texto (limite 972 px dentro da moldura) ===")
checks = [
    ("SALU PRODUÇÕES", playfair(30, 600), 10),
    ("Ensaio de", script(108), 0),
    ("NATAL", playfair(300, 700), 0),
    ("O olhar do casamento,", playfair(44, 500), 0),
    ("agora no Natal.", playfair(44, 500), 0),
    ("INAUGURAÇÃO DO ESTÚDIO  ·  VAGAS LIMITADAS", sans(24), 5),
    ("@salu_producoes", sans(26), 2),
    ("ENSAIO DE NATAL  ·  ESTÚDIO SALU", sans(24), 7),
    ("dois looks, uma memória", script(62), 0),
    ("25 fotos editadas", sans(32), 1),
    ("45 minutos de sessão", sans(32), 1),
    ("galeria online + entrega rápida", sans(32), 1),
    ("lançamento  ·  depois R$ 790", sans(28), 3),
    ("RESERVAR PELO WHATSAPP", sans(28), 4),
    ("10 primeiras sessões  ·  preço de inauguração", sans(26), 3),
]
for text, font, tr in checks:
    w = font.getlength(text) + tr * max(0, len(text) - 1)
    status = "OK" if w <= 972 else "OVERFLOW!"
    print(f"{status:10s} w={w:6.0f}  {text}")

print("\n=== pixels esperados ===")
anuncio = Image.open(os.path.join(ARTES, "arte-anuncio.png")).convert("RGB")
print("fundo creme (10,10):", anuncio.getpixel((10, 10)))
print("moldura ouro (54,54):", anuncio.getpixel((54, 54)))
print("tinta NATAL (540,600):", anuncio.getpixel((540, 600)))

pacote = Image.open(os.path.join(ARTES, "arte-pacote-memoria.png")).convert("RGB")
print("fundo escuro (10,10):", pacote.getpixel((10, 10)))
print("CTA ouro (540,1270):", pacote.getpixel((540, 1270)))

story = Image.open(os.path.join(ARTES, "arte-story.png")).convert("RGB")
banda = np.asarray(story.crop((0, 660, 1080, 1350)))
print("banda da foto — media:", round(float(banda.mean()), 1), "| desvio:", round(float(banda.std()), 1), "(foto presente se desvio > 15)")
print("fundo escuro do story (540,100):", story.getpixel((540, 100)))

sizes = {f: os.path.getsize(os.path.join(ARTES, f)) // 1024 for f in os.listdir(ARTES)}
print("\n=== arquivos ===")
for f, kb in sizes.items():
    print(f"{f}: {kb} KB")
