from encodings.utf_8 import encode
from re import I
import Funcoes
import pandas as pd
import csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
head = ['Produto', 'Preço', 'Quantidade']
'''
-> Modelo utilizado no arquivo de estoque que mostra respectivamente o item, seu preço e sua quantidade
'''
lista = {}
carrinho = {}
valorTotal = []

def TelaInicial (): 
    '''
    -> Função que mostra a tela inicial do programa.
    '''
    Painel("| Lojito Del Tadeo |")
    print(f"{Fore.YELLOW}1 - Admnistrador\n2 - Cliente\n0 - Sair\n{Fore.BLUE}{'-'*20}")
    r = input(f"{Fore.LIGHTYELLOW_EX}Opção: ") #Receberá a resposta do usuário entre 1, 2 e 0, como mostrado pelo menu
    while r not in "120":
        r = input(f"{Fore.RED}Opção inválida. Tente novamente: ")
    return r


def Painel(mensagem): 
    '''
    -> Função genérica para estilizar os títulos e menus do programa
    '''
    print(f"{Fore.BLUE}{'─' * (len(mensagem))}")
    print(f"{Fore.CYAN}{mensagem.center(len(mensagem))}")
    print(f"{Fore.BLUE}{'─' * (len(mensagem))}")


def Cadastrar(): 
    '''
    -> Função para cadastrar um produto (juntamente com seu preço e quantidade) no estoque
    '''
    Funcoes.Painel("Cadastrar Produto")
    while True:
        produto = input(f"{Fore.YELLOW}Nome do produto: ").capitalize().strip()
        preco = float(input(f"{Fore.GREEN}Preço: R$"))
        quantidade = int(input(f"{Fore.YELLOW}Quantidade: "))
        confirmacao = input(f"{Fore.GREEN}Confirmar cadastro [S/N]? ").upper().strip()
        while confirmacao not in "SN ":
            confirmacao = input(f"{Fore.RED}Resposta inválida. Confirmar cadastro [S/N]? ").upper()
        if confirmacao == "S":
            cadastrar = {'Produto':produto,'Preço':preco,'Quantidade':quantidade}
            with open('estoque.csv', 'a', newline='', encoding='utf-8') as f_object:
                dictwriter_object = csv.DictWriter(f_object, fieldnames = head) 
                dictwriter_object.writerow(cadastrar)
                f_object.close()
        resp = input(f"{Fore.YELLOW}\nDeseja continuar [S/N]? ").upper()
        while resp not in "SN ":
            resp = input(f"{Fore.RED}Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            break
        print()


def Remover():
    '''
    Função para remover um produto do estoque
    '''
    while True:
        linha = []
        Funcoes.Listar()
        elementoRetirar = input(f"{Fore.YELLOW}Digite o item que deseja remover: ").capitalize().strip()
        confirmacao = input(f"{Fore.YELLOW}Confirmar remoção [S/N]? ").upper().strip()
        while confirmacao not in "SN":
            confirmacao = input(f"{Fore.RED}Resposta inválida. {Fore.YELLOW}Confirmar remoção [S/N]? ")
        if confirmacao == "S":
            with open('estoque.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                for produto in reader:
                    linha.append(produto)
                    for campo in produto:
                        if campo == elementoRetirar:
                            linha.remove(produto)
                            break
            with open('estoque.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(linha)
            print(f"{elementoRetirar} retirado com sucesso!")
        resp = input(f"\n{Fore.YELLOW}Deseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input(f"{Fore.RED}Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            break
    
def Alterar(): 
    '''
    Função que altera o preço e/ou quantidade de um produto do estoque
    '''
    Funcoes.Listar()
    while True:
        elementoAlterar = input("Informe o item que deseja alterar: ").capitalize().strip()
        novoPreco = float(input(f'Digite o novo preço do produto {elementoAlterar}: R$'))
        novoQntd = int(input(f'Digite a nova quantidade do produto {elementoAlterar}: '))
        linha = []
        with open('estoque.csv', 'r', encoding='utf-8') as readFile:
            reader = csv.reader(readFile)
            for produto in reader:
                linha.append(produto)
                for campo in produto:
                    if campo == elementoAlterar:
                        linha.remove(produto)
                        break
        with open('estoque.csv', 'w', newline='', encoding='utf-8') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(linha)
        alteracao = {'Produto':elementoAlterar,'Preço':novoPreco,'Quantidade':novoQntd}
        with open('estoque.csv', 'a', newline='', encoding='utf-8') as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames = head)
            dictwriter_object.writerow(alteracao)
            f_object.close()
        resp = input("\nDeseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input(f"{Fore.RED}Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            break


def Listar(): 
    '''
    -> Lista todos os produtos do estoque
    '''
    print(f"{Fore.BLUE}{'-'*21}\nLista de Produtos\n{'-'*21}")
    tabela = pd.read_csv('estoque.csv', names=head, skiprows=[0], index_col='Produto')
    print(tabela)


def Acao(): 
    '''
    -> Função que compila todas as ações do administrador da loja
    '''
    while True:
        Painel("| Função ADM |")
        acao = input(f"1 - Cadastrar\n2 - Remover\n3 - Alterar\n4 - Listar\n0 - Sair\n{Fore.BLUE}{'-'*21}\nO que deseja fazer? ").strip()
        while acao not in "12340":
            acao = input(f"{Fore.RED}Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Funcoes.Cadastrar()
        if acao == "2":
            Funcoes.Remover()
        if acao == "3":
            Funcoes.Alterar()
        if acao == "4":
            Listar()
        if acao == "0":
            break


def Cliente(): 
    '''
    -> Função que compila todas as ações do cliente
    '''
    while True:
        Painel("| Função Cliente |")
        acao = input(f"{Fore.YELLOW}1 - Comprar Produtos\n2 - Meu Carrinho\n3 - Finalizar Compra\n0 - Sair\n{Fore.BLUE}{'-'*21}\nO que deseja fazer? ").upper().strip()
        while acao not in "1230":
            acao = input(f"{Fore.RED}Resposta incorreta. Tente novamente: ")
        if acao == "1":
            Listar()
            Funcoes.Comprar()
        if acao == "2":
            Funcoes.MeuCarrinho(carrinho)
        if acao == "3":
            Funcoes.FinalizarCompra()
            break
        if acao == "0":
            break

carrinho = []
carrinho2 = []
def Comprar(): 
    '''
    -> Função que contém as ações de compra de produtos do cliente
    '''
    somaValor = 0
    linha = []
    while True:
        item = input('Selecione o produto para adicionar ao carrinho: ').capitalize().strip()
        quantidade = int(input("Selecione a quantidade do produto: "))
        confirmacao = input("Confirmar produto [S/N]? ").upper().strip()
        while confirmacao not in "SN":
            confirmacao = input(f"{Fore.RED}Resposta inválida. Confirmar produto [S/N]? ")
        if confirmacao == "S":
            df = pd.read_csv('estoque.csv')
            with open('estoque.csv', 'r', encoding="utf-8") as readFile:
                reader = csv.reader(readFile)
                i = -2
                for produto in reader:
                    linha.append(produto)
                    i += 1
                    for campo in produto:
                        if campo == item:
                            antigaQntd = df.loc[i, 'Quantidade'] - quantidade
                            if antigaQntd >= 0:
                                somaValor += df.loc[i, 'Preço'] * quantidade
                                carrinho.append(item)
                                carrinho2.append(quantidade)
                                df.loc[i, 'Quantidade'] -= quantidade
                                df.to_csv('estoque.csv', index=False, encoding="utf-8")
                            else:
                                print("Erro! Quantidade acima do estoque.")
                                while antigaQntd < 0:
                                    quantidade = int(input("Quantidade acima do estoque, digite uma quantidade válida: "))
                                    antigaQntd = df.loc[i, 'Quantidade'] - quantidade
                                    if antigaQntd >= 0:
                                        somaValor += df.loc[i, 'Preço'] * quantidade
                                        carrinho.append(item)
                                        carrinho2.append(quantidade)
                                        df.loc[i, 'Quantidade'] -= quantidade
                                        df.to_csv('estoque.csv', index=False, encoding="utf-8")
                                        break
        resp = input("\nDeseja continuar [S/N]? ").upper()
        while resp not in "SN":
            resp = input(f"{Fore.RED}Resposta inválida. Deseja continuar [S/N]? ").upper()
        if resp == "N":
            valorTotal.append(somaValor)
            break


def MeuCarrinho(produtos): 
    '''
    -> Função que contém as ações que o cliente realizará para adicionar um produto ao carrinho
    '''
    while True:
        Painel('Meu Carrinho')
        if len(produtos) != 0:
            c = 0 #V áriável de contador para listar os produtos em ordem 
            for item in carrinho: # Percorre a lista de produtos, sendo key respectivo ao nome do produto e values respectivo à seus preços e quantidades.
                print(f"Produto: {item} | Quantidade: {carrinho2[c]}")
                c+=1
            somaTotal = sum(valorTotal) # lista = {['Produto']: [preco, quantidade], ['Produto2']: [preco, quantidade]}
            print(f'{Fore.GREEN}Valor total a pagar: R${somaTotal}')
            break
        else:
            resp = input('Carrinho vazio! Deseja voltar ao menu? [S/N]').upper()
            while resp not in 'SN':
                resp = input(f"{Fore.RED}Resposta inválida.\n Deseja voltar ao menu? [S/N]? ").upper()
            if resp == 'S':
                Cliente()
            else:
                break
            

def FinalizarCompra():
    print(f'{Fore.YELLOW}Forma de Pagamento: Apenas Pix\nPix: nifesilva@outlook.com')

def Feedback():
    feedback = int(input('De 1 a 5, o quanto você gostou da experiência? '))
    while not 1 <= feedback <= 5:
        feedback = int(input('De 1 a 5, o quanto você gostou da experiência? '))
    feedback = str(feedback)
    arquivo = open("Feedbacks.txt", "a")

    arquivo.writelines(f"{feedback} \n")
    