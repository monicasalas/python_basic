''''
Generar mediante la libreria de datetime la fecha del día de hoy
'''
#Importo la libreria datetime
import datetime

a= 'hola'
A = 'Mundo'
a = 6
a = 7.1
a = False
print(a)

#Obtiene el valor del día de hoy
hoy=datetime.datetime\
    .now().day
print(hoy)

#Formateando Strings

nombre= 'Mónica'
apellido='Salas'
pais='México'
edad= 27

print('Mi nombre completo es:{} {} '.format(nombre, apellido))

#Ejemplo 1
texto_a= 'Hola QA, mi nombre es: {} y soy de: {} y tengo {} años'.format(nombre,pais, edad)
print(texto_a)

#Ejemplo 2
texto_a = f'Hola QA Minds, mi nombre es: {nombre} y soy de: {pais} y tengo {edad} años'
print(texto_a)

#Ejemplo 3
texto_a = 'Hola QA Minds, mi nombre es %s y soy de: %s y tengo %s años' %(nombre, pais, edad)
print(texto_a)

#Ejemplo 4
texto_a = 'Hola QA Minds, mi nombre es: '+nombre+' y soy de: '+pais+ 'y tengo '+str(edad)+' años'
print(texto_a)


#Tipos de datos Condicionales

#Ejemplo 1
billetera = 100
agua = 100
compra_exitosa = billetera > agua
print(compra_exitosa)

#Operadores relacionales
'''
Hacen referencia a memoria
is -> valor
is not -> es la negación
'''
#Ejemplo
var_a=2
var_b= var_a
print(var_a is var_b)
print(var_a is not var_b)


valor_1= 2
valor_2=4.1
valor_3 = 'Hola'
valor_4= None
valor_5=True
print("-----------------Ejercio C--------------")
print(valor_1 is valor_2)
print(valor_1 == valor_2)
#print(valor_1 < valor_3)
print(valor_1 != valor_2)
print(valor_1 > valor_2)
print(valor_1 >= valor_5)
print(0 == valor_4)
print(1 == valor_4)
print(valor_4 is None)
print(isinstance(valor_2,int)) 

print("----------------------------------------")






