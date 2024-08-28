from typing import Dict
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoAutenticacaoPsicologo:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo):
        self.repositorio_psicologo = repositorio_psicologo

    def autenticar(self, dados: Dict[str, str]):
        if not dados["email"] or not dados["senha"]:
            return None

        psicologo = self.repositorio_psicologo.encontrar_por_email(dados["email"])
        if psicologo.senha != dados["senha"]:
            return None

        return psicologo