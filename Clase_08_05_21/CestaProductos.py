Cesta={}
centinela='si'
while centinela=='si':
    clave=input('introduzca el producto a comprar: ')
    valor= input(clave+ ':')
    Cesta[clave]=valor
    print(Cesta)
    centinela= input("si desea continuar /si, sino No: ")
print(Cesta)