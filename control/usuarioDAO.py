import bcrypt

class UsuarioDAO():
    def __init__(self, db):
        self.db = db

    def login(self, email, senha):
        if email and senha:
            try:
                result = self.db.consultar('select senha_usu, perfil_usu from usuarios where email_usu = %s', (email, ))

                if result:
                    senha_bytes = bytes(result[0][0])
                    verificar_senha_hash = bcrypt.checkpw(senha.encode('utf-8'), senha_bytes)
                    if verificar_senha_hash:
                        return True, result[0][1]
                    else:
                        return False,
                else:
                    return False,
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False,
        else:
            return False,
        
    def registrar(self, nome, email, senha, perfil):
        if nome and email and senha and perfil:
            try:
                senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
                result = self.db.manipular('''
    insert into usuarios (nome_usu, email_usu, senha_usu, perfil_usu) values
                                  (%s, %s, %s, %s)
''', (nome, email, senha_hash, perfil.lower()))
                
                if result:
                    if perfil == 'medico':
                        consulta_email_med = self.db.consultar('''
        select email_med from medicos where email_med = %s
    ''', (email, ))
                        
                        if consulta_email_med:
                            consulta_id_med = self.db.consultar('select id_usuario from usuarios where email_usu = %s', (email, ))
                            self.db.manipular('update medicos set usuario_id = %s', (consulta_id_med[0][0], ))
                    elif perfil == 'enfermeiro':
                        consulta_email_enf = self.db.consultar('''
        select email_enf from enfermeiros where email_enf = %s
    ''', (email, ))
                        
                        if consulta_email_enf:
                            consulta_id_enf = self.db.consultar('select id_usuario from usuarios where email_usu = %s', (email, ))
                            self.db.manipular('update enfermeiros set usuario_id = %s', (consulta_id_enf[0][0], ))

                    return True
                else:
                    return False
            except Exception as e:
                print('Erro: ', e)
                self.db.desconectar()
                return False
        else:
            return False
        