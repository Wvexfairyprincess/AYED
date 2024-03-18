#Elabore un programa para calcular la quinta potencia, la raíz cuadrada, el exponencial, el logaritmo natural y el valor absoluto de un número introducido por el teclado.

import cmath

x = float(input('Digite el numero: '))
quintaPotencia = pow(x, 5)
raizCuadrada = cmath.sqrt(x)
exponencial = cmath.e ** x
logaritmo = cmath.log(x)
valorAbsoluto = abs(x)

print(f'La quinta potencia de {x} es: {quintaPotencia}')
print(f'La raiz cuadrada de {x} es: {raizCuadrada}')
print(f'El exponencial de {x} es: {exponencial}')
print(f'El logaritmo natural de {x} es: {logaritmo}')
print(f'El valor absoluto de {x} es: {valorAbsoluto}')