from PIL import Image
import numpy as np
from scipy.ndimage import convolve
import math

def criar_kernel_gabor(ksize, sigma, theta, lambd, gamma, psi):

    half_size = ksize // 2
    kernel = np.zeros((ksize, ksize), dtype=np.float32)

    for y in range(-half_size, half_size + 1):
        for x in range(-half_size, half_size + 1):
            x_theta = x * np.cos(theta) + y * np.sin(theta)
            y_theta = -x * np.sin(theta) + y * np.cos(theta)
            gabor = np.exp(-0.5 * (x_theta**2 + (gamma**2) * y_theta**2) / (sigma**2))
            gabor *= np.cos(2 * np.pi * x_theta / lambd + psi)
            kernel[y + half_size, x + half_size] = gabor

    return kernel

def aplicar_filtro_gabor(imagem_np, kernel):

    imagem_gray = np.dot(imagem_np[...,:3], [0.2989, 0.5870, 0.1140])
    imagem_filtrada = convolve(imagem_gray, kernel)
    imagem_filtrada = imagem_filtrada - imagem_filtrada.min()
    imagem_filtrada = 255 * (imagem_filtrada / imagem_filtrada.max())
    imagem_filtrada = imagem_filtrada.astype(np.uint8)
    return Image.fromarray(imagem_filtrada)

ksize = 21       
sigma = 4.0       
theta = np.pi / 4  
lambd = 10.0       
gamma = 0.5       
psi = 0            

kernel_gabor = criar_kernel_gabor(ksize, sigma, theta, lambd, gamma, psi)

imagem = Image.open("imagem4.jpg").convert("RGB")
imagem_np = np.array(imagem)

imagem_modificada = aplicar_filtro_gabor(imagem_np, kernel_gabor)
imagem_modificada.save("imagem4modificada.jpg")
