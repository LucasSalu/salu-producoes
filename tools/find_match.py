# -*- coding: utf-8 -*-
"""Procura a foto enviada entre as miniaturas do acervo (comparacao perceptual simples)."""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
ATTACH = r"C:\Users\PC\.dsh\attachments\v1\objects\8e\8eb344f67c064bacef112075a00557eb01012ea0eeb0cfabff1cbb5230677826"


def signature(path):
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("L").resize((64, 64), Image.LANCZOS)
        arr = np.asarray(im, dtype=np.float32)
    arr -= arr.mean()
    std = arr.std() or 1.0
    return arr / std


target = signature(ATTACH)
index = json.load(open(os.path.join(BASE, "selecao", "indice.json"), encoding="utf-8"))

results = []
for item in index:
    thumb = os.path.join(BASE, "public", "thumbs", f"{item['n']:03d}.jpg")
    if not os.path.exists(thumb):
        continue
    try:
        sig = signature(thumb)
    except Exception:  # noqa: BLE001
        continue
    score = float(np.mean((target - sig) ** 2))
    results.append((score, item["n"], item["file"]))

results.sort()
print("Melhores correspondencias (menor = mais parecido):")
for score, n, file in results[:5]:
    print(f"  #{n:03d}  score={score:.4f}  {file}")
