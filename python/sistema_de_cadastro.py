    #BANCO DE DADOS#
lista_cliente = []
lista_senhas = []

    #CADASTRO#
opcao = -1

while opcao != "1":
 
 print("=== MENU ===")
 loguin = input("login: ")       
 senha = input("senha: ")
 input("cadastrar S/N: ")

 lista_cliente.append(loguin)
 lista_senhas.append(senha)

 print(lista_senhas, lista_cliente)
 opcao = print("1 - Fazer login")
 opcao = print("2 - Voltar menu")
 opcao = input("Opção: ")


