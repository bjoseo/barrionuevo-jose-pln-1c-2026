# Definición ÚNICA de la clase. Esta celda es la referencia para todo el notebook.
class ProcesadorTexto:
    """Encapsula un texto y expone operaciones de análisis lingüístico básico."""

    def __init__(self, texto):
        # Nota sobre limpieza: strip() solo elimina caracteres en los extremos del string.
        # Para limpiar puntuación en todo el texto usamos replace(), igual que en limpiar_texto().
        #print(f"Creando procesador para: '{texto[:40]}...'")
        self.texto_original = texto
        caracteres_a_eliminar = ['.', ',', '!', '?', ';', ':', '¿', '¡', '"', "'", '(', ')']
        texto_limpio = texto.strip()
        texto_limpio = texto_limpio.lower()
        for char in caracteres_a_eliminar:
            texto_limpio = texto_limpio.replace(char, '')
        self.texto_limpio = texto_limpio
        self.palabras = self.texto_limpio.split()

    def contar_palabras(self):
        """Devuelve el total de palabras (con repeticiones)."""
        return len(self.palabras)

    def contar_palabras_unicas(self):
        """Devuelve la cantidad de palabras distintas. `set` elimina duplicados."""
        return len(set(self.palabras))

    def calcular_frecuencia(self):
        """Devuelve un diccionario con la frecuencia de cada palabra."""
        frecuencia = {}
        for palabra in self.palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
        return frecuencia

    def calcular_longitud_media(self):
        """Devuelve la longitud promedio de las palabras en el texto."""
        if not self.palabras:
            return 0
        longitudes = [len(palabra) for palabra in self.palabras]
        return sum(longitudes) / len(longitudes)  

    def calcular_longitud_media_optimizada(self):
        """Devuelve la longitud promedio de las palabras en el texto."""
        if not self.palabras:
            return 0
        # Sumamos las longitudes directamente y dividimos por la cantidad de palabras
        return sum(len(p) for p in self.palabras) / len(self.palabras)  
    def resetear_conteo(self):
        self.frecuencias.clear()
    def generar_reporte(self):
        frec = self.calcular_frecuencia()
        top = max(frec, key=frec.get) if frec else "N/A"
        return {
            "total": self.contar_palabras(),
            "unicas": self.contar_palabras_unicas(),
            "top_palabra": top,
            "top_frecuencia": frec.get(top, 0),
            "frecuencias": frec
        }
