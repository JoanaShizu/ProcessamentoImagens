from PIL import Image
import numpy as np

def filtro_remapeamento(imagem_np):

    altura, largura, canais = imagem_np.shape
    centro_x, centro_y = largura // 2, altura // 2

    nova_imagem = np.zeros_like(imagem_np)

    for y in range(altura):
        for x in range(largura):
            dx = x - centro_x
            dy = y - centro_y
            distancia = np.sqrt(dx*dx + dy*dy)

            fator = 1 + 0.0008 * distancia**2  
            novo_x = int(centro_x + dx / fator)
            novo_y = int(centro_y + dy / fator)

            if 0 <= novo_x < largura and 0 <= novo_y < altura:
                nova_imagem[y, x] = imagem_np[novo_y, novo_x]

    return Image.fromarray(nova_imagem)

imagem = Image.open("imagem5.jpg").convert("RGB")
imagem_np = np.array(imagem)

imagem_modificada = filtro_remapeamento(imagem_np)

imagem_modificada.save("imagem5modificada.jpg")
