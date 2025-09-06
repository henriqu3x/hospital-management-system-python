class ManipulacaoDAO():
    def __init__(self):
        pass

    def manipular_insert(self, tabela, dados):
        campos = []
        valores = []
        for campo, valor in dados.items():
            if valor not in ('', None, ' '):
                campos.append(campo)
                valores.append(valor)

        sql = f'''
    insert into {tabela} ({', '.join(campos)}) values
    ({', '.join(['%s'] * len(valores))})
'''
        return sql, valores
    
    def manipular_update(self, tabela, dados, where):
        campos = []
        valores = []

        for campo, valor in dados.items():
            if valor not in ('', None, ' '):
                campos.append(f'{campo} = %s')
                valores.append(valor)

        sql = f'''
    update {tabela} set {', '.join(campos)} where {where} = %s
'''
        return sql, valores