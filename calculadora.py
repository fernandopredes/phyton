def bem_vindo():
    print("*****************")
    print("Caculadora")
    print("*****************")
    calcular()

def calculadora(n, a, b):
    if n == 1:
        c = a + b
        return print("o valor da soma é: %d" %(c))
    elif n == 2:
        c = a - b
        return print("o valor da subtração é: %d" %(c))
    elif n == 3:
        c = a * b
        return print("o valor da multiplicação é: %d" %(c))
    elif n == 4:
        c = a / b
        return print("o valor da divisão é: %d" %(c))

def calcular():
    print("\nEscolha a opção: (1)somar (2)subtrair (3)multiplicar (4)dividir")
    operacao = int(input("Digite o número da opção"))
    if operacao <= 0 or operacao >= 5:
        print("desculpe. Valor inválido")
        return
    primeiro_valor = int(input("Digite o primeiro valor"))
    segundo_valor = int(input("Digite o segundo valor"))

    calculadora(operacao, primeiro_valor, segundo_valor)

bem_vindo()
