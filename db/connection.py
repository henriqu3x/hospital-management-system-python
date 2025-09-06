import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

class Connection():
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.conn = None
        self.cur = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(database=self.database,
                                        user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port)
            
            self.cur = self.conn.cursor()

        except Exception as e:
            print('Erro: ', e)
            self.desconectar()

    def desconectar(self):
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print('Erro ao desconectar: ', e)

    def consultar(self, sql, variaveis=None):
        try:
            self.conectar()

            if variaveis:
                self.cur.execute(sql, variaveis)
            else:
                self.cur.execute(sql)

            result =self.cur.fetchall()

            return result
        except Exception as e:
            print('Erro: ', e)
            return False
        finally:
            self.desconectar()

    def manipular(self, sql, variaveis=None):
        try:
            self.conectar()

            if variaveis:
                self.cur.execute(sql, variaveis)
            else:
                self.cur.execute(sql)
            
            self.conn.commit()
            print('SQL EXECUTADO COM SUCESSO!')
            return True
        except Exception as e:
            print('Erro: ', e)
            return False
        finally:
            self.desconectar()
        
db = Connection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
print(db.consultar('select version()'))