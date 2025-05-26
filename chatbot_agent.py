from flask import Flask, request, jsonify, render_template
from datetime import datetime
import requests

app = Flask(__name__)

API_KEY = "de20275bf5e92a4cecb6bd1703f451c4"  # Pon tu API Key de OpenWeatherMap

def obtener_clima(ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        if datos.get("cod") != 200:
            return "No pude obtener el clima en este momento."
        descripcion = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        return f"En {ciudad.title()}, hace {descripcion} con {temperatura}°C."
    except:
        return "Hubo un error al conectar con el servicio del clima."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    entrada = request.json.get("mensaje", "").lower()
    
      if entrada == "hola":
        print("Chatbot: ¡Hola! ¿En qué puedo ayudarte hoy?")

    elif entrada == "¿qué es ia?" or entrada == "que es ia":
        print("Chatbot: La IA es la simulación de la inteligencia humana por parte de las máquinas.")

    elif entrada == "¿quién eres?" or entrada == "quien eres":
        print("Chatbot: Soy un chatbot de IA simple.")

    elif entrada in ["¿qué hora es?", "que hora es", "qué hora es", "¿que hora es?"]:
        hora_actual = datetime.now().strftime("%H:%M")
        print(f"Chatbot: La hora actual es {hora_actual}.")

    elif entrada == "¿qué fecha es hoy?" or entrada == "que fecha es hoy":
        hoy = datetime.now().strftime("%d/%m/%Y")
        print(f"Chatbot: La fecha de hoy es {hoy}.")

    elif entrada.startswith("clima en ")or entrada == "cual es el clima":
        ciudad = entrada.replace("clima en ", "")
        api_key = "de20275bf5e92a4cecb6bd1703f451c4"  
        clima = obtener_clima(ciudad, api_key)
        print(f"Chatbot: {clima}")

    elif entrada == "ayuda":
        print("Chatbot: Puedes preguntarme cosas sobre la inteligencia artificial.")

    elif entrada == "¿cómo estás?" or entrada == "como estas":
        print("Chatbot: ¡Solo soy código, pero estoy funcionando perfectamente!")

    elif entrada == "¿quién te creó?" or entrada == "quien te creo":
        print("Chatbot: Fui creado como parte de una actividad de laboratorio para demostrar agentes de IA.")

    elif entrada == "define agente":
        print("Chatbot: Un agente es cualquier cosa que percibe su entorno y actúa sobre él.")

    elif entrada == "¿qué es un sensor?" or entrada == "que es input":
        print("Chatbot: En este chatbot, el sensor es la función input(), que captura lo que escribe el usuario.")

    elif entrada == "¿qué es un programa?" or entrada == "que es if/elif":
        print("Chatbot: El programa es la parte que decide qué hacer con la entrada. Aquí usamos if/elif para eso.")

    elif entrada == "¿qué es un actuador?" or entrada == "que es print":
        print("Chatbot: El actuador en este chatbot es print(), que muestra la respuesta al usuario.")

    elif entrada == "¿qué significa array?" or entrada == "que significa array":
        print("Chatbot: Un array es una estructura que almacena múltiples elementos en una sola variable, como una lista en Python.")

    elif entrada == "¿qué significa randint?" or entrada == "que significa randint":
        print("Chatbot: randint es una función del módulo random que genera un número entero aleatorio entre dos valores dados.")

    elif entrada == "¿qué significa radiant?" or entrada == "que significa radiant":
        print("Chatbot: radiant puede referirse a radianes, una unidad para medir ángulos. En Python, se usa en cálculos trigonométricos.")

    elif entrada == "¿qué es hstrack?" or entrada == "que significa hstrack":
        print("Chatbot: hstrack probablemente se refiere a 'horizontal stack' (pila horizontal), usado en gráficos o interfaces para ordenar elementos.")

    elif entrada == "¿qué es vstrack?" or entrada == "que significa vstrack":
        print("Chatbot: vstrack se refiere a 'vertical stack' (pila vertical), para colocar elementos unos debajo de otros.")

    elif entrada == "¿qué significa ==?" or entrada == "que significa ==":
        print("Chatbot: '==' es un operador de comparación en Python. Compara si dos valores son iguales.")

    elif entrada == "¿qué significa while?" or entrada == "que significa while":
        print("Chatbot: 'while' es un bucle que repite un bloque de código mientras se cumpla una condición.")

    elif entrada == "¿qué significa if?" or entrada == "que significa if":
        print("Chatbot: 'if' es una estructura de decisión que ejecuta un bloque de código si se cumple una condición.")

    elif entrada == "¿qué significa else?" or entrada == "que significa else":
        print("Chatbot: 'else' se usa para definir qué hacer si la condición del 'if' no se cumple.")

    elif entrada == "adiós" or entrada == "adios":
        print("Chatbot: ¡Adiós! ¡Que tengas un excelente día!")
        break

    else:
        print("Chatbot: No estoy seguro de cómo responder a eso. Intenta preguntarme otra cosa.")

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
