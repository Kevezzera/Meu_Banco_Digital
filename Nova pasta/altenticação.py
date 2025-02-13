import os

clientes = ["keven, lino"]

print("Bem vindo ao Banco" + "\n")

login = str(input("login: "))
senha = input("senha: ")    

if login == clientes:
    print("1 - Conta normal")
    print("2 - Conta universitaria")
    tipo_de_conta = int(input("Digite o tipo de conta: "))
else:
    print("Erro")
    exit()



os.system('clear')
print("Menu")
print("1 - Saldo: ")
print("2 - Saque: ")
print("3 - Deposito: ")
print("4 - Cheque especial: ")
print("5 - sair: ")
opcao = int(input("Digite a opção desejada: "))

if tipo_de_conta == 1: # conta normal
        if opcao ==  1: # saldo
            os.system('clear')
            print("Seu saldo é de", conta_normal, "R$")
            print("1 - Retornar menu")
            print("2 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                print("Menu")
                print("1 - Saldo: ")
                print("2 - Saque: ")
                print("3 - Deposito: ")
                print("4 - Cheque especial: ")
                print("5 - sair: ")
                opcao = int(input("Digite a opção desejada: "))
            if opcao == 2:
                os.system('clear')
                print("Saindo do sistema")  
                exit()
                
        if opcao == 2: # saque
            saque = int(input("valor do saque?: "))
            if saque <= conta_normal:
                os.system('clear')
                print("Saque realizado com sucesso!")
                conta_normal = conta_normal - saque
                print("seu saldo atual é de ", conta_normal)
                print("1 - Retornar menu")
                print("2 - Sair")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    os.system('clear')
                    print("Menu")
                    print("1 - Saldo: ")
                    print("2 - Saque: ")
                    print("3 - Deposito: ")
                    print("4 - Cheque especial: ")
                    print("5 - sair: ")
                    opcao = int(input("Digite a opção desejada: "))
                if opcao == 2:
                    os.system('clear')
                    print("Saindo do sistema")  
                    exit()
                    
        if opcao == 3: # deposito
            os.system('clear')
            deposito = int(input("valor do deposito?: "))
            conta_normal = conta_normal + deposito
            print("Deposito realizado com sucesso!")
            print("seu saldo atual é de ", conta_normal)
            print("1 - Retornar menu")
            print("2 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                print("Menu")
                print("1 - Saldo: ")
                print("2 - Saque: ")   
                print("3 - Deposito: ")
                print("4 - Cheque especial: ")
                print("5 - sair: ")
                opcao = int(input("Digite a opção desejada: "))
            if opcao == 2:
                os.system('clear')
                print("Saindo do sistema")  
                exit()   
                
        if opcao == 4: # cheque especial
            os.system('clear')
            print("Seu cheque especial é de", cheque_especial, "R$")
            print("Deseja usar o cheque especial?")
            print("1 - Sim")
            print("2 - Não")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                conta_normal = conta_normal + cheque_especial
                print("Seu saldo atual é de ate", conta_normal, "R$")
                print("1 - Sacar")
                print("2 - Sair")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    os.system('clear')
                    saque = int(input("valor do saque?: "))
                    if saque <= conta_normal: 
                        os.system('clear')
                        print("Saque realizado com sucesso!")
                        conta_normal = conta_normal - saque
                        print("seu saldo atual é de ", conta_normal)
                        print("1 - Retornar menu")
                        print("2 - Sair")
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao == 1:
                        os.system('clear')
                        print("Menu")
                        print("1 - Saldo: ")
                        print("2 - Saque: ")
                        print("3 - Deposito: ")
                        print("4 - Cheque especial: ")
                        print("5 - sair: ")
                        opcao = int(input("Digite a opção desejada: "))
                if opcao == 2:
                    os.system('clear')
                    print("Saindo do sistema")  
                    exit()

        if opcao == 5: # sair
            os.system('clear')
            print("Saindo do sistema")
            exit() 

elif tipo_de_conta == 2: # cunnta universitaria
        if opcao ==  1: # saldo
            os.system('clear')
            print("Seu saldo é de", conta_universitaria, "R$")
            print("1 - Retornar menu")
            print("2 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                print("Menu")
                print("1 - Saldo: ")
                print("2 - Saque: ")
                print("3 - Deposito: ")
                print("4 - Cheque especial: ")
                print("5 - sair: ")
                opcao = int(input("Digite a opção desejada: "))
            if opcao == 2:
                os.system('clear')
                print("Saindo do sistema")  
                exit()

        if opcao == 2: # saque
            saque = int(input("valor do saque?: "))
            if saque <= conta_universitaria:
                os.system('clear')
                print("Saque realizado com sucesso!")
                conta_universitaria = conta_universitaria - saque
                print("seu saldo atual é de ", conta_universitaria)
                print("1 - Retornar menu")
                print("2 - Sair")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    os.system('clear')
                    print("Menu")
                    print("1 - Saldo: ")
                    print("2 - Saque: ")
                    print("3 - Deposito: ")
                    print("4 - Cheque especial: ")
                    print("5 - sair: ")
                    opcao = int(input("Digite a opção desejada: "))
                if opcao == 2:
                    os.system('clear')
                    print("Saindo do sistema")  
                    exit()

        if opcao == 3: # deposito
            os.system('clear')
            deposito = int(input("valor do deposito?: "))
            conta_normal = conta_universitaria + deposito
            print("Deposito realizado com sucesso!")
            print("seu saldo atual é de ", conta_universitaria)
            print("1 - Retornar menu")
            print("2 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                print("Menu")
                print("1 - Saldo: ")
                print("2 - Saque: ")   
                print("3 - Deposito: ")
                print("4 - Cheque especial: ")
                print("5 - sair: ")
                opcao = int(input("Digite a opção desejada: "))
            if opcao == 2:
                os.system('clear')
                print("Saindo do sistema")  
                exit()   

        if opcao == 4: # cheque especial
            os.system('clear')
            print("Seu cheque especial é de", cheque_especial, "R$")
            print("Deseja usar o cheque especial?")
            print("1 - Sim")
            print("2 - Não")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                os.system('clear')
                conta_universitaria = conta_universitaria + cheque_especial
                print("Seu saldo atual é de ate", conta_normal, "R$")
                print("1 - Sacar")
                print("2 - Sair")
                opcao = int(input("Digite a opção desejada: "))
                if opcao == 1:
                    os.system('clear')
                    saque = int(input("valor do saque?: "))
                    if saque <= conta_universitaria: 
                        os.system('clear')
                        print("Saque realizado com sucesso!")
                        conta_universitaria = conta_universitaria - saque
                        print("seu saldo atual é de ", conta_normal)
                        print("1 - Retornar menu")
                        print("2 - Sair")
                    opcao = int(input("Digite a opção desejada: "))
                    if opcao == 1:
                        os.system('clear')
                        print("Menu")
                        print("1 - Saldo: ")
                        print("2 - Saque: ")
                        print("3 - Deposito: ")
                        print("4 - Cheque especial: ")
                        print("5 - sair: ")
                        opcao = int(input("Digite a opção desejada: "))
                if opcao == 2:
                    os.system('clear')
                    print("Saindo do sistema")  
                    exit()

        if opcao == 5: # sair
            os.system('clear')
            print("Saindo do sistema")
            exit()                     