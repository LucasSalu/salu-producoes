# -*- coding: utf-8 -*-
"""Atualiza o modelo de preco: 10 fotos inclusas e lotes 250/300/350."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"

TROCAS = [
    # --- pagina /natal ---
    ("src/pages/natal.astro", "preco: '190'", "preco: '250'"),
    ("src/pages/natal.astro", "preco: '240'", "preco: '300'"),
    ("src/pages/natal.astro", "preco: '290'", "preco: '350'"),
    ("src/pages/natal.astro", "'5 fotos editadas'", "'10 fotos editadas'"),
    ("src/pages/natal.astro", "['+5 fotos', 'R$ 100']", "['+5 fotos', 'R$ 80']"),
    ("src/pages/natal.astro", "['+10 fotos', 'R$ 180']", "['+10 fotos', 'R$ 140']"),
    ("src/pages/natal.astro", "['+20 fotos', 'R$ 300']", "['+20 fotos', 'R$ 240']"),
    ("src/pages/natal.astro", "['Galeria completa', 'R$ 400']", "['Galeria completa', 'R$ 350']"),
    ("src/pages/natal.astro", "com cinco fotos inclusas", "com dez fotos inclusas"),
    ("src/pages/natal.astro", "Lote 1 · <strong class=\"text-champagne\">R$ 190</strong> · 8 vagas", "Lote 1 · <strong class=\"text-champagne\">R$ 250</strong> · 8 vagas"),
    ("src/pages/natal.astro", "'8 vagas', 'no Lote 1 por R$ 190'", "'8 vagas', 'no Lote 1 por R$ 250'"),
    ("src/pages/natal.astro", "O lote já inclui 5 fotos.", "O lote já inclui 10 fotos."),
    ("src/pages/natal.astro", "a tabela fica em R$ 350.", "a tabela fica em R$ 400."),
    ("src/pages/natal.astro", "sessão + 5 fotos", "sessão + 10 fotos"),
    ("src/pages/natal.astro", "Foto extra avulsa: R$ 25.", "Foto extra avulsa: R$ 20."),
    ("src/pages/natal.astro", "O Lote 1 custa R$ 190, o Lote 2 R$ 240 e o Lote 3 R$ 290.", "O Lote 1 custa R$ 250, o Lote 2 R$ 300 e o Lote 3 R$ 350."),
    ("src/pages/natal.astro", "a tabela fica em R$ 350.", "a tabela fica em R$ 400."),
    ("src/pages/natal.astro", "Cada lote inclui 5 fotos editadas. Na escolha, você pode levar mais: +5 por R$ 100, +10 por R$ 180, +20 por R$ 300 ou a galeria completa por R$ 400.", "Cada lote inclui 10 fotos editadas. Na escolha, você pode levar mais: +5 por R$ 80, +10 por R$ 140, +20 por R$ 240 ou a galeria completa por R$ 350."),
    ("src/pages/natal.astro", "Lote 1 · R$ 190 · 8 vagas", "Lote 1 · R$ 250 · 8 vagas"),
    ("src/pages/natal.astro", "Lotes a partir de R$ 190 com 5 fotos inclusas", "Lotes a partir de R$ 250 com 10 fotos inclusas"),
    # --- mensagens ---
    ("MENSAGENS-WHATSAPP.md", "R$ 190", "R$ 250"),
    ("MENSAGENS-WHATSAPP.md", "Lote 1 R$ 190 · Lote 2 R$ 240 · Lote 3 R$ 290. Cada lote inclui 5 fotos.", "Lote 1 R$ 250 · Lote 2 R$ 300 · Lote 3 R$ 350. Cada lote inclui 10 fotos."),
    # --- checklist do anuncio ---
    ("CHECKLIST-ANUNCIO.md", "Lote 1: R$ 190 · 8 vagas", "Lote 1: R$ 250 · 8 vagas"),
    ("CHECKLIST-ANUNCIO.md", "(190/240/290)", "(250/300/350)"),
]

for rel, old, new in TROCAS:
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    n = txt.count(old)
    if n == 0:
        print("NAO ENCONTRADO:", rel, "|", old[:50])
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt.replace(old, new))
    print(f"OK ({n}x) {rel}: {old[:45]}")
