from datetime import datetime

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, fecha_de_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_de_vencimiento = fecha_de_vencimiento

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Fecha de Vencimiento: {self.fecha_de_vencimiento}")

# Clase derivada ProductoAlimenticio
class ProductoAlimenticio(Producto):
    def aplicar_descuento(self):
        # Descuento del 20% si el producto vence en una semana
        hoy = datetime.now().date()
        dias_restantes = (self.fecha_de_vencimiento - hoy).days
        if dias_restantes <= 7:
            self.precio *= 0.8

# Clase derivada ProductoElectronico
class ProductoElectronico(Producto):
    def aplicar_descuento(self):
        # Descuento del 10% si el producto tiene más de un año
        hoy = datetime.now().date()
        if hoy.year - self.fecha_de_vencimiento.year >= 1:
            self.precio *= 0.9

# Ejemplo de uso
fecha_vencimiento_alimento = datetime(2024, 11, 15).date()
alimento = ProductoAlimenticio("Leche", 50, fecha_vencimiento_alimento)
alimento.aplicar_descuento()
alimento.mostrar_detalles()

fecha_vencimiento_electronico = datetime(2023, 10, 30).date()
electronico = ProductoElectronico("Laptop", 1000, fecha_vencimiento_electronico)
electronico.aplicar_descuento()
electronico.mostrar_detalles()
