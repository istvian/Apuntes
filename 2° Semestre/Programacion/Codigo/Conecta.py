from Database import *
from Validar import *

db = Database()


def Menu():
    while True:
        print("\033c", end="")
        opcion_menu = input_and_validate(
            "\nElija una opción:\n"
            "\tMenu Asistentes (a)\n"
            "\tMenu Conciertos (c)\n"
            "\tSalir (s)\n"
            "\tIngrese opción=",
            lower=True,
        )
        if opcion_menu == "a":
            while True:
                print("\033c", end="")
                opcion_asistente = input_and_validate(
                    "\nMenu Asistentes:\n"
                    "\tInsertar asistentes (i)\n"
                    "\tModificar asistentes (m)\n"
                    "\tMostrar todos los asistentes (t)\n"
                    "\tMostrar asistentes que empiecen por x letra en mail (x)\n"
                    "\tVolver (v)\n"
                    "\tIngrese opción="
                )
                if opcion_asistente == "i":
                    db.insertar_asistentes()
                elif opcion_asistente == "m":
                    db.modificar_asistentes()
                elif opcion_asistente == "t":
                    db.todos_asistentes()
                elif opcion_asistente == "x":
                    db.mostrar_asistente_letra()
                elif opcion_asistente == "v":
                    break
                input("Presione una tecla para continuar...")
        elif opcion_menu == "c":
            while True:
                print("\033c", end="")
                opcion_concierto = input_and_validate(
                    "\nMenu Conciertos:\n"
                    "\tInsertar conciertos(i)\n"
                    "\tEliminar conciertos (e)\n"
                    "\tMostrar un concierto(c)\n"
                    "\tMostrar conciertos en un rango de precio indicado por teclado(p)\n"
                    "\tVolver(v)\n"
                    "\tIngrese opción="
                )
                if opcion_concierto == "i":
                    db.insertar_conciertos()
                elif opcion_concierto == "e":
                    db.eliminar_concierto()
                elif opcion_concierto == "c":
                    db.mostrar_concierto()
                elif opcion_concierto == "p":
                    db.mostrar_concierto_rango()
                elif opcion_concierto == "v":
                    break
                input("Presione una tecla para continuar...")
        elif opcion_menu == "s":
            print("Cerrando programa")
            break
        else:
            print("La opción no es valida")
