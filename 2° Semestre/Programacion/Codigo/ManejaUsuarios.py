from DatabaseMD5 import *

db = DatabaseMD5()

while True:
    print("\033c", end="")
    elige = input(
        "\nElija:\n\
        Crear un usuario nuevo (c)\n\
        Ingresar a plataforma (i)\n\
        Fin (f)\n=>"
    ).lower()
    if elige == "c":
        db.crearUsuario()
    elif elige == "i":
        db.ingresar()
    elif elige == "f":
        print("Fin")
        db.cerrarBD()
        break
    else:
        print("Opción incorrecta")

    input("Pulse Enter para continuar...")
