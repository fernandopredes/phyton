class Pessoa:
    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha
    def consulta_nome(self):
        return self.__nome

class Aluno(Pessoa):
    def __init__(self, nome, login, senha, curso):
        Pessoa.__init__(self, nome, login, senha)
        self.__curso = curso
    def consulta_curso(self):
        return self.__curso

class Professor(Pessoa):
    def __init__(self, nome, login, senha, titulacao):
        Pessoa.__init__(self, nome, login, senha)
        self.__titulacao = titulacao
    def consulta_titulacao(self):
        return self.__titulacao

pessoa1 = Pessoa("Maria", "maria", 'm123')
print(pessoa1.consulta_nome())

aluna1 = Aluno('Viviane', 'vivi', 'v123', 'Informática')
print(aluna1.consulta_nome())
print(aluna1.consulta_curso())

prof1 = Professor('Tatiana', 'tati', 't123', 'Doutorado')
print(prof1.consulta_nome())
print(prof1.consulta_titulacao())
