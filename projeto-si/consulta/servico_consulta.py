from typing import Dict
from consulta.consulta import Consulta
from consulta.repositorio_consulta import RepositorioConsulta
from paciente.repositorio_paciente import RepositorioPaciente
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoConsulta:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo, repositorio_paciente: RepositorioPaciente, repositorio_consulta: RepositorioConsulta):
        self.repositorio_psicologo = repositorio_psicologo
        self.repositorio_paciente = repositorio_paciente
        self.repositorio_consulta = repositorio_consulta

    def agendar_consulta(self, dados_consulta: Dict[str, str]) -> Consulta:
        paciente = self.repositorio_paciente.encontrar_por_id(dados_consulta["patient_id"])

        psychologist = self.repositorio_psicologo.encontrar_por_id(dados_consulta["psychologist_id"])

        if paciente is None or psychologist is None:
            return None
        
        return self.repositorio_consulta.salvar(Consulta(paciente.id, psychologist.id))
        