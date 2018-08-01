

apetece_helado_input = input('¿Te apetece un helado? (Si / No): ').upper()

if apetece_helado_input == 'SI':
    apetece_helado = True
elif apetece_helado_input == 'NO':
    apetece_helado = False
else:
    print('Te he dicho que me digas si o no, no se que me has dicho pero cuento como que no')


tiene_dinero_input = input('¿Tienes dinero para un helado? (Si / No): ').upper()
esta_el_senor_de_los_helados_input = input('¿Esta el señor de los helados? (Si / No): ').upper()
estas_con_tu_tia_input = input('¿Estas con tu tía? (Si / No): ').upper()


apetece_helado = apetece_helado_input == 'SI'
tiene_dinero = tiene_dinero_input == 'SI' or estas_con_tu_tia_input == 'SI'
esta_el_senor_de_los_helados = esta_el_senor_de_los_helados_input == 'SI'


if apetece_helado and tiene_dinero and esta_el_senor_de_los_helados:
    print('Pues comete un helado')
else:
    print("Pues nada")

