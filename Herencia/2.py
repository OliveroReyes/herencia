# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {self.salario}")

# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Gerente")

    def aumento_salario(self):
        # Aumento del 20% para gerentes
        self.salario *= 1.20

# Clase derivada EmpleadoTemporal
class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Empleado Temporal")

    def aumento_salario(self):
        # Aumento del 10% para empleados temporales
        self.salario *= 1.10

# Ejemplo de uso
gerente = Gerente("Juan", 5000)
gerente.aumento_salario()
gerente.mostrar_detalles()

empleado_temporal = EmpleadoTemporal("Ana", 3000)
empleado_temporal.aumento_salario()
empleado_temporal.mostrar_detalles()
