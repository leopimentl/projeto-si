from typing import List, Optional
from consulta.consulta import Consulta
import mysql.connector
from mysql.connector import Error

class RepositorioConsulta:
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
        
    def salvar(self, consulta: Consulta) -> Optional[Consulta]:
        try:
            cursor = self.conexao.cursor()
            query = """
            INSERT INTO consultas (id_paciente, id_psicologo, data, horario, especialidade)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (consulta.id_paciente, consulta.id_psicologo, consulta.data, consulta.horario, consulta.especialidade))
            self.conexao.commit()
            consulta.id = cursor.lastrowid
            return consulta
        except Error as e:
            print(f"Erro ao salvar consulta: {e}")
            return None
    
    def listar(self) -> List[Consulta]:
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM consultas"
            cursor.execute(query)
            resultados = cursor.fetchall()
            consultas = []
            for row in resultados:
                consulta = Consulta(
                    id=row['id'],
                    id_paciente=row['id_paciente'],
                    id_psicologo=row['id_psicologo'],
                    data=row['data'],
                    horario=row['horario'],
                    especialidade=row['especialidade']
                )
                consultas.append(consulta)
            return consultas
        except Error as e:
            print(f"Erro ao listar consultas: {e}")
            return []
            
    def cancelar(self, id: int) -> bool:
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM consultas WHERE id = %s"
            cursor.execute(query, (id,))
            self.conexao.commit()
            return True
        except Error as e:
            print(f"Erro ao cancelar consulta: {e}")
            return False