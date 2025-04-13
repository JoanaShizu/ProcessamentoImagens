from PIL import Image
import numpy as np

def filtro_media(imagem_np):

    altura, largura, canais = imagem_np.shape
    imagem_suavizada = np.zeros_like(imagem_np)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            for c in range(canais):
                vizinhos = imagem_np[y-1:y+2, x-1:x+2, c]
                media = np.mean(vizinhos)
                imagem_suavizada[y, x, c] = int(media)
    
    return imagem_suavizada

imagem = Image.open("imagem2.jpg").convert("RGB")
imagem_np = np.array(imagem)

imagem_filtrada_np = filtro_media(imagem_np)

imagem_filtrada = Image.fromarray(imagem_filtrada_np)
imagem_filtrada.save("imagem2modificada.jpg")
