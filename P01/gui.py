# -*- coding: utf-8 -*-
from PIL import ImageTk, Image
from tkinter import *
from tkinter.filedialog import askopenfilename
from filtros import *

root = Tk()
root.title('Proceso Digital de Imágenes')

# acceptable formats
formats = [('image files', ('.png', '.jpg')),]
# filters
FILTERS = ['normal', 'mica roja','mica verde','mica azul','0.30r+0.59g+.011b',
           'r+g+b/3','max(r,g,b)','min(r,g,b)','max(r,g,b)+min(r,g,b)/2',
           'azar','alto contraste','alto contraste inverso',
           'Blur','Motion blur','Encontrar bordes','Sharpen','Emboss','Promedio',
           'Mediano',
           'M color','M tonos de grises','MNH#Q...','MNH#Q...(color)',
           'MNH#Q...(b/n)','Poner texto','Dominó Negro','Dominó Blanco','Naipes']

img = None
new = None
name_img = ''

'''Looks for an image'''
def search():
    filename = askopenfilename(filetypes=formats)
    global name_img
    name_img = getName(str(filename))
    path = filename
    global img
    global new
    img = Image.open(filename)
    new = Image.open(filename)
    tkimage = ImageTk.PhotoImage(img)
    lbl = Label(root, image=tkimage)
    lbl.image = tkimage
    lbl.grid(row=0, column=0, columnspan=3)
    # TODO: si elige otra imagen, borrar todo lo anterior
    # TODO: cambiar los botones (StringVar) para elegir entre pŕácticas

def getName(filename):
    f = filename.split('/')
    n = f[-1].split('.')
    return n[0]

def applyFilter():
    name = variable.get()
    photo = None
    print("MY FILTER IS: ", name)
    if (name == 'mica roja'):
        photo = filtroMicaRoja(img, new)
    if (name == 'mica verde'):
        photo = filtroMicaVerde(img, new)
    if (name == 'mica azul'):
        photo = filtroMicaAzul(img, new)
    if (name == '0.30r+0.59g+.011b'):
        photo = filtroFormula(img, new)
    if (name == 'r+g+b/3'):
        photo = filtroPromedio(img, new)
    if (name == 'max(r,g,b)'):
        photo = filtroMaxRGB(img, new)
    if (name == 'min(r,g,b)'):
        photo = filtroMinRGB(img, new)
    if (name == 'max(r,g,b)+min(r,g,b)/2'):
        photo = filtroMinMaxProm(img, new)
    if (name == 'azar'):
        photo = filtroAzar(img, new)
    if (name == 'alto contraste'):
        photo = filtroAltoContraste(img, new)
    if (name == 'alto contraste inverso'):
        photo = filtroAltoContrasteInverso(img, new)
    if (name == 'Blur'):
        photo = filtroBlur(img, new)
    if (name == 'Motion blur'):
        photo = filtroMotionBlur(img, new)
    if (name == 'Encontrar bordes'):
        photo = filtroEncontrarBordes(img, new)
    if (name == 'Sharpen'):
        photo = filtroSharpen(img, new)
    if (name == 'Emboss'):
        photo = filtroEmboss(img, new)
    if (name == 'Promedio'):
        photo = filtroPromedio(img, new)
    if (name == 'Mediano'):
        photo = filtroMediano(img, new)
    if (name == 'M color'):
        photo = img
        filtroM(img, new, name_img)
    if (name == 'M tonos de grises'):
        photo = filtroFormula(img,new)
        filtroM(photo, photo, name_img)
    if (name == 'MNH#Q...'):
        filtroMNHQ(img, new, 'mnhq_' + name_img)
    if (name == 'MNH#Q...(b/n)'):
        photo = filtroFormula(img,new)
        filtroMNHQGris(photo, photo, 'mnhq_bn_' + name_img)
    if (name == 'MNH#Q...(color)'):
        photo = img
        filtroMNHQColor(img, new, 'mnhq_color_' + name_img)
    if (name == 'Naipes'):
        photo = filtroFormula(img,new)
        filtroNaipes(photo, photo, 'naipes_' + name_img)
    if (name == 'Dominó Negro'):
        photo = filtroFormula(img,new)
        filtroDomino(photo, photo, 'domino_negro_' + name_img, 1)
    if (name == 'Dominó Blanco'):
        photo = filtroFormula(img,new)
        filtroDomino(photo, photo, 'domino_blanco_' + name_img, 0)
    tkimage = ImageTk.PhotoImage(photo)
    lbl = Label(root, image=tkimage)
    lbl.image = tkimage
    lbl.grid(row=0, column=0, columnspan=3)

# quit button
btn_quit = Button(root, text='Exit', command=root.quit)
btn_quit.grid(row=1, column=1)
btn_select = Button(root, text='Select Image', command=search)
btn_select.grid(row=1, column=0)
variable = StringVar(root)
variable.set(FILTERS[0]) # default option
filter_menu = OptionMenu(root, variable, *FILTERS)
filter_menu.grid(row=1, column=2)
btn_accept = Button(root, text='Apply', command=applyFilter)
btn_accept.grid(row=1, column=3)

root.mainloop()
