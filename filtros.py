from PIL import Image
from random import randrange

# Funciones auxiliares

mini = lambda x, y : min(x,y) # Nos da el mínimo de dos elementos
maxi = lambda x, y : max(x,y) # Nos da el máximo de dos elementos
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
