import math

# Clase base Figura
class Figura:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def imprimir_detalles(self):
        print(f"Figura: {self.nombre}, Color: {self.color}")

# Clase derivada Círculo
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__("Círculo", color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Radio: {self.radio}, Área: {self.area()}, Perímetro: {self.perimetro()}")

# Clase derivada Rectángulo
class Rectangulo(Figura):
    def __init__(self, color, largo, ancho):
        super().__init__("Rectángulo", color)
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Largo: {self.largo}, Ancho: {self.ancho}, Área: {self.area()}, Perímetro: {self.perimetro()}")

# Ejemplo de uso
circulo = Circulo("rojo", 5)
circulo.imprimir_detalles()

rectangulo = Rectangulo("azul", 4, 6)
rectangulo.imprimir_detalles()
