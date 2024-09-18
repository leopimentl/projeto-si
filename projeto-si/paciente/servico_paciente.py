from paciente.paciente import Paciente
from paciente.repositorio_paciente import RepositorioPaciente

class ServicoPaciente:
    def __init__(self, repositorio_paciente: RepositorioPaciente):
        self.repositorio_paciente = repositorio_paciente

    def salvar(self, paciente: Paciente) -> Paciente:
        existe_paciente_cpf = self.repositorio_paciente.existe_por_cpf(paciente.cpf)
        if existe_paciente_cpf:
            raise ValueError("Cpf já cadastrado.")
    
        existe_paciente_email = self.repositorio_paciente.existe_por_email(paciente.email)
        if existe_paciente_email:
            raise ValueError("Email já cadastrado.")
        
        return self.repositorio_paciente.salvar(paciente)

    def encontrar_consultas_pelo_id(self, patient_id: str) -> list:
        return self.repositorio_consulta.encontra_por_id_paciente(patient_id)