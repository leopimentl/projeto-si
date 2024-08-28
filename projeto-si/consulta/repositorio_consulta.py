from consulta.consulta import Consulta

class RepositorioConsulta:

    def __init__(self, nome_arquivo="psychological_consultations.txt"):
        self.nome_arquivo = nome_arquivo

    def salvar(self, consulta: Consulta) -> Consulta:
        try:
            with open(self.nome_arquivo, "a+") as file:
                file.seek(0)
                lines = file.readlines()
                id_consulta = len(lines) + 1
                consulta.id = id_consulta
                file.write(f"{id_consulta},{consulta}\n")
            return consulta
        except Exception as e:
            print(e)
            return None
    
    def encontra_por_id(self, id: str) -> Consulta:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                for line in lines:
                    dados_consulta = line.strip().split(",")
                    if dados_consulta[0] == id:
                        consultation = Consulta.from_string(line)
                        return consultation
        except Exception as e:
            return None
    
    def encontra_por_id_paciente(self, id_paciente) -> list:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                consultas = []
                for line in lines:
                    dados_consulta = line.strip().split(",")
                    if dados_consulta[1] == id_paciente:
                        consultas.append(Consulta.from_string(line))
                return consultas
        except Exception as e:
            return None
        
    def encontra_por_id_psicologo(self, id_psicologo) -> list:
        try:
            with open(self.nome_arquivo, "r") as file:
                lines = file.readlines()
                consultas = []
                for line in lines:
                    dados_consulta = line.strip().split(",")
                    if dados_consulta[2] == id_psicologo:
                        consultas.append(Consulta.from_string(line))
                return consultas
        except Exception as e:
            return None
    

    