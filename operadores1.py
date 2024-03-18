import cmath, os

#os.system("cls") - En Windows
#os.system("clear") - En Mac
#os.system("cls || clear") - creo que sirve asi tambien para los dos

"""Elabore un programa que solicite dos números enteros y 
presente como resultados cada una de las repuesta de todos los operadores matemáticos"""


x = float(input('Digite el primer numero: '))
y = float(input('Digite el segundo numero: '))

def operaciones(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    divisionEntera = x // y
    modulo = x % y
    exponente = x ** y
    raizCuadrada = cmath.sqrt(x)
    raizCuadrada2 = cmath.sqrt(y)
    return suma, resta, multiplicacion, division, divisionEntera, modulo, exponente, raizCuadrada, raizCuadrada2

suma, resta, multiplicacion, division, divisionEntera, modulo, exponente, raizCuadrada, raizCuadrada2 = operaciones(x, y)

print(f'La suma de {x} + {y} es: {suma}')
print(f'La resta de {x} - {y} es: {resta}')
print(f'La multiplicacion de {x} * {y} es: {multiplicacion}')
print(f'La division de {x} / {y} es: {division}')
print(f'La division entera de {x} // {y} es: {divisionEntera}')
print(f'El modulo de {x} % {y} es: {modulo}')
print(f'El exponente de {x} ** {y} es: {exponente}')
print(f'La raiz cuadrada de {x} es: {raizCuadrada}')
print(f'La raiz cuadrada de {y} es: {raizCuadrada2}')

print('Desea continuar?')
continuar = input('Digite "si" para continuar o "no" para salir: ')
if continuar.lower() == 'si':
    os.system('cls || clear')
    x = float(input('Digite el primer numero: '))
    y = float(input('Digite el segundo numero: '))
    operaciones(x, y)

    print(f'La suma de {x} + {y} es: {suma}')
    print(f'La resta de {x} - {y} es: {resta}')
    print(f'La multiplicacion de {x} * {y} es: {multiplicacion}')
    print(f'La division de {x} / {y} es: {division}')
    print(f'La division entera de {x} // {y} es: {divisionEntera}')
    print(f'El modulo de {x} % {y} es: {modulo}')
    print(f'El exponente de {x} ** {y} es: {exponente}')
    print(f'La raiz cuadrada de {x} es: {raizCuadrada}')
    print(f'La raiz cuadrada de {y} es: {raizCuadrada2}')

else:
    print('Hasta luego')
    exit()