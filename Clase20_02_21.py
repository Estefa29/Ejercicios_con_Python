# TEMAS:Definiciones de variables,Variables y constantes
# ,Definición de operadores Aritméticos ,Lógicos
# Relacionales
# //ingresar el tiempo de un prestamo y calcular la 
# cuota a pagar int=numeros
# interes=0.136
# prestamo=int(input("ingrese valor de prestamo"));
# tiempoP= int(input("Tiempo de Prestamo: "));
# total1 =  interes*tiempoP
# totalT=prestamo+(total1*prestamo)
# cuota=totalT/tiempoP
# print("El valor de cada cuota: ", cuota);
# ------------------ejercicio2-----------------------------------
# # //definición  e impresion de datos personales
# # nombre=input("Ingrese  nombre: ");
# # edad=int(input("Ingrese  edad: "));
# # telefono=int(input("Ingrese  telefono: "));
# 
# # print("Su Nombre es: ",nombre);
# # print("Su Edad es: ",edad);
# # print("Su Telefono es: ",telefono);

# ---------------------------------ejercicio3---------------------
# print("Ingrese el prestamo: ")
# valorP=int(input())
# interesM = int(((valorP/12)*0.018))
# print("La cuota mensual",interesM)
# cuotaM = int(valorP/12) + interesM
# print("")
# 
# total_pagar_anual=((cuotaM*12) | cuotaM)
# print("El valor anual es: ",total_pagar_anual)
# 
# total_pagar_dos=int(cuotaM*2)
# print("total pagar en dos meses",total_pagar_dos)
# total_pagar_nueve=int((cuotaM*9))
# print("Total pagar en nueve meses",total_pagar_nueve)
# interesM=int((cuotaM*12))
# print("Total pagar intereses",interesM)
# ----------------------------------repaso1---------------------------
# valorP=input(float("Ingrese valor del prestamo"))
# cuotaMen=(valorP/12)*0.018
# print("Cuota Mensual")
# 
# totalAnual=((cuotaMen*12)+cuotaMen)
# print("Valor Anual: ",totalAnual)
# servicio=(input("Ingrese el servicio: "))
# if servicio is "sencillo":
#     pagarS=(12000*0.19)+12000
# 
# else:
#     pagarS=(15000*0.19)+15000
# print("Su servicio es:",servicio)
# print("el valor a pagar es: ",pagarS)
# -----------------repaso2--------------------------------
# producto=input("ingrese L-lacteo,O-otro ")
# 
# if producto=="l"or producto=="L":
#     cantidad=int(input("ingrese cantidad de productos: "))
#     valorSinIva=cantidad*12000
#     valorIva=(valorSinIva*0.19)+valorSinIva
# 
# elif  producto=="o"or producto=="O":
#     cantidad=int(input("ingrese cantidad de productos: "))
#     valorSinIva=cantidad*15000
#     valorIva=(valorSinIva*0.19)+valorSinIva
# print("el producto seleccionado es: ",producto)
# print("valor a pagar sin iva: ",valorSinIva)
# print("valor a pagar con iva: ",valorIva)

# -------------repaso3---------------------------------
#nota1=float(input("Ingrese nota 1"))
#nota2=float(input("Ingrese nota 2"))
#nota3=float(input("Ingrese nota 3"))
#nota4=float(input("Ingrese nota 4"))
#nota5=float(input("Ingrese nota 5"))

#promedio_nota=(nota1*0.1)+(nota2*0.2)+(nota3*0.35)+(nota4*0.15)+(nota5*0.2)
#if(promedio_nota>=3.5):
#   print("Ha ganado la materia")
#else:
#   print("Perdio la materia",promedio_nota)
# ----------------------repaso4-------------------------------------


# vehiculo = input("Ingrese el tipo de vehiculo: ")
# lavado = input("Ingrese tipo de lavado: ")

# if(vehiculo=="Taxi") and (lavado=="Sencillo"):
#     print("El valor a pagar por el servicio:",12300)

# elif (vehiculo=="Particular") and (lavado=="Sencillo"):
#     print("El valor a pagar por el servicio:",15000)

# elif(vehiculo=="Camion") and (lavado=="Sencillo"):
#     print("El valor a pagar por el servicio:",23000)

# elif(vehiculo=="Taxi") and (lavado=="Full"):
#     print("El valor a pagar por el servicio:",25000)

# elif(vehiculo=="Particular") and (lavado=="Full"):
#     print("El valor a pagar por el servicio:",27000)

# elif(vehiculo=="Camion") and (lavado=="Full"):
#     print("El valor a pagar por el servicio:",28000)

# else:
#     print("No ha seleccionado ningun vehiculo")