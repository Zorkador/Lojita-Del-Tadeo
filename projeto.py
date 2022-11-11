# --------------- lojito del tadeo carnes -----------------
# | ENTRAR                                                |
# | se for adm: programa solicita código de adm (40028922)|
# | se for usuario: entra direto                          |
#  -------------------------------------------------------
# Adm: Função Cadastrar
# Adm: Função Remover
# Adm: Função Editar
# Cliente: Função Avaliar (Avalia em Estrelas)
# Cliente: Função Comprar.
# Lojita: Função para listar (tela pra listar todos os produtos e informações (código(posição), preço, quantia no estoque))
# Lojita: Tela Inicial.

import Funcoes


while True:
    r = Funcoes.TelaInicial()
    cont = 3
    while r == "1":
        senha = input("Senha: ")
        if senha == "40028922":
            Funcoes.Acao()
            break
        else:
            cont -= 1
            print(f"Senha incorreta! {cont} tentativas restantes.")
            if cont == 0 or senha == '' or senha == '0':
                print("Você foi redirecionado à página inicial.")
                break
    while r == "2":
        Funcoes.Cliente()
        Funcoes.Feedback()
        break
    if r == "0":
        break
print("\nAté mais! Volte sempre!")

# Ajeitar a função Listar
# Fazer a função Alterar
# Alex: Algumas coisas para a parte do cliente:
# Criar uma lista/dicionário para o carrinho
# Poder remover da lista algum produto que foi adicionado
# Fazer o cálculo do valor total da compra
# Cancelar a compra
# Forma de pagamento
# Talvez uma opção para pedir a entrega a domicílio
# Alex: Algumas outras coisas:
# Adicionar um código a cada produto
# Remover por quantidade
# Uma opção de deixar algum feedbacks