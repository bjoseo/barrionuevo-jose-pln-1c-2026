# **Consigna:** A partir del texto dado, escribí un programa que lo convierta a minúsculas, lo divida en palabras y # #               cuente cuántas veces aparece cada una.
#
# El resultado debe ser un diccionario donde las claves sean las palabras y los valores sean sus frecuencias.

texto = "A partir del texto dado, dado escribí un programa que lo convierta a minúsculas, lo divida en palabras y         cuente cuántas veces aparece cada una. una " \
"El resultado debe ser un diccionario donde las claves sean las palabras y los valores sean sus frecuencias "

VERDE = "\033[92m"
NEGRITA = "\033[1m"
RESET = "\033[0m"
# Convertimos a minúsculas
texto_limpio = texto.lower()

# Dividimos el texto en una lista de palabras
palabras = texto_limpio.split()

# Creamos un diccionario para contar las frecuencias
frecuencias = {}

for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1  # Si ya existe, sumamos 1
    else:
        frecuencias[p] = 1   # Si no existe, la creamos con valor 1

print("\n" + "*" * 33)
print(f"{VERDE}{NEGRITA}---  FRECUENCIAS DE PALABRAS  ---{RESET}".center(40, "*"))
print("*" * 33 + "\n")
#print("Frecuencias de palabras:")
print(frecuencias)
#print()

# En Python existe una herramienta llamada Counter que hace exactamente esto en una sola línea. Es muy útil conocerla para cuando se trabaja con muchos datos:

from collections import Counter

# Esto hace todo el trabajo del bucle for automáticamente
resultado = Counter(texto.lower().split())

print("\n" + "*" * 46)
print(f"{VERDE}{NEGRITA}---  FRECUENCIAS DE PALABRAS (con Counter) ---{RESET}".center(40, "*"))
print("*" * 46 + "\n")

print(dict(resultado))

# "¿funcion para vaciar el diccionario de frecuencias para contar otro texto?"*
def resetear_conteo():
    frecuencias.clear()

# "¿Para qué sirve `dict.get(clave, 0)` al contar frecuencias?"*

# El método `dict.get(clave, valor_por_defecto)` se utiliza para obtener el valor asociado a una clave en un diccionario. Si la clave no existe, devuelve el valor por defecto que se le haya especificado (en este caso, 0).

# Opción elegante con .get()
resetear_conteo()
for p in palabras:
    frecuencias[p] = frecuencias.get(p, 0) + 1  # Si la clave no existe, devuelve 0 y luego suma 1
print("\n" + "*" * 45)
print(f"{VERDE}{NEGRITA}---  FRECUENCIAS DE PALABRAS (con .get()) ---{RESET}".center(40, "*"))
print("*" * 45 + "\n")

print(frecuencias)


# "¿Cómo ordenar un diccionario por sus valores de mayor a menor?"*

# Para ordenar un diccionario por sus valores de mayor a menor, puedes usar la función `sorted()` junto con una función lambda para especificar que quieres ordenar por los valores. Aquí te muestro cómo hacerlo:

# Ordenamos el diccionario por sus valores de mayor a menor

frecuencias_ordenadas = dict(sorted(frecuencias.items(), key=lambda item: item[1], reverse=True))

print("\n" + "*" * 44)
print(f"{VERDE}{NEGRITA}---  FRECUENCIAS DE PALABRAS (ordenadas) ---{RESET}".center(40, "*"))
print("*" * 44 + "\n")

print(frecuencias_ordenadas)


# "¿Hay una forma más concisa de hacer un conteo de frecuencias en Python?"*

# Sí, se puede usar la clase `Counter` del módulo `collections` para hacer un conteo de frecuencias de manera más concisa y eficiente. Se muestra en el codigo anterior.
