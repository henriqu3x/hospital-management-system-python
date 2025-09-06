from control.manipulacaoDAO import ManipulacaoDAO

class ExameDAO(ManipulacaoDAO):
    def __init__(self, db):
        self.db = db

    def visualizar_exames(self):
        try:
            consulta = self.db.consultar('''
    select id_exame, nome_pac, nome_med, tipo_exa, data_solicitacao_exa, data_realizacao_exa, status_exa, observacoes_exa from exames
                                         inner join pacientes on paciente_id = id_paciente
                                         inner join medicos on medico_id = id_medico
''')
            
            if consulta:
                return True, consulta
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_exames(self, id_paciente, id_medico, tipo_exa, data_solicitacao, data_realizacao, status, observacoes):
        if id_paciente and id_medico and tipo_exa:
            try:
                consultar_pac = self.db.consultar('select * from pacientes where id_paciente = %s', (id_paciente, ))
                consultar_med = self.db.consultar('select * from medicos where id_medico = %s', (id_medico, ))

                if consultar_pac and consultar_med:
                    dados = {
                        "paciente_id":id_paciente,
                        "medico_id":id_medico,
                        "tipo_exa":tipo_exa,
                        "data_solicitacao_exa":data_solicitacao,
                        "data_realizacao_exa":data_realizacao,
                        "status_exa":status,
                        "observacoes_exa":observacoes
                    }

                    sql, valores = self.manipular_insert('exames', dados)
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

    def atualizar_exames(self, id_exame, data_realizacao, status, observacoes):
        if id_exame:
            try:
                consulta = self.db.consultar('select * from exames where id_exame = %s', (id_exame, ))

                if consulta:
                    dados = {
                        "data_realizacao_exa":data_realizacao,
                        "status_exa":status.lower(),
                        "observacoes_exa":observacoes
                    }

                    sql, valores = self.manipular_update('exames', dados, 'id_exame')
                    valores.append(id_exame)

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

