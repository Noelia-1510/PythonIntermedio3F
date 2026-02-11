from cuenta_corriente import CuentaCorriente
from datetime import date, datetime


cuenta_corriente = CuentaCorriente ("Valentino","123456789", "1995/09/25", 1000)
print(f"Titular de la cuenta: {cuenta_corriente._nombre_titular} ")
print(f"Edad: {cuenta_corriente.obtener_edad()} años")
print(f"Saldo inicial: ${cuenta_corriente.obtener_saldo()}")

cuenta_corriente.depositar(200)
cuenta_corriente.extraer(500)
cuenta_corriente.extraer(1000) # Falla por exceder el límite de extracción.
cuenta_corriente.extraer(700) # Falla por falta de saldo.
print(f"Saldo final cuenta corriente: ${cuenta_corriente.obtener_saldo()}")
