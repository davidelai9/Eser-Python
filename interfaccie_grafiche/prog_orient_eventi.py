
# ! GUI Graphical User Interface -> forse

# ? Tkinter è una libreria di Python -> fa parte della libreria standard quindi non viene scaricata con pip ma va solo importata

# finestra principale si cre con Tk()

from tkinter import * #? si consiglia importare tutto cosi da non dover stare ad importare metodi/classi che potrebbero servire

main = Tk() #? creazione finestra principale

def stampaCiao():
    print("Ciao")

main.geometry("300x300") #? scegli in pixel quanto sia grande la finestra

main.title("Puoi dare il titolo") #? scegli il titolo
# root = Tk()

my_button = Button(main, text = "Clicca qui", bg = "red", command =stampaCiao) # crea bottone ma non lo visualizzi ancora; in command non mettere le parentesi per richiamare la funzione

my_button.bind()   # puoi associare anche più funzioni al bottone

my_button.pack()





main.mainloop() #! crea il main loop cosi da poter visualizzare le finestre create [ per chiuderla basta click nella x della finestra ]

