class Paciente:
    def __init__(self, email: str, senha: str, nome: str, telefone: str, cpf: str, id=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
