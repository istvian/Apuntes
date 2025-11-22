# Certamen 3

## Paso 1: Configurar Appserv

- Abrir la consola mysql (Inicio > Appserv > MySql Comand Line Cliente)
- Ejecutar el código

```sql
-- CREAMOS LA BASE DE DATOS
CREATE DATABASE VIDEOJUEGOS; -- crea la base de datos
USE VIDEOJUEGOS; -- usar la base de datos

-- CREAMOS LAS TABLAS
create table JUEGOS(
CODETAPA int(3) not null primary key,
NOMBREJUGADOR varchar(15),
PUNTAJE int(6)
)engine=innodb;

create table MASTER(
NUMETAPA int(3) not null primary key,
NOMJUGADOR varchar(15),
PUNTOSJUGADOR int(6)
)engine=innodb;

-- INSERTAMOS LOS 8 REGISTROS
INSERT INTO JUEGOS VALUES(1,'JUAN1',10);
INSERT INTO JUEGOS VALUES(2,'JUAN2',20);
INSERT INTO JUEGOS VALUES(3,'JUAN3',30);
INSERT INTO JUEGOS VALUES(4,'JUAN4',40);
INSERT INTO JUEGOS VALUES(5,'JUAN5',50);
INSERT INTO JUEGOS VALUES(6,'JUAN6',60);
INSERT INTO JUEGOS VALUES(7,'JUAN7',70);
INSERT INTO JUEGOS VALUES(8,'JUAN8',80);
```

## Paso 2: Crear archivo php

- En la carpeta "C:\AppServ\www" crear una nueva carpeta llamada "tarea" (cualquier nombre)
- Crea un archivo llamado conecta.php

```php
<?php
$host = "localhost";
$user = "root";
$pass = "12345678"; # CAMBIAR CONTRASEÑA 
$dbname = "videojuegos"; # CAMBIAR NOMBRE DE BASE DE DATOS
try {
    $con = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $ex) {
    echo ($ex);
    die($ex->getMessage());
}
$sql1 = "select * from juegos"; # CAMBIAR NOMBRE DE LA TABLA DE ORIGEN
$stmt = $con->prepare($sql1);
$stmt->execute();
$registros = array();
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    $registros[] = $row;
}
print_r(json_encode($registros));
?>
```
## Paso 2.5: Instalar paquetes python

```bash
pip install pymysql
pip install requests
```

## Paso 3: Crear archivo conexión base de datos en python

- Crear el archivo database2.py en una carpeta y copiar esto:

```python
# database2..py
import pymysql  #antes pip install pymysql
class Database:
    def __init__(self):
        self.conexion=pymysql.connect(
            host='localhost',
            user='root',
            password='12345678', # Cambiar este dato segun corresponda
            database='videojuegos' # Cambiar este dato segun corresponda
        )
        self.cursor=self.conexion.cursor()

```

## Paso 4: Crear archivo "conecta2.py" en python

- En la misma carpeta anterior crear el archivo "conecta2.py" y copiar esto:
- Asegurarse que el servicio de apache este en linea (Inicio > Appserv > Apache Start o Apache Restart) o ver en el navegador si funciona el enlace

> [!NOTE]
> En los pc de inacap como hay varios servicios instalados a veces hay que colocar un puerto. ej: localhost:80/... o localhost:8080/

```python
# import json
import requests
from database2 import * # database2 es el nombre del archivo pero sin el .py

respuesta = requests.get("http://localhost/tarea/conecta.php") # Te esta obteniendo el contenido de la tabla 1 a través del php


class Master:
    def __init__(self, numEtapa, nomJugador, puntosJugador): # Constructor
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


lista = []
db = Database()

for item in respuesta.json():
    lista.append(Master(item["CODETAPA"], item["NOMBREJUGADOR"], item["PUNTAJE"]))
    # llena el objeto lista con los datos desearializados
print("{:10}{:12}{:12}".format("Num Etapa", "Nombre Jugador", "Puntaje"))
for itemLista in lista:
    print("{:10}{:12}{:12}".format(itemLista.numEtapa, itemLista.nomJugador, itemLista.puntosJugador))
    itemLista.insertar(itemLista.numEtapa, itemLista.nomJugador, itemLista.puntosJugador)
```