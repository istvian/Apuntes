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

    def select_uno(self, cod):
        sql = "select * from repuestos where codrep=" + repr(cod)
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep != None:
                print(
                    f"{'Codigo':10}{'Nombre rep.':20}{'Fecha fabr.':12}\
                      {'Precio prov.':12}{'Precio ven.':12}{'Peso':12}"
                )
                print(
                    f"{rep[0]:10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}\
                        {rep[3]:<12}{rep[4]:<12}{rep[5]:<12}"
                )
            else:
                print("Código no existe")
        except Exception as err:
            print(err)

    def venta_todos(self):
        sql = "SELECT * FROM VENTAS"
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print(
                f"{'NúmVenta':10}{'Cod repuesto':20}{'Fecha vent.':12}\
                  {'Monto vent':12}"
            )
            for rep in repu:
                print(
                    f"{rep[0]:<10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}\
                      {rep[3]:<12}"
                )
                # print(rep)
        except Exception as err:
            print(err)

    def venta_uno(self, numVenta):
        sql = "select * from VENTAS where numVenta=" + repr(numVenta)
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep != None:
                print(
                    f"{'NúmVenta':10}{'Cod repuesto':20}{'Fecha vent.':12}\
                  {'Monto vent':12}"
                )
                print(
                    f"{rep[0]:<10}{rep[1]:20}{rep[2].strftime('%d/%m/%Y'):12}\
                      {rep[3]:<12}"
                )
            else:
                print("Código no existe")
        except Exception as err:
            print(err)
