# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")

# Clase derivada Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, eficiencia_combustible):
        super().__init__(marca, modelo, año)
        self.eficiencia_combustible = eficiencia_combustible  # km por litro

    def calcular_combustible(self, distancia):
        return distancia / self.eficiencia_combustible

# Clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, eficiencia_combustible):
        super().__init__(marca, modelo, año)
        self.eficiencia_combustible = eficiencia_combustible  # km por litro

    def calcular_combustible(self, distancia):
        return distancia / self.eficiencia_combustible

# Ejemplo de uso
auto = Automovil("Toyota", "Corolla", 2022, 15)
auto.mostrar_detalles()
print("Combustible necesario para 150 km:", auto.calcular_combustible(150), "litros")

moto = Motocicleta("Yamaha", "FZ", 2021, 25)
moto.mostrar_detalles()
print("Combustible necesario para 150 km:", moto.calcular_combustible(150), "litros")
