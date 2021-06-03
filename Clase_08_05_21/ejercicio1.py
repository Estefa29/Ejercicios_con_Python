def subtotal(valor_producto,cantidad):
    subtotals=valor_producto* cantidad
    return subtotals


Cesta={}
centinela='si'
while centinela=='si':
    clave=input('introduzca el producto a comprar: ')
    valor=int (input(clave+ ':'))
    Cesta[clave]=valor
    print(Cesta)
    centinela= input("si desea continuar /si, sino No: ")
print(Cesta)

total = 0
for null,precio in Cesta.items ():
    
    cantidad=int(input('ingrese la cantidad:  '))
    total=total+subtotal(precio, cantidad)

print(f"el precio es:{total}")
