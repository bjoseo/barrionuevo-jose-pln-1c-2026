#**Consigna:** Escribí un programa que reciba una frase del usuario y evalúe dos condiciones:
# 1. Si la frase contiene la palabra `"Python"`.
# 2. Si la frase es corta (menos de 20 caracteres).
#
# El programa debe imprimir un mensaje diferente para cada situación.

# Pedí al usuario que ingrese una frase
frase_usuario = input("Por favor, ingresa una frase: ")

# longitud de la frase
longitud_frase = len(frase_usuario)

print(f"La frase tiene {longitud_frase} caracteres.")

if "python" in frase_usuario.lower():
    print("La frase menciona a Python.")
else:
    print("Esta frase no menciona a Python.")

# Evaluamos la longitud de la frase
# La función len() cuenta la cantidad de caracteres
if len(frase_usuario) < 20:
    print("La frase es corta (tiene menos de 20 caracteres).")
else:
    print("La frase es larga (tiene 20 caracteres o más).")

#"¿Por qué `'python' in frase` y `'Python' in frase` pueden dar distintos resultados? ¿Cómo se soluciona?"*

# Esto ocurre porque en la mayoría de los lenguajes de programación, incluido Python, las comparaciones de texto son # Case-Sensitive (sensibles a mayúsculas y minúsculas).

# La forma más común y profesional de solucionar esto es la normalización. Consiste en convertir tanto la frase del # # usuario como tu palabra clave al mismo formato (generalmente todo a minúsculas) antes de compararlas.

# Opción A: Usar .lower() (La más común)
# Opción B: Usar .casefold() (Para proyectos internacionales)


#"¿Puedo combinar la condición de longitud y la de pertenencia en un solo `if`? ¿Cómo?"*

# 1. Usando and (Ambas deben cumplirse)

frase = input("Ingresá tu frase (deben cumplirse ambas condiciones): ")

if "python" in frase.lower() and len(frase) < 20:
    print("contiene Python y es corta.")
else:
    print("No cumple con ambas condiciones.")

# 2. Usando or (Al menos una debe cumplirse)

frase = input("Ingresá tu frase (deben cumplirse al menos una de lasgfg condiciones): ")

if "python" in frase.lower() or len(frase) < 20:
    print("La frase cumple con al menos uno de los requisitos.")


#"¿Qué hace `len()` cuando se aplica a un string?"*

# El trabajo de la funcion len() es contar la cantidad total de caracteres que componen esa cadena.
# incluye el conteo de Letras,Espacios en blanco,Signos de puntuación,Números y símbolos