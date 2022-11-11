import tkinter as tk
from tkinter import messagebox

listaId = [0, 1, 2]
listaNome = ['Açucar','Café','Pão']
listaPreco = [1.50, 5.00, 6.50]
listaQuantidade = [10, 20, 30]
#================tela do login das funções do Administrador==================
#============================================================================

def funcoes_admin():
    funAdm = tk.Toplevel()
    funAdm.title("Página do Adm - Lojito del Tadeo")
    funAdm["bg"] = "light green"
    funAdm.resizable(width=tk.FALSE, height=tk.FALSE)

    msg = tk.Label(funAdm, text="Oque deseja fazer?", background="light green",font="Arial 15 bold",fg="black")
    msg.place(x=200, y=50)

    btCadastrar = tk.Button(funAdm, width=15, height=4, text="Cadastrar\n Produtos", command=Cadastrar_produto)
    btCadastrar.place(x=170 , y=100)

    btListar = tk.Button(funAdm, width=15, height=4, text="Listar\n Produtos", command=listar_produto)
    btListar.place(x=300 , y=100)

    btDeletar = tk.Button(funAdm, width=15, height=4, text="Deletar\n Produtos", command=deletar_produtos)
    btDeletar.place(x=170 , y=180)

    btAlterar = tk.Button(funAdm, width=15, height=4, text="Alterar\n Produtos", command=alterar_produtos)
    btAlterar.place(x=300 , y=180)

    voltar = tk.Button(funAdm, width=10, height=3, text="Voltar", command=funAdm.destroy, bg="gray")
    voltar.place(x=250 , y=260)

    funAdm.geometry("600x400")
def login():
    j_admin = tk.Toplevel()
    j_admin.title("Login - Admin")
    j_admin["bg"] = "light green"
    j_admin.resizable(width=tk.FALSE, height=tk.FALSE)

    msg = tk.Label(j_admin, text="Digite a Senha \n para entrar no sistema:", background="light green",font="Arial 15 bold",fg="black")
    msg.place(x=175, y=80)
    
    login = ["40028922"]

    def verificarSenha():
        senha = campo_senha.get()
        if senha == "40028922":
            for widget in campo_senha.winfo_children():
                widget.destroy()
            messagebox.showinfo("Login","Logado com Sucesso!")
            funcoes_admin()
        else:
            messagebox.showwarning("Erro", "Senha Incorreta")
            for widget in campo_senha.winfo_children():
                widget.destroy()

        

    campo_senha = tk.Entry(j_admin, width=20, show="*")
    campo_senha.place(x=230 , y=160)

    voltar = tk.Button(j_admin, width=10, height=3, text="Voltar", command=j_admin.destroy, bg="gray")
    voltar.place(x=300 , y=200)

    logar = tk.Button(j_admin, width=10, height=3, text="Entrar", command=verificarSenha)
    logar.place(x=210 , y=200)


    j_admin.geometry("600x400")
#==========================Interface do Administrador=================================
#=====================================================================================



#Tela do Cadastrar
def Cadastrar_produto():
    cadProduto = tk.Toplevel()
    cadProduto.title("Admin - Cadastrar Produto")
    cadProduto["bg"] = "light green"
    cadProduto.resizable(width=tk.FALSE, height=tk.FALSE)

    msg = tk.Label(cadProduto, text="Cadastrar Produto", background="light green",font="Arial 15 bold",fg="black")
    msg.place(x=205, y=80)

    

    label1 = tk.Label(cadProduto, text="Nome:", background="light green",font="Verdana 10 bold",fg="black")
    label1.place(x=150 , y=140)

    label2 = tk.Label(cadProduto, text="Preço:", background="light green",font="verdana 10 bold",fg="black")
    label2.place(x=150, y=170)

    label3 = tk.Label(cadProduto, text="Quantidade:", background="light green",font="Verdana 10 bold",fg="black")
    label3.place(x=120, y=200)
    
    Camponome = tk.Entry(cadProduto, width=20)
    Camponome.place(x=230 , y=140)

    Campopreco = tk.Entry(cadProduto, width=20)
    Campopreco.place(x=230 , y=170)

    Campoquantidade = tk.Entry(cadProduto, width=20)
    Campoquantidade.place(x=230 , y=200)

    voltar = tk.Button(cadProduto, width=10, height=3, text="Voltar", command=cadProduto.destroy, bg="gray")
    voltar.place(x=300 , y=250)
    def bt_cadastrar():
        nome = Camponome.get()
        preco = Campopreco.get()
        quantidade = Campoquantidade.get()

        contador = len(listaId)


        listaId.append(contador)
        listaNome.append(nome)
        listaPreco.append(preco)
        listaQuantidade.append(quantidade)

        messagebox.showinfo("Cadastro de Produtos", "Cadastrado com Sucesso")

    cadastrar = tk.Button(cadProduto, width=10, height=3, text="Cadastrar", command=bt_cadastrar)
    cadastrar.place(x=210 , y=250)

   

    cadProduto.geometry("600x400")

def listar_produto():

    listarFun = tk.Toplevel()
    listarFun.title("Admin - Lista de Produtos")
    listarFun["bg"] = "light green"
    listarFun.resizable(width=tk.FALSE, height=tk.FALSE)

    msg = tk.Label(listarFun, text="PRODUTOS EM ESTOQUE", background="light green",font="Arial 15 bold italic",fg="gray")
    msg.place(x=170, y=25)

    id = tk.Label(listarFun, text="ID", background="light green",font="Verdana 10 bold",fg="black")
    id.place(x=100 , y=80)

    labelpro = tk.Label(listarFun, text="Produto", background="light green",font="Verdana 10 bold",fg="black")
    labelpro.place(x=205 , y=80)

    labelpre = tk.Label(listarFun, text="Preço(R$)", background="light green",font="Verdana 10 bold",fg="black")
    labelpre.place(x=325 , y=80)

    labelquan = tk.Label(listarFun, text="Quantidade", background="light green",font="Verdana 10 bold",fg="black")
    labelquan.place(x=440, y=80)

    voltar = tk.Button(listarFun, width=10, height=2, text="Voltar", command=listarFun.destroy, bg="gray")
    voltar.place(x=260 , y=300)

    lid = tk.Listbox(listarFun)
    lid.place(x=50,y=100)
    for id in listaId:
        lid.insert(tk.END, id)

    lNome = tk.Listbox(listarFun)
    lNome.place(x=175,y=100)
    for nome in listaNome:
        lNome.insert(tk.END, nome)
    
    lPreco = tk.Listbox(listarFun)
    lPreco.place(x=300,y=100)
    for preco in listaPreco:
        lPreco.insert(tk.END, preco)

    lQuant = tk.Listbox(listarFun)
    lQuant.place(x=425,y=100)
    for quant in listaQuantidade:
        lQuant.insert(tk.END, quant)

    listarFun.geometry("600x400")

def deletar_produtos():
    deletar = tk.Toplevel()
    deletar.title("Admin - Deletar Produtos")
    deletar["bg"] = "light green"
    deletar.resizable(width=tk.FALSE, height=tk.FALSE)
   

    deletar.geometry("600x400")

def alterar_produtos():
    alterar = tk.Toplevel()
    alterar.title("Admin - Alterar Produtos")
    alterar["bg"] = "light green"
    alterar.resizable(width=tk.FALSE, height=tk.FALSE)

    alterar.geometry("600x400")

#============================Interface dos Clientes===================================
#=====================================================================================

#Tela das Funções do Cliente
def funcoes_cliente():
    cliente = tk.Toplevel()
    cliente.title("Cliente - Lojito del Tadeo")
    cliente["bg"] = "light green"
    cliente.resizable(width=tk.FALSE, height=tk.FALSE)

    msg = tk.Label(cliente, text="Oque deseja fazer?", background="light green",font="Arial 15 bold",fg="black")
    msg.place(x=210, y=50)

    btComprar = tk.Button(cliente, width=20, height=3, text="Comprar", command=comprar_produtos)
    btComprar.place(x=230 , y=100)

    btCarrinho = tk.Button(cliente, width=20, height=3, text="Carrinho", command=carrinho)
    btCarrinho.place(x=230 , y=160)

    tFinalizar = tk.Button(cliente, width=20, height=3, text="Finalizar Compra", command=finalizar_compra)
    tFinalizar.place(x=230 , y=220)

    voltar = tk.Button(cliente, width=10, height=3, text="Voltar", command=cliente.destroy, bg="gray")
    voltar.place(x=265 , y=280)

    cliente.geometry("600x400")

def comprar_produtos():
    comprar = tk.Toplevel()
    comprar.title("Cliente - Produtos")
    comprar["bg"] = "light green"
    comprar.resizable(width=tk.FALSE, height=tk.FALSE)

    comprar.geometry("600x400")

def carrinho():
    carrinho = tk.Toplevel()
    carrinho.title("Cliente - Seu Carrinho")
    carrinho["bg"] = "light green"
    carrinho.resizable(width=tk.FALSE, height=tk.FALSE)

    carrinho.geometry("600x400")

def finalizar_compra():
    finalizar = tk.Toplevel()
    finalizar.title("Cliente - finalizar a compra")
    finalizar["bg"] = "light green"
    finalizar.resizable(width=tk.FALSE, height=tk.FALSE)

    finalizar.geometry("600x400")
#=======================================================================================
#=============================Tela Inicial abaixo=======================================

#Tela Inicial da Aplicação
inicio = tk.Tk()
inicio.title("Lojito del Tadeo")

inicio["bg"] = "light green"


titulo = tk.Label(text="Seja Bem-vindo", background="light green",font="Arial 15 bold",fg="black")
titulo.place(x=225, y=80)


btAdmin = tk.Button(inicio, width=20, height=2, text="Admin", command=login)  
btAdmin.place(x=230 , y=160)

btCliente = tk.Button(inicio, width=20, height=2, text="Cliente", command=funcoes_cliente)
btCliente.place(x=230 , y=205)

#Largura x Altura + Margem.Esqu + Margem.Topo
inicio.geometry("600x400")
inicio.mainloop()