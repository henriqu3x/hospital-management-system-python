from control.manipulacaoDAO import ManipulacaoDAO

class ConsultaDAO(ManipulacaoDAO):
    def __init__(self, db):
        self.db = db

    def visualizar_consultas(self):
        try:
            consulta = self.db.consultar('''
    select id_consulta, nome_pac, nome_med, data_con, motivo_con, observacoes_con from consultas
                                         inner join pacientes on consultas.paciente_id = pacientes.id_paciente
                                         inner join medicos on consultas.medico_id = medicos.id_medico           
''')
            
            if consulta:
                return True, consulta
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_consultas(self, id_paciente, id_medico, data_con, motivo, observacoes):
        if id_paciente and id_medico and motivo:
            try:
                consulta_pac = self.db.consultar('select * from pacientes where id_paciente = %s', (id_paciente, ))
                consulta_med = self.db.consultar('select * from medicos where id_medico = %s', (id_medico, ))

                if consulta_pac and consulta_med:

                    dados = {
                        "paciente_id": id_paciente,
                        "medico_id": id_medico,
                        "data_con": data_con,
                        "motivo_con": motivo,
                        "observacoes_con": observacoes
                    }

                    sql, valores = self.manipular_insert('consultas', dados)
                    result = self.db.manipular(sql, valores)

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
        else:
            return False

    def atualizar_consultas(self, id_consulta, observacoes):
        if id_consulta and observacoes:
            try:
                consulta = self.db.consultar('''
    select * from consultas where id_consulta = %s
''', (id_consulta, ))
                
                if consulta:
                    result = self.db.manipular('''
    update consultas set observacoes_con = %s where id_consulta = %s
''', (observacoes, id_consulta))
                    
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
