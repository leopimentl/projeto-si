from typing import Optional
import mysql.connector
from mysql.connector import Error
from paciente.paciente import Paciente

class RepositorioPaciente:
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

    def salvar(self, paciente: Paciente) -> Optional[Paciente]:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return None
        try:
            cursor = self.conexao.cursor()
            query = "INSERT INTO pacientes (nome, email, senha, telefone, cpf) VALUES (%s, %s, %s, %s, %s)"
            valores = (paciente.nome, paciente.email, paciente.senha, paciente.telefone, paciente.cpf)
            cursor.execute(query, valores)
            self.conexao.commit()
            paciente.id = cursor.lastrowid
            return paciente
        except Error as e:
            print(f"Erro ao salvar paciente: {e}")
            return None

    def encontra_por_email(self, email: str) -> Optional[Paciente]:
        if not self.conexao:
            print("Conexão com o banco de dados não estabelecida.")
            return None
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM pacientes WHERE email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            if resultado:
                return Paciente(
                    nome=resultado['nome'],
                    email=resultado['email'],
                    senha=resultado['senha'],
                    telefone=resultado['telefone'],
                    cpf=resultado['cpf']
                )
            return None
        except Error as e:
            print(f"Erro ao encontrar paciente pelo email: {e}")
            return None
        
    def existe_por_email(self, email) -> bool:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return True
        try:
            cursor = self.conexao.cursor()
            query = "SELECT * FROM pacientes WHERE email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            return resultado is not None
        except Error as e:
            print(f"Erro ao verificar email: {e}")
            return True

    def existe_por_cpf(self, cpf) -> bool:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return True
        try:
            cursor = self.conexao.cursor()
            query = "SELECT * FROM pacientes WHERE cpf = %s"
            cursor.execute(query, (cpf,))
            resultado = cursor.fetchone()
            return resultado is not None
        except Error as e:
            print(f"Erro ao verificar CPF: {e}")
            return True