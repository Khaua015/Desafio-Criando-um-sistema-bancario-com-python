menu = '''

(d) - Depositar
(s) - Sacar
(e) - Estrato
(q) - Sair

'''


saldo = 0.0
limite = 0.0
estrato = ''
numeros_saques = 0
limite_saques = 3

while True:
    print("--------------------------------------------------------------------------------------")
    opcao = input(menu)

    if opcao == "d":
        print("--------------------------------------------------------------------------------------")
        deposito = float(input("Valor para depósito: "))
        if deposito < 0:
            print("O depósito não pode ser negativo!!")
        else:
            print(f"depósito de R${deposito:.2f} efetuado")
            saldo += deposito
            estrato += f'\ndepósito de R${deposito:.2f}'
    
    elif opcao == "s":
        print("--------------------------------------------------------------------------------------")
        if numeros_saques == limite_saques:
            print("Limite de saque diário excedido!!!!")
        else: 
            saque = float(input("Valor para saque: "))
            if saque > saldo:
                print("Valor para saque insuficiente!")
            elif saque > 500.0:
                print("O limite monetário para saque é de R$ 500,00")
            else:
                saldo -= saque
                print("Saque efetuado com Sucesso")
                estrato += f'\nsaque de {saque:.2f}'
                numeros_saques += 1
    
    elif opcao == 'e':
        print("--------------------------------------------------------------------------------------")
        print(f"Saldo de R${saldo:.2f}" + estrato )

    elif opcao == "q":
        print("--------------------------------------------------------------------------------------")
        print("Fim do programa!!!!!!!!!!!!!!!!")
        print("--------------------------------------------------------------------------------------")
        break
    else:
        print("Opção inválida, tente novamente:")


    
