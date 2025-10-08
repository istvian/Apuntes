import pymysql


class Database:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost", user="root", password="12345678", database="empresa"
        )
        self.cursor = self.conexion.cursor()

    def cerrarDB(self):
        self.cursor.close()
        self.conexion.close()

    def select_todos(self):
        sql = "SELECT * FROM REPUESTOS"
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print(
                f"{'Codigo':10}{'Nombre rep.':20}{'Fecha fabr.':12}\
                  {'Precio prov.':12}{'Precio ven.':12}{'Peso':12}"
            )
            for rep in repu:
                print(
                    f"{rep[0]:10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}\
                      {rep[3]:<12}{rep[4]:<12}{rep[5]:<12}"
                )
                # print(rep)
        except Exception as err:
            print(err)
