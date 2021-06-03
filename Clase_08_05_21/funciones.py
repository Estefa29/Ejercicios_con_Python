# def suma(a,b):
#     sumas=a+b
#     return sumas

# valor1=int(input("ingrese el primer valor"))
# valor2=int(input("ingrese el segundo valor"))
# print(suma(valor1,valor2))

def subtotal(valor_producto,cantidad):
    subtotals=valor_producto* cantidad
    return subtotals
subtotals(230000,5)

Cesta={}
centinela='si'
while centinela=='si':
    clave=input('introduzca el producto a comprar: ')
    valor= input(clave+ ':')
    Cesta[clave]=valor
    print(Cesta)
    centinela= input("si desea continuar /si, sino No: ")
print(Cesta)

total = 0
for null,precio in Cesta.items ():
    
    cantidad=(input('ingrese la cantidad:  '))
    total=+subtotal(precio, cantidad)

print(f"el precio es:{total}")
print(f"subtotal:{subtotal}")