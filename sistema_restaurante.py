faturamento = 0
opcao = 0
realizados = 0

while opcao != 5:
    opcao = int(input("Selecione uma opção: 1- novo pedido, 2- faturamento, 3- quantidade de pedidos, 4- ticket medio, 5- encerrar: "))
    if opcao == 1:
        nome = input("nome cliente?")
        valor = int(input("qual valor do pedido?"))
        faturamento = faturamento + valor
        realizados = realizados + 1
    elif opcao == 2:
        print(f"{faturamento}")
    elif opcao == 3:
        print(f"{realizados}")
    elif opcao == 4:
        if realizados < 1:
            print("nenhum pedido ainda")
        else:
            medio = faturamento / realizados   
            print(f"{medio}")
    elif opcao == 5:
        print("encerrar")
    else:
        print ("opcao invalida")
        
        
  