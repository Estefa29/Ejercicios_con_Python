# 1. Diseñe una función que permita registrar la información de un grupo de 5 personas como
#  los siguientes datos: identificación, nombre, salario, comisión, bonificaciones.

# 2. La función antes de insertar a la lista debe permitir validar que el salario sea superior
#  de 900000 que las comisiones mayores de 0 al igual que las bonificaciones.

# 3. Deberá diseñar una segunda función donde esta permita mostrar la información contenida
#  en la lista.

# 4. Deberá realizar una función que permita buscar un dato en la lista.
empleados=[]
for i in range(5):

    class registrar:
        def __init__(self, identificacion, nombre , salario) :
            self.identificacion = input(' ingrese su identificacion : ')
            identificacion=identificacion
            self.nombre = input('ingrese su nombre : ' )
            nombre=nombre
            self.salario =  input('  ingrese el salirio(si es mayor a 900000 tiene comision y bonificacion) : ')
            salario=salario
            empleados.append(self.identificacion)


        def __str__(self):
            return "identificacion: " + self.identificacion + ", nombre: "+ str(self.nombre) + ", salario: " + str(self.salario)


    class Insertar(registrar):
        def __init__(self, identificacion, nombre, salario, comision, bonificacion) :
            super().__init__(identificacion, nombre, salario) 
            total=0 
            self.comision =comision  
            self.bonificacion =  bonificacion
            if salario > "900000":
                total=salario+bonificacion+comision
                print(f'tienen derecho a bonificacion {total}') 
            else:
                total=salario
                print(f"No tiene derecho bonificacion {salario}")

        def __str__(self):
            return super().__str__() + ", comision $: " + str(self.comision) + ", bonificacion $: " + str(self.bonificacion)
        

    Registrar = registrar

print(Registrar)

insertar = Insertar("","","","","32.000","50.000") 
print(insertar)

print(empleados)
valor_buscar=(input("Buscar empleado: "))
for i in range (5):
    if empleados[i]==valor_buscar:
        print (empleados[i],i)

print(f"lista de  {i}")






