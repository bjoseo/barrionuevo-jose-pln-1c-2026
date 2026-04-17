# importar gradio
import gradio as gr
# importar la clase ProcesadorTexto desde el archivo ProcesadorTexto.py
from ProcesadorTexto import ProcesadorTexto

#  función para analizar el texto ingresado por el usuario
def analizar_texto(texto):
    """
    Núcleo de la aplicación.
    Recibe un string de texto, lo procesa con ProcesadorTexto y devuelve dos valores:
    - Un string con el resumen del análisis.
    - Un diccionario con la frecuencia de cada palabra.
    """
    # Condición de seguridad: si el usuario no escribe nada, avisamos.
    if not texto.strip():
        return "Por favor, ingresá texto para analizar.", {}

    # instancia de ProcesadorTexto
    procesador = ProcesadorTexto(texto)
    # 
    # obtener: total de palabras
    total_palabras = procesador.contar_palabras()
    # obteer: palabras únicas 
    palabras_unicas = procesador.contar_palabras_unicas()
    # obtener: diccionario de frecuencias
    frecuencia_diccionario = procesador.calcular_frecuencia()
    # Encontrar la palabra más frecuente
    
    palabra_mas_frecuente = max(frecuencia_diccionario, key=frecuencia_diccionario.get) if frecuencia_diccionario else None

    frecuencia_mas_frecuente = frecuencia_diccionario[palabra_mas_frecuente] if palabra_mas_frecuente else 0            

    # --- Resumen del Análisis ---

    resumen = f"""--- Resumen del Análisis ---
                Total de Palabras: {total_palabras}
                Palabras Únicas: {palabras_unicas}
                Palabra Más Frecuente: '{palabra_mas_frecuente}' ({frecuencia_mas_frecuente} veces)"""  

    # la funcion retorna resumen, frecuencia_diccionario
    return resumen, frecuencia_diccionario

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
#demo.launch(share=True)      # Crea un enlace público temporal (requiere internet)