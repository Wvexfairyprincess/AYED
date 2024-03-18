#Programas basicos de python (Promedio de 3 numeros)
print('Digite 3 numeros y te dare el promedio')
num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))
num3 = int(input('Digite el tercer numero: '))
promedio = (num1 + num2 + num3) / 3
print('El promedio es: ', promedio)

#Leer el precio de un producto, calcule el impuesto de valor agregado.
precio = float(input('Digite el precio del producto: '))
iva = precio * 0.15
print('El impuesto de valor agregado es: ', iva)

#Leer el salario de un empleado y aumente dicho salario un 25%
salario = float(input('Digite el salario: '))
aumento = salario * 1.25
print('El impuesto de valor agregado es: ', aumento)

#Leer dos números e intercambiar sus valores.
num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))
aux = num1
num1 = num2
num2 = aux
print('El primer numero es: ', num1)
print('El segundo numero es: ', num2)


#Dado dos numero el primero la base y el segundo el exponente muestre el resultado por pantalla. 
base = float(input('Digite la base del numero: '))
exp = float(input('Digite el exponente del numero: '))
resultado = base ** exp
print('El resultado es: ', resultado)

#Determina la edad de una persona.
from datetime import date
fecha = date.today()
anio = int(input('Digite el año de nacimiento: '))
edad = fecha.year - anio
print('La edad es: ', edad)

#Calcular el total a pagar por la compra de artículos en una tienda. 
#Se sabe que el  impuesto que se aplica es el 10%.
def totalCompra(cantCompra):
    total = sum(compra)
    impuesto = total * 0.10
    totalPagar = total + impuesto
    return totalPagar

cantCompra = int(input('Digite la cantidad de articulos: '))
compra = []

for i in range(cantCompra):
    precio = float(input(f'Digite el precio del articulo {i+1}: '))
    compra.append(precio)

PagoTotal = totalCompra(cantCompra)
print('El total a pagar es: ', PagoTotal)