from PIL import Image
import numpy as np

def dilatacao(imagem_np, iteracoes=3):

    altura, largura = imagem_np.shape
    imagem_resultado = imagem_np.copy()

    for _ in range(iteracoes):
        imagem_temp = imagem_resultado.copy()
        for y in range(1, altura - 1):
            for x in range(1, largura - 1):
                vizinhanca = imagem_temp[y-1:y+2, x-1:x+2]
                imagem_resultado[y, x] = np.max(vizinhanca)

    return imagem_resultado

imagem = Image.open("imagem6.jpg").convert("L")
imagem_np = np.array(imagem)

imagem_dilatada_np = dilatacao(imagem_np, iteracoes=3)
imagem_dilatada = Image.fromarray(imagem_dilatada_np)

imagem_dilatada.save("imagem6modificada.jpg")
