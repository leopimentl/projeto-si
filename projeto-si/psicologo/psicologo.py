class Psicologo:
    def __init__(self, email , senha , nome , telefone , cpf , crp, especialidade=None, id=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.crp = crp
        self.especialidade = especialidade
