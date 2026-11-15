# -*- coding: utf-8 -*-
"""Presente passa a ter 10 fotos."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"

TROCAS = [
    # pagina
    ("src/pages/natal.astro", "fotos: '8 fotos',", "fotos: '10 fotos',"),
    ("src/pages/natal.astro", "'8 fotos editadas'", "'10 fotos editadas'"),
    ("src/pages/natal.astro", "com 8, 15 ou 20 fotos inclusas", "com 10, 15 ou 20 fotos inclusas"),
    ("src/pages/natal.astro", "8, 15 ou 20 fotos. Se quiser mais depois", "10, 15 ou 20 fotos. Se quiser mais depois"),
    ("src/pages/natal.astro", "Presente: 8 fotos por R$ 199.", "Presente: 10 fotos por R$ 199."),
    ("src/pages/natal.astro", "Depende da opção: 8, 15 ou 20.", "Depende da opção: 10, 15 ou 20."),
    ("src/pages/natal.astro", "com 8, 15 ou 20 fotos, a partir de R$ 199", "com 10, 15 ou 20 fotos, a partir de R$ 199"),
    # doc de precos
    ("PACOTES-NATAL.md", "| **Presente** | 8 | **R$ 199** | R$ 24,90 |", "| **Presente** | 10 | **R$ 199** | R$ 19,90 |"),
    ("PACOTES-NATAL.md", "com 8, 15 ou 20 fotos inclusas", "com 10, 15 ou 20 fotos inclusas"),
    ("PACOTES-NATAL.md", "Presente (8 fotos) R$ 199", "Presente (10 fotos) R$ 199"),
    # mensagens
    ("MENSAGENS-WHATSAPP.md", "Presente R$ 199 (8 fotos)", "Presente R$ 199 (10 fotos)"),
    ("MENSAGENS-WHATSAPP.md", "com 8 fotos e 30 minutos de ensaio", "com 10 fotos e 30 minutos de ensaio"),
    ("MENSAGENS-WHATSAPP.md", "com 8 fotos e 30 minutos.", "com 10 fotos e 30 minutos."),
    ("MENSAGENS-WHATSAPP.md", "com 8 fotos.", "com 10 fotos."),
    ("MENSAGENS-WHATSAPP.md", "A partir de R$ 199 (8 fotos, 30 min).", "A partir de R$ 199 (10 fotos, 30 min)."),
    # checklist
    ("CHECKLIST-ANUNCIO.md", "Presente R$ 199 · 8 fotos", "Presente R$ 199 · 10 fotos"),
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
