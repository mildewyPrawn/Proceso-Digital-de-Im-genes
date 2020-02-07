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
           'azar','alto contraste','alto contraste inverso']

img = None
new = None

'''Looks for an image'''
def search():
    filename = askopenfilename(filetypes=formats)
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
