# ESTRUCTURAS PROGRAMATICAS CONDICIONALES

# if <consulta> : => dos puntos significa inicio de bloque de código
# --->acción      => El espacio se llama indentación


# SE PIDE INGRESAR EL PRECIO, SI ES MAYOR A 10.000 SE CALCULA EL 6% DE DESCUENTO
def Ejemplo1():
    precio = int(input("Ingrese precio= "))
    if precio > 10000:
        descuento = precio * 0.06
        print("Descuento del 6%:", descuento)
    print("if finalizado")


# FIN EJEMPLO 1

from time import sleep


# SE PEDIRA EL PESO DE UNA ENCOMIENDA, SI EL PESO ES MAYOR A 40.5 ESCRIBIR NIVEL 2
def Ejemplo2():
    peso_encomienda = float(input("Ingrese peso de encomienda= "))
    print("Calculando...")
    sleep(1)  # Genera una pausa
    if peso_encomienda > 40.5:
        print("Nivel 2")
    print("Fin")


def EjercicioPropuesto():
    monto = 10000000  # asigna el monto
    venta_1 = int(input("Ingrese venta 1: "))  # ingresa 1er valor
    venta_2 = int(input("Ingrese venta 2: "))  # ingresa 2do valor
    venta_3 = int(input("Ingrese venta 3: "))  # ingresa 3er valor
    resultado_1 = venta_1 * 0.32  # calcula el 32%
    resultado_2 = venta_2 * 0.35  # calcula el 35%
    resultado_3 = venta_3 * 0.33  # calcula el 33%
    total = resultado_1 + resultado_2 + resultado_3  # suma los 3 calculos
    if total < monto:  # compara si el total es menor al monto
        # print(total)
        print("Hay un deficit de", round(monto - total))  # imprime


def IfDobleEjemplo1():
    numero = int(input("Ingresa un número entero= "))
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def IfDobleEjemplo2():
    valor = 80000
    monto_1 = int(input("Ingrese monto 1: "))
    monto_2 = int(input("Ingrese monto 2: "))
    total = monto_1 + monto_2
    resultado = total * 1.19
    if resultado <= valor:
        print("Bajo monto")
    else:
        print("El resultado excede a {} en {}".format(valor, resultado - valor))


# Ejemplo1()
# Ejemplo2()
# EjercicioPropuesto()
# IfDobleEjemplo1()
IfDobleEjemplo2()
