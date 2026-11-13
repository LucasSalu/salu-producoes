# -*- coding: utf-8 -*-
"""Remove travessoes (em dash) do texto corrido do site, preservando rotulos de secao."""
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes\src"

TROCAS = [
    ("pages/natal.astro", "Você só chega e sorri — eu dirijo as poses.", "Você só chega e sorri. Eu dirijo as poses."),
    ("pages/natal.astro", "família — sem restrição de número.", "família, sem restrição de número."),
    ("pages/natal.astro", "Pet é muito bem-vindo — é um dos pedidos", "Pet é muito bem-vindo. É um dos pedidos"),
    ("pages/natal.astro", "em até 6 meses — com cartão impresso", "em até 6 meses, com cartão impresso"),
    ("components/sections/Faq.astro", "estiver definida — mas fale", "estiver definida, mas fale"),
    ("components/sections/Faq.astro", "'Sim — e sai mais barato.", "'Sim, e sai mais barato."),
    ("components/sections/Faq.astro", "Chama no WhatsApp — respondemos", "Chama no WhatsApp. Respondemos"),
    ("components/sections/Pacotes.astro", "partida — o orçamento final", "partida. O orçamento final"),
    ("components/sections/Pacotes.astro", "Filme — para reviver", "Filme: para reviver"),
    ("pages/index.astro", "em preto e branco — casamento registrado", "em preto e branco, casamento registrado"),
    ("pages/sobre.astro", "em preto e branco — casamento registrado", "em preto e branco, casamento registrado"),
    ("pages/selecao.astro", "entre 20 e 35 — eu cuido", "entre 20 e 35. Eu cuido"),
]

for rel, old, new in TROCAS:
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    n = txt.count(old)
    if n == 0:
        print("NAO ENCONTRADO:", rel, "->", old[:40])
        continue
    txt = txt.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"OK ({n}x): {rel}: {old[:35]}...")
