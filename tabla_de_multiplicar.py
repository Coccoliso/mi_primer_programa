
numero_tabla = int(input("De que numero deseas obtener la tabla de multiplicar: "))

#muestra los valores del multiplo 5 al 15
for multiplo in range(5, 16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))

#Calcula si la tabla de multiplicar de un numero es multiplo de 2.
for multiplo in range(1, 11):
    if numero_tabla * multiplo % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))


#Calcula la tabla de multiplicar de un numero empezando por el final.
rango = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplo in rango:
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))
