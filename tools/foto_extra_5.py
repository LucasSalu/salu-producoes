# -*- coding: utf-8 -*-
"""Foto extra passa a custar R$ 5 e os pacotes de fotos seguem a mesma regra."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"

TROCAS = [
    ("src/pages/natal.astro", "['+5 fotos', 'R$ 70']", "['+5 fotos', 'R$ 25']"),
    ("src/pages/natal.astro", "['+10 fotos', 'R$ 120']", "['+10 fotos', 'R$ 50']"),
    ("src/pages/natal.astro", "['+20 fotos', 'R$ 200']", "['+20 fotos', 'R$ 100']"),
    ("src/pages/natal.astro", "['Galeria completa', 'R$ 280']", "['Galeria completa', 'R$ 350']"),
    ("src/pages/natal.astro", "Foto extra avulsa: R$ 20.", "Foto extra avulsa: R$ 5."),
    ("src/pages/natal.astro", "+5 por R$ 70, +10 por R$ 120, +20 por R$ 200 ou a galeria completa por R$ 280.", "+5 por R$ 25, +10 por R$ 50, +20 por R$ 100 ou a galeria completa por R$ 350. Cada foto extra sai por R$ 5."),
    ("PACOTES-NATAL.md", "| 1 foto extra | R$ 20 |", "| 1 foto extra | R$ 5 |"),
    ("PACOTES-NATAL.md", "| +5 fotos | R$ 70 |", "| +5 fotos | R$ 25 |"),
    ("PACOTES-NATAL.md", "| +10 fotos | R$ 120 |", "| +10 fotos | R$ 50 |"),
    ("PACOTES-NATAL.md", "| +20 fotos | R$ 200 |", "| +20 fotos | R$ 100 |"),
    ("PACOTES-NATAL.md", "| Galeria completa | R$ 280 |", "| Galeria completa | R$ 350 |"),
]

for rel, old, new in TROCAS:
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    n = txt.count(old)
    if n == 0:
        print("NAO ENCONTRADO:", rel, "|", old[:55])
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt.replace(old, new))
    print(f"OK ({n}x) {rel}")

# JSON
for rel in ("precos-natal.json", "public/precos-natal.json"):
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    d = json.load(open(path, encoding="utf-8"))
    novos = {"foto_extra": 5, "mais_5": 25, "mais_10": 50, "mais_20": 100, "galeria_completa": 350}
    for item in d["avulso"]["fotos"]:
        if item["id"] in novos:
            item["preco"] = novos[item["id"]]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("JSON atualizado:", rel)
