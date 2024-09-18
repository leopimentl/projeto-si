
# Pysicologia - Sistema de gerenciamento de consultas psicológicas

## Visão Geral

O Pysicologia é um sistema de gerenciamento de consultas psicológicas que permite que pacientes agendem consultas com psicólogos e que psicólogos gerenciem suas consultas e perfis. O sistema inclui funcionalidades para autenticação de usuários, agendamento de consultas, visualização de detalhes de consultas e cancelamento de consultas.

## Funcionalidades Principais

- **Autenticação de Usuários**:
  - Login e registro de pacientes e psicólogos.
- **Gerenciamento de Consultas**:
  - Agendamento de consultas.
  - Visualização de consultas agendadas.
  - Cancelamento de consultas.
- **Gerenciamento de Perfis**:
  - Visualização e edição de perfis de psicólogos e pacientes.

## Bibliotecas Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para criação da interface gráfica do usuário (GUI).
  - Justificativa: Tkinter é uma biblioteca padrão do Python para criação de interfaces gráficas, fácil de usar e bem documentada.
- **Tkcalendar**: Biblioteca para seleção de datas na interface gráfica.
  - Justificativa: Fornece widgets de calendário e seleção de datas que são fáceis de integrar com Tkinter.
- **MySQL Connector**: Biblioteca para conexão com o banco de dados MySQL.
  - Justificativa: Necessária para executar operações de banco de dados, como consultas e atualizações.

## Importações Necessárias

Certifique-se de ter as seguintes bibliotecas instaladas para rodar o projeto:

```bash
pip install mysql-connector-python tkcalendar
```

## Organização dos Módulos

O projeto está organizado nos seguintes módulos:

### Modelos:

- `paciente.py`: Define a classe Paciente.
- `psicologo.py`: Define a classe Psicologo.
- `consulta.py`: Define a classe Consulta.

### Repositórios:

- `repositorio_paciente.py`: Gerencia as operações de banco de dados relacionadas aos pacientes.
- `repositorio_psicologo.py`: Gerencia as operações de banco de dados relacionadas aos psicólogos.
- `repositorio_consulta.py`: Gerencia as operações de banco de dados relacionadas às consultas.

### Serviços:

- `servico_paciente.py`: Contém a lógica de negócios relacionada aos pacientes.
- `servico_psicologo.py`: Contém a lógica de negócios relacionada aos psicólogos.
- `servico_consulta.py`: Contém a lógica de negócios relacionada às consultas.

## Como Rodar o Projeto

1. **Configurar o Banco de Dados**:
   - Crie um banco de dados MySQL e configure as tabelas necessárias para pacientes, psicólogos e consultas.
   - Você pode usar o seguinte comando SQL para criar o banco de dados:
     ```sql
     CREATE DATABASE pysicologia;
     ```
   - E os seguintes comandos para criar as tabelas (exemplo):
     ```sql
        CREATE TABLE IF NOT EXISTS pacientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL,
            telefone VARCHAR(20),
            cpf VARCHAR(14) NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS psicologos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha VARCHAR(255) NOT NULL,
            nome VARCHAR(255) NOT NULL,
            telefone VARCHAR(20) NOT NULL,
            cpf VARCHAR(14) NOT NULL UNIQUE,
            crp VARCHAR(20) NOT NULL UNIQUE,
            especialidade VARCHAR(255) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS consultas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_paciente INT NOT NULL,
            id_psicologo INT NOT NULL,
            data DATE NOT NULL,
            horario TIME NOT NULL,
            especialidade VARCHAR(255) NOT NULL,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
            FOREIGN KEY (id_psicologo) REFERENCES psicologos(id)
        );
     ```

2. **Configurar o Arquivo de Conexão**:
   - Configure a conexão com o banco de dados nos arquivos de repositório (ou equivalente). Exemplo:
     ```python
     # repositorio_psicologo.py
     db_config = {
         'user': 'seu_usuario',
         'password': 'sua_senha',
         'host': 'localhost',
         'database': 'pysicologia'
     }
     ```

3. **Executar o Projeto**:
   - Execute o arquivo principal para iniciar a aplicação:
     ```bash
     python main.py
     ```
    - Se você estiver usando macOS e tiver múltiplas versões do Python instaladas, pode ser necessário    especificar `python3`:
         ```bash
        python3 main.py
        ```

### Conclusão

O Pysicologia é uma solução completa para o gerenciamento de consultas psicológicas, facilitando a interação entre pacientes e psicólogos. Através de uma interface amigável e funcionalidades robustas, o sistema busca melhorar a eficiência e a organização das consultas psicológicas.
