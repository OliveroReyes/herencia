# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase derivada Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Rol: Estudiante, Grado: {self.grado}")

# Clase derivada Profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Rol: Profesor, Asignatura: {self.asignatura}")

# Ejemplo de uso
estudiante = Estudiante("Carlos", 20, "Segundo año")
estudiante.mostrar_informacion()

profesor = Profesor("Dr. González", 45, "Matemáticas")
profesor.mostrar_informacion()
