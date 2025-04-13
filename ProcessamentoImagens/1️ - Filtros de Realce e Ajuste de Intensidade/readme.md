# ✨ Ajuste de Contraste em Imagem com Python

Este código em Python realiza o **ajuste de contraste** em uma imagem.

---

## 🧠 O que o código faz?

1. **Carrega uma imagem original** chamada `imagem1`.
2. **Converte a imagem para um array NumPy**, facilitando os cálculos matemáticos.
3. **Ajusta o contraste** da imagem com base em um fator definido (por exemplo, 1.5 para aumentar o contraste).
4. **Aplica a fórmula de contraste** considerando o ponto médio (128) como referência.
5. **Garante que os valores de pixel fiquem entre 0 e 255**, usando o método `clip`.
6. **Converte o array de volta para imagem** usando a biblioteca Pillow.
7. **Salva a imagem modificada** com o nome `imagem1modificada`.

---

## 🔍 Comparação Visual

| Imagem Original | Imagem com Contraste Ajustado |
|------------------|-------------------------------|
| <img src="imagem1.jpg" width="300"/> | <img src="imagem1modificada.jpg" width="300"/> |

---

## 🎛️ Sobre o Fator de Contraste

- **Fator > 1** 👉 aumenta o contraste (mais "drama" e intensidade nas cores)
- **Fator < 1** 👉 reduz o contraste (efeito mais suave, lavado)
- **Fator = 1** 👉 nenhuma alteração na imagem

---

