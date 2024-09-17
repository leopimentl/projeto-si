from typing import Optional
from paciente.paciente import Paciente
from paciente.repositorio_paciente import RepositorioPaciente

class ServicoAutenticacaoPaciente:
    def __init__(self, repositorio_paciente: RepositorioPaciente):
        self.repositorio_paciente = repositorio_paciente

    def autenticar(self, email: str, senha: str) -> Paciente:
        if not email or not senha:
            return None

        paciente = self.repositorio_paciente.encontra_por_email(email)
        if paciente is None or paciente.senha != senha:
            return None

        return paciente