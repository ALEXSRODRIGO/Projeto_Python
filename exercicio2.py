from tkinter import *
janela = Tk()
janela["bg"] = "blue"
app = Frame(janela)
app.grid()

menuPrincipal = Menu(app)
janela.config(menu=menuPrincipal)

def iniciarTelaCadastro():
    print("teste")



def escrever():
    print(entradaDados.get()," - ")

def escreverIdade():
    print(entryIdade.get())




#def limpar():


labelMsg = Label(janela, text="Informe seu nome:",font="Times", bg = "black", foreground="green")
labelMsg.place(x=100, y=100)

entradaDados  = Entry (janela)
entradaDados.place(x=220,y=103)

btnFalaNome = Button(janela,width=20, text='Escreve nome',command=escrever)
btnFalaNome.place(x=150,y=140)

labelIdade = Label(janela, text="Informe sua idade:",font="Times", bg = "black", foreground="green")
labelIdade.place(x=100, y=180)

entryIdade = Entry (janela)
entryIdade.place(x=220,y=183)

btnFalaIdade = Button(janela,width=20, text='Escreve Idade',command=escreverIdade)
btnFalaIdade.place(x=150,y=220)

labelCidade = Label(janela, text="Informe sua cidade:",font="Times", bg = "black", foreground="green")
labelCidade.place(x=100,y=260)

entryCidade = Entry (janela)
entryCidade.place(x=220,y=263)

titleVar ="Sistema Tarumã"
janela.title(titleVar)
janela.geometry("1300x768")
janela.resizable(True,False)
janela.mainloop()
janela.destroy()
#api.get  / api.post  / api.put  / api.delete