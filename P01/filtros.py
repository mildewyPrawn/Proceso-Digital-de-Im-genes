from PIL import Image
from random import randrange
import numpy as np

# Funciones auxiliares

mini = lambda x, y : min(x,y) # Nos da el mínimo de dos elementos
maxi = lambda x, y : max(x,y) # Nos da el máximo de dos elementos
# Nos da la suma del mínimo y máximo de tres elementos
minmaxprom = lambda x,y,z : (mini(x, mini(y, z)))+(maxi(x, maxi(y, z)))


# Filtro de mica roja
def filtroMicaRoja(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()    
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (r,0,0)
    return nueva

# Filtro de mica verde
def filtroMicaVerde(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (0,g,0)
    return nueva

# Filtro de mica azul
def filtroMicaAzul(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            pixels[i,j] = (0,0,b)
    return nueva

# Filtro que resuelve la siguiente fórmula 0.30r+0.59g+.011b
def filtroFormula(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            form= (int(r*0.3) + int(g*0.59) + int(b*0.11))
            pixels[i,j] = (form, form, form)
    return nueva

# Filtro promedio de los tres valores
def filtroPromedio(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            prom = int((r+g+b)/3)
            pixels[i,j] = (prom, prom, prom)
    return nueva

# Filtro max(r,g,b)
def filtroMaxRGB(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            m = maxi(r, maxi(g, b))
            pixels[i,j] = (m,m,m)
    return nueva

# Filtro min(r,g,b)
def filtroMinRGB(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            m = mini(r, mini(g, b))
            pixels[i,j] = (m,m,m)
    return nueva

# Filtro que resuelve la siguiente fórmula 'max(r,b,b)+min(r,b,b)/2'
def filtroMinMaxProm(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            mmp = int(minmaxprom(r,g,b)/2)
            pixels[i,j] = (mmp,mmp,mmp)
    return nueva

# Filtro que coloca colores al azar entre el 1 y 255
def filtroAzar(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            r = randrange(255)
            g = randrange(255)
            b = randrange(255)
            pixels[i,j] = (r,g,b)
    return nueva

# Filtro alto contraste
# TODO: ¿Escala de grises?
def filtroAltoContraste(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            ac = (r+g+b)/3
            ac = 255 if (ac >= 128) else 0
            pixels[i,j] = (ac,ac,ac)
    return nueva

# Filtro alto contraste inverso
def filtroAltoContrasteInverso(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            aci = (r+g+b)/3
            aci = 255 if (aci < 128) else 0
            pixels[i,j] = (aci,aci,aci)
    return nueva

def filtroBlur(imagen, nueva):
    mtx = np.matrix([[0,0,1,0,0],
                     [0,1,1,1,0],
                     [1,1,1,1,1],
                     [0,1,1,1,0],
                     [0,0,1,0,0]])
    factor = 1.0/13.0
    aux = 0.0
    return convierte(imagen, nueva, mtx, factor, aux)

def filtroMotionBlur(imagen, nueva):
    mtx = np.matrix([[1,0,0,0,0,0,0,0,0],
                     [0,1,0,0,0,0,0,0,0],
                     [0,0,1,0,0,0,0,0,0],
                     [0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,1,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0],
                     [0,0,0,0,0,0,1,0,0],
                     [0,0,0,0,0,0,0,1,0],
                     [0,0,0,0,0,0,0,0,1]])
    factor = 1.0/9.0
    aux = 0.0
    return convierte(imagen, nueva, mtx, factor, aux)

def filtroEncontrarBordes(imagen, nueva):
    mtx = np.matrix([[0,0,-1,0,0],
                     [0,0,-1,0,0],
                     [0,0, 2,0,0],
                     [0,0, 0,0,0],
                     [0,0, 0,0,0]])
    factor = 1.0
    aux = 0.0
    return convierte(imagen, nueva, mtx, factor, aux)

def filtroSharpen(imagen, nueva):
    mtx = np.matrix([[-1,-1,-1],
                     [-1, 9,-1],
                     [-1,-1,-1]])
    factor = 1.0
    aux = 0.0
    return convierte(imagen, nueva, mtx, factor, aux)

def filtroEmboss(imagen, nueva):
    mtx = np.matrix([[-1,-1, 0],
                     [-1, 0, 1],
                     [ 0, 1, 1]])
    factor = 1.0
    aux = 128.0
    return convierte(imagen, nueva, mtx, factor, aux)

def convierte(imagen, nueva, matriz, factor, aux):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    x,y = matriz.shape
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            rojo = 0.0
            verde = 0.0
            azul = 0.0
            for k in range(x):
                for l in range(y):
                    imageX = (i - x / 2 + k + width) % width
                    imageY = (j - y / 2 + l + height) % height
                    r,g,b = rgb.getpixel((imageX,imageY))
                    valor = matriz.item((k,l))
                    rojo += r * valor
                    verde += g * valor
                    azul += b * valor
            red = min(max((factor * rojo + aux),0),255)
            green = min(max((factor * verde + aux),0),255)
            blue = min(max((factor * azul + aux),0),255)
            pixels[i,j] = (int(red),int(green),int(blue))
    return nueva

def filtroPromedio(imagen, nueva):
    vecindad = [(0,0)]*9
    for i in range(1,imagen.size[0]-1):
        for j in range(1,imagen.size[1]-1):
            vecindad[0] = imagen.getpixel((i-1,j-1))
            vecindad[1] = imagen.getpixel((i-1,j))
            vecindad[2] = imagen.getpixel((i-1,j+1))
            vecindad[3] = imagen.getpixel((i,j-1))
            vecindad[4] = imagen.getpixel((i,j))
            vecindad[5] = imagen.getpixel((i,j+1))
            vecindad[6] = imagen.getpixel((i+1,j-1))
            vecindad[7] = imagen.getpixel((i+1,j))
            vecindad[8] = imagen.getpixel((i+1,j+1))
            promR = 0
            promG = 0
            promB = 0
            for i in range(len(vecindad)):
                r,g,b = vecindad[i]
                promR = promR + r
                promG = promG + g
                promB = promB + b
            promR = int(promR/len(vecindad))
            promG = int(promG/len(vecindad))
            promB = int(promB/len(vecindad))
            imagen.putpixel((i,j),(promR, promG, promB))
    return nueva

def filtroMediano(imagen, nueva):
    vecindad = [(0,0)]*9
    for i in range(1,imagen.size[0]-1):
        for j in range(1,imagen.size[1]-1):
            vecindad[0] = imagen.getpixel((i-1,j-1))
            vecindad[1] = imagen.getpixel((i-1,j))
            vecindad[2] = imagen.getpixel((i-1,j+1))
            vecindad[3] = imagen.getpixel((i,j-1))
            vecindad[4] = imagen.getpixel((i,j))
            vecindad[5] = imagen.getpixel((i,j+1))
            vecindad[6] = imagen.getpixel((i+1,j-1))
            vecindad[7] = imagen.getpixel((i+1,j))
            vecindad[8] = imagen.getpixel((i+1,j+1))
            vecindad.sort()
            nueva.putpixel((i,j),(vecindad[4]))
    return nueva
