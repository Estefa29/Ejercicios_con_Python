class Reserva_hotel:
    
    def _init_(self,cr, fecha,valor,habit,dias,nombre,cantidad):
        self.Codigo_Reserva=cr
        self.Fecha_Reserva=fecha
        self.Valor_Reserva=valor
        self.Habitacion=habit
        self.Dias_Reserva=dias
        self.Nombre_Reserva=nombre
        self.Cantidad_Persona=cantidad
        self.tipo_servicio=0
        self.datos=[]
        self.plato=0
    
    # asignando en procedimiento el valor de la habitacion  
    def valor_dia_habitacion(self):
        set_valor_reserva = 300000
        return set_valor_reserva
    #se va adicionar en la lista el numero de la reserva en el hotel
    def insertar_reserva(self,dato):
        self.datos.append(dato)   
    # mostrar los valores de la lista(reserva)   
    def mostrar_datos(self):
        print(self.datos) 
    # el valor a pagar por la cantidad personas y por la cantidad de dias
    def calcular_dias(self):
        valor=self.valor_dia_habitacion()
        valor1=set_dias  
        valor3=set_cantidad_reserva  
        
        resultado=0
        if (valor1<=0):
            print ("no ha ingresado cantidad de dias")
            resultado=0
    
        else:
                        
            resultado=(valor1*(valor*valor3))
        return resultado  
            
    
    #calcular valor a pagar con IVA
    def calcular_IVA(self):
        valor=self.calcular_dias()
        return valor+(valor*0.19)
    
    def alimentacion(self,plato):
        
        if (plato==3):
            valor_plato=80000
        elif (plato==2):
            valor_plato= 60000
        else:
            valor_plato=20000  
        return valor_plato
    
    def otros(self,tipo_servicio,cantidad):
    
        if (tipo_servicio=="parqueadero"):
            valor_servicio= 15000* cantidad
        if (tipo_servicio=="lavanderia"):
            valor_servicio=12000*cantidad
        if  (tipo_servicio=="guia turistico"):
            valor_servicio=25000*cantidad 
        return valor_servicio
    
    
    def Pagos_completos(self):
        pago_IVA=self.calcular_IVA()
        alimentacion=self.alimentacion(self.plato)
        servicios=self.otros(set_tipo_servicio,set_cantidad_reserva)
        return pago_IVA+alimentacion+servicios

    def set_tipo_servicio(self,valor):
        self.Tipo_servicio= valor

    def get_valor_tipo_servicio(self):
        return self.Tipo_servicio

    def set_valor_reserva(self,valor):
        self.Valor_Reserva= valor

    def get_valor_reserva(self):
        return self.Valor_Reserva

    def set_codigo_reserva(self,codigo):
        self.Codigo_Reserva=codigo

    def get_codigo_reservar(self):
        return self.Codigo_Reserva

    def set_fecha_reserva(self,fecha):
        self.Fecha_Reserva=fecha

    def get_fecha_reserva(self):
        return self.Fecha_Reserva

    def set_habitacion(self,valor):
        self.Habitacion=valor

    def get_habitacion(self):
        return self.Habitacion 

    def set_dias(self,dias):
        self.Dias_Reserva=dias

    def get_dias(self):
        return self.Dias_Reserva

    def set_nombre_reserva(self,nombre):
        self.Nombre_Reserva

    def get_nombre_reserva(self):
        return self.Nombre_Reserva

    def set_cantidad_reserva(self,valor):
        self.Cantidad_Persona

    def get_Cantidad_reserva(self):
        return self.Cantidad_Persona


obj_reserva=Reserva_hotel()
obj_reserva.valor_dia_habitacion()
set_codigo_reserva=int(input("ingrese el codigo de la reserva"))
obj_reserva.insertar_reserva(set_codigo_reserva)
set_fecha_reserva=input("ingrese la fecha de la reserva")
obj_reserva.insertar_reserva(set_fecha_reserva)
set_dias=int(input("ingrese los dias de la reserva"))
obj_reserva.insertar_reserva(set_dias)
set_habitacion=int(input("ingresar el numero de la habitacion"))
obj_reserva.insertar_reserva(set_habitacion)
set_cantidad_reserva=int(input("Ingrese la cantidad de personas a alojarse"))
obj_reserva.insertar_reserva(set_cantidad_reserva)
obj_reserva.mostrar_datos()

print (obj_reserva.calcular_dias())
obj_reserva.calcular_IVA()
obj_reserva.plato=int (input("ingrese el 3 si quiere las tres comidas, 2: para desayuno y almuerzo,1: para desayuno"))
obj_reserva.alimentacion(obj_reserva.plato)
set_tipo_servicio=input("si requiere parqueadero,lavanderia o guia turistico ")
obj_reserva.otros(set_tipo_servicio,set_cantidad_reserva)
print(obj_reserva.Pagos_completos())