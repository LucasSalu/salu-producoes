# -*- coding: utf-8 -*-
"""Troca o travessao dos rotulos de secao (01 - Sobre) por ponto medio."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes\src"

ROTULOS = [
    ("pages/index.astro", "01 — Sobre", "01 · Sobre"),
    ("pages/index.astro", "02 — Portfólio", "02 · Portfólio"),
    ("components/sections/Pacotes.astro", "03 — Pacotes", "03 · Pacotes"),
    ("components/sections/Processo.astro", "04 — Processo", "04 · Processo"),
    ("components/sections/Faq.astro", "05 — Dúvidas", "05 · Dúvidas"),
]

for rel, old, new in ROTULOS:
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    if old not in txt:
        print("NAO ENCONTRADO:", rel, old)
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt.replace(old, new))
    print("OK:", rel, "->", new)
