## 4. Ejercicio Práctico: Expandiendo Nuestra Clase

#La clase `ProcesadorTexto` ya está definida con tres métodos. Tu tarea es agregarle uno nuevo.

# **Consigna:** Añadí el método `calcular_longitud_media(self)` a la clase. Este método debe calcular y devolver la longitud promedio de las palabras en el texto.
#
# **Pista:** la longitud promedio = suma de las longitudes de todas las palabras / cantidad total de palabras.

#**Pasos sugeridos:**

#1.  Copiá la clase completa desde la sección 3 en la celda de abajo.
#2.  Agregale el método `calcular_longitud_media(self)`.
#3.  Probalo con el texto de ejemplo.

#**Preguntas para trabajar con IA:**

#- *"¿Cómo sumo los valores de una lista usando `sum()` y una comprensión de lista?"*
#- *"¿Cómo evito una división por cero si el texto está vacío?"*
#- *"¿Qué hace `:.2f` dentro de un f-string?"*

from ProcesadorTexto import ProcesadorTexto

    
texto = "Python para NLP es genial porque Python es versátil."
procesador = ProcesadorTexto(texto)
#limpiar_texto = procesador.limpiar_texto()
cantidad_palabras = procesador.contar_palabras()
long_media = procesador.calcular_longitud_media()
print(f"La longitud media de las palabras es: {long_media:.2f}")
long_media = procesador.calcular_longitud_media_optimizada()
print(f"La longitud media de las palabras es: {long_media:.2f}")

# Preguntas para trabajar con IA:

#- *"¿Cómo sumo los valores de una lista usando `sum()` y una comprensión de lista?"*

#Sumar valores con una combinación de sum() y list comprehension es una técnica muy poderosa en Python porque te  permite filtrar o transformar los datos antes de sumarlos, todo en una sola línea.

#  por ejemplo  sum(len(p) for p in self.palabras) / len(self.palabras)  rutina optimizada en la clase ProcesadorTexto, donde se calcula la longitud media de las palabras sin necesidad de crear una lista intermedia de longitudes.

#- *"¿Cómo evito una división por cero si el texto está vacío?"*

# debemos verificar si la lista de palabras está vacía antes de realizar la división.
# por ejemplo 
#   if not self.palabras:
#            return 0

#- *"¿Qué hace `:.2f` dentro de un f-string?"*

# es un especificador de formato. Se usa para controlar cómo se muestran los números decimales (tambien redondea el valor)