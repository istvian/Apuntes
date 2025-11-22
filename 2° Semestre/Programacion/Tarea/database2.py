import pymysql  #antes pip install pymysql
class Database:
    def __init__(self):
        self.conexion=pymysql.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='videojuegos'
        )
        self.cursor=self.conexion.cursor()