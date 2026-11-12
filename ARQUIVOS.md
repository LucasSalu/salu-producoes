# 📁 Mapa do Projeto — onde está cada coisa

**Pasta raiz:** `C:\dev\deepseek\salu_producoes`

> Atalho: aperte **Win + E** e cole o caminho na barra de endereço.

---

## 📄 Documentos de negócio (é aqui que você trabalha)

| Arquivo | Para que serve |
| --- | --- |
| [README.md](README.md) | Planejamento completo: posicionamento, pacotes de casamento, infraestrutura, roadmap |
| [PLANO-20K.md](PLANO-20K.md) | Plano de crescimento: meta de R$ 20k, orgânico, tráfego pago, rotina e metas semanais |
| [MENSAGENS-WHATSAPP.md](MENSAGENS-WHATSAPP.md) | Todas as mensagens prontas: base antiga, leads, follow-up, objeções, pós-sessão |
| [PACOTES-NATAL.md](PACOTES-NATAL.md) | Pacotes do ensaio de Natal, adicionais, pagamento e políticas |
| [MARKETING-NATAL.md](MARKETING-NATAL.md) | Roteiros de stories (inclusive o da esposa), calendário de posts, funil |
| [KIT-ARTES-NATAL.md](KIT-ARTES-NATAL.md) | Paleta, fontes, textos e passo a passo para montar as artes no Canva |
| [DEPLOY.md](DEPLOY.md) | Como publicar no Cloudflare Pages (passo a passo) |

## 🧠 Skill de marketing

| Arquivo | Para que serve |
| --- | --- |
| [skills/marketing-salu/SKILL.md](skills/marketing-salu/SKILL.md) | O playbook que eu carrego (frameworks, funil, objeções, formatos) |

## 💻 Site (código)

| Onde | O que é |
| --- | --- |
| `src/pages/` | Páginas — `natal.astro` é a página do ensaio de Natal |
| `src/components/` | Componentes (hero, pacotes, FAQ, header, footer...) |
| `src/styles/global.css` | Cores, fontes e estilos da marca |
| `public/fotos/` | **As 228 fotos otimizadas** usadas no site |
| `public/thumbs/` | Miniaturas da ferramenta de seleção de fotos |
| `dist/` | O site pronto (gerado pelo build — não editar) |
| `astro.config.mjs` · `package.json` · `wrangler.toml` | Configuração |

## 🗂️ Material bruto (não editar)

| Onde | O que é |
| --- | --- |
| `melhores fotos/` | **334 arquivos originais** (788 MB) — fora do Git |
| `Pacotes Oficial Casamento 2026 (1).pdf` | Catálogo original de pacotes |
| `selecao/` | Folha de contatos (PDF), índice das fotos e as 3 artes geradas (`selecao/artes/`) |
| `tools/` | Scripts que usei (não precisa mexer) |

---

## ▶️ Como ver o site

Com o servidor ligado:

- **http://127.0.0.1:4321** — site
- **http://127.0.0.1:4321/natal/** — página do ensaio de Natal

Para ligar o servidor (terminal na pasta):

```bash
pnpm run preview
```

---

## 💡 Dicas

- Os `.md` abrem bonitos no **VS Code** (Ctrl+Shift+V) ou em qualquer editor Markdown.
- As artes em imagem estão em `selecao/artes/` (as 3 que ficaram feias).
- Se quiser encontrar uma foto específica: `selecao/indice.json` liga o número da folha de contatos ao arquivo original.
