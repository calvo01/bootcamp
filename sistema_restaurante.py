faturamento = 0
opcao = 0

while opcao != 3:
    opcao = int(input("Selecione uma opção: 1- novo pedido, 2- faturamento, 3- encerrar: "))

    if opcao == 1:
        nome = input("nome cliente?")
        valor = int(input("qual valor do pedido?"))
        faturamento = faturamento + valor

    elif opcao == 2:
        print(f"{faturamento}")

    elif opcao == 3:
        print("expediente encerrado")

    else:
        print("opcao invalida")