from PIL import Image
import numpy as np

def filtro_prewitt(imagem_np):
    
    imagem_gray = np.dot(imagem_np[...,:3], [0.2989, 0.5870, 0.1140])

    kernel_x = np.array([[1, 0, -1],
                         [1, 0, -1],
                         [1, 0, -1]])
    kernel_y = np.array([[1,  1,  1],
                         [0,  0,  0],
                         [-1, -1, -1]])

    altura, largura = imagem_gray.shape
    bordas = np.zeros_like(imagem_gray)

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            regiao = imagem_gray[y-1:y+2, x-1:x+2]
            gx = np.sum(kernel_x * regiao)
            gy = np.sum(kernel_y * regiao)
            magnitude = np.sqrt(gx**2 + gy**2)
            bordas[y, x] = magnitude

    bordas = np.clip(bordas, 0, 255).astype(np.uint8)
    return Image.fromarray(bordas)

imagem = Image.open("imagem3.jpg").convert("RGB")
imagem_np = np.array(imagem)

imagem_prewitt = filtro_prewitt(imagem_np)

imagem_prewitt.save("imagem3modificada.jpg")
