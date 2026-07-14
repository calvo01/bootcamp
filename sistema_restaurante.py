faturamento = 0
opcao = 0
realizados = 0
maior_pedido = 0
menor_pedido = 0

while opcao != 7:
    opcao = int(input("Selecione uma opção: 1- novo pedido, 2- faturamento, 3- quantidade de pedidos, 4- ticket medio,5- maior compra, 6- resumo do dia 7- encerrar: "))
    if opcao == 1:
        nome = input("nome cliente?")
        valor = int(input("qual valor do pedido?"))
        faturamento = faturamento + valor
        realizados = realizados + 1
        if valor > maior_pedido:
            maior_pedido = valor
            nome = maior_nome
        if valor < menor_pedido or menor_pedido == 0:
            menor_pedido = valor
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
        print(f"O maior pedido foi de R${maior_pedido}, do cliente {maior_nome}")
    elif opcao == 6:
        print(f"Faturamento do dia: R${faturamento}, quantidade de pedidos: {realizados}, maior pedido: R${maior_pedido})")
    elif opcao == 7:
        print("encerrar")
        
    else:
        print ("opcao invalida")
        
        
  