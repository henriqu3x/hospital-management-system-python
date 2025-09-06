from connection import Connection
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

db = Connection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

db.manipular('drop table if exists usuarios')
db.manipular('drop table if exists exames')
db.manipular('drop table if exists consultas')
db.manipular('drop table if exists internacoes')
db.manipular('drop table if exists medicos')
db.manipular('drop table if exists pacientes')
db.manipular('drop table if exists enfermeiros')
db.manipular('drop table if exists admins')

db.manipular('''
    create table if not exists usuarios(
             id_usuario int generated always as identity primary key,
             nome_usu varchar(50) not null,
             email_usu varchar(50) not null unique,
             senha_usu bytea not null,
             perfil_usu varchar(30) not null,
             data_criacao_usu date default current_date,
             constraint chk_perfil check(perfil_usu in ('enfermeiro', 'medico', 'admin'))
             )
''')

db.manipular('''
    create table if not exists medicos(
             id_medico int generated always as identity primary key,
             usuario_id int,
             nome_med varchar(50) not null,
             crm_med varchar(30) not null,
             data_nascimento_med varchar(10) not null,
             sexo_med varchar(25) default 'preferiu não responder',
             telefone_med varchar(20) not null,
             email_med varchar(50) not null
             )
''')

db.manipular('''
    create table if not exists enfermeiros(
             id_enfermeiro int generated always as identity primary key,
             usuario_id int,
             nome_enf varchar(50) not null,
             data_nascimento_enf varchar(10) not null,
             sexo_enf varchar(25) default 'preferiu não responder',
             telefone_enf varchar(25) not null,
             email_enf varchar(50) not null
             )
''')

db.manipular('''
    create table if not exists pacientes(
             id_paciente int generated always as identity primary key,
             nome_pac varchar(50) not null,
             cpf_pac varchar(11) not null,
             data_nascimento_pac varchar(10) not null,
             sexo_pac varchar(25) default 'preferiu não responder',
             telefone_pac varchar(20) not null,
             email_pac varchar(50) not null
             )
''')

db.manipular('''
    CREATE TABLE internacoes (
    id_internacao int generated always as identity PRIMARY KEY,
    paciente_id INT NOT NULL,
    data_entrada_int DATE DEFAULT CURRENT_DATE,
    data_saida_int DATE,
    quarto_int VARCHAR(50) NOT NULL,
    diagnostico_int VARCHAR(50) DEFAULT 'Paciente ainda não examinado',
    CONSTRAINT fk_internacao_paciente FOREIGN KEY (paciente_id)
        REFERENCES pacientes (id_paciente)
)
''')

db.manipular('''
    CREATE TABLE consultas (
    id_consulta int generated always as identity PRIMARY KEY,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    data_con DATE DEFAULT CURRENT_DATE,
    motivo_con VARCHAR(50) NOT NULL,
    observacoes_con VARCHAR(50) default 'paciente ainda não examinado',
    CONSTRAINT fk_consulta_paciente FOREIGN KEY (paciente_id)
        REFERENCES pacientes (id_paciente),
    CONSTRAINT fk_consulta_medico FOREIGN KEY (medico_id)
        REFERENCES medicos (id_medico)
);
''')

db.manipular('''
    CREATE TABLE exames (
    id_exame int generated always as identity PRIMARY KEY,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    tipo_exa VARCHAR(50) NOT NULL,
    data_solicitacao_exa DATE DEFAULT CURRENT_DATE,
    data_realizacao_exa DATE,
    status_exa VARCHAR(20) DEFAULT 'pendente',
    observacoes_exa VARCHAR(50) default 'paciente ainda não foi examinado',
    CONSTRAINT chk_status check(status_exa in('pendente', 'realizado', 'cancelado')),
    CONSTRAINT fk_exame_paciente FOREIGN KEY (paciente_id)
        REFERENCES pacientes (id_paciente),
    CONSTRAINT fk_exame_medico FOREIGN KEY (medico_id)
        REFERENCES medicos (id_medico)
);
''')
