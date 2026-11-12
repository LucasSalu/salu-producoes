# 🚀 Deploy no Cloudflare Pages

Guia para colocar o site no ar, de graça, com HTTPS e domínio próprio.

| Item | Valor |
| --- | --- |
| **Plataforma** | Cloudflare Pages |
| **Custo** | **R$ 0** (banda e requisições estáticas ilimitadas) |
| **Comando de build** | `pnpm run build` |
| **Pasta de saída** | `dist` |
| **Node mínimo** | 22.23.4 (Astro 7) |
| **Projeto** | `salu-producoes` |

---

## Antes de começar

Você precisa de duas contas gratuitas:

1. **GitHub** — para guardar o código
2. **Cloudflare** — para hospedar

> Não precisa de cartão de crédito.

---

## Passo 1 — Enviar o código para o GitHub

No terminal, dentro da pasta do projeto:

```bash
git init
git add .
git commit -m "Site Salu Produções"
git branch -M main
```

Crie um repositório vazio no GitHub chamado `salu-producoes` e conecte:

```bash
git remote add origin https://github.com/SEU-USUARIO/salu-producoes.git
git push -u origin main
```

> ⚠️ **Importante:** a pasta `melhores fotos/` (788 MB) e o PDF do catálogo **não devem ir para o GitHub**. O `.gitignore` já bloqueia isso. O que sobe é o site otimizado (`public/fotos`, ~24 MB), não o acervo original.

---

## Passo 2 — Criar o projeto no Cloudflare

1. Acesse **dash.cloudflare.com** → **Workers & Pages**
2. Clique em **Create** → aba **Pages** → **Connect to Git**
3. Autorize o GitHub e selecione o repositório `salu-producoes`
4. Preencha as configurações de build:

| Campo | Valor |
| --- | --- |
| Framework preset | **Astro** |
| Build command | `pnpm run build` |
| Build output directory | `dist` |

5. Em **Environment variables**, adicione:

| Nome | Valor |
| --- | --- |
| `NODE_VERSION` | `22.23.4` |

6. Clique em **Save and Deploy**

Em cerca de 1–2 minutos o site estará no ar em:

```
https://salu-producoes.pages.dev
```

---

## Passo 3 — Domínio próprio (opcional, ~R$ 40–100/ano)

Se você comprar `saluproducoes.com.br` no Registro.br:

1. No Cloudflare Pages, abra o projeto → **Custom domains** → **Set up a domain**
2. Digite o domínio desejado
3. Se o domínio estiver no Cloudflare, o DNS é configurado automaticamente
4. Se estiver no Registro.br, aponte o DNS para os nameservers do Cloudflare (ou crie o CNAME indicado)

Depois de conectar o domínio, atualize a URL do site para o sitemap e o canonical:

**Opção A** — editar `astro.config.mjs`:

```js
const site = process.env.SITE_URL ?? 'https://saluproducoes.com.br';
```

**Opção B** — criar a variável `SITE_URL` no Cloudflare com o novo domínio.

Depois é só fazer um novo deploy.

---

## Alternativa: publicar pela linha de comando

Se preferir não usar o GitHub:

```bash
pnpm dlx wrangler@latest login
pnpm dlx wrangler@latest pages project create salu-producoes
pnpm run build
pnpm dlx wrangler@latest pages deploy dist --project-name salu-producoes
```

O arquivo `wrangler.toml` já aponta a saída para `dist`.

---

## O que já está configurado no projeto

| Arquivo | Função |
| --- | --- |
| `public/_headers` | Cache de 1 ano para imagens/fontes, headers de segurança |
| `wrangler.toml` | Nome do projeto e pasta de saída |
| `astro.config.mjs` | Sitemap automático e URL base |
| `public/robots.txt` | Índice para buscadores |
| `.gitignore` | Impede o envio do acervo original |

> O site é **100% estático**: não precisa de banco de dados nem servidor. O formulário envia direto para o WhatsApp `5519993520172`, sem backend.

---

## Pixel da Meta (para anúncios)

O site **já tem o código do Pixel pronto**, mas ele só ativa quando você define o ID.

1. **Criar o Pixel:** [business.facebook.com/events_manager](https://business.facebook.com/events_manager) → *Connect data* → **Web** → criar com o nome `Salu Produções` → copiar o **ID** (só números).
2. **No Cloudflare Pages:** projeto → *Settings* → *Environment variables* → adicionar:
   - Nome: `PUBLIC_META_PIXEL_ID`
   - Valor: o ID copiado
3. **Redeploy** (*Retry deployment* ou novo push).

Já vem configurado:

- Evento **PageView** em todas as páginas
- Evento **Lead** quando alguém clica em qualquer link do WhatsApp
- Fallback para navegadores sem JavaScript

> Sem o Pixel não dá para criar público de retargeting nem medir qual anúncio gera conversa.

---

## Checklist depois do deploy

- [ ] Abrir a URL e conferir as 8 páginas (home, portfólio, filmes, pacotes, sobre, orçamento, obrigado, 404)
- [ ] Testar o formulário — deve abrir o WhatsApp com a mensagem preenchida
- [ ] Testar no celular (menu hambúrguer)
- [ ] Conferir `https://SEU-SITE/robots.txt` e `https://SEU-SITE/sitemap-index.xml`
- [ ] Ativar **Web Analytics** no painel do Cloudflare (grátis, sem cookies)
- [ ] Cadastrar o site no **Google Search Console** e enviar o sitemap
- [ ] Criar o **Google Business Profile** da Salu (essencial para busca local)

---

## Problemas comuns

| Sintoma | Causa provável | Solução |
| --- | --- | --- |
| Build falha com erro de versão do Node | Node antigo no Cloudflare | Definir `NODE_VERSION=22.23.4` |
| Erro de `require is not defined` no build | Layout de `node_modules` com symlinks | Manter `pnpm-workspace.yaml` com `nodeLinker: hoisted` |
| Imagens quebradas | `public/fotos` não foi para o repositório | Conferir se a pasta está versionada |
| Menu mobile não abre | Cache do navegador | Recarregar com Ctrl+Shift+R |

---

## Próximos passos depois de publicar

1. Enviar os **vídeos** para preencher a página `/filmes`
2. Revisar as respostas do **FAQ**
3. Personalizar o **alt text** das 95 fotos
4. Adicionar **depoimentos reais** de casais
