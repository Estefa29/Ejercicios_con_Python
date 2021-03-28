# La escuela marceliano desea obtener el promedio de notas de un grupo de 25 estudiantes,
#  y los 25 se les solicita 5 notas  por cada una de las materias (matemática y lenguaje). 

# Se debe imprimir el promedio de notas por cada materia, se debe imprimir el promedio de
#  notas de las dos asignaturas por estudiante y se debe imprimir el total general del grupo. 

# (Ciclos anidados) 
# Las 5 notas de los estudiantes

promedio=0
suma=0
estudiantes=int(input("Ingrese numero de estudiantes: "))
while(estudiantes<25):
        nombre=input("Ingrese su nombre: ")
        print(nombre)
        matematicas=0
        while(matematicas<5):
            notamateria1=float(input("ingrese la nota de matematicas: "))
            suma=suma+notamateria1
            print (matematicas)
            matematicas=matematicas+1
        promedio=suma/5
        print ("El promedio  de matematicas es ",promedio)
        promedio2=0
        suma2=0
        lenguaje=0
        while(lenguaje<5):
            notamateria2=float(input("ingrese las notas de lenguaje : "))
            suma2=suma2+notamateria2
            print (lenguaje)
            lenguaje=lenguaje+1
        promedio2=suma2/5
        print ("El promedio de lenguaje es ",promedio2)
promedioA=(promedio+promedio2)/2
estudiantes=estudiantes+1
totGrup=(estudiantes + promedioA)/25
print("El numero de personas es:",estudiantes)
print("El total general del grupo es,",totGrup)
print("El promedio de las dos asignaturas es:" ,promedioA)


    

