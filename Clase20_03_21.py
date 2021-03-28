# #ejemplo 1
# contador1=0
# while(contador1<5):
#         nombre=input("Ingrese su nombre: ")
#         print(nombre)
#         contador2=0
#         promedio=0
#         suma=0
#         contadorganador=0
#         contadorperdedor=0
#         while(contador2<5):
#             notamateria=float(input("ingrese la nota: "))
#             suma=suma+notamateria
#             print (notamateria)
#             contador2=contador2+1
#         promedio=suma/5
#         print ("El promedio es ",promedio)

#         if (promedio>3):
#             contadorganador=contadorganador+1
#             print("gano la materia")

#         else:
#             contadorperdedor=contadorperdedor+1
#             print("no gano la materia")
        

# contador1=contador1+1
# print("El numero de personas que ganaron es,",contadorganador)
# print("El numero de personas que perdieron es,",contadorperdedor)

# #ejercicio2
# equipos=0
# while(equipos<2):
#     nombreEquipo=input('ingrese el nombre del equipo: ')
#     print(nombreEquipo)
#     jugadores=0
#     while(jugadores<2):
#         documentoJugador=int(input('ingrese el documento por favor:'))
#         nombreJugador=input('ingrese el nombre por favor: ')
#         posicionJugador=input('ingrese la posicion del jugador: ')
#         jugadores=jugadores+1
#     equipos=equipos+1       
# print("El nombre del equipo  es: ",nombreEquipo)
# print("El nombre del jugador:",nombreJugador)
# print("La posicion del jugador es ",posicionJugador)
# # ejercicio 1 grupo n
# cont=0
# contdel=0
# contgord=0

# while (cont<2):

#     edad=input("ingrese la edad(solo numeros)")
#     peso=float(input("ingrese el peso(solo numeros)"))
#     estatura=float(input("ingrese la estatura(ejm:1.50)"))
#     print(cont)
    
#     imc=peso/(estatura*estatura)
#     pesoideal=30
#     if (imc>pesoideal):
#         print("Estas gordo")
#         contgord+=1
#     else:
#         print("Estas delgado")
#         contdel+=1
#     cont=cont+1
#     print("su imc es:",imc)



#ejercicio 2 alcaldia
# parejasColegios=0
# contO=0
# contA=0

# while (parejasColegios<2):

#     nombreColegio=input("ingrese el nombre del colegio ")
#     print(nombreColegio)
#     estudiante=0
#     while (estudiante<2):
        
#         grado=int(input("ingrese el grado por favor:"))
#         edad=int(input("ingrese el edad por favor:"))
#         sex=input("ingrese A-niña o O-niño:")
#         if sex=="a" or sex=="A":
#             contA=contA+1
#         elif sex=="o" or sex=="O":
#             contO=contO+1
#             print(estudiante)
#         estudiante=estudiante+1
    
# parejasColegios=parejasColegios+1
# print("Número de colegios",parejasColegios)
# print("Número de niñas matriculadas:",contA)
# print("Número de niños matriculados:",contO)
# ejercicio3
# capurgana=1500000
# nequi=1200000 
# islas_margaritas=2000000
# Igosslas_galapa=4000000
# Isla_mukura=1200000
# islas_san_andres=1500000
# personas=0

# while(personas<2):
#     turistas= input("Ingrese numero de turistas: ")
#     print(personas)
    
#     destino = input("Ingrese destino: ")
#     print(destino)
    
#     if(destino=="capurgana"):
#         valueimpuesto= capurgana * 0.20
#         TasaA =  capurgana* 0.15
#         valortotal1=capurgana+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal1)

#     elif (destino=="nequi"):
#         valueimpuesto= nequi * 0.19
#         TasaA =  nequi* 0.09
#         valortotal2 =nequi+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal2)

#     elif (destino=="islas_margaritas:"):
#         valueimpuesto= islas_margaritas * 0.11
#         TasaA =  islas_margaritas* 0.16
#         valortotal3 =islas_margaritas+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal3)

#     elif (destino=="Igosslas_galapa"):
#         valueimpuesto= Igosslas_galapa * 0.09
#         TasaA = Igosslas_galapa* 0.08
#         valortotal4=Igosslas_galapa+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal4)

#     elif (destino=="Isla_mukura"):
#         valueimpuesto= Isla_mukura* 0.09
#         TasaA = Isla_mukura* 0.08
#         valortotal5 =Isla_mukura+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal5)

#     elif(destino=="islas_san_andres"):
#         valueimpuesto= islas_san_andres* 0.13
#         TasaA = islas_san_andres* 0.12
#         valortotal6 =islas_san_andres+(valueimpuesto+TasaA)
#         print ("Total a pagar: ",valortotal6)

#     personas=personas+1
# print ("El porcentaje de personas es: ",personas)


# 4.san felix

# cont=0
# vuelo=80000
# contH=0
# contM=0
# while (cont<2):
#     eps=input("ingrese su eps")
#     print(eps)
#     edad=int(input("ingrese la edad(solo numeros)"))
#     print(cont)

#     if (edad >= 15 and edad <=60):
#         print("Se puede subir " )

#     elif (edad < 15):
#         print("No se puede subir al parapente")

#     sex=input("ingrese M-mujer o H-Hombre:")
#     if (sex=="m" or sex=="M"):
#         contM=contM+1
#     elif (sex=="h" or sex=="H"):
#         contH=contH+1

#     T=contM+contH
#     PH= ((contH*100/T))
#     PM= ((contM*100/T))

# cont=cont+1
# totalD=vuelo*cont
# print("El porcentaje  de mujeres es:",PM)
# print("El porcentaje de hombres es:",PH)
# print("La cantidad de mujeres es:",contM)
# print("La cantidad de hombres es:",contH)
# print("El dinero recaudadodel dia es:",totalD)