class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

pessoa_1 = Pessoa("Carlos")

print(pessoa_1.nome)


class ListaDeNumeros:
    def __init__(self, numeros):
        self.numeros = numeros
    def __str__(self):
        return " ".join([str(n) for n in self.numeros])
    def soma(self):
        return sum(self.numeros)
    def media(self):
        return self.soma()/len(self.numeros)

minha_lista = ListaDeNumeros([1,2,3,4,5,7])
print(f"A soma de {minha_lista} é {minha_lista.soma()}")
print(f"A média de {minha_lista} é {minha_lista.media()}")

class Guy:
    num_pessoas = 0
    def __init__(self, nome):
        self.nome = nome
        Guy.num_pessoas += 1

pessoa1 = Guy("carlos")
print(pessoa1.num_pessoas)

nomes = ['João', 'Paulo', 'Jorge', 'Ringo']
pessoas = [Guy(nome) for nome in nomes]
print(Guy.num_pessoas)
print(pessoas[0].nome)

class Calculadora:
    def soma(self, a, b):
        res = a + b
        return res
calculadora = Calculadora()
print(calculadora.soma(2,3))

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def dobra_idade(self):
        return self.idade * 2

pedro = Aluno("josé", 28)
print(pedro.dobra_idade())

class Calculadora2:
    valor = 1
    def adiciona(self, numero):
        return self.valor + numero

resultado = Calculadora2()
print(resultado.adiciona(2))
