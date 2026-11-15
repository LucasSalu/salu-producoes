# 🎨 Prompt para gerar a imagem do anúncio

Leia o `briefing-arte.json` junto com este arquivo. A regra mais importante está no fim: **a imagem sai sem texto**.

---

## Prompt em português (para ChatGPT, Gemini, etc.)

> Crie uma fotografia editorial minimalista para o anúncio de um estúdio de fotografia de Natal.
>
> **Cena:** um canto de ambiente simples, parede de reboco pintada em creme quente (#F6F1E6). No canto direito, um vaso de cerâmica fosca com um único galho de pinheiro. Ao lado, um presente pequeno embrulhado em papel vinho (#5E2333) com fita fina. Nada mais.
>
> **Luz:** luz de janela difusa entrando pela esquerda, sombra longa e suave, sem sol direto.
>
> **Câmera:** lente 50 mm, profundidade de campo rasa, textura de filme analógico (grão fino, cores levemente dessaturadas), como se fosse fotografado em filme 400 ISO.
>
> **Composição:** formato vertical 4:5. Deixe os dois terços de cima com **espaço vazio** para eu colocar o texto depois. Os objetos ficam no terço inferior, deslocados para a direita, nunca centralizados.
>
> **Cores:** creme, vinho e um toque de dourado fosco. Nada de vermelho vivo, nada de verde saturado.
>
> **Não inclua:** texto, logotipo, marca d'água, pessoas, brilhos, glitter, bolas de bokeh, neve, estrelas, enfeites flutuando, árvore de Natal simétrica, render 3D, aspecto de plástico, degradê, neon, moldura.

---

## Prompt em inglês (para Midjourney, Ideogram, DALL·E)

> Minimalist editorial still life photograph for a Christmas photo studio ad. Warm cream plaster wall, a matte ceramic vase with a single pine branch at the right edge, one small gift wrapped in muted burgundy paper with a thin ribbon. Soft diffused window light from the left, long gentle shadow. Shot on 50mm, shallow depth of field, fine film grain, slightly desaturated Portra 400 palette, calm and warm. Vertical 4:5 composition with large empty negative space in the upper two thirds for typography. Objects placed low and off-center to the right. Palette: cream, burgundy, muted brass gold. No text, no logo, no people, no sparkles, no glitter, no bokeh balls, no snow, no stars, no floating decorations, no symmetrical Christmas tree, no 3D render, no CGI, no plastic look, no neon, no purple gradient, no frame.

**Negative prompt:** text, watermark, logo, sparkles, glitter, bokeh balls, snow, stars, neon, purple gradient, 3D render, CGI, plastic, oversaturated, symmetrical tree, floating ornaments, frame, clip art, canva template.

**Parâmetros (Midjourney):** `--ar 4:5 --style raw --stylize 100`

---

## As 3 variações para pedir

1. **Galho e presente** (a cena do prompt acima)
2. **Canto de sala**: árvore parcialmente fora do quadro, só o galho e as luzes entrando pela lateral
3. **Detalhe**: fita, agulhas de pinheiro e sombra suave em close

---

## Regra de ouro: imagem sem texto

Nenhuma IA escreve texto bonito com confiança. Se ela tentar, sai aquele visual de "IA": letras tortas, acentos quebrados, espaçamento errado.

**Fluxo certo:**

1. Gere a imagem **sem texto nenhum**, com espaço vazio
2. Aplique a tipografia depois no Canva (Playfair Display + Montserrat)
3. Cores do texto: vinho `#5E2333` no título, tinta `#1D1A16` no apoio

Assim a peça parece feita por gente, porque metade dela foi.

---

## Se quiser, eu faço a tipografia

Me manda a imagem que a IA gerar (a versão limpa, sem texto) e eu componho o texto em HTML/CSS no formato 1080×1350, com a fonte certa e o espaçamento correto. É determinístico: não tem erro de acento nem de alinhamento.
