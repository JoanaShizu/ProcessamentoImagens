from PIL import Image
import numpy as np

def ajustar_contraste(imagem_np, fator):
    media = 120
    imagem_contraste = media + fator * (imagem_np - media)
    imagem_contraste = np.clip(imagem_contraste, 0, 255)
    return imagem_contraste.astype(np.uint8)

imagem = Image.open("imagem1.jpg").convert("RGB")
imagem_np = np.array(imagem)

fator_contraste = 3

imagem_modificada_np = ajustar_contraste(imagem_np, fator_contraste)

imagem_modificada = Image.fromarray(imagem_modificada_np)

imagem_modificada.save("imagem1modificada.jpg")
