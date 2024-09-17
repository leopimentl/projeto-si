from typing import List, Optional
import mysql.connector
from mysql.connector import Error
from psicologo.psicologo import Psicologo

class RepositorioPsicologo:
    def __init__(self, host="localhost", database="pysicologia", user="root", password="root"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conexao = self.criar_conexao()

    def criar_conexao(self):
        try:
            conexao = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if conexao.is_connected():
                return conexao
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return None

    def salvar(self, psicologo: Psicologo) -> bool:
        try:
            cursor = self.conexao.cursor()
            query = """
            INSERT INTO psicologos (email, senha, nome, telefone, cpf, crp)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (psicologo.email, psicologo.senha, psicologo.nome, psicologo.telefone, psicologo.cpf, psicologo.crp))
            self.conexao.commit()
            return True
        except Error as e:
            print(f"Erro ao adicionar psicólogo: {e}")
            return False

    def encontra_por_email(self, email: str) -> Optional[Psicologo]:
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM psicologos WHERE email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            if resultado:
                return Psicologo(
                    email=resultado['email'],
                    senha=resultado['senha'],
                    nome=resultado['nome'],
                    telefone=resultado['telefone'],
                    cpf=resultado['cpf'],
                    crp=resultado['crp'],
                    id=resultado['id']
                )
            return None
        except Error as e:
            print(f"Erro ao encontrar psicólogo pelo email: {e}")
            return None

    def existe_por_cpf(self, cpf: str) -> bool:
        try:
            cursor = self.conexao.cursor()
            query = "SELECT 1 FROM psicologos WHERE cpf = %s"
            cursor.execute(query, (cpf,))
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar existência de psicólogo pelo CPF: {e}")
            return False

    def existe_por_email(self, email: str) -> bool:
        try:
            cursor = self.conexao.cursor()
            query = "SELECT 1 FROM psicologos WHERE email = %s"
            cursor.execute(query, (email,))
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar existência de psicólogo pelo email: {e}")
            return False

    def existe_por_crp(self, crp: str) -> bool:
        try:
            cursor = self.conexao.cursor()
            query = "SELECT 1 FROM psicologos WHERE crp = %s"
            cursor.execute(query, (crp,))
            return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar existência de psicólogo pelo CRP: {e}")
            return False