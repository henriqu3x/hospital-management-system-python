class MedicoDAO():
    def __init__(self, db):
        self.db = db

    def visualizar_medicos(self):
        try:
            consultar = self.db.consultar('''
    select id_medico, nome_med, crm_med, data_nascimento_med, sexo_med, telefone_med, email_med from medicos
''')        
            
            if consultar:
                return True, consultar
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_medicos(self, nome, crm, data, sexo, telefone, email):
        if nome and crm and data and sexo and telefone and email:
            try:
                result = self.db.manipular('''
    insert into medicos (nome_med, crm_med, data_nascimento_med, sexo_med, telefone_med, email_med) values
                                  (%s, %s, %s, %s, %s, %s)
''', (nome, crm, data, sexo, telefone, email))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False

    def atualizar_medicos(self, id_medico, nome, crm, data, sexo, telefone, email):
        if id_medico and nome and crm and data and sexo and telefone and email:
            try:
                consulta = self.db.consultar('''
    select * from medicos where id_medico = %s
''', (id_medico, ))
                
                if consulta:
                    result = self.db.manipular('''
        update medicos set nome_med = %s, crm_med = %s, data_nascimento_med = %s, sexo_med = %s, telefone_med = %s, email_med = %s where id_medico = %s
    ''', (nome, crm, data, sexo, telefone, email, id_medico))
                    
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

    def remover_medicos(self, id_medico):
        if id_medico:
            try:
                consulta = self.db.consultar('''
    select * from medicos where id_medico = %s
''', (id_medico, ))
                
                if consulta:
                    result = self.db.manipular('''
        delete from medicos where id_medico = %s
    ''', (id_medico, ))
                    
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