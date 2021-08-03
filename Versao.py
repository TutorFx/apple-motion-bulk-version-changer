import glob, os
from sys import version
from tkinter import filedialog
import tkinter as tk
import re

def rodar(v, path):
    print('rodando panel')
    versionTemplate = '<displayversion>'+v+'</displayversion>'
    os.chdir(path)
    for file in glob.glob(path+"/**/*.moti", recursive= True):

        #print(file) ## 5.4.4
            
        document = open(file, "r").read()
        output = re.sub(r"(?s)<displayversion>.*?</displayversion>", r"%s" % versionTemplate, document, 1)
        with open(file, 'w') as f:
            f.write(output)
        # try:
            
        # except:
        #     print('deu ruim')

def panel(path):
    print('rodando panel')
    root= tk.Tk()
    root.title("LenoFx - Trocador de versão")
    canvas1 = tk.Canvas(root, width = 400, height = 300)
    canvas1.pack()

    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry1)
    def btnSelect():
        root.withdraw()
    def Proceed ():  
        input = entry1.get()
        if input != '':
            label1 = tk.Label(root, text='Processo de alteracao concluso com sucesso para: '+input+" no diretório " + path, font="helvetica 14", wraplength=300, justify="center")
            canvas1.create_window(200, 230, window=label1)
            rodar(input, path)
        else: 
            label1 = tk.Label(root, text= 'Você se esqueceu de colocar uma versão', font="helvetica 14", wraplength=300, justify="center")
            canvas1.create_window(200, 230, window=label1)
        
    button1 = tk.Button(root, text='Alterar versão', command=Proceed)
    canvas1.create_window(200, 180, window=button1)
    root.attributes('-topmost',True)
    root.update()
    root.mainloop()

def run():
    rootd= tk.Tk()
    rootd.title("LenoFx - Trocador de versão")
    #rootd.withdraw()
    def callback():
        name= filedialog.askdirectory() 
        if name != '':
            print(name)
            panel(name)
        else:
            print('diretorio n selecionado')
    errmsg = 'Error!'
    tk.Button(rootd ,text='Clique para selecionar um diretório', 
        command=callback).pack(fill=tk.X)
    tk.mainloop()
    

run()