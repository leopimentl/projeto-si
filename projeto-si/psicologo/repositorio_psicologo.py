from typing import List
from psicologo.psicologo import Psicologo

class RepositorioPsicologo:
    
    def __init__(self, nome_arquivo="psicologos.txt"):
        self.nome_arquivo = nome_arquivo

    def salvar(self, psicologo) -> Psicologo:
        try:
            with open(self.nome_arquivo, "a+") as file:
                file.seek(0)
                linhas = file.readlines()
                id_psicologo = len(linhas) + 1
                psicologo.id = id_psicologo
                file.write(f"{id_psicologo},{psicologo}\n")
            return psicologo
        except Exception as e:
            print(e)
            return None
        
    def encontrar_por_email(self, email: str) -> Psicologo:
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados_psicologo = linha.strip().split(",")
                    if dados_psicologo[1] == email:
                        psychologist = Psicologo.from_string(linha)
                        return psychologist
        except Exception as e:
            return None
    
    def encontrar_por_cpf(self, cpf: str) -> Psicologo:
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados_psicologo = linha.strip().split(",")
                    if dados_psicologo[5] == cpf:
                        psychologist = Psicologo.from_string(linha)
                        return psychologist
        except Exception as e:
            return
        
    def encontrar_por_crp(self, crp: str) -> Psicologo:
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados_psicologo = linha.strip().split(",")
                    if dados_psicologo[6] == crp:
                        psychologist = Psicologo.from_string(linha)
                        return psychologist
        except Exception as e:
            return None

    def encontrar_por_id(self, id: str) -> Psicologo:
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    dados_psicologo = linha.strip().split(",")
                    if dados_psicologo[0] == id:
                        psychologist = Psicologo.from_string(linha)
                        return psychologist
        except Exception as e:
            return None
    
    def encontra_todos(self) -> List[Psicologo]:
        psicologos = []
        try:
            with open(self.nome_arquivo, "r") as file:
                linhas = file.readlines()
                for linha in linhas:
                    psicologo = Psicologo.from_string(linha.strip())
                    psicologos.append(psicologo)
        except Exception as e:
            return psicologos
        return psicologos