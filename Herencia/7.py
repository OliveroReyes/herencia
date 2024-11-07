# Clase base Instrumento
class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def tipo_sonido(self):
        print("Sonido musical")

# Clase derivada Guitarra
class Guitarra(Instrumento):
    def __init__(self, material):
        super().__init__("Guitarra", material)

    def tocar_nota(self, nota):
        print(f"Tocando nota {nota} en la guitarra")

# Clase derivada Piano
class Piano(Instrumento):
    def __init__(self, material):
        super().__init__("Piano", material)

    def tocar_nota(self, nota):
        print(f"Tocando nota {nota} en el piano")

# Ejemplo de uso
guitarra = Guitarra("Madera")
guitarra.tipo_sonido()
guitarra.tocar_nota("Do")

piano = Piano("Metal")
piano.tipo_sonido()
piano.tocar_nota("Sol")
