#1 Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.


def dividir():
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 / num2
        print(resultado)
    except ZeroDivisionError as e:
        print(f"No se puede dividir por 0. {e}")

dividir()


#2 Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.


def sumar():
    try:
        numero = 10
        cadena = "Hola"
        resultado = numero + cadena
        print(resultado)
    except TypeError as e:
        print(f"No se puede sumar un numero y una cadena de texto. {e}")
        
sumar()


#3 Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra.


diccionario = {"nombre" : "Noelia", "apellido" : "Enriquez", "localidad" : "Caseros"}

try:
    print(diccionario["edad"])
except KeyError:
    print(f"La clave no existe en el diccionario.")


#4 Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.



#5 Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.


def dividir_numeros():
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        
        resultado = num1 / num2
        print(f"El resultado es: {resultado}")

    except ValueError as e:
        print(f"Uno de los valores ingresados no es un numero valido. {e}")
    except ZeroDivisionError as z:
        print(f"No es posible dividir por cero. {z}")


dividir_numeros()
















