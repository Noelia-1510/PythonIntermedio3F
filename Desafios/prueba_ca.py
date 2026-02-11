from cuenta_corriente import CuentaCorriente
from cuenta_ahorro import CuentaAhorro


cuenta_ahorro = CuentaAhorro("Lucia", "56824234", "1989/01/15", 5000)
print(f"Titular: {cuenta_ahorro._nombre_titular}")
print(f"Edad: {cuenta_ahorro.obtener_edad()} años")
print(f"Saldo inicial con intereses: ${cuenta_ahorro.obtener_saldo()}")

cuenta_ahorro.depositar(1000) 
cuenta_ahorro.extraer(500) 
cuenta_ahorro.extraer(6000) 

print(f"Saldo final cuenta de ahorro con intereses: ${cuenta_ahorro.obtener_saldo()}")
