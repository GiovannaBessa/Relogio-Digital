from tkinter import*
import tkinter
from datetime import datetime

#Cria a janela
root=Tk()
#Dimensão da janela
root.geometry("420x165")
#Impede que alterem a dimensão da janela
root.resizable(width=0, height=0)
#Titulo da janela
root.title("Relogio Digital")

#Função do Relogio
def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "  " + str(dia) + "/" + str(mes) + "/" + (ano))

l1 = Label(root, text="10:05:05", font=('Arial 80'), bg= 'black', fg= 'white')
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(root, font=('digital-7 20'), bg='black', fg='white')
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
root.mainloop()