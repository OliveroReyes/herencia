# Clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        pass  # Método abstracto

    def mostrar_detalles(self):
        print(f"Animal: {self.nombre}")

# Clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        print("Guau!")

# Clase derivada Gato
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def emitir_sonido(self):
        print("Miau!")

# Ejemplo de uso
perro = Perro("Firulais")
perro.mostrar_detalles()
perro.emitir_sonido()

gato = Gato("Misu")
gato.mostrar_detalles()
gato.emitir_sonido()
