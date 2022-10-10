import tkinter as tk
from PIL import ImageTk, Image

app = tk.Tk()
janela = tk.Toplevel(app)

#imgTeste = Image.open('carro.png')
#imgTeste.show()

titleVar ="Sistema Tarumã"
janela.title(titleVar)
janela.geometry("800x600")
janela.resizable(True,False)
janela.mainloop()
janela.destroy()