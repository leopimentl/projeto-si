from typing import Dict
from paciente.paciente import Paciente
from paciente.repositorio_paciente import RepositorioPaciente

class ServicoAutenticacaoPaciente:
    def __init__(self, repositorio_paciente: RepositorioPaciente):
        self.repositorio_paciente = repositorio_paciente

    def autenticar(self, dados: Dict[str, str]) -> Paciente:
        if not dados["email"] or not dados["senha"]:
            return None

        paciente = self.repositorio_paciente.encontra_por_email(dados["email"])
        if paciente is None or paciente.senha != dados["senha"]:
            return None

        return paciente

    