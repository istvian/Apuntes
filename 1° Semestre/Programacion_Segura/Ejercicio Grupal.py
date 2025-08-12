"""
Leer dos niveles de voltaje.
Aumentar en un 10% el primer voltaje.  Disminuir en un 5% el segundo voltaje.
Sumar ambos voltajes actualizados. Si esta suma es mayor a 10 escribir ‘El total excede en',<aquí va la diferencia entre 10 y el total> sino escribir 'Buen total'
"""

voltaje_1 = float(input("Ingrese voltaje 1: "))
voltaje_2 = float(input("Ingrese voltaje 2: "))
voltaje_1 = voltaje_1 * 1.10
voltaje_2 = voltaje_2 * 0.95
# print(voltaje_1)
# print(voltaje_2)
total = voltaje_1 + voltaje_2
# print(total)
if total > 10:
    # para que no quede en negativo total -10 | si no 10- total
    print("El total excede en", total - 10)
else:
    print("Buen total")
