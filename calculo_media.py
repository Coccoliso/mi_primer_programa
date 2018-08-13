
numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 6:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("¡Numero añadido!")

numero_elementos = 0
sumatorio = sum(numeros_usuario)

for numero in numeros_usuario:
    numero_elementos += 1

media = sumatorio / numero_elementos

print("La media de los numeros introducidos por el usuario es de: {}".format(media))