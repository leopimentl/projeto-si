class Paciente:
    def __init__(self, email, senha, nome, telefone, cpf, id=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    @staticmethod
    def from_string(string) -> "Paciente":
        id, email, senha, nome, telefone, cpf = string.split(",")
        return Paciente(email=email, senha=senha, nome=nome, telefone=telefone, cpf=cpf, id=id)

    def __str__(self):
        return f"{self.email},{self.senha},{self.nome},{self.telefone},{self.cpf}"
