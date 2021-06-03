# Dar solución al siguiente enunciado: se quiere registrar la información de un vehículo,
#  como la placa la fecha de salida, fecha entrada, celda de parqueo, luego se desea calcular
#   el tiempo que duro un vehículo parqueado y generar el valor del boleto a pagar, debe indicar 
#   si la celda  se encuentra ocupada o no.(desarrollar con el uso de funciones)
celdaDisp = [3,6,9]
celdasOcp =[1,2,4,5,7,8,10]

class registrar:
    def __init__(self, placa, fechaEnt, fechasali, celdaP ) :
        
        self.placa = input('  digite la placa : ')
        placa=placa
        self.fechaEnt = int(input('fecha de entrada : ' ))
        fechaEnt=fechaEnt
        self.fechasali = int(input(' fecha de salida (debe ser mayor a la entrada): '))
        fechasali=fechasali
        self.celdaP = int(input('Estas celdas se encuentran disponibles [3,6,9] elija una: '))
        disponible = self.celdaP in celdaDisp
        if disponible == True:
            
            print('celda disponible,puede ingresar')
            
        else:
            print('esta celda no se encuentra disponible, por favor busque otra')
        
        
        
        


    def __str__(self):
        return "placa: " + self.placa + ", fecha entrada: "+ str(self.fechaEnt) + ", fecha salida: " + str(self.fechasali) + ",celda de parqueo: " + str(self.celdaP) 

# valorh=valor hora
class Insertar(registrar):
    def __init__(self, placa, fechaEnt, fechasali, celdaP, tiempo,valorD) :
        super().__init__(placa, fechaEnt, fechasali, celdaP) 
        
        self.tiempo = tiempo
        self.valorD =  valorD
        print(f"debes pagar:")      
        

    def __str__(self):
        return super().__str__() + ", tiempo: " + str(self.tiempo) +" horas " + ",valor a pagar por dia $ :" + str(self.valorD)
Registrar = registrar

print(Registrar)

insertar = Insertar("","","","",24,"17.300") 
print(insertar)

