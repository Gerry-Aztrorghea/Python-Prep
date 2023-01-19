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