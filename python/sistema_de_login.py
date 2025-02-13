       #BANCO DE DADOS#
lista_cliente = ['keven', 'lino']
lista_senhas = ['123', '321']

        #LOGIN
opcao = -1

while opcao != "2":
 print("=== MENU DE LOGIN ===")

 login = input("login")
 senha = input("senha")

 if login in lista_cliente and senha in lista_senhas:
    print("seja bem vindo!!")

 else:
   print("cadastro n encontrado!")

   print("1 - retornar menu")
   print("2 - sair")
   opcao = input("opção")