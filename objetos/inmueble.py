class inmueble:
    dato=[]
    
    def __init__(self,referencia,mtc,prec,ubi,tipo):
        
        self.Referencia = referencia
        self.Metro_cuadrado = mtc
        self.Precio = prec
        self.Ubicacion = ubi
        self.Tipo = tipo
        self.datos=[0]

    def insertar_valores(self,valor):
        self.datos=[]
        self.datos.append(valor)
        return self.datos
        print()

    def mostrar_valores(self):
        
        print (self.datos) 

    def get_Referencia(self):
        return self.Referencia

    def set_Referencia(self, referencia):
        self.Referencia = referencia

    def get_Metro_cuadrado(self):
        return self.Metro_cuadrado 

    def set_Metro_cuadrado(self,mtc):
        self.Metro_cuadrado  = mtc

    def get_Precio(self):
        return self.Precio

    def set_referencia(self, prec):
        self.Precio = prec
        
    def get_Ubicacion(self):
        return self.Ubicacion

    def set_referencia(self, ubi):
        self.Ubicacion = ubi
        
    def get_Tipo(self):
        return self.Tipo

    def set_tipo(self, tipo):
        self.Tipo = tipo

# def new_func():
#     datos=[]


obj1=inmueble("",0,0,"","")
centinela="si"
while centinela=="si":
    set_Referencia=int(input("ingrese la referencia: "))
    obj1.insertar_valores(set_Referencia)
    centinela=input("desea continuar si/no: ")
    obj1.mostrar_valores()

valor=obj1.mostrar_valores()

for i in range (0, len(valor)):
    print(valor[i])

obj1.mostrar_valores()
# set_Referencia=int("ingrese la referencia")
# obj1.insertar_valores(set_Referencia)

# set_Metro_cuadrado=int(input("ingrese la metros cuadrados"))
# obj1.insertar_valores(set_Metro_cuadrado)
# obj1.mostrar_valores()



# obj1=inmueble("",0,0,"","")

# datos=[]
# for i in range(0,22):

#     obj1.set_Referencia=int(input("ingrese la informacion del inmueble"))
# datos.append(obj1.Set_Referencia)

