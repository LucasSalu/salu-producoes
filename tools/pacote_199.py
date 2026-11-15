# -*- coding: utf-8 -*-
"""Pacote unico de Natal: R$ 199, 30 min, 10 fotos, entrega 24h uteis, extra R$ 6."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\dev\deepseek\salu_producoes"
NATAL = f"{BASE}\\src\\pages\\natal.astro"

with open(NATAL, encoding="utf-8") as f:
    s = f.read()

# 1) array de opcoes -> array vazio (a secao nova nao usa)
ini = s.index("const opcoes = [")
fim = s.index("];", ini) + 2
s = s[:ini] + "const opcoes = [];" + s[fim:]

# 2) valores do avulso
s = s.replace("['+5 fotos', 'R$ 25']", "['+5 fotos', 'R$ 30']")
s = s.replace("['+10 fotos', 'R$ 50']", "['+10 fotos', 'R$ 60']")
s = s.replace("['+20 fotos', 'R$ 100']", "['+20 fotos', 'R$ 120']")
s = s.replace("  ['Entrega em 24 h', 'R$ 80'],\n", "")

# 3) hero
s = s.replace(
    "Trinta minutos, de 10 a 20 fotos e entrega rápida. O Natal que você quer\n          guardar, com um preço que cabe no bolso.",
    "Trinta minutos, 10 fotos editadas e entrega em 24 horas úteis. O Natal que você\n          quer guardar, com um preço que cabe no bolso.",
)
s = s.replace(
    "Bom, barato e rápido · a partir de <strong class=\"text-champagne\">R$ 199</strong> · agenda de terça a domingo",
    "<strong class=\"text-champagne\">R$ 199</strong> · 30 min · 10 fotos · entrega em 24h úteis",
)
s = s.replace('<a href="#opcoes" class="btn btn-ghost">Ver as opções</a>', '<a href="#pacote" class="btn btn-ghost">Ver o que inclui</a>')

# 4) prova
s = s.replace("['30 min', 'de ensaio no estúdio'],", "['30 min', 'de ensaio no estúdio'],")
s = s.replace("['Até 5 dias', 'para receber as fotos'],", "['24h úteis', 'para receber as fotos'],")

# 5) beneficios
s = s.replace(
    """            <h3 class="mt-6 font-display text-xl">Ninguém fica perdido</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              Eu dirijo cada pose. Você só precisa estar com quem ama.
            </p>""",
    """            <h3 class="mt-6 font-display text-xl">Trinta minutos e pronto</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              É chegar, fotografar e ir. Eu dirijo as poses, você só aproveita.
            </p>""",
)
s = s.replace(
    """            <h3 class="mt-6 font-display text-xl">Você escolhe o tamanho</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              10, 15 ou 20 fotos inclusas. Foto extra a R$ 5, sem pacote fechado.
            </p>""",
    """            <h3 class="mt-6 font-display text-xl">Entrega em 24h</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              Suas fotos editadas em até 24 horas úteis depois da escolha.
            </p>""",
)
s = s.replace(
    """            <h3 class="mt-6 font-display text-xl">Pronto antes do Natal</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              Entrega em até 5 dias úteis para presentear e postar no dia 24.
            </p>""",
    """            <h3 class="mt-6 font-display text-xl">Foto extra a R$ 6</h3>
            <p class="mt-3 text-sm leading-relaxed text-cream/60">
              Gostou de mais alguma? Cada foto adicional custa R$ 6, sem pacote fechado.
            </p>""",
)

# 6) secao de opcoes -> pacote unico
ini = s.index("    <!-- OPCOES -->")
fim = s.index("    <!-- AVULSO -->")
novo = """    <!-- PACOTE -->
    <section id="pacote" class="px-6 py-24 md:py-28" style="background: var(--color-surface);">
      <div class="mx-auto max-w-7xl">
        <p class="label mb-4" data-reveal>O ensaio</p>
        <h2 class="max-w-2xl text-balance font-display text-[clamp(2rem,4.4vw,3.4rem)] leading-tight" data-reveal>
          Um preço. Tudo que importa.
        </h2>
        <p class="mt-5 max-w-2xl text-cream/60" data-reveal>
          Sem três opções para escolher e sem taxa escondida. Um ensaio de 30 minutos,
          10 fotos editadas e entrega em 24 horas úteis.
        </p>

        <article class="mx-auto mt-14 max-w-xl border border-gold/60 bg-card p-8" data-reveal>
          <p class="label">30 min · 10 fotos · entrega em 24h úteis</p>
          <h3 class="mt-3 font-display text-3xl">Ensaio de Natal</h3>
          <p class="mt-5 flex items-baseline gap-2">
            <span class="font-sans text-[0.6rem] uppercase tracking-[0.2em] text-champagne">R$</span>
            <span class="font-display text-5xl leading-none">199</span>
          </p>
          <p class="mt-2 text-xs uppercase tracking-[0.12em] text-cream/40">tudo incluso</p>
          <ul class="mt-7 space-y-3 text-sm text-cream/70">
            {[
              '30 minutos no estúdio',
              '1 look · 1 cenário',
              '10 fotos editadas',
              'entrega em até 24h úteis',
              'pet bem-vindo, sem custo',
            ].map((item) => (
              <li class="flex gap-3">
                <span class="mt-2 h-px w-3 shrink-0" style="background: var(--color-champagne);"></span>
                {item}
              </li>
            ))}
          </ul>
          <a
            href={wa('Olá! Quero reservar o ensaio de Natal de R$ 199 🎄')}
            target="_blank"
            rel="noopener"
            class="btn btn-gold mt-9 w-full"
          >
            Quero reservar
          </a>
        </article>

        <p class="mt-10 text-center text-sm text-cream/50" data-reveal>
          Preço de inauguração válido para as primeiras 40 sessões. Depois, R$ 249.
        </p>
      </div>
    </section>

"""
s = s[:ini] + novo + s[fim:]

# 7) FAQ
s = s.replace(
    """  {
    q: 'Quais são as opções?',
    a: 'Presente: 10 fotos por R$ 199. Clássico: 15 fotos por R$ 230. Completo: 20 fotos por R$ 250. Todos com 30 minutos de ensaio.',
  },""",
    """  {
    q: 'O que está incluso?',
    a: 'Ensaio de 30 minutos, 10 fotos editadas e entrega em até 24 horas úteis depois da escolha das fotos. Pet é bem-vindo sem custo extra.',
  },""",
)
s = s.replace(
    "a: 'É o preço de inauguração, válido para as primeiras 40 sessões. Depois sobe para R$ 249, R$ 289 e R$ 319.',",
    "a: 'É o preço de inauguração, válido para as primeiras 40 sessões. Depois passa para R$ 249.',",
)
s = s.replace(
    "a: 'Depende da opção: 10, 15 ou 20. Na escolha, você pode adicionar mais: +5 por R$ 25, +10 por R$ 50, +20 por R$ 100 ou a galeria completa por R$ 350. Cada foto extra sai por R$ 5.',",
    "a: 'O pacote inclui 10 fotos editadas. Se quiser mais, cada foto adicional custa R$ 6 (+5 por R$ 30, +10 por R$ 60). Não é obrigatório.',",
)
s = s.replace(
    "a: 'Individual, casal, grupo ou família. O tempo de ensaio é de 30 minutos.',",
    "a: 'Individual, casal, grupo ou família. O tempo de ensaio é de 30 minutos.',",
)

# 8) CTA final
s = s.replace('<p class="label mb-6">A partir de R$ 199 · 30 min</p>', '<p class="label mb-6">R$ 199 · 30 min · 10 fotos · entrega em 24h</p>')
s = s.replace(
    "Sessões até 20/12 com entrega garantida antes do dia 24.",
    "Sessões até 20/12 com entrega garantida antes do dia 24.",
)

with open(NATAL, "w", encoding="utf-8") as f:
    f.write(s)
print("natal.astro atualizado")

# --- JSON ---
for rel in ("precos-natal.json", "public/precos-natal.json"):
    path = f"{BASE}\\{rel.replace('/', chr(92))}"
    d = json.load(open(path, encoding="utf-8"))
    d["opcoes"] = [{
        "id": "ensaio_natal",
        "nome": "Ensaio de Natal",
        "preco": 199,
        "fotos_inclusas": 10,
        "duracao_minutos": 30,
        "entrega": "24 horas úteis após a escolha das fotos",
        "preco_depois": 249,
        "inclui": [
            "30 minutos de ensaio",
            "1 look, 1 cenário",
            "10 fotos editadas",
            "pet bem-vindo sem custo"
        ]
    }]
    for item in d["avulso"]["fotos"]:
        if item["id"] == "foto_extra":
            item["preco"] = 6
        if item["id"] == "mais_5":
            item["preco"] = 30
        if item["id"] == "mais_10":
            item["preco"] = 60
        if item["id"] == "mais_20":
            item["preco"] = 120
    d["avulso"]["sessao"] = [i for i in d["avulso"]["sessao"] if i["id"] != "entrega_24h"]
    d["politicas"]["entrega_dias_uteis"] = 1
    d["politicas"]["entrega"] = "24 horas úteis após a escolha das fotos"
    d["vigencia"]["sessoes_limite"] = 40
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("JSON:", rel)
