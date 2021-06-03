# class persona:
#     # variables
#     identificacion=0
#     apellido=""
#     nombres=""
#     fecha_nacimiento="2003"

class persona:
    def __init__(self,nombre,edad):
        
        self._nombre = nombre
        self._edad = edad

        def get_nombre(self):
            return self._nombre

        def set_nombre(self, nombre):
            return self._nombre

        def get_edad(self):
            return self._edad

        def set_edad(self, edad):
            return self._edad
            
            

# objeto
        p1=persona("",0)
        print(p1.get_nombre())
        print(p1.get_edad())

        p1.set_nombre("karla")
        p1.set_edad(20)
        print(p1.get_nombre())
        print(p1.get_edad())