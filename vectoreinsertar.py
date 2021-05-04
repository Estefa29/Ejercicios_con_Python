datos=[]
for i in range (0,7):
    nuevoDato=int(input("ingrese valores enteros"))
    datos.append(nuevoDato)

for i in range (0,7):
    print (datos[i])
valor_buscar=(int(input("cual es el valor a buscar")))
for i in range (0,7):
    if datos[i]==valor_buscar:
        print (datos[i],i)

valor_buscar_eliminar=(int(input("cual es el valor a eliminar y reemplazar en 0:")))
for i in range (0,7):
    
    if datos[i]==valor_buscar_eliminar:
        print (datos[i],i)
        datos[i]=0
for i in range (0,7):
    print (datos[i])

# valor_buscar_eliminar=(int(input("cual es el valor a eliminar y desplazar")))
# for i in range (0,7):
    
#     if datos[i]==valor_buscar_eliminar:
#         print (datos[i],i)
#         datos[i]=0

# j=i
# while j<7:
#     aux=datos[j+1]
#     datos[j]=aux
# j +=1
# for i in range (0,7):
#     print (datos[i])
# print("Orden")
# for i in range(0,7):
#     print(datos[i])

# print("desorden")
# for i in range (0,1):
#     datos.sort()
# print(datos)
    