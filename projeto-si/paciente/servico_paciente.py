from typing import Dict
from consulta.repositorio_consulta import RepositorioConsulta
from paciente.paciente import Paciente
from paciente.repositorio_paciente import RepositorioPaciente
from consulta.consulta import Consulta

class ServicoPaciente:
    def __init__(self, repositorio_paciente: RepositorioPaciente, repositorio_consulta: RepositorioConsulta):
        self.repositorio_paciente = repositorio_paciente
        self.repositorio_consulta = repositorio_consulta
    
    def paciente_to_dict(self, paciente: Paciente) -> Dict[str, str]:
        return {
            "id": paciente.id,
            "email": paciente.email,
            "senha": paciente.senha,
            "nome": paciente.nome,
            "telefone": paciente.telefone,
            "cpf": paciente.cpf
        }
    
    def dict_to_paciente(self, dados: Dict[str, str]) -> Paciente:
        return Paciente(
            email=dados["email"],
            senha=dados["senha"],
            nome=dados["nome"],
            telefone=dados["telefone"],
            cpf=dados["cpf"]
        )

    def salvar(self, dados_paciente: Dict[str, str]) -> Paciente:
        existe_paciente_cpf = self.repositorio_paciente.existe_por_cpf(dados_paciente["cpf"])
        existe_paciente_email = self.repositorio_paciente.existe_por_email(dados_paciente["email"])
        
        if existe_paciente_cpf or existe_paciente_email:
            return None
        
        return self.repositorio_paciente.salvar(self.dict_to_paciente(dados_paciente))

    def encontrar_consultas_pelo_id(self, patient_id: str) -> list:
        return self.repositorio_consulta.encontra_por_id_paciente(patient_id)