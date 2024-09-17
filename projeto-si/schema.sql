-- Remove o banco de dados se ele existir
DROP DATABASE IF EXISTS pysicologia;

-- Cria o banco de dados se ele não existir
CREATE DATABASE IF NOT EXISTS pysicologia;

-- Usa o banco de dados criado
USE pysicologia;

-- Cria a tabela pacientes se ela não existir
CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    cpf VARCHAR(14) NOT NULL UNIQUE
);

-- Cria a tabela psicologos se ela não existir
CREATE TABLE IF NOT EXISTS psicologos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    crp VARCHAR(20) NOT NULL UNIQUE
);