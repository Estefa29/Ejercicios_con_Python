from herencia import persona as persona

class empleado(persona):

    def __init__(self, nombre, edad,apellido,direccion,telefono,email,mun_re,mun_nac,fecha, sueldo,cargo,auxilio):
        # super().__init__(self,nombre, edad,apellido,direccion,telefono,email,mun_re,mun_nac,fecha)
        persona().__init__(self,nombre,edad,apellido,direccion,telefono,email,mun_re,mun_nac,fecha)
        self.Sueldo = sueldo
        self.Cargo=cargo  
        self.Auxilio_transporte=auxilio

    def get_sueldo(self):
            return self.__Sueldo
        
    def set_(self,valor):
        self.__Sueldo = valor

    def get_cargo(self):
            return self.__Cargo
        
    def set_cargo(self,valor):
        self.__Cargo = valor

    def get_auxilio(self):
            return self.__Auxilio_transporte
        
    def set_auxilio(self,valor):
        self.__Auxilio_transporte = valor
    




    # Persona= persona("juan",28)
    # print(Persona)

    Empleado= empleado("juan",37,"gomez","carrera 34-56",3324354,"juang@gmail.com","medellin","marinilla"
    ,"02-03-1990",2300000,"jefe ventas",23000)
    print(Empleado)