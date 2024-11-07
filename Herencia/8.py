# Clase base Transporte
class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def calcular_tiempo_viaje(self, distancia):
        return distancia / self.velocidad_maxima

# Clase derivada Avion
class Avion(Transporte):
    def __init__(self, capacidad, velocidad_maxima):
        super().__init__(capacidad, velocidad_maxima)

# Clase derivada Barco
class Barco(Transporte):
    def __init__(self, capacidad, velocidad_maxima):
        super().__init__(capacidad, velocidad_maxima)

# Ejemplo de uso
avion = Avion(150, 800)  # 800 km/h
print("Tiempo de viaje en avión para 1600 km:", avion.calcular_tiempo_viaje(1600), "horas")

barco = Barco(300, 50)  # 50 km/h
print("Tiempo de viaje en barco para 1600 km:", barco.calcular_tiempo_viaje(1600), "horas")
