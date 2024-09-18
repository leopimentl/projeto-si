from datetime import datetime
from typing import Dict, List
from consulta.consulta import Consulta
from consulta.repositorio_consulta import RepositorioConsulta
from paciente.repositorio_paciente import RepositorioPaciente
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoConsulta:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo, repositorio_paciente: RepositorioPaciente, repositorio_consulta: RepositorioConsulta):
        self.repositorio_psicologo = repositorio_psicologo
        self.repositorio_paciente = repositorio_paciente
        self.repositorio_consulta = repositorio_consulta

    def salvar(self, consulta: Consulta) -> Consulta:
        # Não pode ter consulta no mesmo dia e horário
        consultas = self.repositorio_consulta.listar()
        for c in consultas:
            c_horario_time = (datetime.min + c.horario).time()
            if c.data == consulta.data and c_horario_time == consulta.horario:
                raise Exception("Já existe uma consulta marcada para esse dia e horário")
        
        return self.repositorio_consulta.salvar(consulta)
    
    def listar_proximas_consultas(self, id_paciente: int, quantidade: int = 2) -> List[Consulta]:
        consultas = self.repositorio_consulta.listar()
        consultas_paciente = [c for c in consultas if c.id_paciente == id_paciente and c.data >= datetime.now().date()]
        consultas_paciente.sort(key=lambda c: (c.data, c.horario))
        return consultas_paciente[:quantidade]

    def listar_proximas_consultas_psicologo(self, id_psicologo: int, quantidade: int = 2) -> List[Consulta]:
        consultas = self.repositorio_consulta.listar()
        consultas_psicologo = [c for c in consultas if c.id_psicologo == id_psicologo and c.data >= datetime.now().date()]
        consultas_psicologo.sort(key=lambda c: (c.data, c.horario))
        return consultas_psicologo[:quantidade]
        