# -*- coding: utf-8 -*-
"""Ajusta so a linha de Natal: tom aspiracional, pet e maquiagem sem cobranca extra."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
NATAL = f"{BASE}\\src\\pages\\natal.astro"

TROCAS_NATAL = [
    # hero
    ("Trinta minutos de ensaio no estúdio da Salu, com 10, 15 ou 20 fotos inclusas.\n          Você escolhe quantas quer levar.",
     "Trinta minutos, de 10 a 20 fotos e entrega rápida. O Natal que você quer\n          guardar, com um preço que cabe no bolso."),
    # extras: sem pet e sem maquiagem cobrados
    ("  ['Pet', 'R$ 60'],\n", ""),
    ("  ['Maquiagem parceira', 'R$ 200'],\n", ""),
    # prova
    ("['Estúdio', 'em Paulínia'],", "['Terça a domingo', 'agenda aberta'],"),
    # beneficio 2
    ("10, 15 ou 20 fotos. Se quiser mais depois, compra avulso, sem pacote fechado.",
     "10, 15 ou 20 fotos inclusas. Foto extra a R$ 5, sem pacote fechado."),
    # sinal por dia
    ("d: 'Sinal de R$ 100 no Pix garante a sua vaga.'",
     "d: 'Sinal de R$ 50 de terça a quinta, R$ 100 no fim de semana.'"),
    # faq pet + maquiagem
    ("""  {
    q: 'Posso levar meu pet?',
    a: 'Pode! Pet é muito bem-vindo. É um dos pedidos que mais recebi. Tem adicional de R$ 60.',
  },""",
     """  {
    q: 'Posso levar meu pet?',
    a: 'Pode! Pet é muito bem-vindo, sem custo extra. Foi um dos pedidos que mais recebi.',
  },
  {
    q: 'A maquiagem está inclusa?',
    a: 'Não. Você pode vir maquiada do jeito que gosta, ou eu indico uma maquiadora parceira.',
  },"""),
    # nota do avulso
    ("Foto extra avulsa: R$ 5. Sinal de R$ 100 no Pix garante a vaga.",
     "Foto extra avulsa: R$ 5. Pet é bem-vindo, sem custo. Sinal de R$ 50 de terça a quinta, R$ 100 no fim de semana."),
]

with open(NATAL, encoding="utf-8") as f:
    s = f.read()
for old, new in TROCAS_NATAL:
    n = s.count(old)
    if n == 0:
        print("NAO ENCONTRADO:", old[:60].replace("\n", " "))
        continue
    s = s.replace(old, new)
    print(f"OK ({n}x): {old[:50].strip()}")
with open(NATAL, "w", encoding="utf-8") as f:
    f.write(s)

# --- JSON ---
for rel in ("precos-natal.json", "public/precos-natal.json"):
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    d = json.load(open(path, encoding="utf-8"))
    d["avulso"]["sessao"] = [i for i in d["avulso"]["sessao"] if i["id"] not in ("pet", "maquiagem")]
    d["inclusos"] = {
        "pet": "sem custo extra",
        "maquiagem": "não inclusa (indicação de parceira)"
    }
    d["pagamento"]["sinal"] = {"terca_a_quinta": 50, "fim_de_semana": 100}
    d["pagamento"]["sinal_metodo"] = "Pix"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("JSON:", rel)

# --- doc de precos ---
DOC = f"{BASE}\\PACOTES-NATAL.md"
with open(DOC, encoding="utf-8") as f:
    d2 = f.read()
d2 = d2.replace("| Pet | R$ 60 |\n", "")
d2 = d2.replace("| Maquiagem (parceira) | R$ 200 |\n", "")
d2 = d2.replace("| Sinal para reservar | **R$ 100** (Pix) |",
                "| Sinal | **R$ 50** de terça a quinta · **R$ 100** no fim de semana (Pix) |")
d2 = d2.replace("| **Total** | **54 sessões** |", "> Pet é bem-vindo sem custo extra. A maquiagem não está inclusa: indique uma parceira.\n\n| **Total** | **54 sessões** |")
with open(DOC, "w", encoding="utf-8") as f:
    f.write(d2)
print("DOC atualizado")
