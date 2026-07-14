faturamento = 0
opcao = 0
realizados = 0
maior_pedido = 0
menor_pedido = 0
maior_nome = 0

nomes = []
valores = []
while opcao != 7:
    opcao = int(input("Selecione uma opção: 1- novo pedido, 2- faturamento, 3- quantidade de pedidos, 4- ticket medio,5- maior compra, 6- resumo do dia 7- encerrar: "))
    if opcao == 1:
        nome = input("nome cliente?")
        nomes.append(nome)
        valor = int(input("qual valor do pedido?"))
        valores.append(valor)
        faturamento = faturamento + valor
        realizados = realizados + 1
        if valor > maior_pedido:
            maior_pedido = valor
            maior_nome = nome
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
        print(nomes, valores)
        
    else:
        print ("opcao invalida")
        
        
  