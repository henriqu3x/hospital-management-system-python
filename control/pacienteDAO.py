class PacienteDAO():
    def __init__(self, db):
        self.db = db

    def visualizar_pacientes(self):
        try:
            consultar = self.db.consultar('''
    select id_paciente, nome_pac, cpf_pac, data_nascimento_pac, sexo_pac, telefone_pac, email_pac from pacientes
''')        
            
            if consultar:
                return True, consultar
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_pacientes(self, nome, cpf, data, sexo, telefone, email):
        if nome and cpf and data and sexo and telefone and email:
            try:
                result = self.db.manipular('''
    insert into pacientes (nome_pac, cpf_pac, data_nascimento_pac, sexo_pac, telefone_pac, email_pac) values
                                  (%s, %s, %s, %s, %s, %s)
''', (nome, cpf, data, sexo, telefone, email))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False

    def atualizar_pacientes(self, id_paciente, nome, cpf, data, sexo, telefone, email):
        if id_paciente and nome and cpf and data and sexo and telefone and email:
            try:
                consulta = self.db.consultar('''
    select * from pacientes where id_paciente = %s
''', (id_paciente, ))
                
                if consulta:
                    result = self.db.manipular('''
        update pacientes set nome_pac = %s, cpf_pac = %s, data_nascimento_pac = %s, sexo_pac = %s, telefone_pac = %s, email_pac = %s where id_paciente = %s
    ''', (nome, cpf, data, sexo, telefone, email, id_paciente))
                    
                    if result:
                        return True
                    else:
                        return False
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False

    def remover_pacientes(self, id_paciente):
        if id_paciente:
            try:
                consulta = self.db.consultar('''
    select * from pacientes where id_paciente = %s
''', (id_paciente, ))
                
                if consulta:
                    result = self.db.manipular('''
        delete from pacientes where id_paciente = %s
    ''', (id_paciente, ))
                    
                    if result:
                        return True
                    else:
                        return False
                
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False