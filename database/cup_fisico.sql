-- Criação Candidato
CREATE TABLE Candidato (
    CandidatoID SERIAL PRIMARY KEY,
    Nome VARCHAR(80),
    Nascimento DATE,
    Endereco TEXT,
    Email VARCHAR(80),
    Telefone VARCHAR(20),
    Educacao TEXT,
    Experiencia_Profissional TEXT
);

-- Criação Vaga
CREATE TABLE Vaga (
    VagaID SERIAL PRIMARY KEY,
    Titulo VARCHAR(40),
    Descricao TEXT,
    Requisitos TEXT,
    Jornada_Trabalho VARCHAR(20),
    Salario DECIMAL(10,2)
);

-- Criação Formulário
CREATE TABLE Formulario (
    FormularioID SERIAL PRIMARY KEY,
    CandidatoID INT,
    VagaID INT,
    Data_Preenchimento DATE,
    Status VARCHAR(20),
    FOREIGN KEY (CandidatoID) REFERENCES Candidato (CandidatoID),
    FOREIGN KEY (VagaID) REFERENCES Vaga (VagaID)
);

-- Vaga
INSERT INTO Vaga (Titulo, Descricao, Requisitos, Jornada_Trabalho, Salario)
VALUES ('Analista Financeiro', 'Responsável pela análise financeira da empresa.', 'Experiência com Excel e BI', 'Integral', 4500.00),
       ('Gerente de Marketing', 'Gerenciar equipe de marketing e campanhas.', 'Experiência com gestão de equipe', 'Integral', 6500.00);

-- Candidato
INSERT INTO Candidato (Nome, Nascimento, Endereco, Email, Telefone, Educacao, Experiencia_Profissional)
VALUES ('João Silva', '2000-10-10', 'Rua das Flores, 123, São Paulo', 'joao.silva@email.com', '(11) 99999-9999', 'Graduação em Administração', '5 anos em gestão financeira'),
       ('Maria Oliveira', '1994-10-10', 'Av. Brasil, 456, Rio de Janeiro', 'maria.oliveira@email.com', '(21) 88888-8888', 'Mestrado em Marketing', '3 anos em marketing digital');

-- Formulário - Status (Enviado, Em Análise, Aprovado, Rejeitado)
INSERT INTO Formulario (CandidatoID, VagaID, Data_Preenchimento, Status)
VALUES (1, 1, '2024-04-11', 'Enviado'),
       (2, 2, '2024-04-11', 'Enviado');
       