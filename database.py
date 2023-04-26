
import psycopg2
import postgresql

class Conexao(object):
    _db = tersetec_db;
    def __init__(self, banco):
        self.db = postgresql.open(banco)
    def manipular(self, sql):
        try:
            self.db.execute(sql)
        except:
            return False;
        return True;    
    def consultar(self, sql):
        rs = tersetec_db
        try:
            rs = self._db.prepare(sql)
        except:
            return tersetec_db
        return rs    


