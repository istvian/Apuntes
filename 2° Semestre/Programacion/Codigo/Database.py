import pymysql
from Validar import *
from datetime import *


class Database:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost", user="root", password="12345678", database="conciertos"
        )
        self.cursor = self.conexion.cursor()

    def cerrarDB(self):
        self.cursor.close()
        self.conexion.close()

    def insertar_asistentes(self):
        id = input_and_validate("Ingrese idAsistente=")
        sql1 = "Select idAsistente from Asistentes where idAsistente=" + repr(id)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                email = input_and_validate("Ingrese email=")
                edad = input_and_validate("Ingrese edad=", "int")
                codConcierto = input_and_validate("Ingrese código de concierto=", "int")
                sql_check = (
                    "SELECT CODCONCIERTO from CONCIERTOS WHERE CODCONCIERTO= "
                    + repr(codConcierto)
                )
                try:
                    self.cursor.execute(sql_check)
                    if self.cursor.fetchone() != None:
                        sql2 = (
                            "insert into asistentes values ("
                            + repr(id)
                            + ","
                            + repr(email)
                            + ","
                            + repr(edad)
                            + ","
                            + repr(codConcierto)
                            + ")"
                        )
                        try:
                            self.cursor.execute(sql2)
                            self.conexion.commit()
                            print("Se ha insertado correctamente")
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                    else:
                        print("No existe el codConcierto")
                except:
                    print("No existe codConcierto")

            else:
                print("El código de asistente ya existe")
        except Exception as err:
            print(err)

    def modificar_asistentes(self):
        codR = input_and_validate("Ingrese id asistente=")
        sql1 = "select * from asistentes where idAsistente=" + repr(codR)
        try:
            self.cursor.execute(sql1)
            asis = self.cursor.fetchone()
            if asis != None:
                print(
                    f"{'idAsistente':10}{'email':20}{'edad.':12}\
                  {'codConcierto':12}"
                )
                print(
                    f"{asis[0]:<10}{asis[1]:20}{asis[2]:12}\
                      {asis[3]:<12}"
                )
                elige = input_and_validate(
                    "\n¿Qué desea modificar? email(e), edad(ed), codConcierto(c))=",
                    lower=True,
                )
                if elige == "c":
                    newCodConcierto = input_and_validate(
                        "Ingrese nuevo codConcierto=", "int"
                    )
                    sql_check = (
                        "SELECT CODCONCIERTO from CONCIERTOS WHERE CODCONCIERTO= "
                        + repr(newCodConcierto)
                    )
                    self.cursor.execute(sql_check)
                    if self.cursor.fetchone() == None:
                        print("Código no existe ingrese uno valido")
                    else:
                        sql2 = (
                            "update asistentes set codConcierto="
                            + repr(newCodConcierto)
                            + " where idAsistente="
                            + repr(codR)
                        )
                        try:
                            self.cursor.execute(sql2)
                            self.conexion.commit()
                            print("Se ha modificado correctamente")
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                else:
                    if elige == "e":
                        campo = "email"
                        nuevo = input_and_validate("Ingrese nuevo email=")
                    if elige == "ed":
                        campo = "edad"
                        nuevo = input_and_validate("Ingrese nueva edad=")
                    sql3 = (
                        "update asistentes set "
                        + campo
                        + "="
                        + repr(nuevo)
                        + " where idAsistente ="
                        + repr(codR)
                    )
                    try:
                        self.cursor.execute(sql3)
                        self.conexion.commit()
                        print("Se ha modificado correctamente")
                    except Exception as err:
                        self.conexion.rollback()
                        print(err)
            else:
                print("No existe ese código")
        except Exception as err:
            print(err)

    def todos_asistentes(self):
        sql = "SELECT * FROM ASISTENTES"
        try:
            self.cursor.execute(sql)
            asistentes = self.cursor.fetchall()
            print(
                f"{'idAsistente':20}{'email':20}{'edad.':12}\
                      {'codConcierto':12}"
            )
            for asis in asistentes:
                print(
                    f"{asis[0]:<20}{asis[1]:<20}{asis[2]:<12}\
                          {asis[3]:<12}"
                )
        except Exception as err:
            print(err)

    def insertar_conciertos(self):
        codConciertos = input_and_validate("Codigo del concierto=", "int")
        sql1 = "Select codConcierto from Conciertos where codConcierto=" + repr(
            codConciertos
        )
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                precio = input_and_validate("precio=", "int")
                fecha = input_and_validate("Fecha de Concierto(dd/mm/aaaa)=", "date")
                ciudad = input_and_validate("Ciudad de concierto=")
                sql2 = (
                    "insert into conciertos values ("
                    + repr(codConciertos)
                    + ","
                    + repr(precio)
                    + ", str_to_date("
                    + repr(fecha)
                    + ",'%d/%m/%Y'),"
                    + repr(ciudad)
                    + ")"
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                    print("Se ha insertado correctamente")

                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No se puede insertar, código ya existe")
        except Exception as err:
            print(err)

    def eliminar_concierto(self):
        codConciertos = input_and_validate("Código=")
        sql1 = "select * from conciertos where codConcierto=" + repr(codConciertos)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                sql3 = "delete from conciertos where codConcierto=" + repr(
                    codConciertos
                )
                try:
                    self.cursor.execute(sql3)
                    self.conexion.commit()
                    print("Se ha eliminado correctamente")
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe ese código")
        except Exception as err:
            print(err)

    def mostrar_concierto(self):
        codConciertos = input_and_validate("Ingrese código de concierto=")
        sql = "select * from Conciertos where codConcierto=" + repr(codConciertos)
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep != None:
                print(
                    f"{'Codigo':10}{'Precio.':20}{'FechaConc.':12}\
                      {'Ciudad.':12}"
                )
                print(
                    f"{rep[0]:<10}{rep[1]:<20}{rep[2].strftime('%d/%m/%Y'):12}\
                        {rep[3]:<12}"
                )
            else:
                print("El concierto no existe o no se ha realizado")
        except Exception as err:
            print(err)

    def mostrar_concierto_rango(self):
        desde = input_and_validate("Ingrese precio desde=")
        hasta = input_and_validate("Ingrese precio hasta=")
        sql = (
            "select * from Conciertos where precio between"
            + repr(desde)
            + " and "
            + repr(hasta)
        )
        try:
            self.cursor.execute(sql)
            conciertos = self.cursor.fetchall()
            if conciertos != None:
                print(
                    f"{'Codigo':10}{'Precio.':20}{'FechaConc.':12}\
                      {'Ciudad.':12}"
                )
                for conc in conciertos:
                    print(
                        f"{conc[0]:<10}{conc[1]:<20}{conc[2].strftime('%d/%m/%Y'):12}\
                        {conc[3]:<12}"
                    )
            else:
                print("El concierto no existe o no se ha realizado")
        except Exception as err:
            print(err)

    def mostrar_asistente_letra(self):
        inicial = input_and_validate("Ingrese inicial de correo=")
        sql = "select * from asistentes where email like" + repr(inicial) + '"%"'
        try:
            self.cursor.execute(sql)
            asistentes = self.cursor.fetchall()
            if asistentes != None:
                print(
                    f"{'idAsistente':20}{'email':20}{'edad.':12}\
                      {'codConcierto':12}"
                )
                for asis in asistentes:
                    print(
                        f"{asis[0]:<20}{asis[1]:<20}{asis[2]:<12}\
                          {asis[3]:<12}"
                    )
            else:
                print("No hay asistentes")
        except Exception as err:
            print(err)
