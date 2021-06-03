asignaturas={'calculo':6,'etica':2,'fisica':3,'programacion':5,'baseDT':5}
total_creditos=0
for materias,creditos in asignaturas.items():
    print(materias,'tiene',creditos)
    total_creditos+= creditos
print(' el total de creditos es',total_creditos)

matricula={}
centinela='si'
while centinela=='si':
    clave=input('el dato a introducir')
    valor=input(clave+ ':')
    matricula[clave]=valor
    print(matricula)
centinela= input("si desea continuar/si, sino No")