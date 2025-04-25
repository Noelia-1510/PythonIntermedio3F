# Agrego ejercicio #4 de la ejercitacion anterior.
#4 Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.

nombre_archivo = "datos.txt"

try:
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    print(f"Contenido del archivo: {contenido}")
    
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
    print("Creando el archivo...")
    
    archivo = open(nombre_archivo, 'w')
    archivo.write("Contenido del archivo nuevo.")
    archivo.close()
    print(f"Archivo '{nombre_archivo}' creado con exito.")


#1 Calcular el mayor de dos números ingresados por teclado usando un operador ternario.

def calcular_mayor(*args):
    return max(args)

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

resultado = calcular_mayor(num1, num2)
print(f"El numero mayor es: {resultado}")


#2 Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.


def buscar_palabra(palabra, *palabras_lista):
    return f"La palabra buscada es: '{palabra}'" if palabra in palabras_lista else f"No encontrada en la lista"

buscar = input("¿Que palabra estas buscando? ")
lista = input("Escribe varias palabras separadas por espacios: ").split()

print(buscar_palabra(buscar, *lista))


#3 Determinar si un número es par o impar.


def verificar_numeros(*args):
    for num in args:
        print(f"El numero {num} es {'par' if num % 2 == 0 else 'impar'}")

numero = int(input("Ingresa un numero: "))

verificar_numeros(numero)


#4 Calcular el promedio de una lista de números usando args y un operador ternario.


def calcular_promedio(*numeros):
    return 0 if len(numeros) == 0 else sum(numeros) / len(numeros)

try:
    entrada = input("Ingresa numeros separados por espacios: ")
    numeros = []
    for valor in entrada.split():
        try:
            numeros.append(float(valor))
        except ValueError:
            print(f"'{valor}' no es un número y será ignorado.")
    
    if numeros:
        print(f"El promedio es: {calcular_promedio(*numeros)}")
    else:
        print("No ingresaste numeros validos.")
        
except Exception:
    print("Ocurrio un error.")

    
#5 Imprimir un mensaje de error si no se pasan suficientes argumentos.

def pocos_argumentos(**kwargs):
    parametros_necesarios = ["nombre", "edad"]
    
    for parametro in parametros_necesarios:
        if parametro not in kwargs:
            print(f"Error: Falta el parámetro requerido '{parametro}'")
            return None
    
    print(f"Procesando los parámetros: {kwargs}")
    return kwargs

pocos_argumentos(nombre = "Noelia")
