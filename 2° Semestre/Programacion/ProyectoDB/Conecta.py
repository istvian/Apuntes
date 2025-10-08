from Database import *
from Validar import *

db = Database()

while True:
    print("\033c", end="")
    elige = input(
        "\nElija una opción:\n\
                  \tMostrar un repuesto(u)\n\
                  \tMostrar todos los repuestos(t)\n\
                  \tMostrar todas las ventas(vv)\n\
                  \tMostrar una venta(v)\n\
                  \tInsertar repuesto (i)\n\
                  \tFin(f)\n\
                  \t=>".lower()
    )
    if elige == "u":
        # codABuscar = input("Ingrese código a buscar=")
        codABuscar = input_and_validate("Ingrese código a buscar=")
        db.select_uno(codABuscar)
    elif elige == "t":
        db.select_todos()
    elif elige == "vv":
        db.venta_todos()
    elif elige == "v":
        codABuscar = input_and_validate("Ingrese código a buscar=")
        db.venta_uno(codABuscar)
    elif elige == "i":
        db.insertar()
    elif elige == "f":
        print("Fin")
        db.cerrarDB()
        break
    else:
        print("Error de opción")

    input("Pulse Enter para continuar...")
