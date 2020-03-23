from PIL import Image, ImageFont, ImageDraw
from random import randrange
import numpy as np

# Funciones auxiliares

mini = lambda x, y : min(x,y) # Nos da el mínimo de dos elementos
maxi = lambda x, y : max(x,y) # Nos da el máximo de dos elementos
# Nos da la suma del mínimo y máximo de tres elementos
minmaxprom = lambda x,y,z : (mini(x, mini(y, z)))+(maxi(x, maxi(y, z)))

# abrir y cerrar líneas en HTML
abreRGB = '<font size="1" style="color:rgb('
cierraRGB = ');">M</font>'

# fonts
cards = "<PRE><style>@font-face{font-family: 'Playcrds';src: url('dominos-cartas_FILES/Playcrds.TTF') format('truetype');}font{font-family: 'Playcrds'}</style>"
negro = "<PRE><style>@font-face{font-family: 'lasvbld_';src: url('dominos-cartas_FILES/lasvbld_.TTF') format('truetype');}font{font-family: 'lasvbld_'}</style>"
blnco = "<PRE><style>@font-face{font-family: 'lasvwd__';src: url('dominos-cartas_FILES/lasvwd__.TTF') format('truetype');}font{font-family: 'lasvwd__'}</style>"

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

def filtroM(imagen, nueva, nombre):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    f = open(nombre + '.html', 'w')
    for i in range(height):
        for j in range(width):
            r,g,b = rgb.getpixel((j,i))
            f.write(abreRGB + str(r)+','+str(g)+','+str(b) + cierraRGB)
        f.write('<br>')
    f.close()

def filtroMNHQ(imagen, nueva, nombre):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write('<PRE>')
    for i in range(height):
        for j in range(width):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 16):
                f.write('<font size="1">M</font>')
            elif(r >= 16 and r < 32):
                f.write('<font size="1">N</font>')
            elif(r >= 32 and r < 48):
                f.write('<font size="1">H</font>')
            elif(r >= 48 and r < 64):
                f.write('<font size="1">#</font>')
            elif(r >= 64 and r < 80):
                f.write('<font size="1">Q</font>')
            elif(r >= 80 and r < 96):
                f.write('<font size="1">U</font>')
            elif(r >= 96 and r < 112):
                f.write('<font size="1">A</font>')
            elif(r >= 112 and r < 128):
                f.write('<font size="1">D</font>')
            elif(r >= 128 and r < 144):
                f.write('<font size="1">O</font>')
            elif(r >= 144 and r < 160):
                f.write('<font size="1">Y</font>')
            elif(r >= 160 and r < 176):
                f.write('<font size="1">2</font>')
            elif(r >= 176 and r < 192):
                f.write('<font size="1">$</font>')
            elif(r >= 192 and r < 208):
                f.write('<font size="1">%</font>')
            elif(r >= 208 and r < 224):
                f.write('<font size="1">+</font>')
            elif(r >= 224 and r < 240):
                f.write('<font size="1">-</font>')
            elif(r >= 240 and r < 256):
                f.write('<font size="1"> </font>')
        f.write('<br>')
    f.close()

def filtroMNHQGris(imagen, nueva, nombre):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write('<PRE>')
    for i in range(height):
        for j in range(width):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 16):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">M</font>')
            elif(r >= 16 and r < 32):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">N</font>')
            elif(r >= 32 and r < 48):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">H</font>')
            elif(r >= 48 and r < 64):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">#</font>')
            elif(r >= 64 and r < 80):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">Q</font>')
            elif(r >= 80 and r < 96):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">U</font>')
            elif(r >= 96 and r < 112):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">A</font>')
            elif(r >= 112 and r < 128):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">D</font>')
            elif(r >= 128 and r < 144):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">O</font>')
            elif(r >= 144 and r < 160):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">Y</font>')
            elif(r >= 160 and r < 176):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">2</font>')
            elif(r >= 176 and r < 192):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">$</font>')
            elif(r >= 192 and r < 208):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">%</font>')
            elif(r >= 208 and r < 224):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">+</font>')
            elif(r >= 224 and r < 240):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">-</font>')
            elif(r >= 240 and r < 256):
                f.write(abreRGB +str(0)+','+str(0)+','+str(0)+','+');"> </font>')
        f.write('<br>')
    f.close()

def filtroMNHQColor(imagen, nueva, nombre):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    gris = filtroFormula(imagen,nueva)
    widthG = gris.size[0]
    heightG = gris.size[1]
    rgbG = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write('<PRE>')
    for i in range(heightG):
        for j in range(widthG):
            r,g,b = rgb.getpixel((j,i))
            rG,gG,bG = rgbG.getpixel((j,i))
            if(rG >= 0 and rG < 16):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">M</font>')
            elif(rG >= 16 and rG < 32):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">N</font>')
            elif(rG >= 32 and rG < 48):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">H</font>')
            elif(rG >= 48 and rG < 64):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">#</font>')
            elif(rG >= 64 and rG < 80):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">Q</font>')
            elif(rG >= 80 and rG < 96):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">U</font>')
            elif(rG >= 96 and rG < 112):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">A</font>')
            elif(rG >= 112 and rG < 128):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">D</font>')
            elif(rG >= 128 and rG < 144):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">O</font>')
            elif(rG >= 144 and rG < 160):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">Y</font>')
            elif(rG >= 160 and rG < 176):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">2</font>')
            elif(rG >= 176 and rG < 192):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">$</font>')
            elif(rG >= 192 and rG < 208):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">%</font>')
            elif(rG >= 208 and rG < 224):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">+</font>')
            elif(rG >= 224 and rG < 240):
                f.write(abreRGB+str(r)+','+str(g)+','+str(b)+');">-</font>')
            elif(rG >= 240 and rG < 256):
                f.write(abreRGB +str(0)+','+str(0)+','+str(0)+','+');"> </font>')
        f.write('<br>')
    f.close()

def filtroNaipes(imagen, nueva, nombre):
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write(cards)
    for i in range(height):
        for j in range(width):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 19):
                f.write('<font size="1">A</font>')
            elif(r >= 19 and r < 38):
                f.write('<font size="1">B</font>')
            elif(r >= 38 and r < 57):
                f.write('<font size="1">C</font>')
            elif(r >= 57 and r < 76):
                f.write('<font size="1">D</font>')
            elif(r >= 76 and r < 95):
                f.write('<font size="1">E</font>')
            elif(r >= 95 and r < 114):
                f.write('<font size="1">F</font>')
            elif(r >= 114 and r < 133):
                f.write('<font size="1">G</font>')
            elif(r >= 133 and r < 152):
                f.write('<font size="1">H</font>')
            elif(r >= 152 and r < 171):
                f.write('<font size="1">I</font>')
            elif(r >= 171 and r < 190):
                f.write('<font size="1">J</font>')
            elif(r >= 190 and r < 209):
                f.write('<font size="1">K</font>')
            elif(r >= 209 and r < 228):
                f.write('<font size="1">L</font>')
            elif(r >= 228 and r < 256):
                f.write('<font size="1">M</font>')
        f.write('<br>')
    f.close()

def filtroDomino(imagen, nueva, nombre, color):
    current = negro if color == 1 else blnco
    width = imagen.size[0]
    height = imagen.size[1]
    rgb = imagen.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write(current)
    for i in range(height):
        for j in range(width):
            r,g,b = rgb.getpixel((j,i))
            if(r >= 0 and r < 25):
                f.write('<font size="1">0</font>')
            elif(r >= 25 and r < 50):
                f.write('<font size="1">1</font>')
            elif(r >= 50 and r < 75):
                f.write('<font size="1">2</font>')
            elif(r >= 75 and r < 100):
                f.write('<font size="1">3</font>')
            elif(r >= 100 and r < 125):
                f.write('<font size="1">4</font>')
            elif(r >= 125 and r < 150):
                f.write('<font size="1">5</font>')
            elif(r >= 150 and r < 175):
                f.write('<font size="1">6</font>')
            elif(r >= 175 and r < 200):
                f.write('<font size="1">7</font>')
            elif(r >= 200 and r < 225):
                f.write('<font size="1">8</font>')
            elif(r >= 225 and r < 256):
                f.write('<font size="1">9</font>')
        f.write('<br>')
    f.close()

def marcaDeAgua(imagen, nueva, texto):
    tSize = 50
    tX = 10
    tY = 30
    font = 'dominos-cartas_FILES/From Cartoon Blocks.ttf'
    return marcaDeAguaAux(imagen, texto, tSize, 400, 200, font)

def marcaDeAguaAux(imagen, texto, size, tX, tY, font):
    rgba = imagen.convert('RGBA')
    tImage = Image.new('RGBA', rgba.size, (255,255,255,0))
    font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(tImage)
    draw.text((tX, tY), texto, font=font, fill=(255,0,0,255))
    return Image.alpha_composite(rgba, tImage)

def quitaMarca(imagen, nueva):
    rgb = imagen.convert('RGB')
    pixels = nueva.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            if ((r - g) < 10):
                pass
            else:
                prom = (int)((1.3475)*((r+g+b)/3))
                pixels[i,j] = (prom, prom, prom)
    return nueva
