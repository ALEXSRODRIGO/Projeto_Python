import tkinter as tk
from tkinter import Scrollbar, ttk
import mysql.connector
#cmd ....pip install mysql-connector
from tkinter.messagebox import showinfo
#from PIL import ImageTk, Image
#from numpy import Imag

class Usuarios:
        def __init__(self, id, nome,sobrenome,cidade,estado,data_nascimento):
                self.id = id
                self.nome = nome
                self.sobrenome = sobrenome
                self.cidade = cidade
                self.estado = estado
                self.data_nascimento = data_nascimento


def conexao():
        try:
                conexao = mysql.connector.connect(host="localhost",user="root",passwd="",db="banco_python")
                print("conectado")
                return conexao
        except mysql.connector.Error as e:
                print(f'Erro ao conectar no servidor MySql: {e}')

def desconectar(conexao):
        if conexao:
                conexao.close()

def selecionarUsuarios(janelaUsuarios):
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        table = cursor.fetchall()
        print('\n Usuarios: ')
        
        columns = ('id','nome','sobrenome','cidade','estado','data_nascimento')
        tree = ttk.Treeview(janelaUsuarios,columns=columns,show='headings')
        #define cabeçalhos
        tree.heading('id',text="#")
        tree.heading('nome',text="Nome")
        tree.heading('sobrenome',text="SobreNome")
        tree.heading('cidade',text="Cidade")
        tree.heading('estado',text="Estado")
        tree.heading('data_nascimento',text="Data Nascimento")

        def item_selected(self):
               item = tree.focus()

        tree.bind('<<TreeviewSelect>>',item_selected)
        tree.grid(row=0,column=0,sticky=tk.NSEW)

        #adicionar uma barra de rolagem
        Scrollbar = ttk.Scrollbar(janelaUsuarios, orient=tk.VERTICAL,command=tree.yview)
        tree.configure(yscroll=Scrollbar.set)
        Scrollbar.grid(row=0,column=1,sticky='ns')

        
        usuarios = []
        for row in table:
               usuarios.append((f'{row[0]}',f'{row[1]}',f'{row[2]}',f'{row[3]}',f'{row[4]}',f'{row[5]}'))
        for user in usuarios:
               tree.insert('',tk.END,values=user)

def abrirTelaUsuarios():
    janelaUsuarios = tk.Toplevel(app)

    selecionarUsuarios(janelaUsuarios)

    lblNome = tk.Label(janelaUsuarios,text="Informe o seu nome: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblNome.place(x=100,y=300)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=230,y=305)
    
    lblSobrenome = tk.Label(janelaUsuarios,text="Informe o seu sobrenome: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblSobrenome.place(x=100,y=325)
    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=260, y=330)

    lblDataNascimento = tk.Label(janelaUsuarios,text="Informe sua data de nascimento"
            ,font="Times"
            ,bg="white", foreground="black")
    lblDataNascimento.place(x=100, y=350)
    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=300, y=355)

    lblCidade = tk.Label(janelaUsuarios,text="Informe a sua cidade"
            ,font="Times"
            ,bg="white", foreground="black")
    lblCidade.place(x=100,y=375)
    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place(x=230,y=380)

    lblEstado = tk.Label(janelaUsuarios, text="Informe o estado: "
            ,font="Times"
            ,bg="white",foreground="black")
    lblEstado.place(x=100, y=400)
    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place(x=230, y=405)

 
    def inserirUsuarios(usuario):
                conn = conexao()
                cursor = conn.cursor()
                cursor.execute(
                f"INSERT INTO usuarios(id, nome, sobrenome, cidade, estado, data_nascimento)" f"VALUES('{usuario.id}','{usuario.nome}','{usuario.sobrenome}','{usuario.cidade}','{usuario.estado}','{usuario.data_nascimento}')")
                conn.commit()
                desconectar(conn)
    
    def salvarUsuario():
        #conn = conexao()
        #print("O nome informado foi: ",entryNome.get())
        #print("O sobrenome informado foi: ",entrySobrenome.get())
        #print("A data de nascimento informada foi: ",entryDataNascimento.get())
        #print("A cidade informada foi: ",entryCidade.get())
        #print("O estado informado foi: ",entryEstado.get())
        usuario = Usuarios(None,entryNome.get(),entrySobrenome.get(),entryCidade.get(),entryEstado.get(),entryDataNascimento.get())

        inserirUsuarios(usuario)

    btnSalvar = tk.Button(janelaUsuarios,width=20,text="Salvar", command=salvarUsuario)
    btnSalvar.place(x=100,y=430)
    
    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")

    #entryNome.insert("end","teste")
    #entryNome.insert("end","tormes")

        
    
    


def abrirTelaProdutos():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários",command=abrirTelaUsuarios)
fileMenu.add_command(label="Cadastrar Produtos",command=abrirTelaProdutos)
menuPrincipal.add_cascade(label="Funcao",menu=fileMenu)

#buttonExample = tk.Button(app, 
#              text="Create new window",
#              command=createNewWindow)
#buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()