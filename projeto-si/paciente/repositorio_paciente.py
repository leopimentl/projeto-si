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
                    id=resultado['id'],
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

    def atualizar(self, paciente: Paciente, id: int) -> Optional[Paciente]:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return None
        try:
            cursor = self.conexao.cursor()
            query = """
            UPDATE pacientes
            SET nome = %s, telefone = %s
            WHERE id = %s
            """
            cursor.execute(query, (paciente.nome, paciente.telefone, id))
            self.conexao.commit()
            if cursor.rowcount > 0:
                print(f"Paciente com ID {id} atualizado com sucesso.")
                return paciente
            else:
                print(f"Nenhuma linha foi afetada. Verifique se o ID {id} existe.")
                return None
        except Error as e:
            print(f"Erro ao atualizar paciente: {e}")
            return None
        
    def excluir(self, id: int) -> bool:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return False
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM pacientes WHERE id = %s"
            cursor.execute(query, (id,))
            self.conexao.commit()
            if cursor.rowcount > 0:
                print(f"Paciente com ID {id} excluído com sucesso.")
                return True
            else:
                print(f"Nenhuma linha foi afetada. Verifique se o ID {id} existe.")
                return False
        except Error as e:
            print(f"Erro ao excluir paciente: {e}")
            return False
        
    def buscar_por_id(self, id: int) -> Optional[Paciente]:
        if self.conexao is None:
            print("Conexão com o banco de dados não estabelecida.")
            return None
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM pacientes WHERE id = %s"
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()
            if resultado:
                return Paciente(
                    id=resultado['id'],
                    nome=resultado['nome'],
                    email=resultado['email'],
                    senha=resultado['senha'],
                    telefone=resultado['telefone'],
                    cpf=resultado['cpf']
                )
            return None
        except Error as e:
            print(f"Erro ao buscar paciente por ID: {e}")
            return None