class Pessoa:
    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha
    def consulta_nome(self):
        return self.__nome

class Professor(Pessoa):
    def __init__(self, nome, login, senha, titulacao):
        Pessoa.__init__(self, nome, login, senha)
        self.__titulacao = titulacao
    def consulta_titulacao(self):
        return self.__titulacao


class EntradaUniversidade:
    def __init__(self):
        pass
    def permite_entrada(self,pessoa):
        print("Pode entrar, " + pessoa.consulta_nome())

class Coordenador(Pessoa):
    def __init__(self, nome, login, senha):
        Pessoa.__init__(self, nome, login, senha)

entrada = EntradaUniversidade()

prof1 = Professor('Tatiana', 'tati', 't123', 'Doutorado')
print(entrada.permite_entrada(prof1))

coord1 = Coordenador('Marcos', 'mk', 'm123')
print(entrada.permite_entrada(coord1))
