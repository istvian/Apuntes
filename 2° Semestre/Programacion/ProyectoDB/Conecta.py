from Database import *

db = Database()

while True:
    print("\033c", end="")
    elige = input(
        "\nElija una opción:\n\
                  \tMostrar un repuesto(u)\n\
                  \tMostrar todos los repuestos(t)\n\
                  \tFin(f)\n\
                  \t=>".lower()
    )
    if elige == "u":
        codABuscar = input("Ingrese código a buscar=")
        db.select_uno(codABuscar)
    elif elige == "t":
        db.select_todos()
    elif elige == "f":
        print("Fin")
        db.cerrarDB()
        break
    else:
        print("Error de opción")

    input("Pulse Enter para continuar...")
