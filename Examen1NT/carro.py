# Santiago desea adquirir un carro para ello le solicitan el 30% de la cuota inicial,
#  y el resto para financiamiento, teniendo en cuenta las políticas del negocio, permite
# 
#  la financiación si el préstamo se hace como mínimo 3 años y máximo 5 años para su cancelación; 
# el préstamo cuenta con una tasa del 12.5% anual. 

# ¿Cuánto dinero se paga en el mes? 
# # ¿cuánto dinero para de acuerdo con la cantidad de años seleccionados por el cliente? 
# Nota: debe solicitar el valor del vehículo  y el tiempo de financiación de este. 
# //valor1=valor del carro ,valor f= financiamiento
valorI = int(input("Ingrese el valor del vehivulo: "))
print (valorI)
cuotaI=valorI*0.3
valorF=valorI-cuotaI


tiempoF= int(input("Ingrese el tiempo de financiación: "))
if(tiempoF==1):
        tasa1= valorI * 0.125
        valorT1=valorI+tasa1
        valorM1=valorT1/12
        print ("Total a pagar Por un año: ",valorT1)
        print ("Total a pagar cada mes: ",valorM1)
elif(tiempoF==2):
        tasa2= valorI * (0.125)*2
        valorT2=valorI+tasa2
        valorM2=valorT2/24
        print ("Total a pagar Por dos años: ",valorT2)
        print ("Total a pagar cada mes: ",valorM2)
elif(tiempoF==3):
        tasa3= valorI * (0.125)*3
        valorT3=valorI+tasa3
        valorM3=valorT3/36
        print ("Total a pagar Por tres años: ",valorT3)
        print ("Total a pagar cada mes: ",valorM3)
elif(tiempoF==4):
        tasa4= valorI * (0.125)*4
        valorT4=valorI+tasa4
        valorM4=valorT4/48
        print ("Total a pagar Por cuatro años: ",valorT4)
        print ("Total a pagar cada mes: ",valorM3)
elif(tiempoF==5):
        tasa5= valorI * (0.125)*5
        valorT5=valorI+tasa5
        valorM5=valorT5/60
        print ("Total a pagar Por cinco años: ",valorT5)
        print ("Total a pagar cada mes: ",valorM5)
else: print("usted no selecciono de 1 a 5 años")