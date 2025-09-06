from control.manipulacaoDAO import ManipulacaoDAO

class InternacaoDAO(ManipulacaoDAO):
    def __init__(self, db):
        self.db = db

    def visualizar_internacoes(self):
        try:
            consulta = self.db.consultar('''
    select id_internacao, nome_pac, data_entrada_int, data_saida_int, quarto_int, diagnostico_int from internacoes
                                         inner join pacientes on internacoes.paciente_id = pacientes.id_paciente                                  
''')
            
            if consulta:
                return True, consulta
            else:
                return False, None
        except Exception as e:
            print('Erro: ', e)
            self.db.desconectar()
            return False, None

    def adicionar_internacoes(self, id_paciente, data_entrada, data_saida, quarto, diagnostico):
        if id_paciente and quarto:
            try:
                consultar = self.db.consultar('select * from pacientes where id_paciente = %s', (id_paciente, ))

                if consultar:
                    dados = {
                        "paciente_id": id_paciente,
                        "data_entrada_int": data_entrada,
                        "data_saida_int": data_saida,
                        "quarto_int": quarto,
                        "diagnostico_int": diagnostico
                    }

                    sql, valores = self.manipular_insert('internacoes', dados)

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

    def atualizar_internacoes(self, id_internacao, data_saida, diagnostico):
        if id_internacao:
            try:
                consultar = self.db.consultar('select quarto_int from internacoes where id_internacao = %s', (id_internacao, ))

                if consultar:
                    dados = {
                        "data_saida_int":data_saida,
                        "diagnostico_int":diagnostico,
                    }

                    sql, valores = self.manipular_update('internacoes', dados, 'id_internacao')
                    valores.append(id_internacao)
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

        