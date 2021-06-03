# Cuarto: Crear una clase que permita Matricula con la siguiente información
# · -código matricula
# · -nombre completos
# · -Dirección
# · -Teléfono
# · Curso
# - Deberá realizar el constructor de la clase.
# - El método de inscripción
# - El método de consulta
# - El método de eliminación de la matricula.
class Matricula:
    def __init__(self, codigoMatricula, nombreCompleto, direccion, telefono, curso):
        self.CodigoMatricula = codigoMatricula
        self.NombreCompleto = nombreCompleto
        self.Direccion = direccion
        self.Telefono = telefono
        self.Curso = curso
        self.matriculaAlumno = {}

    def inscripcion(self):
        self.matriculaAlumno['Codigo Matricula'] = self.CodigoMatricula
        self.matriculaAlumno['Nombre completo'] = self.NombreCompleto
        self.matriculaAlumno['Direccion'] = self.Direccion
        self.matriculaAlumno['Telefono'] = self.Telefono
        self.matriculaAlumno['Curso'] = self.Curso
        return 'Se Agrego la matricula'

    def consulta(self):
        return f'Matricula consultada correctamente {self.matriculaAlumno}'

    def eliminar(self):
    
        return f'Matricula eliminada correctamente { self.matriculaAlumno.clear()}'



matricula = Matricula(2918,'cinthia estefania sanchez','cra 30 # 09', 29101283, 'artes')

print(matricula.NombreCompleto)
print(matricula.inscripcion())
print(matricula.consulta())
print(matricula.eliminar())
print(matricula.matriculaAlumno)