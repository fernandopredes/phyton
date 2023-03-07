#Associação, Agregação e Composição

from heranca import Pessoa
from heranca import Professor
import datetime

class Aluno(Pessoa):
    def __init__(self, nome, login, senha, curso, orientador):
        Pessoa.__init__(self, nome, login, senha)
        self.__curso = curso
        self.__orientador = orientador

    def consulta_curso(self):
        return self.__curso

    def consulta_orientador(self):
        return self.__orientador

    def consulta_nome(self):
        return Pessoa.consulta_nome(self)

professorMarcos = Professor('Marcos', 'mk', 'm123', 'Doutor')

novoAluno = Aluno('Isabela', 'isa', 'i123', 'Engenharia', professorMarcos)
print(novoAluno.consulta_orientador().consulta_nome())

class Historico():
    def __init__(self) -> None:
        self.__data_matricula = datetime.datetime.today()
        self.__ocorrencias = []

    def imprime(self):
        print("Matriculado em {}".format(self.__data_matricula))
        print("Ocorrências: ")
        for ocor in self.__ocorrencias:
            print("-", ocor)

    def add_ocorrencia(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

paulo = Historico()
paulo.add_ocorrencia(["se perdeu","atrasado"])
print(paulo.imprime())

class Aluno(Pessoa):
    def __init__(self, nome, login, senha, curso, orientador):
        Pessoa.__init__(self, nome, login, senha)
        self.__curso = curso
        self.__orientador = orientador
        self.__historico = Historico()

    def consulta_curso(self):
        return self.__curso

    def consulta_orientador(self):
        return self.__orientador

    def consulta_nome(self):
        return Pessoa.consulta_nome(self)

    def consulta_login(self):
        return Pessoa.consulta_login(self)

    def gera_ocorrencia(self,ocorrencia):
        self.__historico.add_ocorrencia(ocorrencia)

    def consulta_historico(self):
        self.__historico.imprime()

novo_aluno = Aluno("clara", "claraaa", "1234", "matemática", "carlos")
print(novo_aluno.consulta_nome())
print(novo_aluno.consulta_login())

novo_aluno.gera_ocorrencia(["atrasado","faltou aula"])
print(novo_aluno.consulta_historico())
