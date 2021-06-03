listas=["renault","chevrolet","mazda"]
for i in listas:
    print(i,end="")

for i in range (len(listas)):
    print(listas[i],end="")


for i in range (len(listas)-2):
    print(listas[i],end="")


    auxiliar=listas [:2]
    print (auxiliar)

    listas.insert(3,"audi")
    print (listas)

    auxiliar=listas [1:]
    print (auxiliar)
    listas.remove("renault")
    print (listas)
    listas.clear
    print (listas)
    listas[0]
    listas[i:j]
    listas[i:]
    listas[:j]
    lista3= listas+auxiliar

    tupla=(1,2,4,5)
    tupla2=(3,8,9,6)
    tupla3=tupla+tupla2

