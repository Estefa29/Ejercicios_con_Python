# Crear con el uso de diccionarios una cesta de Compras, 
# que permita adicionar prendas de vestir como: camisetas, pantalones, 
# , camisas, pantalonetas para hombres, en la compra deberá limitar que no exceda más de 
# 10 productos. Se debe ingresar la prenda el precio y la talla para cada uno.
# Luego deberá calcular el precio a pagar.
# for i in range(11):
# prenda={'camisetas, pantalones,  camisas, pantalonetas}
Cesta = {}
articulo=1

centinela ='si'
while centinela =='si' and articulo <=2:

    print('prendas de vestir: camisetas, pantalones,  camisas, pantalonetas ')
    
    clave= input('¿Que articulo deseas comparar : ')
    print('ingrese la talla de la prenda')
    talla = input(clave+ '  :  ')
    print('ingrese el precio de la prenda')
    precio = int(input(clave + ',  talla:  '+ talla+ ', valor :  '))
    Cesta[clave]= precio
    centinela= input("si desea continuar /si, sino No: ")
    print(Cesta)
    articulo= articulo +1
    
    
if len(Cesta)>=10:
    print('no exceda más de  10 productos')
total = 0
for null,precio in Cesta.items():
    total += precio
    
print(f"Esto es lo que compraste:  {Cesta}") 
print(f"Su total a pagar es : {total}")


