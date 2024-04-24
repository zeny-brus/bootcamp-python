

menu = 22*"#"+" MENU "+ 22*"#" + """
[D] Depositar | [S] Sacar | [E] Extrato | [Q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu).upper()
    if opcao == "Q":        
        break
    elif opcao == "D":
        valor_deposito = int(input("digite o valor de deposito: "))
        saldo += valor_deposito
        mensagem = (f"Deposito +R$ {valor_deposito} \nSaldo: R$ {saldo} ")
        extrato += "\n"+mensagem        
        print (mensagem)
    elif opcao == 'S':
        print("seu saldo é de R$ %.2f"% saldo)
        valor_saque = int(input("digite o valor para saque: "))
        if valor_saque > saldo:
            print("Saldo insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saque excedido!!")
        elif valor_saque >= limite:
            print ("valor do saque maior que limite!")
        else:       
            numero_saques += 1
            saldo -= valor_saque
            mensagem = (f"Saque -R$ {valor_saque} \nSaldo: R$ {saldo} ")
            extrato += "\n"+mensagem
            print(mensagem)            
    elif opcao == 'E':
        print (extrato)
    else:
        print ('Opção inválida, por favor selecione novamente a operação desejada!')