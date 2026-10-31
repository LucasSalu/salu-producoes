# 💍 Salu Produções — Site de Fotografia e Filme de Casamento

> **"A saudade é o passar e o repassar das memórias antigas."** — Machado de Assis *(citação do catálogo oficial)*

Documento de estrutura e planejamento do projeto · **versão 2.3** · Outubro de 2026
Baseado no catálogo `Pacotes Oficial Casamento 2026` + acervo de 306 fotos + dados de contato confirmados
Direção de arte *dark luxury* · Persuasão ética · Infraestrutura 100% gratuita

---

## Sumário

1. [Resumo executivo](#1-resumo-executivo)
2. [O que mudou da v1 para a v2](#2-o-que-mudou-da-v1-para-a-v2)
3. [Posicionamento real (extraído do catálogo)](#3-posicionamento-real-extraído-do-catálogo)
4. [Pacotes e investimento](#4-pacotes-e-investimento)
5. [Identidade visual da marca](#5-identidade-visual-da-marca)
6. [Direção de arte do site: dark luxury](#6-direção-de-arte-do-site-dark-luxury)
7. [Tipografia](#7-tipografia)
8. [Acervo de fotos: inventário](#8-acervo-de-fotos-inventário)
9. [Curadoria do acervo](#9-curadoria-do-acervo)
10. [Banco de imagens (stock)](#10-banco-de-imagens-stock)
11. [Stack tecnológica](#11-stack-tecnológica)
12. [Melhores bibliotecas CSS](#12-melhores-bibliotecas-css)
13. [Melhores plugins e integrações](#13-melhores-plugins-e-integrações)
14. [Templates de referência](#14-templates-de-referência)
15. [Estrutura de pastas](#15-estrutura-de-pastas)
16. [Mapa de páginas](#16-mapa-de-páginas)
17. [Copy e storytelling](#17-copy-e-storytelling)
18. [Persuasão ética em vez de dark patterns](#18-persuasão-ética-em-vez-de-dark-patterns)
19. [Formulário e captação de orçamento](#19-formulário-e-captação-de-orçamento)
20. [Infraestrutura gratuita](#20-infraestrutura-gratuita)
21. [Custos](#21-custos)
22. [SEO, acessibilidade e performance](#22-seo-acessibilidade-e-performance)
23. [Roadmap](#23-roadmap)
24. [Decisões pendentes](#24-decisões-pendentes)
25. [Checklist de conteúdo](#25-checklist-de-conteúdo)
26. [Próximos passos](#26-próximos-passos)
27. [Referências](#27-referências)
28. [Estado atual do projeto](#28-estado-atual-do-projeto)

---

## 1. Resumo executivo

| Item | Definição |
| --- | --- |
| **Marca** | Salu Produções |
| **Negócio real** | **Fotografia e filme de casamento** (não é assessoria/cerimonial) |
| **Promessa** | "Um registro honesto, bem conduzido e pensado para atravessar o tempo" |
| **Objetivo do site** | Gerar pedidos de orçamento qualificados + provar competência pelo portfólio |
| **Ativos disponíveis** | Catálogo com 4 pacotes + 306 fotos (788 MB) + identidade visual (estrela, creme, preto, dourado) |
| **Serviços** | Fotografia **e filme** de casamento (vídeo é serviço próprio, pareado com foto) |
| **Atuação** | **Paulínia (sede) + todo o estado de São Paulo** |
| **Contato** | WhatsApp **(19) 99352-0172** · Instagram **@salu_producoes** |
| **Direção de arte** | Dark luxury: preto + creme + dourado, serifada editorial, estrela como símbolo |
| **Stack** | Astro 7 + Tailwind 4 + GSAP + Lenis + PhotoSwipe |
| **Hospedagem** | Cloudflare Pages (grátis, banda ilimitada, uso comercial permitido) |
| **Custo mensal** | **R$ 0** |
| **Custo único opcional** | Domínio `.com.br` (~R$ 40–100/ano) |

---

## 2. O que mudou da v1 para a v2

| Item | v1 (suposição) | v2 (realidade do material) |
| --- | --- | --- |
| Serviço | Assessoria/cerimonial/decoração | **Fotografia e filme de casamento** |
| Pacotes | Genéricos, "a definir" | **4 pacotes reais com preços** |
| Conteúdo visual | Fotos de banco até ter acervo | **306 fotos próprias** já disponíveis |
| Paleta | Preto + dourado | Preto + **creme** + dourado (identidade do catálogo) |
| Símbolo | Não definido | **Estrela/asterisco** da marca |
| Páginas | Sem página de preços | **Página de pacotes é obrigatória** |
| Vídeo | Hero em vídeo | Hero em **foto** (não há vídeos no acervo) |
| Biblioteca de animação | Genérica | **GSAP agora é 100% gratuito**, todos os plugins |
| Template | Do zero | Recomendação com **referências prontas** |

---

## 3. Posicionamento real (extraído do catálogo)

### 3.1 O que está escrito no catálogo

> "A Salu Produções trabalha com fotografia e filme de casamento para que o casal viva o dia com tranquilidade.
> Chegamos ao casamento com tudo alinhado, acompanhamos com discrição e cuidamos da memória com atenção e responsabilidade.
> Um registro honesto, bem conduzido e pensado para atravessar o tempo."

### 3.2 A grande ideia do site

> **Não vendemos fotos. Guardamos o dia para sempre.**

O concorrente vende "cobertura fotográfica". A Salu vende **tranquilidade no dia** + **memória que atravessa o tempo**. Isso muda o site: menos "pacote e preço", mais **prova de olhar** e **confiança no processo**.

### 3.3 Pilares da comunicação

| Pilar | Como aparece no site |
| --- | --- |
| **Tranquilidade** | "Você curte o dia. A gente cuida da memória." |
| **Discrição** | Bastidores: como a equipe trabalha sem interferir |
| **Honestidade do registro** | Edição premium, sem "fotos plastificadas" |
| **Longevidade** | Álbum físico + galeria online + pendrive personalizado |
| **Olhar autoral** | Portfólio forte, casais reais, ensaios reais |

### 3.4 Público

- Noivos de 25–40 anos, classe A/B, que valorizam estética e querem se sentir seguros
- Quem já tem referências (Instagram/Pinterest) e compara fotógrafos
- Quem está fechando fornecedores com 6–18 meses de antecedência
- Decisão emocional, mas com pesquisa racional de preço e portfólio

### 3.5 Serviço e área de atuação

| Item | Definição |
| --- | --- |
| **Serviços** | Fotografia + **filme** de casamento (o vídeo é serviço próprio, com pacote e preço) |
| **Atuação** | **Paulínia** (sede) + **todo o estado de São Paulo** |
| **WhatsApp** | (19) 99352-0172 → link `https://wa.me/5519993520172` |
| **Instagram** | @salu_producoes → `https://instagram.com/salu_producoes` |

> O botão flutuante de WhatsApp deve apontar para `https://wa.me/5519993520172?text=...` com mensagem pré-preenchida (ex.: "Olá! Vi o site e quero um orçamento para meu casamento."). Isso aumenta a conversão porque o casal não precisa digitar nada.

---

## 4. Pacotes e investimento

### 4.1 O que o catálogo oferece

| Pacote | O que inclui | Parcelado | À vista |
| --- | --- | --- | --- |
| **BRONZE** | Fotografia: cobertura do casamento e festa · seleção das melhores imagens · edição premium · galeria online + pendrive personalizado | 10× R$ 199 = **R$ 1.990** | **R$ 1.790** (−10%) |
| **PRATA** | Fotografia: dia da noiva + casamento · seleção + edição premium · **mini álbum** · galeria online + pendrive | 10× R$ 350 = **R$ 3.500** | **R$ 3.000** (−15%) |
| **OURO** | Fotografia: dia da noiva + noivo · seleção + edição premium · **álbum premium** · galeria online + pendrive · **sessão pré-wedding** | 10× R$ 470 = **R$ 4.700** | **R$ 4.199** |
| **PROMOÇÃO** (p. 17) | Fotografia "casamento completo": pré-wedding, making of, cerimônia e festa — **oferta de entrada para casamentos de baixo ticket** | — | **de R$ 3.000 por R$ 1.999** |

> ℹ️ O pacote **CASA não entra no site** — foi criado para amigos. Fica fora de pacotes, formulário e qualquer menção pública.
> ⚠️ A única inconsistência que sobra: o PRATA anuncia "−15%", mas R$ 3.000 sobre R$ 3.500 é −14,3% (R$ 25 de diferença). Ajuste o percentual ou o valor.

### 4.2 Referência de mercado — 2026

**Fotografia de casamento** (Freelans, jun/2026):

| Tipo de cobertura | Faixa de mercado |
| --- | --- |
| Civil simples (1–3 h) | R$ 400 – 1.500 |
| Mini wedding / elopement (2–6 h) | R$ 800 – 3.500 |
| Casamento tradicional (8–12 h) | R$ 3.000 – 8.500 |
| Premium / equipe completa | R$ 8.500 – 15.000+ |
| Ensaio pré-wedding avulso | R$ 500 – 1.500 |

> A maioria dos casais investe entre **R$ 2.500 e R$ 7.500**. No interior de São Paulo os valores tendem ao piso da faixa — Paulínia e região ficam nesse recorte.

**Filmagem de casamento** (NatalStudios, 2026):

| Nível | Faixa de mercado |
| --- | --- |
| Teaser simples (3–5 min, 1 câmera) | R$ 1.800 – 3.000 |
| Filme completo (cerimônia + festa, 2 câmeras, 15–40 min) | R$ 3.000 – 7.000 |
| Produção premium (drone, same day edit, múltiplas câmeras) | R$ 7.000 – 15.000+ |

> Drone soma R$ 500–1.500. **Combo foto + vídeo costuma sair 15–25% mais barato** que contratar separado — e é o argumento mais forte para vender os dois juntos.

### 4.3 Diagnóstico: onde os pacotes atuais estão

| Pacote | Escopo | Preço | Leitura de mercado | Veredito |
| --- | --- | --- | --- | --- |
| **BRONZE** | Fotografia: casamento + festa (dia inteiro) | R$ 1.990 | Tradicional começa em R$ 3.000 | ⚠️ **Barato demais** para prometer "dia inteiro" |
| **PRATA** | Dia da noiva + cerimônia + festa + mini álbum | R$ 3.500 | Faixa R$ 3.000–5.000 | ✅ Competitivo (boa porta de entrada) |
| **OURO** | Completo + álbum premium + pré-wedding | R$ 4.700 | Faixa R$ 4.000–6.500 | ✅ Melhor custo-benefício da escada |
| **PROMOÇÃO** | Completo (pré + making of + cerimônia + festa) | R$ 1.999 | — | ✅ Faz sentido como **isca de baixo ticket** — mas entrega mais que o BRONZE |

**Atenção a um detalhe:** a PROMOÇÃO (R$ 1.999) entrega pré-wedding + making of, enquanto o BRONZE (R$ 1.990) entrega só casamento + festa. Se as duas ficarem no ar sem prazo, o casal sempre escolhe a promoção e o BRONZE vira letra morta. Dê à promoção um **prazo ou limite real de vagas** e mantenha o BRONZE como pacote padrão.

**Sobre o BRONZE a R$ 1.990:** como porta de entrada, o preço baixo pode ser estratégia. Mas chamá-lo de "cobertura completa" nesse valor desvaloriza a marca — ou limite o escopo (ex.: até 6 h), ou assuma que é oferta de entrada.

### 4.4 Proposta de escada (para você aprovar)

**Mantém os seus preços onde eles já estão certos** e corrige só o que está fora da faixa:

| Pacote | Escopo | Parcelado | À vista |
| --- | --- | --- | --- |
| **BRONZE** | Cobertura do casamento e festa · galeria online + pendrive | 10× R$ 199 = R$ 1.990 | R$ 1.790 |
| **PROMOÇÃO** | Casamento completo: pré-wedding + making of + cerimônia + festa (oferta de entrada) | — | R$ 1.999 |
| **PRATA** | Dia da noiva + cerimônia + festa · mini álbum · galeria + pendrive | 10× R$ 350 = R$ 3.500 | R$ 3.000 |
| **OURO** | Dia completo noiva + noivo · álbum premium · pré-wedding · galeria + pendrive | 10× R$ 470 = R$ 4.700 | R$ 4.199 |
| **ATELIER** *(novo, opcional)* | Ouro + 2º fotógrafo + álbum grande + filme teaser | 10× R$ 690 = R$ 6.900 | R$ 6.210 |

**Vídeo (Opção A aprovada — detalhes na seção 4.5):**

| Pacote | Escopo | Parcelado | À vista |
| --- | --- | --- | --- |
| **Filme Essencial** | Teaser de 3–5 min + cerimônia · 1 câmera · áudio dedicado | 10× R$ 240 = R$ 2.400 | R$ 2.160 |
| **Filme Completo** | Cerimônia + festa · 2 câmeras · áudio · filme de 15–30 min + teaser | 10× R$ 420 = R$ 4.200 | R$ 3.780 |
| **Combo Ouro + Filme Completo** | Ouro + Filme Completo | **R$ 7.590** (−15% sobre R$ 8.900) | R$ 7.190 |

**Por que isso funciona:**

1. **BRONZE fica como você definiu** (cobertura do casamento e festa a R$ 1.990) — é a porta de entrada da escada.
2. **A PROMOÇÃO tem papel claro**: é a isca de baixo ticket, com pré-wedding incluso. Para não canibalizar o resto, precisa de prazo ou limite real de vagas.
3. **ATELIER a R$ 6.900** (opcional) cria uma âncora acima do Ouro e captura casais de maior poder aquisitivo.
4. **Vídeo com preço próprio** — porque hoje ele não tem preço nem oferta no catálogo.
5. **O combo é a oferta principal do site**: maior ticket e melhor argumento ("equipe única, identidade visual única").

> 💡 Os valores de ATELIER e dos filmes são **recomendação**, não decisão. BRONZE, PRATA, OURO e PROMOÇÃO ficam exatamente como você definiu.

### 4.5 Como o vídeo entra no site (Opção A — aprovada)

O vídeo entra como **serviço próprio, com preço público**, e também como adicional dos pacotes de foto:

| Pacote | O que entrega | Parcelado | À vista |
| --- | --- | --- | --- |
| **Filme Essencial** | Teaser de 3–5 min + cerimônia · 1 câmera · áudio dedicado | 10× R$ 240 = R$ 2.400 | R$ 2.160 |
| **Filme Completo** | Cerimônia + festa · 2 câmeras · áudio · filme de 15–30 min + teaser | 10× R$ 420 = R$ 4.200 | R$ 3.780 |
| **Combo Ouro + Filme Completo** | Ouro + Filme Completo (15% de desconto) | **R$ 7.590** | R$ 7.190 |

**Como o site apresenta:**

- Seção **Filme** na home, entre Portfólio e Números, com 2–3 vídeos e CTA "quero foto + filme"
- Página **/filmes** com o portfólio completo
- No card de cada pacote de foto, um botão discreto "adicionar filme"
- No formulário, o campo "Quer filme/vídeo?" passa a ser obrigatório

**Por que preço público (e não "sob consulta"):**

- O casal vê que existe e consegue somar ao orçamento sozinho
- O combo eleva o ticket de R$ 4.700 para R$ 7.590
- O mercado já pratica esses valores (teaser R$ 1.800–3.000; filme completo R$ 3.000–7.000), então não há risco de assustar

### 4.6 Como apresentar no site (sem parecer tabela de supermercado)

- **Cards editoriais**, um por pacote, com foto de fundo e nome em serifada
- **"A partir de"** no card, valor cheio no detalhe (reduz o impacto do número)
- **Destaque no OURO** com selo "Mais escolhido"; o **ATELIER** (se entrar) funciona como âncora de preço
- **Combo Foto + Filme em destaque** — é a oferta de maior ticket e maior margem
- **PROMOÇÃO com prazo real** — se tiver data ou vagas, mostrar; se não tiver, não inventar contagem
- **CTA por pacote**: "Quero este pacote" → formulário já com o pacote pré-selecionado
- **Comparativo simples**: o que muda entre BRONZE → PRATA → OURO (álbum, pré-wedding, horas)

### 4.7 O que o site deve dizer sobre preço

> "Os valores variam conforme data, local e duração. Os pacotes acima são o ponto de partida — o orçamento final é feito sob medida para o seu casamento."

Isso é honesto, protege a margem e evita que o casal trate o valor como preço fechado.

---

## 5. Identidade visual da marca

### 5.1 O que já existe (do catálogo)

| Elemento | Descrição |
| --- | --- |
| **Símbolo** | Estrela/asterisco de 8 pontas, preta, dentro de um selo creme com grade radial sutil |
| **Cor principal** | Creme/off-white `#F2F0E9` |
| **Cor secundária** | Preto `#0B0B0C` |
| **Acento** | Dourado champanhe `#D4AF37` (usado nos destaques de preço) |
| **Tipografia** | Serifada de alto contraste, estilo Didot/Playfair (títulos) + sans neutra (apoio) |
| **Tom** | Editorial, calmo, sofisticado, com muito respiro |

### 5.2 A evolução para o site

O catálogo é **claro** (creme). O site será **escuro** por decisão sua — mas sem perder a marca:

| Uso | Catálogo | Site |
| --- | --- | --- |
| Fundo | Creme | **Preto profundo** |
| Texto | Preto | **Creme** |
| Acento | Preto/dourado | **Dourado** |
| Seções claras | — | **Página de pacotes em creme** (espelha o catálogo) |
| Símbolo | Selo creme | **Estrela dourada** sobre preto |

> A página de pacotes em fundo creme é o "espelho" do catálogo: quem chega de um PDF reconhece a marca imediatamente. O resto do site é dark. Isso dá ritmo e evita monotonia.

---

## 6. Direção de arte do site: dark luxury

### 6.1 Paleta

| Token | HEX | Uso |
| --- | --- | --- |
| `--bg` | `#0A0A0B` | Fundo principal |
| `--surface` | `#131315` | Seções alternadas |
| `--card` | `#1B1B1F` | Cards |
| `--cream` | `#F2F0E9` | Texto principal e seções claras |
| `--gold` | `#C9A227` | Acento (linhas, ícones, detalhes) |
| `--champagne` | `#E8D5A8` | Texto dourado com bom contraste |
| `--muted` | `#9C9A96` | Texto secundário |
| `--line` | `rgba(232, 213, 168, 0.16)` | Divisórias de 1px |

### 6.2 Princípios

- **Preto como palco**: a foto é a protagonista; o fundo escuro faz a luz do casamento brilhar
- **Dourado como joia**: usar pouco — linhas, ícones, hover, números
- **Creme como respiro**: seções claras pontuais (pacotes, depoimentos) quebram o dark
- **A estrela como assinatura**: aparece no logo, como marca d'água sutil e em transições
- **Movimento lento**: revelações suaves, parallax discreto, nada de "pisca-pisca"
- **Muito espaço**: luxo é silêncio visual

### 6.3 Efeitos (com moderação)

- Grain/ruído fino sobre o fundo (textura de filme)
- Linhas douradas de 1px separando blocos
- Vinheta suave nas fotos
- Header com blur ao rolar
- Hover com zoom lento (1.03×) e brilho dourado
- **Evitar**: neon, gradientes coloridos, sombras pesadas, carrossel automático

### 6.4 Estrutura de uma seção

```
┌──────────────────────────────────────────────┐
│  01 — PORTFÓLIO                              │ ← label em versalete dourado
│                                              │
│  Casais reais,                              │ ← título serifado grande
│  histórias que ficam.                       │
│                                              │
│  [ grid de fotos com zoom no hover ]        │
└──────────────────────────────────────────────┘
```

---

## 7. Tipografia

### 7.1 Recomendação principal (continuidade com o catálogo)

| Papel | Fonte | Por quê |
| --- | --- | --- |
| **Títulos** | **Playfair Display** | É a família com o mesmo DNA da serifada do catálogo |
| **Alternativa editorial** | **Bodoni Moda** | Contraste ainda mais alto, cara de revista de moda |
| **Alternativa delicada** | **Cormorant Garamond** | Mais leve e romântica |
| **Script (acento)** | **Great Vibes** | Nome do casal, assinatura, "Salu" |
| **Corpo/UI** | **Jost** | Geométrica, moderna, ótima em fundo escuro |

### 7.2 Alternativas gratuitas

| Papel | Opções |
| --- | --- |
| Serifada display | Playfair Display · Bodoni Moda · Cormorant Garamond · Marcellus · Cinzel · Italiana |
| Script | Great Vibes · Parisienne · Italianno · Pinyon Script · Allura |
| Sans | Jost · Montserrat · Inter · Outfit · Manrope |
| Fora do Google Fonts | Fontshare: **Zodiak**, **Gambetta**, **Sentient**, **General Sans** (grátis para uso comercial) |

### 7.3 Regras técnicas

- Self-host com **Fontsource** (sem requisição ao Google, melhor privacidade e performance)
- Subset `latin` + `latin-ext`; pré-carregar só 2 arquivos
- `font-display: swap`
- Títulos: `clamp(2.4rem, 6vw, 5rem)`, `letter-spacing` levemente negativo
- Versaletes/labels: `letter-spacing: 0.14em`, `text-transform: uppercase`
- Corpo: 17–18px, `line-height: 1.7` (dark mode pede texto maior)
- Máximo **3 famílias** no site
- Script só em palavras curtas, nunca em parágrafos

---

## 8. Acervo de fotos: inventário

### 8.1 Números reais

| Métrica | Valor |
| --- | --- |
| Arquivos de imagem | **306** |
| Peso total | **788,5 MB** |
| Retrato (vertical) | **207** (68%) |
| Paisagem (horizontal) | **95** (31%) |
| Quadradas | **4** |
| Alta resolução (≥ 3000 px) | **76** |
| Boa resolução (2000–2999 px) | **229** |
| Resolução baixa (< 2000 px) | **1** |
| Nomes base únicos | **224** |
| Arquivos duplicados (extra) | **82** (em 54 grupos) |
| Cópias idênticas (mesmo byte) | **3 grupos** |
| Pastas | raiz (281) + **`joyce & Marcos`** (25) |

### 8.2 Leitura do acervo

- **Qualidade**: ótima — 75% em 2000 px+, luz natural, ensaios e casamentos reais
- **Formato**: maioria vertical, ideal para grid editorial, stories e retratos
- **Ponto forte**: já existe um **casamento completo** (`joyce & Marcos`) — vira estudo de caso
- **Problema**: 82 arquivos repetidos sem padrão de nome (`-2`, `(1)`, `~2`) — precisa de limpeza
- **Faltando**: fotos horizontais de cerimônia para o hero e vídeos (o catálogo cita "vídeos trend", mas não há arquivos de vídeo na pasta)

### 8.3 O que o acervo permite fazer hoje

| Uso no site | Status |
| --- | --- |
| Grid de portfólio | ✅ ótimo (muitas verticais) |
| Hero em tela cheia | ⚠️ funciona com vertical (object-fit), melhor com horizontal |
| Estudo de caso Joyce & Marcos | ✅ 25 fotos, pronto |
| Seção "sobre" | ✅ retratos de casais disponíveis |
| Vídeo de abertura | ❌ nenhum vídeo no acervo |
| Fotos de bastidores da equipe | ❌ não identificadas |

---

## 9. Curadoria do acervo

### 9.1 Meta: de 306 para ~32 fotos no site

| Destino | Quantidade | Critério |
| --- | --- | --- |
| Hero | 1–2 | Impacto imediato, luz bonita, espaço para texto |
| Seção sobre | 2–3 | Retratos com emoção, bastidores |
| Portfólio (home) | 8–10 | Variedade de casais, luz e momentos |
| Página de portfólio | 18–24 | Seleção ampliada, por casamento |
| Estudo de caso Joyce & Marcos | 15–20 | Sequência narrativa (preparo → cerimônia → festa) |
| Pacotes | 4 | Uma foto por pacote, coerente com o que ele entrega |
| Depoimentos | 3 | Rosto do casal que depõe |

### 9.2 Fluxo de curadoria

1. **Deduplicar** — remover os 82 repetidos (manter a melhor versão de cada)
2. **Renomear** no padrão `casal-ano-local-01.jpg` (ex.: `joyce-marcos-2025-01.jpg`)
3. **Selecionar** — nota de 1 a 5 por foto; usar só 4 e 5
4. **Tratar** — correção leve de cor, sem "plastificar"
5. **Exportar** — AVIF/WebP em 3 larguras (640 / 1280 / 1920 px)
6. **Descrever** — alt text real (SEO + acessibilidade)
7. **Autorizar** — confirmar permissão de uso de imagem de cada casal

### 9.3 Regras de imagem para o site

- **Nunca** subir o original: 788 MB derrubaria o site
- Meta: home inteira **< 2 MB** de imagens (lazy loading)
- Hero: 1920 px, AVIF ~200 KB
- Grid: 640/1280 px, AVIF ~60–120 KB cada
- `width`/`height` sempre definidos (evita layout shift)
- `loading="lazy"` em tudo abaixo da dobra
- `object-position` ajustado foto a foto (rosto nunca cortado)

### 9.4 Direitos de imagem (LGPD)

- Guardar autorização escrita (ou e-mail) de cada casal para uso no site e redes
- Ter um caminho de remoção rápida caso alguém peça para sair
- Não publicar foto de convidado identificável sem contexto do evento
- Não usar fotos de outros fotógrafos sem licença

---

## 10. Banco de imagens (stock)

Você autorizou usar banco de imagens — ótimo como **complemento**, nunca como substituto do acervo real.

### 10.1 Onde buscar (grátis, uso comercial)

| Banco | Licença | Melhor para |
| --- | --- | --- |
| **Unsplash** | Unsplash License (livre, comercial) | Fotos editoriais de casamento, luz natural |
| **Pexels** | Pexels License (livre, comercial) | Cerimônias, detalhes, decoração |
| **Pixabay** | Pixabay License | Texturas, fundos, detalhes |

> Sempre confira a licença na página da foto e evite pessoas reconhecíveis em contexto sensível.

### 10.2 Termos de busca úteis

- `bride getting ready window light`
- `wedding ceremony golden hour`
- `wedding rings detail macro`
- `couple portrait field sunset`
- `wedding reception candles night`
- `bride veil wind portrait`

### 10.3 Onde usar stock (e onde não)

| Usar | Não usar |
| --- | --- |
| Texturas, fundos, detalhes (alianças, convite, flores) | Retratos de "casais" como se fossem clientes |
| Hero provisório até ter a foto ideal | Portfólio (quebra a confiança) |
| Blog/SEO (dicas para noivos) | Depoimentos |

**Regra:** portfólio e depoimentos só com material real. Stock em portfólio é o tipo de coisa que o casal descobre e não perdoa.

---

## 11. Stack tecnológica

### 11.1 Versões atuais (verificadas em outubro/2026)

| Ferramenta | Versão | Observação |
| --- | --- | --- |
| **Astro** | **7.4.4** | Exige Node ≥ 22.23.4 |
| **Tailwind CSS** | **4.3.3** | Configuração via CSS (`@theme`), sem `tailwind.config.js` |
| **GSAP** | 3.x | **100% gratuito, todos os plugins** (desde a aquisição pela Webflow) |
| **Node local** | 24.21.0 | ✅ compatível |
| **pnpm local** | 11.28.5 | ✅ compatível |

### 11.2 Stack final

```
Astro 7 (SSG) + TypeScript
├── Tailwind CSS 4.3           → estilos (config no CSS)
├── GSAP 3 + ScrollTrigger     → animações de scroll e texto
├── Lenis                      → smooth scroll
├── PhotoSwipe 5               → lightbox da galeria
├── Splide                     → carrossel de depoimentos
├── Motion (opcional)          → micro-interações em islands React
├── Fontsource                 → fontes self-hosted
├── Sharp (astro:assets)       → imagens AVIF/WebP
├── Web3Forms                  → formulário sem backend
└── Cloudflare Pages           → deploy + CDN grátis
```

### 11.3 Por que Astro (e não Next.js)

| Critério | Astro | Next.js |
| --- | --- | --- |
| Vitrine/portfólio | ✅ ideal | ✅ possível |
| JS enviado ao cliente | Mínimo | Maior |
| SEO e LCP | Nativo | Configurável |
| Hospedagem grátis com uso comercial | ✅ Cloudflare Pages | ❌ Vercel Hobby proíbe uso comercial |
| Curva de manutenção | Baixa | Média |

---

## 12. Melhores bibliotecas CSS

### 12.1 Veredito

| Biblioteca | Usar? | Papel | Por quê |
| --- | --- | --- | --- |
| **Tailwind CSS 4.3** | ✅ **Base** | Utilitários | Design sob medida rápido, sem CSS morto, ótimo com Astro |
| **DaisyUI 5** | ⚠️ Opcional | Componentes | Acelera form/accordion, mas impõe visual — usar só se o tempo apertar |
| **Open Props** | ⚠️ Opcional | Tokens CSS | Boa base de variáveis; o projeto já terá tokens próprios |
| **UnoCSS** | ❌ | Utilitários | Redundante com Tailwind; seria troca, não adição |
| **Bootstrap 5** | ❌ | Framework | Visual genérico, CSS pesado, difícil de "customizar para luxo" |
| **Bulma** | ❌ | Framework | Parado no tempo, sem ecossistema Astro |
| **Animate.css** | ❌ | Classes prontas | Só para protótipo; animação de verdade é GSAP |
| **AOS** | ❌ | Scroll reveal | Datado e pesado; GSAP/IntersectionObserver resolvem melhor |

**Decisão:** Tailwind puro + componentes próprios. O visual é o diferencial da marca — não dá para terceirizar para um kit genérico.

### 12.2 Como organizar o CSS

```
src/styles/global.css
├── @import "tailwindcss"
├── @theme { --color-bg, --color-gold, --font-display ... }   ← tokens
├── @layer base { html, body, selection, scrollbar }
├── @layer components { .btn-gold, .card, .section-label }
└── @layer utilities { .text-balance, .grain }
```

---

## 13. Melhores plugins e integrações

### 13.1 Animação e interação

| Plugin | O que faz | Prioridade |
| --- | --- | --- |
| **GSAP + ScrollTrigger** | Parallax, pin de seção, revelação de texto, sequências | 🔴 Alta |
| **GSAP SplitText** | Quebra título em letras/palavras para animar | 🔴 Alta (agora grátis) |
| **Lenis** | Scroll com inércia (sensação premium) | 🔴 Alta |
| **PhotoSwipe 5** | Lightbox com zoom, teclado, gestos | 🔴 Alta |
| **Splide** | Carrossel leve de depoimentos | 🟡 Média |
| **Motion** | Micro-interações em React islands | 🟡 Média |
| **Swup** | Transição entre páginas sem recarregar | 🟢 Baixa |

### 13.2 Integrações Astro

| Pacote | Função |
| --- | --- |
| `@astrojs/sitemap` | Sitemap automático |
| `@astrojs/cloudflare` | Adapter para Cloudflare Pages |
| `@astrojs/mdx` | Conteúdo em Markdown enriquecido |
| `astro-icon` | Ícones (Lucide, Phosphor) |
| `astro-seo` | Meta tags e Open Graph |
| `@fontsource/playfair-display` etc. | Fontes self-hosted |
| `@astrojs/partytown` | Scripts de terceiros fora da thread principal |
| `decap-cms` | Painel para você editar textos e fotos sem código |
| `@astrojs/rss` | Feed (se criar blog) |

### 13.3 O que **não** usar

| Evitar | Motivo |
| --- | --- |
| jQuery | Desnecessário em 2026 |
| Slider automático no hero | Tira o controle e atrapalha o LCP |
| Pop-up de "assine a newsletter" na entrada | Bloqueia a experiência e derruba conversão |
| Música automática | Sustos e acessibilidade |
| Player de vídeo pesado no topo | LCP ruim; usar poster + clique |
| Google Fonts via CDN | Privacidade e performance; usar Fontsource |

---

## 14. Templates de referência

Não vamos usar um template pronto como base (o design é o diferencial), mas vale estudar e **usar como referência** de estrutura, ritmo e seções.

### 14.1 Templates de casamento (Framer) — referência de estrutura

| Template | Preço | Por que olhar |
| --- | --- | --- |
| **Kenzie Lake Photos** | Grátis | Site de fotógrafa: hero full-screen, galerias, preços, "conheça a fotógrafa", contato |
| **Celluloid** | Grátis | Feito para filmmakers: cada filme com página, player, créditos |
| **CÉLESTE** | US$ 99 | Editorial premium para fotógrafo/estúdio de alto padrão |
| **Still & Vow** | US$ 11 | Image-led, 8 páginas, fluxo de contato pronto |
| **Eloria** | Grátis | Referência de "processo" e depoimentos (para a parte de confiança) |

### 14.2 Temas Astro — referência técnica

| Tema | Preço | Por que olhar |
| --- | --- | --- |
| **Astro Photo Folio** | Grátis | Grid de fotos, lightbox, foco em imagem |
| **Horizon** | Grátis | Estrutura limpa de portfólio |
| **Aperture / Drift** (AeroLaunch) | US$ 49 | Fotografia com índice de trabalho e galeria em colunas |

### 14.3 Decisão

**Construir sob medida em Astro**, usando:
- do **Kenzie Lake** e **CÉLESTE**: a estrutura de páginas e o ritmo editorial
- do **Celluloid**: a ideia de página por filme (quando houver vídeos)
- do **Astro Photo Folio**: a mecânica de grid + lightbox

**Plano B (sem código):** se em algum momento você preferir não manter código, um template Framer gratuito (Kenzie Lake) resolve — mas perde controle de SEO fino e fica preso ao plano do Framer.

---

## 15. Estrutura de pastas

```
salu-producoes/
├── .github/workflows/deploy.yml
├── public/
│   ├── favicon.svg                 # estrela da marca
│   ├── og-image.jpg                # 1200×630
│   └── robots.txt
├── src/
│   ├── assets/
│   │   ├── fotos/                  # originais curados (o Astro otimiza)
│   │   ├── logos/                  # estrela em SVG
│   │   └── videos/                 # quando houver
│   ├── components/
│   │   ├── layout/  Header · Footer · WhatsAppFloat
│   │   ├── ui/      Button · SectionLabel · GoldLine · Reveal · StarMark
│   │   ├── sections/ Hero · Manifesto · Servicos · Portfolio · Pacotes
│   │   │             · Processo · Depoimentos · Faq · Orcamento
│   │   └── portfolio/ Galeria · Lightbox
│   ├── content/                     # Content Collections
│   │   ├── pacotes/
│   │   ├── depoimentos/
│   │   ├── portfolio/              # um casamento por arquivo
│   │   └── faq/
│   ├── layouts/Base.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── portfolio.astro
│   │   ├── portfolio/[slug].astro  # estudo de caso
│   │   ├── pacotes.astro           # fundo creme (espelho do catálogo)
│   │   ├── sobre.astro
│   │   ├── orcamento.astro
│   │   ├── obrigado.astro
│   │   └── 404.astro
│   ├── lib/ seo.ts · schema.ts · analytics.ts
│   ├── styles/global.css
│   └── consts.ts
├── tools/                          # scripts de apoio (fora do build)
├── astro.config.mjs
├── tsconfig.json
├── package.json
└── README.md
```

> **Importante:** a pasta `tools/` e os arquivos originais (`melhores fotos/`, PDF) ficam **fora** do build. O Astro só publica o que está em `public/` e o que é importado de `src/assets/`.

---

## 16. Mapa de páginas

### 16.1 Home — a experiência

| # | Seção | Objetivo | Conteúdo |
| --- | --- | --- | --- |
| 01 | **Hero** | Impacto imediato | Foto full-screen, logo/estrela, H1, sub, 2 CTAs |
| 02 | **Faixa** | Ritmo | "TRANQUILIDADE · OLHAR · MEMÓRIA · DETALHE" |
| 03 | **Manifesto** | Conexão | Texto do catálogo + foto |
| 04 | **Serviços** | Clareza | Fotografia, Filme, Pré-wedding, Álbum |
| 05 | **Portfólio** | Prova | Grid 8–10 fotos, hover, "ver todos" |
| 06 | **Números** | Prova objetiva | Casamentos, anos, casais — só reais |
| 07 | **Pacotes** | Conversão | Bronze, Prata, Ouro, Promoção + filmes + combo |
| 08 | **Processo** | Reduz medo | 5 passos: conversa → proposta → ensaio → o dia → entrega |
| 09 | **Depoimentos** | Prova emocional | 3–6 casais |
| 10 | **FAQ** | Objeções | 6–8 perguntas |
| 11 | **Orçamento** | Conversão | Formulário + WhatsApp |
| 12 | **Footer** | Fecho | Contato, Instagram, Paulínia/SP |

> **Com vídeo:** inserir a seção **Filme** entre Portfólio (05) e Números (06) — um player com o reel do ano + CTA "quero foto + filme". O filme é o serviço que mais eleva o ticket, então merece destaque próprio na home, não só um card em Serviços.

### 16.2 Páginas internas

| Página | Papel |
| --- | --- |
| `/portfolio` | Galeria completa, filtros por ano/casal |
| `/portfolio/joyce-e-marcos` | Estudo de caso com narrativa |
| `/filmes` | Portfólio de filmes e teasers (quando os vídeos chegarem) |
| `/pacotes` | Preços detalhados, comparativo, FAQ de contratação — **fundo creme** |
| `/sobre` | História, olhar, bastidores, equipe |
| `/orcamento` | Formulário dedicado |
| `/obrigado` | Confirmação + WhatsApp |
| `/404` | Erro com o mesmo clima |

### 16.3 Wireframe do hero

```
┌────────────────────────────────────────────────────────────┐
│  ✦ SALU PRODUÇÕES      PORTFÓLIO  PACOTES  SOBRE  [ORÇAMENTO] │
│                                                              │
│              ── FOTOGRAFIA E FILME DE CASAMENTO ──           │
│                                                              │
│           O dia passa.                                │ ← Playfair enorme
│           A memória fica.                             │
│                                                              │
│              Salu Produções · [cidade]                       │ ← Great Vibes
│                                                              │
│        [ QUERO MEU ORÇAMENTO ]    [ VER PORTFÓLIO ]           │
│                                                              │
│                        ↓ scroll                              │
└────────────────────────────────────────────────────────────┘
   foto full-screen · overlay preto 55% · grain · estrela dourada
```

---

## 17. Copy e storytelling

### 17.1 Headlines (escolher 1 + testar 2)

1. **"O dia passa. A memória fica."**
2. "Um registro honesto para atravessar o tempo."
3. "Você vive o dia. A gente guarda para sempre."
4. "Não é sobre fotos bonitas. É sobre lembrar de como foi."
5. "A saudade começa no dia seguinte. A gente cuida dela."

> A opção 1 conversa direto com a citação do Machado de Assis que já está no catálogo — ótima para coerência de marca.

### 17.2 Subheadline

> "Fotografia e filme de casamento com tranquilidade, discrição e um olhar que atravessa gerações."

### 17.3 CTAs

| Contexto | Texto |
| --- | --- |
| Hero | **Quero meu orçamento** |
| Hero (secundário) | Ver portfólio |
| Após pacotes | Quero este pacote |
| Final | **Solicitar orçamento sem compromisso** |
| Flutuante | Falar no WhatsApp |

### 17.4 Manifesto (rascunho)

> Todo casamento tem um dia.
> E todo dia tem detalhes que ninguém vê: a mão que treme, o abraço antes de entrar, o riso na hora errada.
>
> A Salu Produções existe para que nada disso se perca.
> Chegamos com tudo alinhado, acompanhamos com discrição e cuidamos de cada imagem como se fosse da nossa própria família.
>
> Você não precisa se preocupar com a foto.
> Você só precisa viver o dia.
> O resto é com a gente.

### 17.5 Microcopy de confiança

- "Resposta em até 24 h úteis."
- "Primeira conversa gratuita, sem compromisso."
- "Contrato claro, escopo definido, sem surpresa."
- "Atendemos [cidade/região] e casamentos fora da cidade."
- "Galeria online + pendrive personalizado em todos os pacotes."

---

## 18. Persuasão ética em vez de dark patterns

### 18.1 O combinado

Como definimos: **nada de padrão escuro que engana**. O tema é escuro; a conduta é clara. Para fotografia de casamento, isso é ainda mais decisivo — o casal entrega o dia inteiro a você.

### 18.2 Substituições

| ❌ Dark pattern | ✅ Alternativa ética |
| --- | --- |
| Contagem regressiva falsa | **Agenda real**: "datas de [mês] ainda disponíveis" |
| "Últimas vagas!" inventado | **Limite real** de casamentos por mês |
| Depoimento fabricado | **Depoimentos reais** com autorização |
| Preço escondido | **Faixas e pacotes transparentes** |
| Urgência artificial | **Prazo real** de fechamento para datas concorridas |
| Opt-in pré-marcado | Consentimento **desmarcado** + LGPD |
| FOMO inventado | **Portfólio real** (que já é forte) |

### 18.3 Gatilhos legítimos para este negócio

| Gatilho | Aplicação |
| --- | --- |
| **Prova** | Portfólio vasto e casais reais |
| **Autoridade** | Anos de estrada, casamentos entregues, parcerias |
| **Afinidade** | Rosto da Salu, bastidores, tom próximo |
| **Redução de risco** | "Você só decide depois de conversar" |
| **Escassez honesta** | Agenda real de datas |
| **Reciprocidade** | Guia gratuito: *"O que perguntar ao fotógrafo antes de contratar"* (PDF) |

---

## 19. Formulário e captação de orçamento

### 19.1 Campos

| Campo | Tipo | Obrigatório |
| --- | --- | --- |
| Nome | texto | ✅ |
| E-mail | email | ✅ |
| WhatsApp | tel | ✅ |
| Data do casamento | date | ✅ (+ "não definimos") |
| Cidade / local | texto | ✅ |
| Nº de convidados | select | ✅ |
| **Pacote de interesse** | select (Bronze/Prata/Ouro/Promoção/Ainda não sei) | ⬜ |
| **Quer filme/vídeo?** | select (sim/não/talvez) | ⬜ |
| Como nos conheceu | select | ⬜ |
| Conte sobre o casamento | textarea | ⬜ |
| Consentimento LGPD | checkbox | ✅ |
| Honeypot | hidden | — |

### 19.2 Fluxo

```
Formulário → Web3Forms → e-mail da Salu → /obrigado → evento de conversão
```

### 19.3 Pós-envio

- Página `/obrigado` no mesmo clima
- "Recebemos! Enviamos também nosso guia 'O que perguntar ao fotógrafo'."
- Botão de WhatsApp

---

## 20. Infraestrutura gratuita

| Item | Solução | Limite grátis | Custo |
| --- | --- | --- | --- |
| Hospedagem | **Cloudflare Pages** | Banda e requisições estáticas ilimitadas · uso comercial OK · sem cartão | **R$ 0** |
| Framework | Astro 7 | Open source | R$ 0 |
| Domínio | Subdomínio `pages.dev` | Ilimitado | R$ 0 |
| Domínio próprio | `.com.br` | — | ~R$ 40–100/ano |
| Formulário | **Web3Forms** | 250 envios/mês | R$ 0 |
| Formulário (alt.) | Formspree | 50 envios/mês | R$ 0 |
| Banco (fase 2) | **Neon Postgres** | 1 GB/projeto | R$ 0 |
| Analytics | Cloudflare Web Analytics | Ilimitado, sem cookies | R$ 0 |
| Fontes | Google Fonts / Fontshare | Licença livre | R$ 0 |
| Repositório | GitHub | Público ilimitado | R$ 0 |
| CI/CD | GitHub Actions | 2.000 min/mês | R$ 0 |

> **Não usar Vercel Hobby** para este site: o plano gratuito é restrito a uso pessoal e não comercial.

---

## 21. Custos

| Cenário | Anual |
| --- | --- |
| **100% grátis** (subdomínio) | **R$ 0** |
| **Profissional** (domínio próprio) | **~R$ 40–100** |
| Opcional: Neon Pro, e-mail profissional, banco de fotos extra | variável |

---

## 22. SEO, acessibilidade e performance

### 22.1 SEO

- Title por página com cidade: `Salu Produções | Fotografia e Filme de Casamento em Paulínia e SP`
- Meta description emocional + palavra-chave (Paulínia · Campinas · estado de SP)
- **JSON-LD** `ProfessionalService` + `LocalBusiness` + `ImageObject`, com `areaServed` = Paulínia + São Paulo
- Sitemap e robots automáticos
- URLs limpas: `/portfolio/joyce-e-marcos`
- Alt text descritivo em todas as fotos
- **Google Business Profile** (essencial para busca local)
- Conteúdo de apoio: "fotógrafo de casamento em [cidade]" no texto

### 22.2 Acessibilidade

- Contraste AA (creme sobre preto; dourado claro para texto)
- Foco visível dourado
- `prefers-reduced-motion` desliga animações
- Navegação por teclado na galeria e no lightbox
- Labels e erros claros no formulário
- Vídeos (quando houver): legendas e controle de pausa

### 22.3 Performance (site com 300 fotos exige disciplina)

| Meta | Valor |
| --- | --- |
| LCP | < 2,5 s |
| CLS | < 0,1 |
| Peso da home | < 2 MB |
| Imagens da home | < 1,2 MB |
| JS na home | < 60 KB gzip |

**Estratégias:**
- AVIF/WebP em 3 larguras via `astro:assets`
- Hero com `fetchpriority="high"`; resto `loading="lazy"`
- `width`/`height` sempre
- GSAP e Lenis carregados só quando necessário
- Fotos em `srcset` com `sizes` correto

---

## 23. Roadmap

| Fase | Entrega | Estimativa |
| --- | --- | --- |
| **0 — Fundação** | Projeto Astro 7 + Tailwind 4 + tokens + deploy Cloudflare | 1 dia |
| **1 — Curadoria** | Deduplicar, renomear, selecionar ~32 fotos, exportar | 1–2 dias |
| **2 — Hero e identidade** | Header, hero, estrela, tipografia, CTA | 2 dias |
| **3 — Conteúdo** | Manifesto, serviços, portfólio + lightbox, estudo de caso | 2–3 dias |
| **4 — Conversão** | Pacotes (página creme), depoimentos, FAQ, formulário | 2 dias |
| **5 — Polimento** | GSAP, responsivo, a11y, SEO, OG | 2 dias |
| **6 — Lançamento** | Analytics, testes reais, domínio, go-live | 1 dia |

**Total:** ~11–13 dias de trabalho.

### Ordem se o tempo apertar

1. Hero + formulário (gera contato)
2. Portfólio + pacotes (gera confiança e decisão)
3. Estudo de caso e o resto

---

## 24. Decisões pendentes

Preciso da sua confirmação nestes pontos antes de publicar:

| # | Pendência | Por quê |
| --- | --- | --- |
| 1 | **Prazo ou vagas da PROMOÇÃO** | Sem isso ela canibaliza BRONZE/PRATA |
| 2 | **Arquivos de vídeo** para o portfólio | A Opção A está aprovada, mas falta o material |
| 3 | **Autorização de uso das fotos** por casal | LGPD e confiança |
| 4 | **Quais casais podem aparecer** com nome | Depoimentos e estudos de caso |
| 5 | **Nome do domínio** desejado | Registrar |
| 6 | **Prazo de resposta** que você consegue cumprir | Prometer 24 h e furar é pior que não prometer |

---

## 25. Checklist de conteúdo

- [x] WhatsApp (19) 99352-0172
- [x] Instagram @salu_producoes
- [x] Atuação: Paulínia + estado de SP
- [ ] Logo em SVG (estrela) — ou autorização para vetorizar
- [x] Decisão sobre vídeo (Opção A aprovada)
- [ ] Prazo/vagas da promoção
- [ ] 32 fotos selecionadas e autorizadas
- [ ] Vídeos para o portfólio (reels, teasers)
- [ ] Texto da história da Salu
- [ ] Depoimentos reais (5–10) com nome
- [ ] FAQ respondido por você
- [ ] Números reais (casamentos, anos)
- [ ] E-mail de contato
- [ ] Domínio escolhido

---

## 26. Próximos passos

1. **Aprovar a escada de pacotes** da seção 4.4 (ou manter os seus números)
2. **Iniciar a Fase 0**: Astro 7 + Tailwind 4 + deploy no Cloudflare Pages
3. **Ligar o WhatsApp** `https://wa.me/5519993520172` no botão flutuante e no formulário
4. **Fazer a curadoria** das fotos (posso gerar uma folha de contatos para você escolher rápido)
5. **Construir o hero** para aprovar o clima visual
6. Seguir o roadmap até o lançamento

---

## 27. Referências

**Templates e inspiração**
- [12 melhores templates de casamento no Framer (2026)](https://framplates.com/blog/best-wedding-framer-templates)
- [Melhores temas Astro 2026](https://aerolaunch.app/blog/best-astro-themes-2026/)
- [Astro Photo Folio](https://astro.build/themes/details/astro-photo-folio/)
- [Horizon para Astro](https://astro.build/themes/details/horizon/)

**Stack e bibliotecas**
- [Astro 7.4.4 (npm)](https://registry.npmjs.org/astro/latest)
- [Tailwind CSS 4.3.3 (npm)](https://registry.npmjs.org/tailwindcss/latest)
- [GSAP — todos os plugins gratuitos](https://raw.githubusercontent.com/greensock/gsap-skills/main/skills/llms.txt)
- [PhotoSwipe](https://photoswipe.com/)
- [Lenis](https://lenis.darkroom.engineering/)

**Preços de mercado**
- [Quanto custa um fotógrafo de casamento em 2026 — Freelans (jun/2026)](https://freelans.com.br/blog/quanto-custa-fotografo-de-casamento-2026)
- [Quanto custa a filmagem de casamento em 2026 — NatalStudios](http://natalstudios.com.br/casamento/quanto-custa-filmagem-de-casamento.html)

**Infraestrutura gratuita**
- [Comparativo de planos gratuitos de hospedagem (set/2026)](https://flaviocopes.pages.dev/hosting-free-tiers/)
- [Bancos de dados gratuitos — limites reais 2026](https://stackwrite.com/blog/free-tier-databases-2026/)
- [Web3Forms — 250 envios/mês](https://web3forms.com/)
- [Formspree — limites](https://help.formspree.io/fr/articles/account-management/account-limits.md)
- [Preço de domínio `.com.br`](https://www.rollinhost.com.br/dominio-com-br)

---

## 28. Estado atual do projeto

**Fase 0 concluída e site navegável.**

| Item | Status |
| --- | --- |
| Build | ✅ `pnpm run build` gera 8 páginas em `dist/` |
| Preview local | ✅ `pnpm run preview` em `http://127.0.0.1:4321` |
| Páginas | `/` · `/portfolio` · `/filmes` · `/pacotes` · `/sobre` · `/orcamento` · `/obrigado` · `404` |
| Design system | ✅ tokens preto/creme/dourado, Playfair Display + Great Vibes + Jost |
| Hero | ✅ foto #070 (saída com sparklers) + headline "O dia passa. A memória fica." |
| Fotos | ✅ **95 selecionadas** (76 retratos · 19 paisagens) · 231 arquivos WebP responsivos (480/960/1600) |
| Portfólio | ✅ 95 fotos em masonry + lightbox PhotoSwipe |
| Movimento | ✅ Lenis (scroll suave) + GSAP/ScrollTrigger (reveals, parallax, barra de progresso) + entrada do hero em CSS |
| Editorial | ✅ tipografia grande (clamp até 7.2rem), grid assimétrico de 12 colunas, citação do Machado de Assis |
| Interação | ✅ cursor personalizado (desktop), transições entre páginas, lightbox PhotoSwipe nas 95 fotos |
| Seções | ✅ Hero · Faixa animada · Sobre · Citação · Portfólio · Pacotes · Processo · FAQ · CTA |
| Pacotes | ✅ Bronze, Prata, Ouro, Promoção + 2 filmes + combo |
| Formulário | ✅ envia direto para o WhatsApp `5519993520172` com mensagem pronta |
| SEO | ✅ title, description, Open Graph, JSON-LD, sitemap e robots |
| Fontes | ✅ 7 arquivos woff2 (subset latino) |
| CSS | ✅ ~24 KB |
| Deploy | ✅ pronto para Cloudflare Pages: `_headers` (cache + segurança), `wrangler.toml` e guia em `DEPLOY.md` |
| Pendente | vídeos reais, alt text específico por foto, depoimentos, Web3Forms (opcional) |

**Comandos**

```bash
pnpm install --node-linker=hoisted   # instala (layout hoisted é necessário no Windows)
pnpm run dev                         # desenvolvimento com hot reload
pnpm run build                       # gera o site estático em dist/
pnpm run preview                     # serve o dist/ localmente
```

> ⚠️ **Nota técnica:** neste ambiente, o Astro 7 + Vite 8 só carrega a configuração com o `node_modules` no layout *hoisted*. Por isso existe o `pnpm-workspace.yaml` com `nodeLinker: hoisted`. Não remova.

**Próximo passo:** curadoria das fotos (de 306 para ~32) e inclusão dos vídeos reais.

---

> **Salu Produções** · *O dia passa. A memória fica.*
