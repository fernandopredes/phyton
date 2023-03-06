from heranca import Pessoa
from heranca import Professor
#Associação, Agregação e Composição

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
