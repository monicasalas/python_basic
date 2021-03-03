'''
numero = 25
numero //=4
print(numero)

numero = 10
numero %= 2
print(numero)


number = 7
suma=0
control=0
while number >= control:
    suma += number
print(f'Resultado {suma}')


Escribe un script que dado un numero permita calcular la sumatoria de todos los numeros pares que lo proceden desde cero
numero = 5
resultado = 2+4

numero = 9
control = 0
suma = 0
while control <= numero:
    mod=control%2
    if mod == 0:
        suma += control
    control+=1
print(suma)


numero_a = 8
numero_b = 5
#reusltado = 6, 7

control = 0
while numero_b < numero_b:
    dato = numero_b += 1
    print(f '{dato} + {dato}')

#Sol

numero_a = 9
numero_b = 3
numero = ''
numero_b +=1
num_max=0
num_min=0

if numero_a > numero_b:
    num_max = numero_a
    num_min = numero_b
else:
    num_max = numero_b
    num_min = numero_a

while num_min < num_max:
    numero += '{}, '.format(num_min)
    num_min +=1
print('los numeros son: {}'.format(numero))

import random
intento = 1
numero = random.randint(0,10)
print(numero)
my_value = int(input('Ingrese un numero:' ))

while my_value != numero:
    my_value = int(input('Ingrese un numero:' ))
    intento += 1
print(f'Hiciste {int(intento)} intentos')


for number in range(0,10, 2):
    print(number)

'''
import random
numero = random.randint(0,10)
print(f'Tabla del {numero}')
for val in range(1,11):
    oper = val * numero
    print(f'{val} X {numero} = {oper}')