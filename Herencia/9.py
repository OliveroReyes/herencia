# Clase base Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}
        self.ventas_totales = 0

    def agregar_producto(self, producto, cantidad, precio):
        self.inventario[producto] = {'cantidad': cantidad, 'precio': precio}

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            del self.inventario[producto]

    def mostrar_informacion(self):
        print(f"Tienda: {self.nombre}, Ventas Totales: ${self.ventas_totales}")

# Clase derivada TiendaRopa
class TiendaRopa(Tienda):
    def vender_producto(self, producto, cantidad):
        if producto in self.inventario and self.inventario[producto]['cantidad'] >= cantidad:
            total = cantidad * self.inventario[producto]['precio']
            self.ventas_totales += total
            self.inventario[producto]['cantidad'] -= cantidad
            print(f"Vendido: {producto}, Cantidad: {cantidad}, Total: ${total}")
        else:
            print("Producto no disponible o cantidad insuficiente")

# Clase derivada TiendaElectronica
class TiendaElectronica(Tienda):
    def vender_producto(self, producto, cantidad):
        if producto in self.inventario and self.inventario[producto]['cantidad'] >= cantidad:
            total = cantidad * self.inventario[producto]['precio']
            self.ventas_totales += total
            self.inventario[producto]['cantidad'] -= cantidad
            print(f"Vendido: {producto}, Cantidad: {cantidad}, Total: ${total}")
        else:
            print("Producto no disponible o cantidad insuficiente")

# Ejemplo de uso
tienda_ropa = TiendaRopa("Moda Joven")
tienda_ropa.agregar_producto("Camisa", 10, 20)
tienda_ropa.vender_producto("Camisa", 2)
tienda_ropa.mostrar_informacion()

tienda_electronica = TiendaElectronica("Tech Shop")
tienda_electronica.agregar_producto("Laptop", 5, 800)
tienda_electronica.vender_producto("Laptop", 1)
tienda_electronica.mostrar_informacion()
