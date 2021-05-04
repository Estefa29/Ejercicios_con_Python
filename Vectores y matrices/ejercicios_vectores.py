# #   Inserte valores numéricos en el siguiente vector y ordénelos de forma ascendente, 
# # descendente. Muestre el menor valor y el mayor valor.
print('Digite 11 numeros: ',end='')
numeros = list(map(int, input().split()))

print(numeros)

numeros.sort()

print(numeros)

numeros.reverse()

print(numeros)
# # Se tiene un vector de 20 posiciones donde se desean almacenar marcas de vehículos,
# # se tiene un segundo vector donde se almacenan los precios del mismo.

Marca=[]
Precio=[]
for i in range(20):
    ArrayM=(input("Ingrese Marca de Vehiculo: "))
    ArrayP=int(input("Ingrese Precio de Vehiculo $: "))
    Marca.append(ArrayM)
    Precio.append(ArrayP)
print(Marca)
print(Precio)

    # Se tiene un vector que almacenara los nombres científicos de hongos, 
    # se deberá realizar un algoritmo que permita insertar los nombres en el vector, 
    # realizar la búsqueda, realizar la consulta por nombre. Para un total de 10 muestras.

hongos=[]

for i in range(0,10):
    nombre=(input("Ingrese el nombre científico del hongo: "))
    hongos.append(nombre)

print(hongos)
valor_buscar=(input("Buscar nombre del hongo: "))
for i in range (0,10):
    if hongos[i]==valor_buscar:
        print (hongos[i],i)

# Se desea realizar un algoritmo que almacene las letras del alfabeto,
#  y debe mostrar las posiciones de las letras donde se encuentran cuando una persona,
#  digita un nombre o una palabra.
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
valor_buscar=(input("ingrese la letra que desea buscar:  "))
for i in range (0,26):
    if alfabeto[i]==valor_buscar:
        print (alfabeto[i],i)
        
cadena ='cinthia'

for i, c in enumerate(cadena):
    print ('Caracter: %s - índice: %i'% (c, i))

# //no supe como complementar este ejercicio pero se busca cada letra del alfabeto
# y hice una cadena que muestre cada posicion de una palabra

# Se desea realizar un algoritmo que permita almacenar dos valores que son ingresados en
#  código binario, y se debe de realizar la suma y la resta de estos dos valores.

import numpy as np
a= 1010
dec = int(str(a), 2)
print (dec)


b= 11001
dec2 = int(str(b), 2)
print (dec2)
binarios1 = np.array([dec2, dec])
print(binarios1)
binarios2 = np.array([dec,dec2])
print(binarios2)
menu=input("desea hacer una suma o una resta?: ")
if menu=="suma":
    operacion = binarios1 + binarios2
elif menu=="resta":
    operacion = binarios1 - binarios2


print(operacion)
# converti los binarios en decimales para hacer la suma y la resta

# 6.Se desea almacenar en un vector seis posiciones que corresponde a las caras de un dado,
#  con la formula de valores aleatorios debe de generar un valor de uno a seis,
#  se debe solicitar el numero de lanzamientos a realizar y luego calcular el valor obtenido 
# en cada uno de los lances.

import random


def roll_dice(caras, cantidad, tiradas):
    rolls = [0] * tiradas
    for i in range(tiradas):
        for _ in range(cantidad):
            t = random.randint(1, caras)
            rolls[i] += t           
    return rolls


if __name__ == "__main__":
    caras = int(input("Inserte la cantidad de caras por dado: "))
    cantidad = int(input("\nInserte la cantidad de dados: "))
    tiradas = int(input("\nInserte la cantidad de tiradas: "))

    result = roll_dice(caras, cantidad, tiradas)
    print(result)


# https://www.youtube.com/watch?v=l1UGYczWCV4&t=10s
# https://www.youtube.com/watch?v=nrW04QjjSpk
# https://www.youtube.com/watch?v=61PIPtDqEd0&t=4s
# https://es.stackoverflow.com/questions/200229/programa-de-simulaci%C3%B3n-de-tirada-de-dados