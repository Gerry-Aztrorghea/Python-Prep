# 1) Crear una variable que contenga un elemento del conjunto de números enteros
#  y luego imprimir por pantalla si es mayor o menor a cero

numero = 0

if numero > 0:
    print("El numero es mayor que 0")
elif numero < 0:
    print("El numero es menor que 0")
else:
    print("El numero es igual a 0")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

texto = 'hola'
numero_decimal = 6.2

if type(texto) == type(numero_decimal):
    print('Son del mismo timpo')
else:
    print(f'''la variable uno es de tipo: {type(texto)} y la variable dos es 
    de tipo: {type(numero_decimal)} por eso son diferentes''' )

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for numero in range(1,21):
    if numero % 2 == 0:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo 
# a la potencia igual a 3

for numero in range(0,6):
    print(f'el numero {numero} elevado a tercera potencia es: {numero**3}')

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma 
# cantidad de ciclos

valor = 15
for valor in range(valor):
    print(f"El valor es {valor + 1}")

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una
#  variable, sólo si la variable contiene un número entero mayor a 0

numero = 5
factorial = 1
try:
    if numero > 0:
        while numero > 0:
            factorial *= numero
            numero -= 1
        print(f'El factorial es: {factorial}')
    else:
        print(f'el {numero} no se le puede sacar factorial')
except:
    print("Integraste un valor tipo cadena")


# 7) Crear un ciclo for dentro de un ciclo while

n = 0
while n == 0:
    for num in range(5):
        print(num + 1)
        n += 1

# 8) Crear un ciclo while dentro de un ciclo for

numero = 3
for i in range(numero):
    numero = 0
    while numero < 3:
        print('vuelta '+ str(numero))
        numero += 1

# 9) Imprimir los números primos existentes entre 0 y 30
contador = 0

for valor in range(0,31):
    if valor % 2 == 0:
        print(valor)
    contador += 1

print(contador)

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las 
# sentencias break y/ó continue para tal fin

for valor in range(0,31):
    if valor % 2 == 0:
        print(valor)
    else:
        continue 

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos
#  y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

contador1 = 0
for valor in range(0,31):
    if valor % 2 == 0:
        print(valor)
    else:
        continue 

    contador1 += 1
print(contador1)

#  nota --> en el primer ciclo entra todas las veces mientras que en el otro proceso 
#           es mas rapido por que salta ese dato y no entra al contador

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización 
# crece?

print ( ' ')

contador = 0

for valor in range(0,101):
    if valor % 2 == 0:
        print(valor)
    contador += 1

print('========================================' +str(contador))

contador1 = 0
for valor in range(0,101):
    if valor % 2 == 0:
        print(valor)
    else:
        continue 

    contador1 += 1

    
print('=================================' + str(contador1))


contador2 = 0
for valor in range(0,101):
    if valor % 2 == 0:
        print(valor)
    else:
        continue 

    contador2 += 1


print('=================================' + str(contador2))

# en el primero hace 101 mientras que continue hace 51 y el break 51 por lo que son
# fundamentales usarlos para optimizar el codigo

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores 
# divisibles por 12, dentro del rango de números de 100 a 300

n = 99
while (n <= 300):
    n += 1
    if (n % 12 != 0):
        continue
    print(n) 


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, 
# para encontrar números primos y dar la opción al usario de buscar el siguiente

numero = int(input('Ingresa un numero'))

for valor in range(1, numero + 1):
    if numero % valor == 0:

print('Es primo', valor)
