# EJEMPLO 1

# nombre = input("Ingrese su nombre=")
# print("Su nombre es", nombre)

# EJEMPLO 2

# venta_1 = int(input("Ingrese monto de primera venta="))
# venta_2 = int(input("Ingrese monto de segunda venta="))
# total = venta_1 + venta_2
# total = int(venta_1) + float(venta_2)
# print("El total es:", total)

# EJEMPLO 3

# rut = int(input("Ingrese su rut (sin dígito verificador)="))
# dv = input("Ingrese su dígito verificador=")
# # print("Su rut completo es: ", rut, end="", sep="")
# # print("-", dv, sep="")
# # print("Su rut completo es: ", rut, "-", dv, sep="")
# print("Su rut completo es: " + str(rut) + "-" + dv)

# EJEMPLO 4
# from math import pi

# valor = float(input("Ingrese el valor con decimales: "))
# resultado = valor / pi
# print("El resultado es:", round(resultado, 2))


# EJEMPLO 5
# Ingresar el lado de un cubo y calcular y mostrar su volumen (Pista: El volumen de un cubo es el lado elevado al cubo)
# from math import pow

# lado = float(input("Ingrese el lado de un cubo: "))
# # volumen = lado**3
# volumen = pow(lado, 3)
# print("El volumen es:", volumen)

# EJEMPLO 6
# Ingresar los dos catetos de un triangulo rectangulo. Calcular y mostrar su hipotenusa. (Pista: la hipotenusa es la raiz cuadrada de la suma de los cuadrados de los catetos)
# from math import sqrt, pow

# # test = pow(27, (1 / 3)) Eleva a funcion 1/3. Resultado raiz cubica
# # print(test)
# cat1 = float(input("Ingrese cateto 1: "))
# cat2 = float(input("Ingrese cateto 2: "))
# resultado = sqrt(pow(cat1, 2) + pow(cat2, 2))
# # resultado = sqrt(cat1**2 + cat2**2)
# print("El resultado es: ", round(resultado, 2))

# EJERCICIO 7
# CALCULAR EL MONTO FINAL DE UN AHORRO, APLICANDO INTERES COMPUESTO
# monto_inicial = int(input("Ingrese el monto inicial: "))
# tasa_interes = float(input("Ingrese tasa de interes: "))
# cantidad_de_años = float(input("Ingrese cantidad de años: "))
# monto_final = monto_inicial * (1 + tasa_interes) ** cantidad_de_años
# print("El monto final sera de:", round(monto_final, 2))
