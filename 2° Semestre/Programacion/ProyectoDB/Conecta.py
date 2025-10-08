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
