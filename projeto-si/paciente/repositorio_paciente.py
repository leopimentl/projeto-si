from paciente.paciente import Paciente

class RepositorioPaciente:
    def __init__(self, nome_arquivo="pacientes.txt"):
        self.nome_arquivo = nome_arquivo

    def salvar(self, paciente) -> Paciente:
        try:
            with open(self.nome_arquivo, "a+") as arquivo:
                arquivo.seek(0)
                linhas = arquivo.readlines()
                id_paciente = len(linhas) + 1
                paciente.id = id_paciente
                arquivo.write(f"{id_paciente},{paciente}\n")
            return paciente
        except Exception as e:
            print(e)
            return None
        
    def existe_por_email(self, email) -> bool:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                for line in lines:
                    dados_paciente = line.strip().split(",")
                    if dados_paciente[1] == email:
                        return True
                return False
        except Exception as e:
            return True
        
        
    def existe_por_cpf(self, cpf) -> bool:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                for line in lines:
                    dados_paciente = line.strip().split(",")
                    if dados_paciente[5] == cpf:
                        return True
                return False
        except Exception as e:
            return True
        
    def encontra_por_email(self, email) -> Paciente:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                for line in lines:
                    dados_paciente = line.strip().split(",")
                    if dados_paciente[1] == email:
                        paciente = Paciente.from_string(line)
                        return paciente
        except Exception as e:
            return None
        
    def encontrar_por_id(self, id) -> Paciente:
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados_paciente = linha.strip().split(",")
                    if dados_paciente[0] == id:
                        patient = Paciente.from_string(linha)
                        return patient
        except Exception as e:
            return None
