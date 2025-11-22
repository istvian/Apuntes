# import json
import requests
from database2 import *

respuesta = requests.get("http://localhost/tarea/conecta.php") # Te esta obteniendo el contenido de la tabla 1 a través del php


class Master:
    def __init__(self, numEtapa, nomJugador, puntosJugador):
        self.numEtapa = numEtapa
        self.nomJugador = nomJugador
        self.puntosJugador = puntosJugador

    def insertar(self, numEtapa, nomJugador, puntosJugador): # agregando el item en la tabla 2 (en este caso es master)
        sql1 = "select numEtapa from master where numEtapa=" + repr(numEtapa)
        try:
            db.cursor.execute(sql1)
            if db.cursor.fetchone() == None:  # valida que el número de fact. no exista
                sql2 = (
                    "insert into master values("
                    + repr(numEtapa)
                    + ","
                    + repr(nomJugador)
                    + ","
                    + repr(puntosJugador)
                    + ")"
                )
                try:
                    db.cursor.execute(sql2)
                    db.conexion.commit()
                except Exception as err:
                    db.conexion.rollback()
                    print(err)
            else:
                print("Ya existe ese número de etapa")
        except Exception as err:
            print(err)


lista :list[Master]= []
db = Database() # Este es el nombre de la clase dentro del archivo database2.py

for item in respuesta.json():
    lista.append(Master(item["CODETAPA"], item["NOMBREJUGADOR"], item["PUNTAJE"]))
    # llena el objeto lista con los datos desearializados
print("{:10}{:12}{:12}".format("Num Etapa", "Nombre Jugador", "Puntaje"))
for itemLista in lista:
    print("{:10}{:12}{:12}".format(itemLista.numEtapa, itemLista.nomJugador, itemLista.puntosJugador))
    itemLista.insertar(itemLista.numEtapa, itemLista.nomJugador, itemLista.puntosJugador)