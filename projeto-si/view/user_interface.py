import os
import time
from typing import Dict, List

from consulta.consulta import Consulta

class UserInterface:
    def __init__(self):
        pass

    def menu(self) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|         [1] Fazer login          |")
        print("|         [2] Criar conta          |")
        print("|         [S] Sair                 |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")

    def tela_criacao_conta(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|         [1] Conta Paciente       |")
        print("|         [2] Conta Psicólogo(a)   |")
        print("|         [V] Voltar               |")   
        print("------------------------------------")
        return input("\nEscolha uma opção: ")

    def input_confirmacao(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|      [1] Preencher meus dados    |")
        print("|      [V] Voltar                  |")
        print("------------------------------------")
        return input("\n Escolha uma opção: ")

    def tela_dados_paciente(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        Preencha seus dados       |")
        print("------------------------------------")

        email = input("Email: ")
        if "@" not in email or "." not in email:
            return None
        
        senha = input("Senha (8+ caracteres): ")
        if len(senha) <= 7:
            return None
        
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        if not telefone.isnumeric() or len(telefone) < 10:
            return None
        
        cpf = input("CPF (Apenas números): ")
        if len(cpf) <= 10:
            return None
           
        return {
            "email": email,
            "senha": senha,
            "nome": nome,
            "telefone": telefone,
            "cpf": cpf
        }
    
    def input_detalhes_psicologo(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        Preencha seus dados       |")
        print("------------------------------------")
        email = input("Email: ")
        senha = input("Senha (8+ caracteres): ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cpf = input("CPF (Apenas números): ")
        crp = input("CRP: (Apenas números): ")
        return {
            "email": email,
            "senha": senha,
            "nome": nome,
            "telefone": telefone,
            "cpf": cpf,
            "crp": crp
        }
    
    def tela_conta_criada(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|       Conta criada com sucesso   |")
        print("------------------------------------")
        time.sleep(0.7)

    def saida(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|            Saindo...             |")
        print("------------------------------------")
        time.sleep(0.5)
        os.system("cls")

    def printa_opcao_invalida(self):
        print("Opção inválida.")
        time.sleep(0.7)

    def tela_erro_criacao_conta(self):
        print("Erro ao criar conta.")
        time.sleep(0.7)

    def login(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|           Faça seu login         |")
        print("------------------------------------")
        print("|          Tipo de conta:          |")
        print("|          [1] Paciente            |")
        print("|          [2] Psicólogo(a)        |")
        print("------------------------------------")
        email = input("Email: ")
        senha = input("Senha: ")
        tipo = input("Tipo de conta: ")
        return {
            "email": email,
            "senha": senha,
            "tipo": tipo
        }
    
    def erro_login(self):
        print("Email ou senha incorretos.")
        time.sleep(0.7)

    def erro_consulta(self):
        print("Erro ao agendar consulta")
        time.sleep(0.7)

    def login_success(self):
        print("Login realizado com sucesso.")
        time.sleep(0.5)


    # MENUS DO PACIENTE LOGADO
    def menu_paciente(self) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|         [1] Consultas            |")
        print("|         [2] Perfil               |")
        print("|         [S] Sair                 |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def menu_paciente_consultas(self) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        [1] Agendar consulta      |")
        print("|        [2] Consultas agendadas   |")
        print("|        [V] Voltar                |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def perfil_paciente(self, patient_data: Dict[str, str]) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|\n")
        print(f" Email: {patient_data['email']}")
        print(f" Nome: {patient_data['nome']}")
        print(f" Telefone: {patient_data['telefone']}")
        print(f" CPF: {patient_data['cpf']}")
        print("------------------------------------")
        print("|            [V] Voltar            |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
      


    # Psicologos logados

    def menu_psicologo(self) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|         [1] Consultas            |")
        print("|         [2] Perfil               |")
        print("|         [S] Sair                 |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def menu_psicologo_consultas(self) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        [2] Consultas agendadas   |")
        print("|        [V] Voltar                |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")

    def consultas_do_paciente(self, consultas: List[Consulta]):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        Consultas agendadas       |")
        print("------------------------------------")
        for consulta in consultas:
            print(f"ID: {consulta.id}")
            print(f"Psicólogo(a): {consulta.id_psicologo}")
            print("------------------------------------")
        print("|            [V] Voltar            |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def consultas_do_psicologo(self, consultas: List[Consulta]):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        Consultas agendadas       |")
        print("------------------------------------")
        for consulta in consultas:
            print(f"ID: {consulta.id}")
            print(f"Paciente: {consulta.id_paciente}")
            print("------------------------------------")
        print("|            [V] Voltar            |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def perfil_psicologo(self, psychologist_data: Dict[str, str]) -> str:
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|\n")
        print(f" Email: {psychologist_data['email']}")
        print(f" Nome: {psychologist_data['nome']}")
        print(f" Telefone: {psychologist_data['telefone']}")
        print(f" CPF: {psychologist_data['cpf']}")
        print(f" CRP: {psychologist_data['crp']}")
        print("------------------------------------")
        print("|            [V] Voltar            |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")
    
    def consulta_criada(self):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|    Consulta agendada com sucesso |")
        print("------------------------------------")
        time.sleep(0.7)

    def escolha_de_psicologo(self, dados_psicologos):
        os.system("cls")
        print("------------------------------------")
        print("|           Pysicologia            |")
        print("|  Sistema de gestão de consultas  |")
        print("|----------------------------------|")
        print("|        Lista de psicólogos       |")
        print("------------------------------------")
        for psicologo in dados_psicologos:
            print(f"ID: {psicologo["id"]}")
            print(f"Nome: {psicologo["nome"]}")
            print(f"Telefone: {psicologo["telefone"]}")
            print("------------------------------------")
        print("|            [V] Voltar            |")
        print("------------------------------------")
        return input("\nEscolha uma opção: ")