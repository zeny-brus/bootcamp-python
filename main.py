'''
desafio 2
criar funçao de sacar (keyword only) X
criar funcao de depositar(positional only) X
criar funcao de extrato (positional only, keyword only) X

criar funcao conta cliente em uma lista (nome, nascimento,
cpf,endereco = "logradouro, nro - bairro - cidade/sigla estado)
cpf = chave só podendo ser somente 1 X

criar conta corrente e vincular com cliente em uma lista(
    numero da conta sequencial, numero da  agencia fixo '0001'
) 
cliente pode ter mais de uma conta, mas uma conta só pode ter apenas 1 cliente
lista de usuarios buscando o numero do cpf
utilizar argumentos por posiçao e nomedos

AVISO:
criar um README com checkbox do desafio 1 no github antes de commitar e subir este desafio
e alterar o README com novos checkbox do desafio 2
'''
import os
import textwrap


def menu():
    menu ='\n'+22*"="+'MENU'+22*"="+'''
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrado
    [C]\tNova conta
    [L]\tListar contas
    [U]\tNovo usuario
    [Q]\tSair
    ==>'''
    return input (textwrap.dedent(menu)).upper()

def limpa_tela():
    os.system('cls || clear')

def deposito(saldo,valor,extrato,/):
    saldo += valor
    mensagem = f"Deposito +R$ {valor}"
    extrato += "\n"+mensagem
    print (mensagem)
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, limite_saque, numero_saques):
    saldo_insuficiente = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saques >= limite_saque

    if saldo_insuficiente:
        print('Saldo insuficiente!!')
    elif limite_excedido:
        print(f'você excedeu o limite de R$ {limite}')
    elif saque_excedido:
        print(f'Você excedeu o limite saque: {limite_saque}')
    else:
        saldo -= valor 
        numero_saques += 1       
        mensagem = f"Saque -R$ {valor}"
        extrato += "\n"+mensagem 
        print (mensagem)
    
    return saldo, extrato, numero_saques

def exibir_extrato (saldo, /, *, extrato):
    print (22*"="+'EXTRATO'+22*"=")
    print("Não foi realizado movimentações" if not extrato else extrato)
    print (f'\nSaldo: R${saldo:.2f}')

def novo_usuario(usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("Cpf já cadastro!!!")
        return  
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
    endereco = input("Digite o endereco(rua, nro - bairro - cidade/sigla estado): ")

    
    usuarios.append({"nome":nome, "data_nascimento":data_nascimento,"cpf":cpf, "endereco":endereco})
    print('\nusuário cadastrado com sucesso!!')
    


def verifica_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o seu CPF: ')
    usuario = verifica_usuario(cpf, usuarios)   

    if usuario:        
        print("\n=== Conta criada!! ===")
        return{"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}    
    
    print('\n !!! usuario nao encontrado, conta nao criada !!!')

def listar_contas(contas):
    for conta in contas:
        dados = f"""Agencia: {conta["agencia"]}
                \n Conta: {conta["numero_conta"]}
                \n Nome: {conta["usuario"]["nome"]}"""
        print("-"*50)
        print(dados)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        limpa_tela()
        if opcao == "Q":        
            break
        
        elif opcao == "D":
            valor = float(input("digite o valor de deposito: "))
            saldo,extrato = deposito(saldo, valor, extrato) 

        elif opcao == 'S':
            print("seu saldo é de R$ %.2f"% saldo)
            valor = float(input("digite o valor para saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                limite_saque = LIMITE_SAQUES,
                numero_saques = numero_saques
            )    

        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'U':
            novo_usuario(usuarios)

        elif opcao == 'C':
            numero_conta = len(contas)+1
            conta = nova_conta(AGENCIA,numero_conta,usuarios)              
            
            if conta:
                contas.append(conta)

        elif opcao == 'L':
            listar_contas(contas)
        
        else:
            print ('Opção inválida, por favor selecione novamente a operação desejada!')




main()