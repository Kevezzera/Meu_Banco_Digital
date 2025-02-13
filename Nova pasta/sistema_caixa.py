import os

saldo = 1000

opcao = -1
while opcao != 0:
    
    os.system('cls')
    print("MENU")
    print("1 - sacar")
    print("2 - extrato")
    print("3 - deposito")
    print("0 - sair")
    opcao = int(input("opção: "))

    if opcao == 1:                                     #SAQUE#
        
        os.system('cls')
        saque = int(input("valor do saque: "))
        
        if saque <= saldo:                             #SALDO SUFICIENTE#
            
            os.system('cls')
            print("saque realizado com sucesso!")
            print()
            print("1 - menu")
            print("2 - sair")
            opcao = input("opção: ")

            if opcao == "2":
                
                os.system('cls')
                break

        elif saque > saldo:                            #SALDO INSUFICIENTE#
            
            os.system('cls')
            print("saldo insuficiente")
            print()
            print("1 - menu")
            print("2 - sair")
            opcao = input("opção: ")

            if opcao == "2":
                
                os.system('cls')
                break

    elif opcao == 2:                                  #EXTRATO# 

        
        os.system('cls')
        print("Seu saldo é de ", saldo) 
        print()
        print("1 - menu")
        print("2 - sair")
        opcao = input("opção: ")

        if opcao == "2":
                
            os.system('cls')
            break

    elif opcao == 3:                                  #DEPOSITO#
        
        os.system('cls')
        deposito = int(input("valor do deposito: "))

        saldo = saldo + deposito

        os.system('cls')
        print("Deposito realizado com sucesso!")

        print()
        print("1 - menu")
        print("2 - sair")
        opcao = input("opção: ")

        if opcao == "2":
                
            os.system('cls')
            break
        
    elif opcao == 0:                                   #EXIT#
        print("extrato...")
        exit()
