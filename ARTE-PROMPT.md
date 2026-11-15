# 🎨 Prompts — arte de feed e arte de stories

Mesma linguagem visual, duas composições. **As imagens saem sem texto.**

---

## Peça 1 · Post de feed (1080×1350)

### Prompt (português)

> Crie uma fotografia editorial minimalista, formato vertical 4:5, para um estúdio de fotografia de Natal.
>
> **Cena:** parede de reboco em creme quente (#F6F1E6) ocupando a metade de cima, vazia. Na metade de baixo, um still life simples: vaso de cerâmica fosca com um único galho de pinheiro, ao lado um presente pequeno em papel vinho (#5E2333) com fita fina de algodão. Nada mais.
>
> **Luz:** janela difusa pela esquerda, sombra longa e suave, sem sol direto.
>
> **Câmera:** 50 mm, profundidade rasa, grão fino de filme 400 ISO, cores levemente dessaturadas.
>
> **Composição:** objetos no terço inferior, deslocados para a direita. Muito espaço vazio em cima para o texto.
>
> **Não inclua:** texto, logotipo, pessoas, brilhos, glitter, bokeh, neve, estrelas, 3D, plástico, degradê, neon, moldura.

### Texto (aplicar depois)

```
ENSAIO DE NATAL
R$ 199
30 min · 10 fotos · entrega em 24h
Salu Produções
```

---

## Peça 2 · Stories (1080×1920)

### Prompt (português)

> Crie uma fotografia editorial minimalista, formato vertical 9:16, para stories de um estúdio de fotografia de Natal.
>
> **Cena:** parede de reboco em creme quente (#F6F1E6) ocupando dois terços de cima, vazia. No terço inferior, um galho de pinheiro saindo de um vaso de cerâmica fosca, e um presente pequeno em papel vinho com fita fina.
>
> **Luz:** janela difusa lateral, sombra longa, clima calmo e quente.
>
> **Câmera:** 50 mm, profundidade rasa, grão fino de filme 400 ISO.
>
> **Composição:** objetos só na parte de baixo. Muito espaço vazio da metade para cima.
>
> **Não inclua:** texto, logotipo, pessoas, brilhos, glitter, bokeh, neve, estrelas, 3D, plástico, degradê, neon, moldura.

### Zonas seguras do stories

| Faixa | Uso |
|---|---|
| 0 a 15% | vazio (nome do perfil e barra do topo) |
| 15 a 30% | margem |
| **30 a 55%** | **texto** |
| 55 a 85% | foto |
| 80 a 85% | chamada ("Reserve pelo WhatsApp") |
| 85 a 100% | vazio (barra de resposta e figurinhas) |

### Texto (aplicar depois)

```
ENSAIO DE NATAL
R$ 199
30 min · 10 fotos · 24h
Reserve pelo WhatsApp
@salu_producoes
```

---

## Versões em inglês (Midjourney / Ideogram)

**Feed (4:5)**
> Minimalist editorial still life, vertical 4:5, for a Christmas photo studio. Warm cream plaster wall filling the upper half, empty. Lower third: matte ceramic vase with a single pine branch, a small gift in muted burgundy paper with a thin cotton ribbon. Soft diffused window light from the left, long gentle shadow. 50mm, shallow depth of field, fine film grain, desaturated Portra 400 palette. Objects low and off-center right. No text, no logo, no people, no sparkles, no glitter, no bokeh, no snow, no stars, no 3D, no plastic, no gradient, no neon, no frame.
> `--ar 4:5 --style raw --stylize 100`

**Stories (9:16)**
> Minimalist editorial still life, vertical 9:16, for Instagram stories. Warm cream plaster wall filling the upper two thirds, empty. Lower third: matte ceramic vase with a pine branch and a small burgundy gift with thin ribbon. Soft lateral window light, long shadow. 50mm, shallow depth of field, fine film grain. Objects only at the bottom. No text, no logo, no people, no sparkles, no glitter, no bokeh, no snow, no stars, no 3D, no plastic, no gradient, no neon, no frame.
> `--ar 9:16 --style raw --stylize 100`

---

## Regra de ouro

Peça **sem texto**. A tipografia entra depois:

- Título: **Playfair Display**, vinho `#5E2333`
- Apoio: **Montserrat** caixa alta, espaçada, tinta `#1D1A16`
- Linha de separação: dourado `#C9A227`, 1 px

Se quiser, me manda as duas imagens limpas e eu componho as duas peças em HTML/CSS no tamanho exato (1080×1350 e 1080×1920), com o texto já alinhado.
