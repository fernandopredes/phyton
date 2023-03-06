import abc

class Pessoa(abc.ABC):
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    @abc.abstractmethod
    def consulta_nome(self):
        raise NotImplementedError()

pessoa1 = Pessoa()
