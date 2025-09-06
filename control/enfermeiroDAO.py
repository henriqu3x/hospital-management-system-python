class EnfermeiroDAO():
    def __init__(self, db):
        self.db = db

    def visualizar_enfermeiros(self):
        try:
            consultar = self.db.consultar('''
    select id_enfermeiro, nome_enf, data_nascimento_enf, sexo_enf, telefone_enf, email_enf from enfermeiros
''')        
            
            if consultar:
                return True, consultar
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_enfermeiros(self, nome, data, sexo, telefone, email):
        if nome and data and sexo and telefone and email:
            try:
                result = self.db.manipular('''
    insert into enfermeiros (nome_enf, data_nascimento_enf, sexo_enf, telefone_enf, email_enf) values
                                  (%s, %s, %s, %s, %s)
''', (nome, data, sexo, telefone, email))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False

    def atualizar_enfermeiros(self, id_enfermeiro, nome, data, sexo, telefone, email):
        if id_enfermeiro and nome and data and sexo and telefone and email:
            try:
                consulta = self.db.consultar('''
    select * from enfermeiros where id_enfermeiro = %s
''', (id_enfermeiro, ))
                
                if consulta:
                    result = self.db.manipular('''
        update enfermeiros set nome_enf = %s, data_nascimento_enf = %s, sexo_enf = %s, telefone_enf = %s, email_enf = %s where id_enfermeiro = %s
    ''', (nome, data, sexo, telefone, email, id_enfermeiro))
                    
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

    def remover_enfermeiros(self, id_enfermeiro):
        if id_enfermeiro:
            try:
                consulta = self.db.consultar('''
    select * from enfermeiros where id_enfermeiro = %s
''', (id_enfermeiro, ))
                
                if consulta:
                    result = self.db.manipular('''
        delete from enfermeiros where id_enfermeiro = %s
    ''', (id_enfermeiro, ))
                    
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