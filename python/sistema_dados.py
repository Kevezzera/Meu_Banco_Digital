                        
                         #Banco de dados#

lista_cliente = []
lista_senha = []

opcao = -1

while opcao != "n":

 login = input("login: ")  
 if login in lista_cliente:
    print("Este login ja esta sendo usado!!")

    opcao = input("Tentar novamente? S/N: ")
    
 else:
    lista_cliente.append(login)
    print("Cadastro realizado com sucesso!!")

    print(lista_cliente)
    
    opcao = input("Fazer novo cadastro? S/N: ")