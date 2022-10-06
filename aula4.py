from cgitb import text 
import tkinter as tk
#from turtle import width
#from PIL import ImageTk, Image

#from numpy import imag

  


def cadastrarUsuario():
    janelaUsuario = tk.Toplevel(app)

    #labelMsg = Label(janela, text="Informe seu nome:",font="Times", bg = "black", foreground="green")
    #labelMsg.place(x=100, y=100)

    #entradaDados  = Entry (janela)
    #entradaDados.place(x=220,y=103)

    janelaUsuario.grid()

    lblNome = tk.Label(janelaUsuario, text="Informe seu nome:",font="Times", bg = "white", foreground="green")
    lblNome.place(x=100,y=100)
    varNome = tk.Entry(janelaUsuario)
    varNome.place(x=100,y=130)

    lblSobrenome = tk.Label(janelaUsuario, text="Informe seu sobrenome:",font="Times", bg = "white", foreground="green")
    lblSobrenome.place(x=350,y=100)
    varSobrenome = tk.Entry(janelaUsuario)
    varSobrenome.place(x=350,y=130)

    lblCidade = tk.Label(janelaUsuario, text="Informe sua Cidade:",font="Times", bg = "white", foreground="green")
    lblCidade.place(x=100,y=160)
    varCidade = tk.Entry(janelaUsuario)
    varCidade.place(x=100,y=190)

    lblEstado = tk.Label(janelaUsuario, text="Informe o Estado:",font="Times", bg = "white", foreground="green")
    lblEstado.place(x=350,y=160)
    varEstado = tk.Entry(janelaUsuario) 
    varEstado.place(x=350,y=190)

    lblDtNasc = tk.Label(janelaUsuario, text="Informe a Data de Nascimento:",font="Times", bg = "white", foreground="green")
    lblDtNasc.place(x=100,y=220)
    varDtNasc = tk.Entry(janelaUsuario)
    varDtNasc.place(x=100,y=250)

    lblSexo = tk.Label(janelaUsuario, text="Informe o Sexo:",font="Times", bg = "white", foreground="green")
    lblSexo.place(x=350,y=220)
    varSexo = tk.Entry(janelaUsuario)
    varSexo.place(x=350,y=250)

    #botão cadastrar
    btnSalvar = tk.Button(janelaUsuario, text="Salvar", command=salvarUsuario)
    btnSalvar.place(x=100,y=300)

    btnLimpar = tk.Button(janelaUsuario, text="Limpar", command="" )
    btnLimpar.place(x=200,y=300)

    btlTeste = tk.Listbox(janelaUsuario)
    btlTeste.place(x=300,y=300)

    def salvarUsuario():
        print("O nome e sobrenome informado foi:" , varNome.get(), varSobrenome.get())

    janelaUsuario.title("Cadastro de usuários")
    janelaUsuario.geometry("800x600")
    janelaUsuario.resizable(True,False)
    

def cadastrarProduto():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
    janelaProduto.resizable(True,False)

app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar usuário",command=cadastrarUsuario)
fileMenu.add_command(label="Cadastrar produto",command=cadastrarProduto)
menuPrincipal.add_cascade(label="Função",menu=fileMenu)
fileMenuD = tk.Menu(menuPrincipal)
fileMenuD.add_command(label="Produtos",command="")
menuPrincipal.add_cascade(label="Relatórios",menu=fileMenuD)

fileMenu.add_command(label="Sair",command=exit)

#buttonExample = tk.Button(app, text="Create new Window",command="teste")
#buttonExample.place(x=100,y=50)

app.title("Sistema Tarumã")
app.geometry("800x600")
app.resizable(False,False)
app.mainloop()
app.destroy()
