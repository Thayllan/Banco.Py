def criar_usuario():
  nome = input("Insira o nome do usuário: ")
  email = input("Insira o email do usuário: ")
  senha = input("Insira a senha do usuário: ")
  
  # Crie o objeto usuário com os dados digitados
  usuario = {"nome": nome, "email": email, "senha": senha}
  
  # Retorne o usuário criado
  return usuario






menu = """

[d] Depositar
[n] Novo usuario
[s] Sacar
[e] Extrato
[q] Sair


=> """
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    if opcao == "n":
        novo_usuario = criar_usuario()

    print(novo_usuario)

    if opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor >limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
             print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido. ")    

    elif opcao == "e":
        print("\n==================EXTRATO======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")

    elif opcao == "q":
        break

