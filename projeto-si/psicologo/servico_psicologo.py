from typing import Dict, List
from consulta.repositorio_consulta import RepositorioConsulta
from psicologo.psicologo import Psicologo
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoPsicologo:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo, repositorio_consulta: RepositorioConsulta):
        self.repositorio_psicologo = repositorio_psicologo
        self.repositorio_consulta = repositorio_consulta

    def salvar(self, dados_psicologo: Dict[str, str]) -> Psicologo:
        for campo, valor in dados_psicologo.items():
            if not valor.strip():
                return None
        
        if len(dados_psicologo["senha"]) <= 7:
            return None
        
        if len(dados_psicologo["cpf"]) != 11:
            return None
        
        if "@" not in dados_psicologo["email"] or "." not in dados_psicologo["email"]:
            return None
        
        if not dados_psicologo["telefone"].isnumeric() or len(dados_psicologo["telefone"]) < 10:
            return None
        
        if self.repositorio_psicologo.encontrar_por_cpf(dados_psicologo["cpf"]) is not None:
            return None

        if self.repositorio_psicologo.encontrar_por_email(dados_psicologo["email"]) is not None:
            return None
        
        if self.repositorio_psicologo.encontrar_por_crp(dados_psicologo["crp"]) is not None:
            return None

        return self.repositorio_psicologo.salvar(self.dict_to_psicologo(dados_psicologo))

    def dict_to_psicologo(self, dados_psicologo: Dict[str, str]) -> Psicologo:
        return Psicologo(
                email=dados_psicologo["email"],
                senha=dados_psicologo["senha"],
                nome=dados_psicologo["nome"],
                telefone=dados_psicologo["telefone"],
                cpf=dados_psicologo["cpf"],
                crp=dados_psicologo["crp"]
            )
    
    def psicologo_to_dict(self, psychologist: Psicologo) -> Dict[str, str]:
        return {
            "id": psychologist.id,
            "email": psychologist.email,
            "senha": psychologist.senha,
            "nome": psychologist.nome,
            "telefone": psychologist.telefone,
            "cpf": psychologist.cpf,
            "crp": psychologist.crp
        }
    
    def encontrar_todos(self) -> List[Dict[str, str]]:
        return [self.psicologo_to_dict(psychologist) for psychologist in self.repositorio_psicologo.encontra_todos()]
    
    def existe_pelo_id(self, psychologist_id: str) -> bool:
        return self.repositorio_psicologo.encontrar_por_id(psychologist_id) is not None
    
    def encontra_por_id(self, psychologist_id: str) -> Psicologo:
        return self.repositorio_psicologo.encontrar_por_id(psychologist_id)
    
    def encontrar_consultas_pelo_id(self, psychologist_id: str) -> list:
        return self.repositorio_consulta.encontra_por_id_psicologo(psychologist_id)