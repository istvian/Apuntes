from datetime import *


def input_and_validate(text, type="text", lower=False):
    data = ""
    while data =="":
        try:
            if type == "int":
                data = int(input(text))
                while data == "":
                    data = int(input("Ingrese un valor, " + text))
            elif type == "float":
                data = float(input(text))
                while data == "":
                    data = float(input("Ingrese un valor, " + text))
            elif type == "date":
                while True:
                    nueva = input(text)
                    try:
                        fecha = datetime.strptime(nueva, "%d/%m/%Y")  # Convierte a fecha
                        break
                    except ValueError:
                        print("Error de fecha")
                data = nueva

            else:
                data = input(text)
                while data == "":
                    data = input("Ingrese un valor, " + text)
        except ValueError:
            print("Valor no válido")
    if lower:
        return data.lower()
    else:
        return data