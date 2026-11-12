# -*- coding: utf-8 -*-
"""Gera as artes da campanha de Natal (posts, card de pacote e story)."""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
FONTS = os.path.join(BASE, "tools", "fonts")
OUT = os.path.join(BASE, "selecao", "artes")
os.makedirs(OUT, exist_ok=True)

CREAM = (246, 241, 230)
INK = (29, 26, 22)
GOLD = (201, 162, 39)
CHAMP = (232, 213, 168)
WINE = (94, 35, 51)
DARK = (14, 13, 11)
CREAM_SOFT = (212, 205, 190)


def playfair(size, weight=500):
    font = ImageFont.truetype(os.path.join(FONTS, "PlayfairDisplay.ttf"), size)
    try:
        font.set_variation_by_axes([weight])
    except Exception:  # noqa: BLE001
        pass
    return font


def script(size):
    return ImageFont.truetype(os.path.join(FONTS, "GreatVibes-Regular.ttf"), size)


def sans(size):
    return ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", size)


def tracked(draw, xy, text, font, fill, tracking=0.0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x


def center(draw, y, text, font, fill, width=1080, tracking=0.0):
    w = draw.textlength(text, font=font) + tracking * max(0, len(text) - 1)
    tracked(draw, ((width - w) / 2, y), text, font, fill, tracking)


def star(draw, cx, cy, r, fill):
    pts = []
    for i in range(8):
        ang = math.pi * i / 4 - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.36
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill)


def divider(draw, y, color, width=1080, inset=170):
    draw.line([(inset, y), (width / 2 - 22, y)], fill=color, width=1)
    d = 9
    draw.polygon(
        [(width / 2 - d, y), (width / 2, y - d), (width / 2 + d, y), (width / 2, y + d)],
        outline=color,
        width=1,
    )
    draw.line([(width / 2 + 22, y), (width - inset, y)], fill=color, width=1)


def tree(draw, cx, base, h, color, lw=2):
    tris = [
        (95, 90),   # (half_width, height) de baixo para cima
        (74, 74),
        (55, 58),
    ]
    y0 = base
    for half, th in tris:
        y_top = y0 - th
        draw.polygon(
            [(cx - half, y0), (cx + half, y0), (cx, y_top)],
            outline=color,
            width=lw,
        )
        y0 = y_top + 6
    draw.line([(cx, base), (cx, base + 26)], fill=color, width=lw)


def frame(draw, inset, color, w=2):
    draw.rectangle([inset, inset, 1080 - inset, 1080 - inset], outline=color, width=w)


# ---------------------------------------------------------------- anuncio
def arte_anuncio():
    img = Image.new("RGB", (1080, 1350), CREAM)
    d = ImageDraw.Draw(img)

    frame(d, 54, GOLD)

    star(d, 540, 168, 22, GOLD)
    center(d, 222, "SALU PRODUÇÕES", playfair(30, 600), INK, tracking=10)

    divider(d, 306, GOLD, inset=200)

    center(d, 396, "Ensaio de", script(108), WINE)
    center(d, 486, "NATAL", playfair(280, 700), INK)

    tree(d, 540, 952, 168, GOLD)

    center(d, 1026, "O olhar do casamento,", playfair(44, 500), INK)
    center(d, 1086, "agora no Natal.", playfair(44, 500), WINE)

    center(d, 1188, "INAUGURAÇÃO DO ESTÚDIO  ·  VAGAS LIMITADAS", sans(24), (120, 110, 100), tracking=5)
    center(d, 1238, "@salu_producoes", sans(26), (150, 140, 128), tracking=2)

    img.save(os.path.join(OUT, "arte-anuncio.png"))
    print("anuncio ok")


# ---------------------------------------------------------------- card de pacote
def arte_pacote():
    img = Image.new("RGB", (1080, 1350), DARK)
    d = ImageDraw.Draw(img)

    frame(d, 54, GOLD)

    center(d, 92, "ENSAIO DE NATAL  ·  ESTÚDIO SALU", sans(24), CHAMP, tracking=7)
    star(d, 540, 168, 15, GOLD)

    center(d, 218, "Memória", playfair(140, 600), CREAM)
    center(d, 382, "dois looks, uma memória", script(62), GOLD)

    divider(d, 470, GOLD, inset=220)

    itens = [
        "45 minutos de sessão",
        "2 looks · 1 cenário",
        "25 fotos editadas",
        "5 impressões 15×21",
        "galeria online + entrega rápida",
    ]
    y = 540
    for item in itens:
        center(d, y, item, sans(32), CREAM_SOFT, tracking=1)
        y += 66

    # preço
    w_r = d.textlength("R$", font=sans(56))
    w_v = d.textlength("690", font=playfair(172, 700))
    total = w_r + 18 + w_v
    x0 = (1080 - total) / 2
    d.text((x0, 1004), "R$", font=sans(56), fill=CHAMP)
    d.text((x0 + w_r + 18, 962), "690", font=playfair(172, 700), fill=CREAM)

    center(d, 1172, "lançamento  ·  depois R$ 790", sans(28), GOLD, tracking=3)

    d.rounded_rectangle([170, 1230, 910, 1312], radius=41, fill=GOLD)
    center(d, 1254, "RESERVAR PELO WHATSAPP", sans(28), DARK, tracking=4)

    center(d, 1290 + 0, "", sans(10), DARK)  # noop

    img.save(os.path.join(OUT, "arte-pacote-memoria.png"))
    print("pacote ok")


# ---------------------------------------------------------------- story
def arte_story():
    img = Image.new("RGB", (1080, 1920), DARK)
    d = ImageDraw.Draw(img)

    d.rectangle([48, 48, 1032, 1872], outline=GOLD, width=2)

    star(d, 540, 128, 18, GOLD)
    center(d, 180, "SALU PRODUÇÕES", sans(24), CHAMP, tracking=8)
    center(d, 262, "Ensaio de", script(84), CHAMP)
    center(d, 336, "NATAL", playfair(212, 700), CREAM)

    divider(d, 596, GOLD, inset=200)

    # faixa de foto
    foto = Image.open(os.path.join(BASE, "public", "fotos", "070-1600.webp")).convert("RGB")
    foto = foto.resize((1080, 720), Image.LANCZOS)
    img.paste(foto, (0, 648))
    d.rectangle([0, 648, 1079, 1367], outline=GOLD, width=2)

    center(d, 1458, "O olhar do casamento,", playfair(46, 500), CREAM)
    center(d, 1520, "agora no Natal.", playfair(46, 500), WINE)

    d.rounded_rectangle([170, 1618, 910, 1700], radius=41, fill=GOLD)
    center(d, 1642, "RESERVAR PELO WHATSAPP", sans(28), DARK, tracking=4)

    center(d, 1746, "10 primeiras sessões  ·  preço de inauguração", sans(26), GOLD, tracking=3)
    center(d, 1806, "@salu_producoes", sans(24), (190, 180, 165), tracking=2)

    img.save(os.path.join(OUT, "arte-story.png"))
    print("story ok")


arte_anuncio()
arte_pacote()
arte_story()
print("pronto:", OUT)
