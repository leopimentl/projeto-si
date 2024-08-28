class Psicologo:
    def __init__(self, email , senha , nome , telefone , cpf , crp, id=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.crp = crp

    @staticmethod
    def from_string(string) -> "Psicologo":
        id, email, senha, nome, telefone, cpf, crp = string.split(",")
        return Psicologo(email, senha, nome, telefone, cpf, crp, id=id)

    def __str__(self):
        return f"{self.email},{self.senha},{self.nome},{self.telefone},{self.cpf},{self.crp}"