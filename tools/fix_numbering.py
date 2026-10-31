# -*- coding: utf-8 -*-
"""Corrige a numeracao (preenche buraco) e re-renderiza as folhas a partir do indice."""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
ROOT = os.path.join(BASE, "melhores fotos")
OUT = os.path.join(BASE, "selecao")
IDX = os.path.join(OUT, "indice.json")

COLS, ROWS = 6, 5
CELL_W, CELL_H = 260, 340
IMG_W, IMG_H = 240, 300
MARGIN = 24
HEADER = 80


def load_font(size, bold=False):
    for path in (
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except Exception:  # noqa: BLE001
            continue
    return ImageFont.load_default()


with open(IDX, encoding="utf-8") as fh:
    index = json.load(fh)

# 1) preenche o buraco: a DSC04468 (1) era a foto que estava no numero 54
for item in index:
    if item["file"].endswith("DSC04468 (1).jpg"):
        item["n"] = 54

# 2) renumera as novas para ficarem consecutivas
novas = sorted([i for i in index if i["n"] >= 203], key=lambda i: i["n"])
for k, item in enumerate(novas, start=203):
    item["n"] = k

index.sort(key=lambda i: i["n"])

nums = [i["n"] for i in index]
faltando = [n for n in range(1, max(nums) + 1) if n not in set(nums)]
print("Total:", len(index), "| max:", max(nums), "| faltando:", faltando)

# 3) re-renderiza
font_num = load_font(26, bold=True)
font_title = load_font(30, bold=True)
font_sub = load_font(20)

per_sheet = COLS * ROWS
sheets = []

for start in range(0, len(index), per_sheet):
    chunk = index[start : start + per_sheet]
    sheet = Image.new(
        "RGB", (MARGIN * 2 + COLS * CELL_W, HEADER + MARGIN * 2 + ROWS * CELL_H), (10, 10, 11)
    )
    draw = ImageDraw.Draw(sheet)
    page = start // per_sheet + 1
    total_pages = (len(index) + per_sheet - 1) // per_sheet
    draw.text((MARGIN, 18), "Salu Produções — folha de contatos", font=font_title, fill=(242, 240, 233))
    draw.text(
        (MARGIN, 52),
        f"Página {page} de {total_pages} · marque os números das fotos que você quer no site",
        font=font_sub,
        fill=(201, 162, 39),
    )

    for i, item in enumerate(chunk):
        n = item["n"]
        col, row = i % COLS, i // COLS
        x = MARGIN + col * CELL_W
        y = HEADER + MARGIN + row * CELL_H
        path = os.path.join(os.path.dirname(ROOT), item["file"].replace("/", os.sep))

        try:
            with Image.open(path) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                thumb = ImageOps.pad(im, (IMG_W, IMG_H), color=(19, 19, 21), method=Image.LANCZOS)
                sheet.paste(thumb, (x + (CELL_W - IMG_W) // 2, y + 32))
        except Exception as exc:  # noqa: BLE001
            print("ERRO", path, exc)

        label = f"{n:03d}"
        bbox = draw.textbbox((0, 0), label, font=font_num)
        pad = 8
        draw.rectangle(
            [x + 6, y + 6, x + 6 + (bbox[2] - bbox[0]) + pad * 2, y + 6 + (bbox[3] - bbox[1]) + pad * 2],
            fill=(201, 162, 39),
        )
        draw.text((x + 6 + pad, y + 6 + pad - 2), label, font=font_num, fill=(10, 10, 11))
        item["page"] = page

    sheets.append(sheet)

for old in os.listdir(OUT):
    if old.startswith("folha-") and old.endswith(".jpg"):
        os.remove(os.path.join(OUT, old))

for i, sheet in enumerate(sheets, start=1):
    sheet.save(os.path.join(OUT, f"folha-{i:02d}.jpg"), quality=88, optimize=True)

pdf_path = os.path.join(OUT, "folha-de-contatos.pdf")
sheets[0].save(pdf_path, save_all=True, append_images=sheets[1:], resolution=120.0)

with open(IDX, "w", encoding="utf-8") as fh:
    json.dump(index, fh, ensure_ascii=False, indent=1)

print("Folhas:", len(sheets), "| PDF:", os.path.getsize(pdf_path) // 1024, "KB")
