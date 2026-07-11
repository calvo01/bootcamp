

## (chamar py)

`python -i` ou terminal Python

python
print('Testando PY');

x = input("Qual sua idade?")
if 4 >= x;
    print('Maior que 4')
else;
    print('Menor que 4')


`dir()` `help()` — ver todos os métodos dentro do objeto


# variaveis
python
age = 20
name = "felipe"
print(f'My name is {name}, i am {age} years old')


___________________________________


age = 20
name = ("Felipe")

printf"My name is {name} and i am {age} years old"

x=str(input("age"))
if x < 18:
    print("menor de idade)
else:
    print("maior de idade")

_______________________________________

x=input("Qual o seu nome?")
y=int(input("Qual é sua idade?"))

if y >= 18:
    print(f"Olá {x}, você é Maior de idade")
else:
    print(f"Olá {x}, você é Menor de idade")
______________

y=int(input("Qual é o seu salário?"))

if y >= 5000:
    print("Você ganha acima da média brasileira.")
else:
    print("Continue estudando. Seu potencial é muito maior.")
    ___________
    

saldo = int(input("Qual seu saldo?"))
saque = int(input("Quanto deseja sacar?"))


if saque > saldo:
    print("Saldo Insulficiente")
else:
    print("Saque concluido")

saldo = saldo-saque


    print(f"Seu saldo é de {saldo}")




    ___________

user = input("Qual o nome do Usário?").lower()
password = input("Qual a senha do Usário?")

if (user == "felipe") and (password == "python123"):
    print(f"Bem-vindo, {user}!")
else:
    print("Senha e login invalido")


    ___________________

peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >=25 and imc <= 29.9:
    print("Acima do peso")
else:
    print("Obeso")

print(f"Seu IMC é {imc}")



____________

name = input("Qual seu nome?")
valor = float(input("Qual valor da compra"))

if valor >= 100.00:
    print(f" Olá, {name} o valor da sua compra era de {valor} porem com o desconto de {valor * 0.10}, sua compra ficou em {valor * 0.90}" )
else:
    print(f"Olá {name}, o valor da sua compra ficou no valor de {valor}, você não recebeu desconto")

___________

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
    
_________

contador = 1
limite = int(input("Até qual número deseja contar?"))

while contador <= limite:
    print(contador)
    contador = contador + 1

__________________

senha = input("Qual a senha")

while senha != "fefe":
    print("senha incorreta")
    senha = input("Qual a senha")
    print("senha correta")

____________________________
contador = 5

while contador >=0:
    print(contador)
    contador  = contador - 1 
    --

    --------------

    for numero in range(2, 12, 2):
   print(numero)
   ___________________________
   for numero in range(10, 0, -2):
   print(numero)
   ______________________
   numero = int(input("digite um numero"))

for contador in range(1, 11):
    print(f"{numero} X {contador} = {numero*contador}")

_______________________________

total = 0  

opcao = 0 
while opcao != 3:

    opcao = int(input("""
==== MERCADO ====

1 - Comprar
2 - Ver total
3 - Sair

Escolha: """))

    if opcao == 1:
        valor = float(input("Quanto custou? "))
        total = total + valor
        print("Compra adicionada!")

    elif opcao == 2:
        print(f"Total da compra: R$ {total:.2f}")

    elif opcao == 3:
        print("Programa encerrado!")

    else:
        print("Opção inválida.")

______________________



    
