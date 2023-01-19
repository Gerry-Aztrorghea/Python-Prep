# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

numero = 1520
print(numero)

# 2) Imprimir el tipo de dato de la constante 8.5

NUMERO = 8.5
print(type(NUMERO))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(numero))

# 4) Crear una variable que contenga tu nombre

name = 'gerardo garduno rosas'

# 5) Crear una variable que contenga un número complejo

numero_complejo = 5 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(numero_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 3.1415


# 8) Crear una variable que contenga el valor 'True' y 
# otra que contenga el valor True. ¿Se trata de lo mismo?

valor = True
valor1 = 'True'

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print(f'''El primer valor es un booleano:  {valor}, mientras que el 
otro es una variable: {valor1}''')

# 10) Asignar a una variable, la suma de un número entero y otro decimal

suma = ( 5 + 2.3 )

# 11) Realizar una operación de suma de números complejos

numero1 = 5 + 3j
numero2 = 4 + 2j
suma1 = ((numero1.real + numero2.real) )
suma2 = (numero1.imag + numero2.imag)
print(str(suma1) + " + " + str(suma2) + "j")

# 12) Realizar una operación de suma de un número real y otro complejo

real = 2.36
suma_real_complejo =( str(numero1.real + real) + ' + ' + str(numero1.imag) + "j" )
print(suma_real_complejo)

# 13) Realizar una operación de multiplicación

multiplicacion = 5 * 33
print(multiplicacion)

#14) Mostrar el resultado de elevar 2 a la octava potencia

potencia = 2**8
print(potencia)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y 
# luego mostrarla

division_completa = 24 / 4
print(division_completa)

#16) De la división anterior solamente mostrar la parte entera

division_entera = 24 // 4
print(division_entera)

#17) De la división de 27 entre 4 mostrar solamente el resto

residuo = 24 % 4
print(residuo)

#18) Utilizando como operandos el número 4 y los resultados obtenidos 
# en los puntos 16 y 17. Obtener 27 como resultado
# duda de la solucion ---->
operacion = 6 * 4 + 3
print(operacion)

#19) Utilizar el operador "+" en una operación donde intervengan solo 
# variables alfanuméricas

texto = 'En el mundo'
texto1 = " se necesitan muchos programadores"
print( texto + texto1)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

respuesta = '2' == 2
print(respuesta)

# 21) Utilizar las funciones de cambio de tipo de dato, para 
# que la validación del punto 20 resulte verdadera

print( int('2') == 2 )

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

print(float('3.8'))
# arroja error por usar comas en lugar de puntos 


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar
#  su contenido

variable = 3 
variable -= 1
print(variable)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema 
# de numeración binario?

operacion2 = 1 << 2
print(operacion2)
# creo que se desplaza dos numeros en memoria

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos
#  operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#print( 2 + '2')
# marca error por que no se pueden hacer operaciones enteras con texto por eso se usa casting

# 26) Realizar una operación válida entre valores de tipo entero y string

texto = 'setiene que castear el numero para hacer string '
numero3 = 5

print(texto + str(numero3))