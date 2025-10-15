from Database import *
from Validar import *

db = Database()

while True:
    print("\033c", end="")
    elige = input(
        "\nElija una opción:\n\
                  \tMostrar un repuesto(u)\n\
                  \tMostrar todos los repuestos(t)\n\
                  \tMostrar una venta(v)\n\
                  \tMostrar todas las ventas(vv)\n\
                  \tInsertar repuesto (i)\n\
                  \tModificar repuesto (m)\n\
                  \tEliminar repuesto (d)\n\
                  \tInsertar venta (iv)\n\
                  \tModificar venta (mv)\n\
                  \tEliminar venta (dv)\n\
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
    elif elige == "m":
        db.modificar()
    elif elige == "d":
        db.eliminar()
    elif elige == "dv":
        db.eliminar_venta()
    elif elige == "mv":
        db.modificar_venta()
    elif elige == "iv":
        db.insertar_venta()
    elif elige == "f":
        print("Fin")
        db.cerrarDB()
        break
    else:
        print("Error de opción")

    input("Pulse Enter para continuar...")
