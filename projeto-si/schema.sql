DROP DATABASE IF EXISTS pysicologia;
CREATE DATABASE IF NOT EXISTS pysicologia;
USE pysicologia;

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

