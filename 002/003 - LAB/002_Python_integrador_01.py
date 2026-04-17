# importar gradio
import gradio as gr
# importar la clase ProcesadorTexto desde el archivo ProcesadorTexto.py
from ProcesadorTexto import ProcesadorTexto

def analizar_texto(texto):
    if not texto.strip():
        return "Por favor, ingresá texto para analizar.", {}

    proc = ProcesadorTexto(texto)
    
    # Obtenemos el diccionario una sola vez
    frecuencias = proc.calcular_frecuencia()
    
    # Simplificamos la búsqueda de la palabra más frecuente
    if frecuencias:
        top_word = max(frecuencias, key=frecuencias.get)
        top_count = frecuencias[top_word]
    else:
        top_word, top_count = "N/A", 0

    # Usamos un f-string más limpio (sin tantos espacios al principio de cada línea)
    resumen = (
        f"--- Resumen del Análisis ---\n"
        f"Total de Palabras: {proc.contar_palabras()}\n"
        f"Palabras Únicas: {proc.contar_palabras_unicas()}\n"
        f"Palabra Más Frecuente: '{top_word}' ({top_count} veces)"
    )

    return resumen, frecuencias

# Configurar la Interfaz de Gradio ---
demo = gr.Interface(
    fn=analizar_texto,

    inputs=gr.Textbox(
        lines=10,
        placeholder="Escribí o pegá un texto acá para analizarlo...",
        label="Texto a analizar"
    ),

    outputs=[
        gr.Textbox(label="Resumen del Análisis"),
        gr.JSON(label="Frecuencia de Palabras")
    ],

    title="Analizador de Texto",
    description="Introducí un texto y obtené un análisis básico de PLN.",
    flagging_mode="never"
)

# Descomentá la línea que corresponda a tu entorno:
# demo.launch()                # En Google Colab (crea una URL pública temporal con share=True)
demo.launch(inbrowser=True)  # En entorno local: abre el navegador automáticamente
# demo.launch(share=True)      # Crea un enlace público temporal (requiere internet)