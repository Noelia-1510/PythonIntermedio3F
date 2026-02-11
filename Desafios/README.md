# 🚀 Desafíos de Python Intermedio

En esta carpeta se encuentra la resolución de los desafíos lógicos y prácticos desarrollados durante el curso. El contenido demuestra un dominio de las estructuras de datos, el manejo de errores y la arquitectura de software bajo el paradigma de POO.

---

## 🏗️ Proyecto: Sistema de Gestión Bancaria (POO)
Este conjunto de archivos representa un sistema de cuentas bancarias donde se aplican los pilares de la **Programación Orientada a Objetos**:

* **`cuenta_bancaria.py`**: Clase base abstracta (`ABC`) que define la estructura principal (titular, DNI, saldo) y utiliza la librería `datetime` para el cálculo de edad.
* **`cuenta_ahorro.py`**: Clase hija que implementa una **tasa de interés automática** (0.1%) aplicada en cada depósito o consulta de saldo.
* **`cuenta_corriente.py`**: Clase hija que incluye un **límite de extracción** configurable para mayor seguridad.
* **`prueba_ca.py` / `prueba_cc.py`**: Scripts de prueba para verificar depósitos, extracciones y la lógica de intereses.

---

## 📝 Guías de Ejercitación
Resolución de problemas prácticos sobre lógica y sintaxis avanzada de Python:

### 🔹 [Práctica 1: Estructuras de Datos](./practica1_python_intermedio.py)
* Uso intensivo de **Sets (Conjuntos)**.
* Implementación de operaciones de Unión (`|`), Intersección (`&`), Diferencia Simétrica y validación de subconjuntos (`issubset`).

### 🔹 [Práctica 2: Robustez y Excepciones](./practica2_python_intermedio.py)
* Implementación de bloques `try-except` para un código a prueba de errores.
* Manejo específico de: `ZeroDivisionError`, `TypeError`, `ValueError` y `KeyError`.

### 🔹 [Práctica 3: Funciones y Archivos](./practica3_python_intermedio.py)
* Uso de **operadores ternarios** para simplificar la lógica.
* Implementación de argumentos variables (`*args` y `**kwargs`).
* **Manejo de archivos**: Lógica para abrir archivos existentes o crearlos automáticamente en caso de que no existan (`FileNotFoundError`).

---

## 🛠️ Tecnologías y Conceptos Aplicados
* **Python 3.x**
* **Paradigma POO:** Herencia, Polimorfismo y Abstracción.
* **Persistencia:** Manejo básico de lectura y escritura de archivos `.txt`.
* **Clean Code:** Nombramiento de variables en *snake_case* y código documentado.
