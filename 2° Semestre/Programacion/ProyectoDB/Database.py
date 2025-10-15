import pymysql
from Validar import *
from datetime import *


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

    def insertar(self):
        codR = input_and_validate("Código=")
        sql1 = "Select codrep from repuestos where codrep=" + repr(codR)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                nomR = input_and_validate("Nombre=")
                fechaF = input_and_validate(
                    "Fecha de Fabricación (dd/mm/aaaa)=", "date"
                )
                precioProv = input_and_validate("Precio de Proveedor=", "int")
                precioVen = input_and_validate("Precio de Venta=", "int")
                peso = input_and_validate("Peso(kg)=", "float")
                sql2 = (
                    "insert into repuestos values ("
                    + repr(codR)
                    + ","
                    + repr(nomR)
                    + ", str_to_date("
                    + repr(fechaF)
                    + ",'%d/%m/%Y'),"
                    + repr(precioProv)
                    + ","
                    + repr(precioVen)
                    + ","
                    + repr(peso)
                    + ")"
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()

                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No se puede insertar, código ya existe")
        except Exception as err:
            print(err)

    def insertar_venta(self):
        codR = input_and_validate("Código=")
        sql1 = "Select codrep from repuestos where codrep=" + repr(codR)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                numVenta = input_and_validate("Num. Venta=", "int")
                fechaVenta = input_and_validate("Fecha de Venta (dd/mm/aaaa)=", "date")
                montoVenta = input_and_validate("Monto de venta=", "int")
                sql2 = (
                    "insert into ventas values ("
                    + repr(numVenta)
                    + ","
                    + repr(codR)
                    + ", str_to_date("
                    + repr(fechaVenta)
                    + ",'%d/%m/%Y'),"
                    + repr(montoVenta)
                    + ")"
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()

                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("Ingrese un código de repuesto que exista")
        except Exception as err:
            print(err)

    def eliminar(self):
        codR = input_and_validate("Código=")
        sql1 = "select * from repuestos where codrep=" + repr(codR)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                sql2 = "select * from ventas where codrepuesto=" + repr(codR)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchone() != None:
                        print("No se puede eliminar, porque está en la tabla Ventas")
                    else:
                        sql3 = "delete from repuestos where codrep=" + repr(codR)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                            print("Repuesto eliminado")
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print("No existe ese código")
        except Exception as err:
            print(err)

    def eliminar_venta(self):
        numVenta = input_and_validate("Código=")
        sql1 = "select * from ventas where numVenta=" + repr(numVenta)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                sql2 = "delete from ventas where numVenta =" + repr(numVenta)
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                    print("Venta eliminada")
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe ese número de venta")
        except Exception as err:
            print(err)

    def modificar(self):
        codR = input_and_validate("Código=")
        sql1 = "select * from repuestos where codrep=" + repr(codR)
        try:
            self.cursor.execute(sql1)
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
                elige = input_and_validate(
                    "\n¿Qué desea modificar? (nombre(n), fecha fabr.(f), precio prov.(p), precio venta(v), peso(k))=",
                    lower=True,
                )
                if elige == "f":
                    nueva = input_and_validate(
                        "Ingrese una fecha (dd/mm/aaaa)=", "date"
                    )
                    sql2 = (
                        "update repuestos set fechafabr=str_to_date("
                        + repr(nueva)
                        + ",'%d/%m/%Y') where codrep="
                        + repr(codR)
                    )
                else:
                    if elige == "n":
                        campo = "nomrep"
                        nuevo = input_and_validate("Ingrese nuevo nombre=")
                    if elige == "p":
                        campo = "precioproveedor"
                        nuevo = input_and_validate(
                            "Ingrese nuevo precio de proveedor=", "int"
                        )
                    if elige == "v":
                        campo = "precioventa"
                        nuevo = input_and_validate(
                            "Ingrese nuevo precio de venta=", "int"
                        )
                    if elige == "k":
                        campo = "peso"
                        nuevo = input_and_validate("Ingrese nuevo peso=", "int")

                    sql2 = (
                        "update repuestos set "
                        + campo
                        + "="
                        + repr(nuevo)
                        + " where codrep ="
                        + repr(codR)
                    )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe ese código")
        except Exception as err:
            print(err)

    def modificar_venta(self):
        codR = input_and_validate("Ingrese número de venta=")
        sql1 = "select * from ventas where numventa=" + repr(codR)
        try:
            self.cursor.execute(sql1)
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
                elige = input_and_validate(
                    "\n¿Qué desea modificar? fecha venta(f), monto vent.(m), codigo rep(c))=",
                    lower=True,
                )
                if elige == "f":
                    nueva = input_and_validate(
                        "Ingrese una fecha (dd/mm/aaaa)=", "date"
                    )
                    sql2 = (
                        "update ventas set fechaVenta=str_to_date("
                        + repr(nueva)
                        + ",'%d/%m/%Y') where numVenta="
                        + repr(codR)
                    )
                else:
                    if elige == "m":
                        campo = "montoVenta"
                        nuevo = input_and_validate("Ingrese nuevo monto=", "int")
                    if elige == "c":
                        campo = "codRepuesto"
                        nuevo = input_and_validate("Ingrese nuevo codigo repuesto=")
                        sqlCheck = "select * from repuestos where codRep =" + repr(
                            nuevo
                        )
                        self.cursor.execute(sqlCheck)
                        res = self.cursor.fetchone()
                        if res == None:
                            raise ValueError("Codigo repuesto no existe")
                    sql2 = (
                        "update ventas set "
                        + campo
                        + "="
                        + repr(nuevo)
                        + " where numVenta ="
                        + repr(codR)
                    )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe ese código")
        except Exception as err:
            print(err)
