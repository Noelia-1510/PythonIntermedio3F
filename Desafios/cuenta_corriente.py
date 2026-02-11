from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def extraer(self, monto):
        if monto <= self._saldo and monto <= self._limite_extraccion:
            self._saldo -= monto
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto, se excede el limite.")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")

    def depositar(self,monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado ${monto} a la cuenta, su saldo actual es de: ${self.obtener_saldo()}")
        else:
            print("No se puede depositar saldo negativo en la cuenta.")



