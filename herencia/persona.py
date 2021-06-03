class persona:
    def __init__(self,nombre , edad,apellido,direccion,telefono,email,mun_re,mun_nac,fecha): 
        self.Nombre= nombre
        self.Edad =edad
        self.Apellido =apellido
        self.Direccion =direccion
        self.Telefono = telefono
        self.Email =email
        self.Municiopio_residencia =mun_re
        self.Municiopio_nacimiento =mun_nac
        self.Fecha=fecha
        

    def insertar():
        return 0

    def consultar():
            return 0

    def get_nombre(self):
        return self.__Nombre
    
    def set_nombre(self,valor):
        self.__Nombre = valor

    def get_edad(self):
        return self.__Edad
    
    def set_nombre(self,valor):
        self.__Edad = valor

    def get_apellido(self):
        return self.__Apellido
    
    def set_nombre(self,valor):
        self.__Apellido = valor
    
    

    def get_dirreccion(self):
        return self.__Dirreccion
    
    def set_dirreccion(self,valor):
        self.__Dirreccion = valor

    def get_telefono(self):
        return self.__Telefono
    
    def set_telefono(self,valor):
        self.__Telefono = valor

    def get_email(self):
        return self.__Email
    
    def set_email(self,valor):
        self.__Email = valor

    def get_mun_re(self):
        return self.__Municipo_residencia
    
    def set_mun_re(self,valor):
        self.__Municipo_residencia = valor

    def get_mun_nac(self):
        return self.__Municipio_nacimiento
    
    def set_mum_nac(self,valor):
        self.__Municipio_nacimiento = valor

    def get_fecha(self):
        return self.__Fecha
    
    def set_fecha(self,valor):
        self.__Fecha = valor

persona=persona("juan",23,"gomez","calle4",42424,"andres@gam","medellin","marinilla","03-03")