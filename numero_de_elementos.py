
numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 6:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("¡Numero añadido!")

cantidad_elementos = 0

for numero in numeros_usuario:
    cantidad_elementos += 1

print("La cantidad de numeros introducidos por el usuario es de: {}".format(cantidad_elementos))