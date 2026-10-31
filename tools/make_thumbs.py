# -*- coding: utf-8 -*-
"""Gera miniaturas otimizadas + JSON para a pagina interativa de selecao."""
import json
import os
import sys

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
PHOTOS = os.path.join(BASE, "melhores fotos")
OUT = os.path.join(BASE, "public", "thumbs")
DATA_DIR = os.path.join(BASE, "src", "data")

os.makedirs(OUT, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

with open(os.path.join(BASE, "selecao", "indice.json"), encoding="utf-8") as fh:
    index = json.load(fh)

MAX_SIDE = 460
data = []

for item in index:
    path = os.path.join(os.path.dirname(PHOTOS), item["file"].replace("/", os.sep))
    name = f"{item['n']:03d}.jpg"
    try:
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im).convert("RGB")
            w, h = im.size
            thumb = im.copy()
            thumb.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
            thumb.save(os.path.join(OUT, name), quality=76, optimize=True, progressive=True)
    except Exception as exc:  # noqa: BLE001
        print("ERRO", path, exc)
        continue

    data.append(
        {
            "n": item["n"],
            "thumb": f"/thumbs/{name}",
            "w": w,
            "h": h,
            "portrait": h >= w,
        }
    )

# preserva a ordem numerica
data.sort(key=lambda d: d["n"])

with open(os.path.join(DATA_DIR, "fotos.json"), "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))

total_kb = sum(os.path.getsize(os.path.join(OUT, f"{d['n']:03d}.jpg")) for d in data) // 1024
print("Miniaturas:", len(data))
print("Peso total:", total_kb, "KB")
print("JSON:", os.path.join(DATA_DIR, "fotos.json"))
