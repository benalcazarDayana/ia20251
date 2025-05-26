import requests
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# 🔧 Función para obtener el clima
def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        if respuesta.status_code == 200:
            descripcion = datos["weather"][0]["description"]
            temperatura = datos["main"]["temp"]
            return f"El clima en {ciudad.title()} es {descripcion}, con una temperatura de {temperatura}°C."
        elif datos.get("message") == "city not found":
            return "No encontré esa ciudad. Verifica que esté bien escrita."
        else:
            return "No pude obtener el clima en este momento."
    except Exception as e:
        return f"Error al consultar el clima: {str(e)}"

# 💬 Procesamiento de entrada del usuario
def procesar_entrada():
    entrada = entrada_texto.get().lower()
    entrada_texto.delete(0, tk.END)
    mostrar_conversacion(f"Tú: {entrada}")

    if entrada == "salir":
        ventana.quit()
    elif entrada == "hola":
        mostrar_conversacion("Chatbot: ¡Hola! ¿En qué puedo ayudarte hoy?")
    elif entrada in ["¿qué es ia?", "que es ia"]:
        mostrar_conversacion("Chatbot: La IA es la simulación de la inteligencia humana por parte de las máquinas.")
    elif entrada in ["¿quién eres?", "quien eres"]:
        mostrar_conversacion("Chatbot: Soy un chatbot de IA simple.")
    elif entrada in ["¿qué hora es?", "qué hora es", "que hora es", "¿que hora es?"]:
        hora_actual = datetime.now().strftime("%H:%M")
        mostrar_conversacion(f"Chatbot: La hora actual es {hora_actual}.")
    elif entrada in ["¿qué fecha es hoy?", "que fecha es hoy"]:
        hoy = datetime.now().strftime("%d/%m/%Y")
        mostrar_conversacion(f"Chatbot: La fecha de hoy es {hoy}.")
    elif entrada.startswith("clima en "):
        ciudad = entrada.replace("clima en ", "")
        api_key = "de20275bf5e92a4cecb6bd1703f451c4"  # Tu API key
        clima = obtener_clima(ciudad, api_key)
        mostrar_conversacion(f"Chatbot: {clima}")
    elif entrada == "cual es el clima":
        mostrar_conversacion("Chatbot: Especifica la ciudad, por ejemplo: clima en Quito")
    elif entrada == "ayuda":
        mostrar_conversacion("Chatbot: Puedes preguntarme sobre IA, clima, hora, fecha, o conceptos de programación.")
    elif entrada in ["¿cómo estás?", "como estas"]:
        mostrar_conversacion("Chatbot: ¡Solo soy código, pero estoy funcionando perfectamente!")
    elif entrada in ["¿quién te creó?", "quien te creo"]:
        mostrar_conversacion("Chatbot: Fui creado como parte de una actividad de laboratorio para demostrar agentes de IA.")
    elif entrada == "define agente":
        mostrar_conversacion("Chatbot: Un agente es cualquier cosa que percibe su entorno y actúa sobre él.")
    elif entrada in ["¿qué es un sensor?", "que es input"]:
        mostrar_conversacion("Chatbot: El sensor en este chatbot es la función input(), que captura lo que escribe el usuario.")
    elif entrada in ["¿qué es un programa?", "que es if/elif"]:
        mostrar_conversacion("Chatbot: El programa decide qué hacer con la entrada. Usamos if/elif para eso.")
    elif entrada in ["¿qué es un actuador?", "que es print"]:
        mostrar_conversacion("Chatbot: El actuador es print(), que muestra la respuesta al usuario.")
    elif entrada in ["¿qué significa array?", "que significa array"]:
        mostrar_conversacion("Chatbot: Un array es como una lista en Python, almacena varios elementos.")
    elif entrada in ["¿qué significa randint?", "que significa randint"]:
        mostrar_conversacion("Chatbot: randint genera un número entero aleatorio entre dos valores dados.")
    elif entrada in ["¿qué significa radiant?", "que significa radiant"]:
        mostrar_conversacion("Chatbot: Puede referirse a radianes, unidad para medir ángulos.")
    elif entrada in ["¿qué es hstrack?", "que significa hstrack"]:
        mostrar_conversacion("Chatbot: Puede referirse a 'horizontal stack', usado en interfaces gráficas.")
    elif entrada in ["¿qué es vstrack?", "que significa vstrack"]:
        mostrar_conversacion("Chatbot: 'Vertical stack', disposición vertical de elementos.")
    elif entrada in ["¿qué significa ==?", "que significa =="]:
        mostrar_conversacion("Chatbot: Es un operador para comparar si dos valores son iguales.")
    elif entrada in ["¿qué significa while?", "que significa while"]:
        mostrar_conversacion("Chatbot: 'while' es un bucle que repite un bloque de código mientras una condición sea verdadera.")
    elif entrada in ["¿qué significa if?", "que significa if"]:
        mostrar_conversacion("Chatbot: 'if' es una estructura condicional que evalúa si una condición es verdadera.")
    elif entrada in ["¿qué significa else?", "que significa else"]:
        mostrar_conversacion("Chatbot: 'else' indica qué hacer cuando la condición del 'if' no se cumple.")
    elif entrada in ["adiós", "adios"]:
        mostrar_conversacion("Chatbot: ¡Adiós! ¡Que tengas un excelente día!")
        ventana.quit()
    else:
        mostrar_conversacion("Chatbot: No estoy seguro de cómo responder a eso. Intenta preguntarme otra cosa.")

# 🖼️ Mostrar conversación en el cuadro de texto
def mostrar_conversacion(texto):
    conversacion.config(state=tk.NORMAL)
    conversacion.insert(tk.END, texto + "\n")
    conversacion.config(state=tk.DISABLED)
    conversacion.see(tk.END)

# 🎨 Interfaz gráfica
ventana = tk.Tk()
ventana.title("Chatbot de IA - Aprendizaje Básico")
ventana.geometry("550x500")
ventana.configure(bg="#e3f2fd")

titulo = tk.Label(ventana, text="🤖 Chatbot de IA - Aprendizaje Interactivo", font=("Arial", 14, "bold"), bg="#e3f2fd")
titulo.pack(pady=10)

conversacion = scrolledtext.ScrolledText(ventana, width=65, height=20, wrap=tk.WORD, state=tk.DISABLED)
conversacion.pack(pady=10)

frame_input = tk.Frame(ventana, bg="#e3f2fd")
frame_input.pack(pady=5)

entrada_texto = tk.Entry(frame_input, width=45, font=("Arial", 12))
entrada_texto.grid(row=0, column=0, padx=5)

btn_enviar = tk.Button(frame_input, text="Enviar", command=procesar_entrada, bg="#64b5f6", font=("Arial", 11))
btn_enviar.grid(row=0, column=1)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, bg="#ef5350", font=("Arial", 11), width=10)
btn_salir.pack(pady=10)

# Mensaje inicial
mostrar_conversacion("Chatbot: ¡Hola! Soy tu agente de IA. Escribe algo como 'clima en Quito', '¿qué es IA?', '¿qué hora es?'...")

ventana.mainloop()