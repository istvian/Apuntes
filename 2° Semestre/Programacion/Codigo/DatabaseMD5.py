import pymysql
from tabulate import tabulate
from pwinput import pwinput
from hashlib import md5
from Conecta import *
from Validar import *


class DatabaseMD5:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost", user="root", password="12345678", database="conciertos"
        )
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    def login(self):
        nombre = input("Ingrese nombre del usuario=")
        while nombre == "":
            nombre = input("Ingrese nombre del usuario=")
        password = pwinput("Ingrese password=")
        while password == "":
            password = pwinput("Ingrese password=")
        passwordEnc = md5(password.encode("utf-8")).hexdigest()
        return nombre, passwordEnc

    def crearUsuario(self):
        nom, passw = self.login()
        sql1 = "SELECT * FROM USUARIOS WHERE NOMBRE= " + repr(nom)
        try:
            self.cursor.execute(sql1)
            result = self.cursor.fetchone()
            if result == None:
                sql2 = (
                    "INSERT INTO USUARIOS VALUES(" + repr(nom) + "," + repr(passw) + ")"
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()  # confirma la ejecución de mysql
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("Ya existe ese usuario")
        except Exception as err:
            print(err)

    def ingresar(self):
        nom, passw = self.login()
        sql1 = (
            "SELECT * FROM USUARIOS WHERE NOMBRE= "
            + repr(nom)
            + " and password="
            + repr(passw)
        )
        try:
            self.cursor.execute(sql1)
            result = self.cursor.fetchone()
            if result != None:
                # aqui debe ir el del menu completo de su certamen 2
                Menu()
            else:
                print("Usuario no existe")
        except Exception as err:
            print(err)
