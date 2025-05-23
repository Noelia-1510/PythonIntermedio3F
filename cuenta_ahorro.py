from cuenta_bancaria import CuentaBancaria

class CuentaAhorro (CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001

    
    def _aplicar_interes(self):
        interes_ganado = self._saldo * self._tasa_interes
        self._saldo += interes_ganado
        print(f"Se han aplicado intereses a su cuenta de ahorro. Su saldo actual es: {self._saldo}")
    

    def obtener_saldo(self):
        self._aplicar_interes()
        return super().obtener_saldo()
    
    def depositar(self,monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado ${monto} a la cuenta de {self._nombre_titular}.")
            self._aplicar_interes()
            print(f"Su nuevo saldo con intereses es de: ${self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def extraer(self,monto):
        saldo_actual_para_extraccion = self.obtener_saldo()
        
        if monto > 0 and monto <= saldo_actual_para_extraccion:
            self._saldo -= monto
            print(f"Se ha extraído ${monto} de su cuenta.")
            self._aplicar_interes()
            print(f"Su nuevo saldo con intereses es de: ${self.obtener_saldo()}")
        elif monto <= 0:
            print("El monto a extraer debe ser mayor a 0.")
        else:
            print(f"Usted no posee saldo suficiente para realizar la operación. Saldo actual: ${saldo_actual_para_extraccion}, Monto a extraer: ${monto}")

