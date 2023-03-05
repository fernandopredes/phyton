#mostrar no console
print("Hello World")

# variaveis
string = "Aluno"
inteiro = 4
um_float = 7.858
um_booleano = True

print(um_float)
print(type(um_float))

#potencia
resultado_1 = 2 ** 4
#resto
resultado_2 = 13 % 4

#parsing

print("resultado da soma = " + str(4 + 4))
print("potencia de 2 a 4 = " + str(resultado_1))
print("resto da divisão de 13 por 4 = " + str(resultado_2))

#decremento e incremento

um_inteiro = 7
um_inteiro -= 3
print("resultado: " + str(um_inteiro))
um_inteiro += 5
print("resultado: " + str(um_inteiro))

#comparação e operadores lógicos
var_um = 1
var_dois = 2
var_tres = 3

equal = 1 == var_um
not_equal = 2 == var_um

print("1 é igual a var_um? " + str(equal))
print("2 é igual a var_um? " + str(not_equal))

print ((2 > 1) and (3 > 1))
print ((0 > 1) and (3 > 1))
print ((2 > 1) or (3 > 1))
print ((0 > 1) or (3 > 1))
print ((0 > 1) or (0 > 3))

#strings

programacao = "WOW! such a string"
print(len(programacao))
print(programacao[0])#pega na posição
print(programacao[-1]) #conta de trás pra frente
print(programacao[1:]) #antes do : é o index de inicio e depois o final(final não é incluso)
print(programacao[0:2])

vezes_sete = programacao * 7 #multiplicador de string
print(vezes_sete)

print("estiu estudando\n" + "outras coisas") #\n quebra a linha (scaping)

print(programacao.lower())
print(programacao.upper())


nome = "Bela"
numero_inteiro = 7
numero_decimal = 7.584
print("Olá, meu nome é %s! tenho %d anos e % dreais!"
    %(nome, numero_inteiro, numero_decimal))
print("Olá, meu nome é %s! tenho %d anos e %f reais!"
    %(nome, numero_inteiro, numero_decimal))
print("Olá, meu nome é %s! tenho %d anos e %.2f reais!"
    %(nome, numero_inteiro, numero_decimal))

programacao_python = "Programação em Python"
print("Python" in programacao_python)
print("python" in programacao_python)
print("abacate" in programacao_python)

#Coleções

##Listas
numeros = [1, 10, 100, 1000]
print(numeros)
print(numeros[0])
