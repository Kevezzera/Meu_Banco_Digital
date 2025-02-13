import os

cliente_etudantil = "lino"
cliente_normal = "keven"
cliente_especial = "domisia"
senhas = "123"

print("MENU")
opcao = input("1 - Dados da conta")
opcao = input("2 - Cadastrar-se")
opcao = input("Opção: ")

if opcao == 1:                                  #EXTRATO CONTA ESTU...

    os.system('cls')                            #TIPO DE CONTA
    print("Tipos de conta \n")
    print("1 - Estudantil")
    print("2 - Normal")
    print("3 - Especial")
    tipo_de_conta = input("Qual seu tipo de conta?:")

    if tipo_de_conta == "1":                    #LOGIN EXTRATO
        
        os.system('cls') 
        login = input("Login: ")                
        senha = input("Senha: ")

        if login == cliente_etudantil and senha == senhas:
            
            print("O senhor(a) esta cadastrado como um client Estudantil!")





elif opcao == 2:

 os.system('cls')   
 print("Cadastro \a")
 opcao = input("Deseja criar uma conta? S/N:")

if opcao == "s":

    os.system('cls')
    deposito = int(input("De quanto seria seu deposito inicial?: "))

    if deposito <= 100:                  #CONTA ESTUDANTIL

        os.system('cls')
        print("Essa quantia lhe permite criar uma conta ESTUDANTIL")
        opcao = input("Deseja priseguir? S/N: ")

        if opcao == "s":

            os.system('cls')
            login = input("Escolha um login: ")
            senha = input("Escolha uma senha: ")
            cliente = login
            senhas = senha
            

        elif opcao == "n":
            exit()
   
    elif deposito <= 1000:               #CONTA NORMAL

        os.system('clear') 
        print("1 - Conta estudantil")
        print("2 - Conta normal")
        opcao = input("Opição: ")

    elif deposito <= 10000:              #CONTA ESPECIAL

        os.system('clear')
        print("1 - Conta estudantil")
        print("2 - Conta normal")
        print("3 - Especial")
        opcao = input("Opição: ")


elif opcao == "n":                       #EXITE#

    print("Volte sempre")
    exit()