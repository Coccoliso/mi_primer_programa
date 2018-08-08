
mi_lista = []

input_usuario = ""


while input_usuario != "FIN":
    input_usuario = input("¿Que necesitas comprar? (escribe FIN para salir): ")
    if input_usuario != "FIN":
        mi_lista.append(input_usuario)


#largo_lista = len(mi_lista)
#ndice_actual = 0

#while indice_actual < largo_lista:
#    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
#   indice_actual += 1

#Este codigo simplifica el while de arriba por cada item de la lista el for ejecuta el codigo de dentro# .

for item in mi_lista:
    print("Tengoo que comprar {}".format(item))


print("Esta es la lista de la compra")
