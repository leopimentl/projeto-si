from datetime import date, time

class Consulta:
    def __init__(self, id_paciente, id_psicologo, data: date, horario: time, especialidade, id=None):
        self.id = id
        self.id_paciente = id_paciente
        self.id_psicologo = id_psicologo
        self.data = data
        self.horario = horario
        self.especialidade = especialidade