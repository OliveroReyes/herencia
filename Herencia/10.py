from datetime import date

# Clase base Pago
class Pago:
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha

    def mostrar_detalles(self):
        print(f"Monto: ${self.monto}, Fecha: {self.fecha}")

# Clase derivada PagoTarjeta
class PagoTarjeta(Pago):
    def __init__(self, monto, fecha, numero_tarjeta):
        super().__init__(monto, fecha)
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self):
        print("Procesando pago con tarjeta...")

    def generar_recibo(self):
        print(f"Recibo: Pago con tarjeta de ${self.monto} el {self.fecha}")

# Clase derivada PagoPayPal
class PagoPayPal(Pago):
    def __init__(self, monto, fecha, email):
        super().__init__(monto, fecha)
        self.email = email

    def procesar_pago(self):
        print("Procesando pago con PayPal...")

    def generar_recibo(self):
        print(f"Recibo: Pago con PayPal de ${self.monto} el {self.fecha}")

# Ejemplo de uso
pago_tarjeta = PagoTarjeta(100, date.today(), "1234-5678-9876-5432")
pago_tarjeta.procesar_pago()
pago_tarjeta.generar_recibo()
pago_tarjeta.mostrar_detalles()

pago_paypal = PagoPayPal(50, date.today(), "correo@ejemplo.com")
pago_paypal.procesar_pago()
pago_paypal.generar_recibo()
pago_paypal.mostrar_detalles()
