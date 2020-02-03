# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

root = Tk()
root.title('Proceso Digital de Imágenes')

# acceptable formats
formats = [('image files', ('.png', '.jpg')),]
# filters
FILTERS = ['normal','azar','r+g+b/3','0.30r+0.59g+.011b',
           'max(r,b,b)+min(r,b,b)/2','max(r,g,b)','min(r,g,b)','mica roja',
           'mica verde','mica azul','alto contraste','alto contraste inverso']

'''Looks for an image'''
def search():
    filename = askopenfilename(filetypes=formats)
    img = Image.open(filename)
    tkimage = ImageTk.PhotoImage(img)
    lbl = Label(root, image=tkimage)
    lbl.image = tkimage
    lbl.grid(row=0, column=0, columnspan=3)

def applyFilter():
    name = variable.get()
    print("MY FILTER IS: ", name)

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
