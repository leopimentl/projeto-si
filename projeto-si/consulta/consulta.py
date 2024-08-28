class Consulta:
    def __init__(self, id_paciente, id_psicologo, id=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_psicologo = id_psicologo

    @staticmethod
    def from_string(string):
        id, id_paciente, id_psicologo = string.split(",")
        return Consulta(id_paciente=id_paciente, id_psicologo=id_psicologo, id=id)

    def __str__(self):
        return f"{self.id_paciente},{self.id_psicologo}"