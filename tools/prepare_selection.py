# -*- coding: utf-8 -*-
"""Prepara as fotos selecionadas: mapeia numeros, gera WebP responsivo e JSON."""
import json
import os
import sys

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
PHOTOS = os.path.join(BASE, "melhores fotos")
OUT = os.path.join(BASE, "public", "fotos")
DATA = os.path.join(BASE, "src", "data")

NUMEROS = [
    2, 6, 7, 8, 16, 27, 28, 32, 33, 34, 36, 37, 38, 39, 41, 45, 46, 47, 51, 53,
    54, 56, 59, 62, 63, 65, 67, 68, 70, 71, 73, 75, 78, 79, 85, 90, 91, 93, 99, 103,
    104, 106, 107, 109, 114, 116, 118, 120, 121, 126, 134, 137, 142, 143, 145, 147, 148, 149, 152, 153,
    160, 161, 162, 165, 166, 167, 168, 172, 180, 181, 186, 187, 189, 191, 198, 199, 203, 205, 206, 207,
    208, 209, 210, 212, 213, 215, 216, 218, 219, 220, 221, 223, 224, 227, 228,
]

os.makedirs(OUT, exist_ok=True)
os.makedirs(DATA, exist_ok=True)

with open(os.path.join(BASE, "selecao", "indice.json"), encoding="utf-8") as fh:
    index = json.load(fh)

by_n = {item["n"]: item for item in index}
selecionadas = [n for n in NUMEROS if n in by_n]
faltando = [n for n in NUMEROS if n not in by_n]

print("Selecionadas:", len(selecionadas))
print("Faltando do indice:", faltando)

WIDTHS = (480, 960, 1600)
result = []

for n in selecionadas:
    item = by_n[n]
    path = os.path.join(os.path.dirname(PHOTOS), item["file"].replace("/", os.sep))
    with Image.open(path) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        w, h = img.size
        variants = {}
        for target in WIDTHS:
            if target >= w:
                continue
            nh = max(1, round(h * target / w))
            resized = img.resize((target, nh), Image.LANCZOS)
            name = f"{n:03d}-{target}.webp"
            resized.save(os.path.join(OUT, name), "WEBP", quality=80, method=6)
            variants[target] = f"/fotos/{name}"

        # se a imagem for menor que todas as larguras, gera uma unica versao
        if not variants:
            name = f"{n:03d}-{w}.webp"
            img.save(os.path.join(OUT, name), "WEBP", quality=82, method=6)
            variants[w] = f"/fotos/{name}"

    result.append(
        {
            "n": n,
            "w": w,
            "h": h,
            "portrait": h >= w,
            "variants": variants,
        }
    )

with open(os.path.join(DATA, "selecionadas.json"), "w", encoding="utf-8") as fh:
    json.dump(result, fh, ensure_ascii=False, separators=(",", ":"))

portrait = sum(1 for r in result if r["portrait"])
landscape = len(result) - portrait
grandes = sum(1 for r in result if max(r["w"], r["h"]) >= 3000)
total_kb = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)) // 1024

print("Retrato:", portrait, "| Paisagem:", landscape)
print("Alta resolucao (>=3000px):", grandes)
print("Arquivos WebP gerados:", len(os.listdir(OUT)))
print("Peso total WebP:", total_kb // 1024, "MB")
print("\nPaisagens (candidatas a hero):")
for r in result:
    if not r["portrait"]:
        print(f"  #{r['n']:03d}  {r['w']}x{r['h']}  {by_n[r['n']]['file']}")
