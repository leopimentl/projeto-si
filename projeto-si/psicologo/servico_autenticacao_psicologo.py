from typing import Optional
from psicologo.psicologo import Psicologo
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoAutenticacaoPsicologo:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo):
        self.repositorio_psicologo = repositorio_psicologo

    def autenticar(self, email: str, senha: str) -> Optional[Psicologo]:
        if not email or not senha:
            return None

        psicologo = self.repositorio_psicologo.encontrar_por_email(email)
        if psicologo is None or psicologo.senha != senha:
            return None

        return psicologo