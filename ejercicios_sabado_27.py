'''
dinero_disponible=200
chocolate = 150
agua=100
print(f'Tú dinero {dinero_disponible}')
dinero_disponible=dinero_disponible-chocolate
print(f'Compraste chocolate \nCosto {chocolate} \nTú cambio es:{dinero_disponible}')
dinero_disponible=dinero_disponible-agua 
print (f'Comparar agua {dinero_disponible}')


#Ejercicio Condicional 1

primavera= (3, 4, 5)
verano= (6,7,8)
otonio=(9,10,11)
invierno=(12,1,2)
mes=1
if mes in primavera:
    print("Estación PRIMAVERA")
elif mes in verano:
    print("Estación VERANO")
elif mes in otonio:
    print("Estación Otoño")
elif mes in invierno:
    print("Estación IVNIERNO")
else:
    print("No pertenece a una estación")

#Ejercicio 2

edad_perm = 14
estatura_perm = 1.62

edad=11
altura = 1.21
if altura >= estatura_perm and edad >= edad_perm:
    print("Puedes subirte a 'PUSH-PULL'")
elif altura >= estatura_perm or edad >=edad_perm:
    print("No puedes subirte pues No tienes edad suficiente")
elif altura >= estatura_perm or edad >=edad_perm:
    print("No puedes subirte pues No tienes estatura suficiente")
else:
    print("Lo sentimos 'NO PUEDES SUBIRTE A PUSH-PULL' \nPor tu edad ni estatura")
'''

#Ejercicio 3



