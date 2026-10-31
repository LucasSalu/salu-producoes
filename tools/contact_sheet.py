# -*- coding: utf-8 -*-
"""Gera folha de contatos numerada, preservando numeros ja distribuidos."""
import os
import re
import sys
import json

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"C:\dev\deepseek\salu_producoes\melhores fotos"
OUT = r"C:\dev\deepseek\salu_producoes\selecao"
INDEX_PATH = os.path.join(OUT, "indice.json")
EXTS = (".jpg", ".jpeg", ".png", ".webp")
COLS, ROWS = 6, 5
CELL_W, CELL_H = 260, 340
IMG_W, IMG_H = 240, 300
MARGIN = 24
HEADER = 80

os.makedirs(OUT, exist_ok=True)


def base_key(name: str) -> str:
    stem = os.path.splitext(name)[0]
    stem = re.sub(r"\s*\(\d+\)", "", stem)
    prev = None
    while prev != stem:
        prev = stem
        stem = re.sub(r"[-_~]\d+$", "", stem)
    return stem.lower().strip()


def load_font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:  # noqa: BLE001
            continue
    return ImageFont.load_default()


def rel(path: str) -> str:
    return os.path.relpath(path, os.path.dirname(ROOT)).replace("\\", "/")


# ---------- coleta e deduplicacao ----------
files = []
for dirpath, _dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if fn.lower().endswith(EXTS):
            files.append(os.path.join(dirpath, fn))

groups: dict[str, list[str]] = {}
for path in files:
    groups.setdefault(base_key(os.path.basename(path)), []).append(path)


def score(path: str):
    ext = os.path.splitext(path)[1].lower()
    return (os.path.getsize(path), 1 if ext == ".jpg" else 0)


selected = [max(paths, key=score) for paths in groups.values()]

# ---------- numeracao estavel ----------
prev_index = []
if os.path.exists(INDEX_PATH):
    with open(INDEX_PATH, encoding="utf-8") as fh:
        prev_index = json.load(fh)

prev_numbers = {item["file"]: item["n"] for item in prev_index}
max_old = max(prev_numbers.values(), default=0)

old_sel = sorted([p for p in selected if rel(p) in prev_numbers], key=lambda p: prev_numbers[rel(p)])
new_sel = sorted([p for p in selected if rel(p) not in prev_numbers], key=lambda p: rel(p))

ordered = old_sel + new_sel
numbers = [prev_numbers[rel(p)] for p in old_sel] + list(range(max_old + 1, max_old + 1 + len(new_sel)))

print("Arquivos encontrados:", len(files))
print("Fotos unicas:", len(selected))
print("Duplicatas removidas:", len(files) - len(selected))
print("Fotos ja numeradas:", len(old_sel))
print("FOTOS NOVAS:", len(new_sel))
for p in new_sel:
    print("  +", rel(p), f"-> {prev_numbers.get(rel(p), 'NOVA')}")

# ---------- gera folhas ----------
font_num = load_font(26, bold=True)
font_title = load_font(30, bold=True)
font_sub = load_font(20)

per_sheet = COLS * ROWS
sheets = []
index = []

for start in range(0, len(ordered), per_sheet):
    chunk = ordered[start : start + per_sheet]
    sheet = Image.new("RGB", (MARGIN * 2 + COLS * CELL_W, HEADER + MARGIN * 2 + ROWS * CELL_H), (10, 10, 11))
    draw = ImageDraw.Draw(sheet)

    page = start // per_sheet + 1
    total_pages = (len(ordered) + per_sheet - 1) // per_sheet
    draw.text((MARGIN, 18), "Salu Produções — folha de contatos", font=font_title, fill=(242, 240, 233))
    draw.text(
        (MARGIN, 52),
        f"Página {page} de {total_pages} · marque os números das fotos que você quer no site",
        font=font_sub,
        fill=(201, 162, 39),
    )

    for i, path in enumerate(chunk):
        n = numbers[start + i]
        col, row = i % COLS, i // COLS
        x = MARGIN + col * CELL_W
        y = HEADER + MARGIN + row * CELL_H

        try:
            with Image.open(path) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                thumb = ImageOps.pad(im, (IMG_W, IMG_H), color=(19, 19, 21), method=Image.LANCZOS)
                sheet.paste(thumb, (x + (CELL_W - IMG_W) // 2, y + 32))
                w, h = im.size
        except Exception as exc:  # noqa: BLE001
            print("ERRO", path, exc)
            w = h = 0

        label = f"{n:03d}"
        bbox = draw.textbbox((0, 0), label, font=font_num)
        pad = 8
        draw.rectangle(
            [x + 6, y + 6, x + 6 + (bbox[2] - bbox[0]) + pad * 2, y + 6 + (bbox[3] - bbox[1]) + pad * 2],
            fill=(201, 162, 39),
        )
        draw.text((x + 6 + pad, y + 6 + pad - 2), label, font=font_num, fill=(10, 10, 11))

        index.append({"n": n, "file": rel(path), "w": w, "h": h, "page": page})

    sheets.append(sheet)

# ---------- salva ----------
for old in os.listdir(OUT):
    if old.startswith("folha-") and old.endswith(".jpg"):
        os.remove(os.path.join(OUT, old))

paths = []
for i, sheet in enumerate(sheets, start=1):
    p = os.path.join(OUT, f"folha-{i:02d}.jpg")
    sheet.save(p, quality=88, optimize=True)
    paths.append(p)

pdf_path = os.path.join(OUT, "folha-de-contatos.pdf")
sheets[0].save(pdf_path, save_all=True, append_images=sheets[1:], resolution=120.0)

with open(INDEX_PATH, "w", encoding="utf-8") as fh:
    json.dump(index, fh, ensure_ascii=False, indent=1)

print("Folhas:", len(sheets), "| total numerado:", len(index))
print("PDF:", pdf_path, os.path.getsize(pdf_path) // 1024, "KB")
