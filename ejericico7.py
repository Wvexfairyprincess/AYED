#Calcular el total a pagar por la compra de artículos en una tienda. 
#Se sabe que el  impuesto que se aplica es el 10%.
def totalCompra(cantCompra):
    subtotal = sum(compra)
    impuesto = subtotal * 0.10
    total = subtotal + impuesto
    return total

cantCompra = int(input('Digite la cantidad de articulos: '))
compra = []

for i in range(cantCompra):
    precio = float(input(f"Digite el precio del articulo {i+1}: "))
    compra.append(precio)

PagoTotal = totalCompra(cantCompra)
print('El total a pagar es: ', PagoTotal)