# -*- coding: utf-8 -*-
"""Alinha mensagens e checklist as tres opcoes 199/230/250 com 8/15/20 fotos."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"

TROCAS = [
    # mensagens - ordem importa (frases maiores primeiro)
    ("MENSAGENS-WHATSAPP.md", "O Lote 1 está em R$ 250, com 8 vagas. Depois o preço sobe.", "A opção Presente está em R$ 199, com 8 fotos e 30 minutos de ensaio."),
    ("MENSAGENS-WHATSAPP.md", "O Lote 1 está em R$ 250, com 8 vagas.", "A opção Presente está em R$ 199, com 8 fotos e 30 minutos."),
    ("MENSAGENS-WHATSAPP.md", "O Lote 1 está em R$ 250.", "A opção Presente está em R$ 199, com 8 fotos."),
    ("MENSAGENS-WHATSAPP.md", "(a partir de R$ 250 no Lote 1)", "(a partir de R$ 199)"),
    ("MENSAGENS-WHATSAPP.md", "A partir de R$ 250 (Lote 1, 8 vagas).", "A partir de R$ 199 (8 fotos, 30 min)."),
    ("MENSAGENS-WHATSAPP.md", "Lote 1 R$ 250 · Lote 2 R$ 300 · Lote 3 R$ 350. Cada lote inclui 10 fotos.", "Presente R$ 199 (8 fotos) · Clássico R$ 230 (15 fotos) · Completo R$ 250 (20 fotos). Todos com 30 min."),
    # checklist do anuncio
    ("CHECKLIST-ANUNCIO.md", "Lote 1: R$ 250 · 8 vagas", "Presente R$ 199 · 8 fotos"),
    ("CHECKLIST-ANUNCIO.md", "(250/300/350)", "(199/230/250)"),
    ("CHECKLIST-ANUNCIO.md", "**Lote 1: R$ 250 · 8 vagas**", "**A partir de R$ 199 · 30 min**"),
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
    print(f"OK ({n}x) {rel}: {old[:50]}")
