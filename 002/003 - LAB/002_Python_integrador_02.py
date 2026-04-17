# importar gradio
import gradio as gr
# importar la clase ProcesadorTexto desde el archivo ProcesadorTexto.py
from ProcesadorTexto import ProcesadorTexto

def analizar_texto(texto):
    if not texto.strip():
        return "Error: Texto vacío", {}

    datos = ProcesadorTexto(texto).generar_reporte()
    
    resumen = f"""--- Resumen ---
Total: {datos['total']}
Únicas: {datos['unicas']}
Top: '{datos['top_palabra']}' ({datos['top_frecuencia']} veces)"""

    return resumen, datos['frecuencias']

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