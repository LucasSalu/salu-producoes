# 📁 Onde estão todos os arquivos

**Pasta raiz:** `C:\dev\deepseek\salu_producoes`

> Atalho: **Win + E** → cole o caminho na barra de endereço.

---

## 📄 Documentos de estratégia (na raiz)

| Arquivo | O que tem |
| --- | --- |
| [PLANO-20K.md](PLANO-20K.md) | Plano dos R$ 20k: conta, canais, orgânico, organograma de metas |
| [TRAFEGO-BAIXO-ORCAMENTO.md](TRAFEGO-BAIXO-ORCAMENTO.md) | Anúncios com pouco dinheiro: níveis de R$ 0 a R$ 300, setup, conta pequena |
| [CHECKLIST-ANUNCIO.md](CHECKLIST-ANUNCIO.md) | Passo a passo para publicar o anúncio (campos já preenchidos) |
| [MENSAGENS-WHATSAPP.md](MENSAGENS-WHATSAPP.md) | Todas as mensagens prontas: base antiga, leads, follow-up, objeções |
| [PACOTES-NATAL.md](PACOTES-NATAL.md) | Pacotes, preços, adicionais, pagamento e políticas |
| [MARKETING-NATAL.md](MARKETING-NATAL.md) | Roteiros de stories (inclusive o da sua esposa) e calendário |
| [KIT-ARTES-NATAL.md](KIT-ARTES-NATAL.md) | Paleta, fontes, textos e passo a passo no Canva |
| [DEPLOY.md](DEPLOY.md) | Como publicar no Cloudflare Pages + Pixel da Meta |
| [README.md](README.md) | Planejamento completo do site e do posicionamento |
| [ARQUIVOS.md](ARQUIVOS.md) | Este mapa |

---

## 🎨 Artes prontas para postar

### `selecao\anuncios\` — feitas a partir das suas artes do GPT

| Arquivo | Formato | Para quê |
| --- | --- | --- |
| `arte1-feed.png` | 1080×1350 | Anúncio de descoberta (sem preço) |
| `arte1-story.png` | 1080×1920 | Stories |
| `arte2-feed.png` | 1080×1350 | Anúncio da oferta (com tabela) |
| `arte2-story.png` | 1080×1920 | Stories |

### `selecao\artes\` — as 3 primeiras (as que ficaram feias)

`arte-anuncio.png` · `arte-pacote-memoria.png` · `arte-story.png`

---

## 🧠 Skill de marketing

`skills\marketing-salu\SKILL.md` — o playbook (frameworks, funil, objeções, formatos)

---

## 💻 Site

| Onde | O que é |
| --- | --- |
| `src\pages\natal.astro` | Página `/natal` (pacotes, vale-presente, FAQ) |
| `src\` | Demais páginas e componentes |
| `public\fotos\` | Imagens otimizadas do site (WebP) |
| `dist\` | Site pronto (gerado pelo build — não editar) |

---

## 🗂️ Material bruto

| Onde | O que é |
| --- | --- |
| `melhores fotos\` | 334 arquivos originais (fora do Git) |
| `Pacotes Oficial Casamento 2026 (1).pdf` | Catálogo original |
| `selecao\` | Folha de contatos, índice das fotos e as artes |
| `tools\` | Scripts que geram as imagens e artes |

---

## ▶️ Como ver o site

Com o servidor ligado: **http://127.0.0.1:4321** (Natal em `/natal/`)

Para ligar:

```bash
pnpm run preview
```

---

## 💡 Dicas

- Os `.md` ficam bonitos no **VS Code** (Ctrl+Shift+V) ou em qualquer editor Markdown
- Os PNGs de anúncio estão em `selecao\anuncios\` — é só arrastar no Gerenciador de Anúncios
- Tudo é salvo **no seu computador**; nada fica na nuvem além do GitHub (código do site)
