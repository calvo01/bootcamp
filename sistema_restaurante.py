faturamento = 0
opcao = 0
realizados = 0
maior_pedido = 0
menor_pedido = 0
maior_nome = 0

nomes = []
valores = []


while opcao != 8:
    opcao = int(input("Selecione uma opção: 1- Novo Pedido, 2- Faturamento, 3- Quantidade de Pedidos, 4- Ticket Médio, 5- Maior Compra, 6- Resumo do Dia, 7-Lista de Compras 8- Encerrar: "))
    if opcao == 1:
        nome = input("Qual o nome do cliente?")
        nomes.append(nome)
        valor = int(input("Qual o valor do pedido?"))
        valores.append(valor)
        faturamento = faturamento + valor
        realizados = realizados + 1
        if valor > maior_pedido:
            maior_pedido = valor
            maior_nome = nome
        if valor < menor_pedido or menor_pedido == 0:
            menor_pedido = valor
    elif opcao == 2:
        print(f"O faturamento do dia foi de R${faturamento}")
    elif opcao == 3:
        print(f" A quantidade de pedidos realizados foi de {realizados}")
    elif opcao == 4:
        if realizados < 1:
            print("Nenhum pedido realizado, não é possível calcular o ticket médio")
        else:
            medio = faturamento / realizados   
            print(f"O ticket médio do dia foi de R${medio}")
    elif opcao == 5:
        print(f"O maior pedido foi de R${maior_pedido}, do cliente {maior_nome}")
    elif opcao == 6:
        print(f"Faturamento do dia: R${faturamento}, quantidade de pedidos: {realizados}, maior pedido: R${maior_pedido})")
    elif opcao == 7:
        print(f"Clientes: {nomes}, Valores: {valores}")
    elif opcao == 8:
        print("Programa Encerrado")
        
    else:
        print ("Opção inválida")
        
  