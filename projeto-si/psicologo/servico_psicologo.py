from psicologo.psicologo import Psicologo
from psicologo.repositorio_psicologo import RepositorioPsicologo

class ServicoPsicologo:
    def __init__(self, repositorio_psicologo: RepositorioPsicologo):
        self.repositorio_psicologo = repositorio_psicologo

    def salvar(self, psicologo: Psicologo):

        existe_psicologo_email = self.repositorio_psicologo.existe_por_email(psicologo.email)
        if existe_psicologo_email:
            raise ValueError("Email já cadastrado.")

        existe_psicologo_cpf = self.repositorio_psicologo.existe_por_cpf(psicologo.cpf)
        if existe_psicologo_cpf:
            raise ValueError("CPF já cadastrado.")

        existe_psicologo_crp = self.repositorio_psicologo.existe_por_crp(psicologo.crp)
        if existe_psicologo_crp:
            raise ValueError("CRP já cadastrado.")
        
        return self.repositorio_psicologo.salvar(psicologo)

