from control.usuarioDAO import UsuarioDAO
from control.medicoDAO import MedicoDAO
from control.enfermeiroDAO import EnfermeiroDAO
from control.pacienteDAO import PacienteDAO
from control.internacaoDAO import InternacaoDAO
from control.consultaDAO import ConsultaDAO
from control.exameDAO import ExameDAO
from db.connection import Connection
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

db = Connection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

back_usuario = UsuarioDAO(db)
back_medico = MedicoDAO(db)
back_enfermeiro = EnfermeiroDAO(db)
back_paciente = PacienteDAO(db)
back_internacao = InternacaoDAO(db)
back_consulta = ConsultaDAO(db)
back_exame = ExameDAO(db)


def visualizar_exames():
    result = back_exame.visualizar_exames()

    if result[0]:
        for e in result[1]:
            print(F'\nID EXAME: {e[0]} | PACIENTE: {e[1]} | MEDICO: {e[2]} | TIPO EXAME: {e[3]} | DATA SOLICITAÇÃO: {e[4]} | DATA REALIZAÇÃO: {e[5]} | STATUS: {e[6]} | OBSERVAÇÕES: {e[7]}')
    else:
        print('\nNenhum exame adicionado até o momento')

def adicionar_exames():
    id_paciente = input('Digite o id do paciente: ')
    id_medico = input('Digite o id do medico: ')
    tipo_exa = input('Digite o tipo de exame: ')
    data_solicitacao = input('Digite a data de solicitação(DEIXE EM BRANCO PARA A DATA ATUAL): ')
    data_realizacao = input('Digite a data de realização(DEIXE EM BRANCO SE AINDA NÃO ACONTECEU): ')
    status = input('Digite o status do exame(pendente, realizado, cancelado) DEIXE EM BRANCO PARA PENDENTE: ')
    obersevacoes = input('Digite as observações do exame(DEIXE EM BRANCO SE O PACIENTE AINDA NÃO FOI EXAMINADO): ')
    result = back_exame.adicionar_exames(id_paciente, id_medico, tipo_exa, data_solicitacao, data_realizacao, status, obersevacoes)

    if result:
        print('\nExame adicionado com sucesso!')
    else:
        print('\nFalha ao adicionar exame')


def atualizar_exames():
    id_exame = input('Digite o id do exame: ')
    data_realizacao = input('Digite a data de realização(DEIXE EM BRANCO SE VOCÊ NÃO QUER MUDAR ISSO): ')
    status = input('Digite o status do exame(pendente, realizado, cancelado) DEIXE EM BRANCO SE VOCÊ NÃO QUER MUDAR ISSO: ')
    obersevacoes = input('Digite as observações do exame(DEIXE EM BRANCO SE VOCÊ NÃO QUER MUDAR ISSO): ')
    result = back_exame.atualizar_exames(id_exame, data_realizacao, status, obersevacoes)

    if result:
        print('\nExame atualizado com sucesso!')
    else:
        print('\nFalha ao atualizar exame')


def visualizar_consultas():
    result = back_consulta.visualizar_consultas()

    if result[0]:
        for c in result[1]:
            print(f'\nID CONSULTA: {c[0]} | PACIENTE: {c[1]} | MEDICO: {c[2]} | DATA CONSULTA: {c[3]} | MOTIVO CONSULTA: {c[4]} | OBSERVAÇÕES: {c[5]}')
    else:
        print('\nNenhum paciente foi consultado até o momento')

def adicionar_consultas():
    id_paciente = input('Digite o id do paciente: ')
    id_medico = input('Digite o id do medico: ')
    data_con = input('Digite a data em que a consulta foi realizada(deixe em branco para o dia atual): ')
    motivo = input('Digite o motivo da consulta: ')
    obersevacoes = input('Digite as observações da consulta(deixe em branco se o paciente ainda não foi examinado): ')
    result = back_consulta.adicionar_consultas(id_paciente, id_medico, data_con, motivo, obersevacoes)
    if result:
        print('\nNova consulta adicionada!')
    else:
        print('\nFalha ao adicionar consulta')

def atualizar_consultas():
    id_consulta = input('Digite o id da consulta: ')
    observacoes = input('Digite as observações da consulta: ')
    result = back_consulta.atualizar_consultas(id_consulta, observacoes)

    if result:
        print('\nStatus da consulta atualizada com sucesso!')
    else:
        print('\nFalha ao atualizar status da consulta')


def visualizar_internacoes():
    result = back_internacao.visualizar_internacoes()

    if result[0]:
        for i in result[1]:
            print(f'\nID INTERNAÇÃO: {i[0]} | PACIENTE: {i[1]} | DATA ENTRADA: {i[2]} | DATA SAIDA: {i[3]} | QUARTO: {i[4]} | DIAGNOSTICO: {i[5]}')
    else:
        print('\nNenhum paciente internado no momento')

def adicionar_internacoes():
    id_paciente = input('Digite o id do paciente: ')
    data_entrada = input('Digite a data de entrada do paciente(deixe em branco para o dia atual): ')
    data_saida = input('Digite a data de saida do paciente(deixe em branco se o paciente ainda está internado): ')
    quarto = input('Digite o quarto em que o paciente está: ')
    diagnostico = input('Digite o diagnostico do paciente(deixe em branco se ainda não foi examinado): ')
    result = back_internacao.adicionar_internacoes(id_paciente, data_entrada, data_saida, quarto, diagnostico)

    if result:
        print('\nNova internação adicionada!')
    else:
        print('\nFalha ao adicionar internação')

def atualizar_internacoes():
    id_internacao = input('Digite o id da internação: ')
    data_saida = input('Digite a data de saida do paciente(Deixe em branco se você não deseja alterar isso): ')
    diagnostico = input('Digite o diagnostico do paciente(Deixe em branco se você não deseja alterar isso): ')
    result = back_internacao.atualizar_internacoes(id_internacao, data_saida, diagnostico)

    if result:
        print('\nStatus da internação atualizada com sucesso!')
    else:
        print('\nFalha ao atualizar status da internação')


def visualizar_pacientes():
    result = back_paciente.visualizar_pacientes()

    if result[0]:
        for pac in result[1]:
            print(f'\nID:{pac[0]} | NOME:{pac[1]} | CPF: {pac[2]} | DATA NASCIMENTO:{pac[3]} | SEXO:{pac[4]} | TELEFONE:{pac[5]} | EMAIL:{pac[6]}')
    else:
        print('\nNenhum paciente encontrado')

def adicionar_pacientes():
    nome = input('Digite o nome do paciente: ')
    cpf = input('Digite o cpf do paciente: ')
    data = input('Digite a data de nascimento do paciente: ')
    sexo = input('Digite o sexo do paciente: ')
    telefone = input('Digite o telefone do paciente: ')
    email = input('Digite o email do paciente: ')
    result = back_paciente.adicionar_pacientes(nome, cpf, data, sexo, telefone, email)

    if result:
        print('\nPaciente adicionado com sucesso!')
    else:
        print('\nFalha ao adicionar paciente')

def atualizar_pacientes():
    id_paciente = input('Digite o id do paciente que voce deseja atualizar: ')
    nome = input('Digite o novo nome do paciente: ')
    cpf = input('Digite o cpf do paciente')
    data = input('Digite a nova data de nascimento do paciente: ')
    sexo = input('Digite o sexo do paciente: ')
    telefone = input('Digite o novo telefone do paciente: ')
    email = input('Digite o novo email do paciente: ')
    result = back_paciente.atualizar_pacientes(id_paciente, nome, cpf, data, sexo, telefone, email)

    if result:
        print('\nPaciente atualizado com sucesso!')
    else:
        print('\nFalha ao atualizar paciente')

def remover_pacientes():
    id_paciente = input('Digite o id do paciente que será removido: ')
    result = back_paciente.remover_pacientes(id_paciente)

    if result:
        print('\nPaciente removido com sucesso!')
    else:
        print('\nFalha ao remover paciente')

def gerenciar_pacientes():
    print('\nGerenciar Pacientes')

    while True:
        print('''
    1.Visualizar pacientes
    2.Adicionar pacientes
    3.Atualizar pacientes
    4.Remover pacientes
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_pacientes()
        elif op == '2':
            adicionar_pacientes()
        elif op == '3':
            atualizar_pacientes()
        elif op == '4':
            remover_pacientes()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def gerenciar_internacoes():
    print('\nGerenciar Internações')

    while True:
        print('''
    1.Visualizar internações
    2.Adicionar internação
    3.Atualizar internação
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_internacoes()
        elif op == '2':
            adicionar_internacoes()
        elif op == '3':
            atualizar_internacoes()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def gerenciar_consultas():
    print('\nGerenciar Consultas')

    while True:
        print('''
    1.Visualizar consultas
    2.Adicionar consulta
    3.Atualizar consulta
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_consultas()
        elif op == '2':
            adicionar_consultas()
        elif op == '3':
            atualizar_consultas()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def gerenciar_exames():
    print('\nGerenciar Exames')

    while True:
        print('''
    1.Visualizar exames
    2.Adicionar exame
    3.Atualizar exame
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_exames()
        elif op == '2':
            adicionar_exames()
        elif op == '3':
            atualizar_exames()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def visualizar_enfermeiros():
    result = back_enfermeiro.visualizar_enfermeiros() 
    if result[0]:
        for enf in result[1]:
            print(f'\nID:{enf[0]} | NOME:{enf[1]} | DATA NASCIMENTO:{enf[2]} | SEXO:{enf[3]} | TELEFONE:{enf[4]} | EMAIL:{enf[5]}')
    else:
        print('\nNenhum enfermeiro encontrado')

def adicionar_enfermeiros():
    nome = input('Digite o nome do enfermeiro: ')
    data = input('Digite a data de nascimento do enfermeiro: ')
    sexo = input('Digite o sexo do enfermeiro: ')
    telefone = input('Digite o telefone do enfermeiro: ')
    email = input('Digite o email do enfermeiro: ')
    result = back_enfermeiro.adicionar_enfermeiros(nome, data, sexo, telefone, email)

    if result:
        print('\nEnfermeiro adicionado com sucesso!')
    else:
        print('\nFalha ao adicionar enfermeiro')

def atualizar_enfermeiros():
    id_enfermeiro = input('Digite o id do enfermeiro que voce deseja atualizar: ')
    nome = input('Digite o novo nome do enfermeiro: ')
    data = input('Digite a nova data de nascimento do enfermeiro: ')
    sexo = input('Digite o sexo do enfermeiro: ')
    telefone = input('Digite o novo telefone do enfermeiro: ')
    email = input('Digite o novo email do enfermeiro: ')

    result = back_enfermeiro.atualizar_enfermeiros(id_enfermeiro, nome, data, sexo, telefone, email)

    if result:
        print('\nEnfermeiro atualizado com sucesso!')
    else: 
        print('\nFalha ao tentar atualizar enfermeiro')

def remover_enfermeiros():
    id_enfermeiro = input('Digite o id do enfermeiro que será removido: ')
    result = back_enfermeiro.remover_enfermeiros(id_enfermeiro)

    if result:
        print('\nEnfermeiro deletado com sucesso!')
    else:
        print('\nFalha ao deletar enfermeiro')

def visualizar_medicos():
    result = back_medico.visualizar_medicos() 
    if result[0]:
        for med in result[1]:
            print(f'\nID:{med[0]} | NOME:{med[1]} | CRM:{med[2]} | DATA NASCIMENTO:{med[3]} | SEXO:{med[4]} | TELEFONE:{med[5]} | EMAIL:{med[6]}')
    else:
        print('\nNenhum medico encontrado')

def adicionar_medicos():
    nome = input('Digite o nome do medico: ')
    crm = input('Digite o CRM do medico: ')
    data = input('Digite a data de nascimento do medico: ')
    sexo = input('Digite o sexo do medico: ')
    telefone = input('Digite o telefone do medico: ')
    email = input('Digite o email do medico: ')
    result = back_medico.adicionar_medicos(nome, crm, data, sexo, telefone, email)

    if result:
        print('\nMedico adicionado com sucesso!')
    else:
        print('\nFalha ao adicionar medico')

def atualizar_medicos():
    id_medico = input('Digite o id do medico que voce deseja atualizar: ')
    nome = input('Digite o novo nome do medico: ')
    crm = input('Digite o novo crm do medico: ')
    data = input('Digite a nova data de nascimento do medico: ')
    sexo = input('Digite o sexo do medico: ')
    telefone = input('Digite o novo telefone do medico: ')
    email = input('Digite o novo email do medico: ')

    result = back_medico.atualizar_medicos(id_medico, nome, crm, data, sexo, telefone, email)

    if result:
        print('\nMedico atualizado com sucesso!')
    else: 
        print('\nFalha ao tentar atualizar medico')

def remover_medicos():
    id_medico = input('Digite o id do medico que será removido: ')
    result = back_medico.remover_medicos(id_medico)

    if result:
        print('\nMedico deletado com sucesso!')
    else:
        print('\nFalha ao deletar medico')


def gerenciar_medicos():
    print('\nGerenciar medicos')

    while True:
        print('''
    1.Visualizar medicos
    2.Adicionar medicos
    3.Atualizar medicos
    4.Remover medicos
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_medicos()
        elif op == '2':
            adicionar_medicos()
        elif op == '3':
            atualizar_medicos()
        elif op == '4':
            remover_medicos()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def gerenciar_enfermeiros():
    print('\nGerenciar enfermeiros')

    while True:
        print('''
    1.Visualizar enfermeiros
    2.Adicionar enfermeiros
    3.Atualizar enfermeiros
    4.Remover enfermeiros
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            visualizar_enfermeiros()
        elif op == '2':
            adicionar_enfermeiros()
        elif op == '3':
            atualizar_enfermeiros()
        elif op == '4':
            remover_enfermeiros()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida')

def login_admin():
    while True:
        print('''
    1.Gerenciar Medicos
    2.Gerenciar Enfermeiros
    0.Voltar
''')
        
        op = input('Escolha uma opção: ')

        if op == '1':
            gerenciar_medicos()
        elif op == '2':
            gerenciar_enfermeiros()
        elif op == '0':
            print('\nVOLTANDO...')
            break
        else:
            print('\nOPÇÃO INVALIDA')

def login_medico():
    while True:
        print('''
    1. Gerenciar Pacientes
    2. Gerenciar Internações
    3. Gerenciar Consultas
    4. Gerenciar Exames
    0. Sair
''')
        
        op = input('Escolha uma opção: ')

        if op == '1':
            gerenciar_pacientes()
        elif op == '2':
            gerenciar_internacoes()
        elif op == '3':
            gerenciar_consultas()
        elif op == '4':
            gerenciar_exames()
        elif op == '0':
            print('\nVOLTANDO...')
            break
        else:
            print('\nOPÇÃO INVALIDA')

def login_enfermeiro():
    while True:
        print('''
    1. Visualizar Pacientes
    2. Visualizar Medicos
    3. Visualizar Enfermeiros
    4. Visualizar Internações
    5. Visualizar Consultas
    6. Visualizar Exames
    0. Sair
''')
        
        op = input('Escolha uma opção: ')

        if op == '1':
            visualizar_pacientes()
        elif op == '2':
            visualizar_medicos()
        elif op == '3':
            visualizar_enfermeiros()
        elif op == '4':
            visualizar_internacoes()
        elif op == '5':
            visualizar_consultas()
        elif op == '6':
            visualizar_exames()
        elif op == '0':
            print('\nVOLTANDO...')
            break
        else:
            print('\nOPÇÃO INVALIDA')

def login():
    print('\nFAÇA SEU LOGIN')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    result = back_usuario.login(email, senha)
    if result[0]:
        if result[1] == 'admin':
            print('\nLogin como admin efetuado com sucesso!')
            login_admin()
        elif result[1] == 'medico':
            print('\nLogin como medico efetuado com sucesso!')
            login_medico()
        else:
            print('\nLogin como enfermeiro efetuado com sucesso!')
            login_enfermeiro()
    else:
        print('\nEmail ou senha incorretos')


def registrar():
    print('FAÇA SEU CADASTRO')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    tipo = input('Digite o perfil de usuario(medico, enfermeiro, admin): ')
    result = back_usuario.registrar(nome, email, senha, tipo)

    if result:
        print('\nUsuario registrado com sucesso!')
    else:
        print('\nFalha ao registrar usuario')

print('Sistema Hospitalar')

while True:
    print('''
    1. Login
    2. Registrar
    0. Sair
''')
    
    op = input('SELECIONE UMA OPÇÃO: ')

    if op == '1':
        login()
    elif op == '2':
        registrar()
    elif op == '0':
        print('\nSAINDO DO PROGRAMA...')
        break
    else:
        print('\nOPÇÃO INCORRETA')