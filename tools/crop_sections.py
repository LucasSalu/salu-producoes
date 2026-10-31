# -*- coding: utf-8 -*-
"""Recorta as secoes a partir do screenshot de pagina inteira."""
import json
import os

from PIL import Image

BASE = r"C:\dev\deepseek\salu_producoes\selecao"
full = Image.open(os.path.join(BASE, "full.png"))
positions = json.load(open(os.path.join(BASE, "positions.json"), encoding="utf-8"))

order = ["sobre", "citacao", "portfolio", "pacotes", "processo", "faq", "contato"]
total = positions.get("total", full.height)

for i, name in enumerate(order):
    y = positions[name]
    end = positions[order[i + 1]] if i + 1 < len(order) else total
    height = min(end - y, 1200)
    crop = full.crop((0, max(0, y), full.width, max(0, y) + height))
    crop.save(os.path.join(BASE, f"sec-{name}.png"))
    print(name, y, height)
