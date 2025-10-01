# Chat con Mistral

from huggingface_hub import InferenceClient

HF_TOKEN = "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"

client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2", token=HF_TOKEN)


# Prompt
system_prompt = """
Eres un chatbot de apoyo emocional para estudiantes universitarios en Colombia.
Responde SIEMPRE en español, de forma empática, cálida y cercana, como si fueras un buen amigo que escucha.
No uses frases impersonales como "Hola estudiante".
En vez de eso, usa saludos naturales como "hola", "qué gusto hablar contigo", "entiendo lo que sientes".
Si es necesario recomendar ayuda profesional, sugiere líneas de atención en Colombia como la Línea 106 o líneas locales de apoyo emocional.
Nunca respondas en inglés ni uses tecnicismos difíciles.
"""

# Historial de la conversación
historial = [{"role": "system", "content": system_prompt}]

def chat_con_mistral(mensaje_usuario):
    historial.append({"role": "user", "content": mensaje_usuario})

    respuesta = client.chat_completion(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=historial,
        max_tokens=250,
        temperature=0.7
    )

    texto_respuesta = respuesta.choices[0].message["content"]

    historial.append({"role": "assistant", "content": texto_respuesta})
    return texto_respuesta


# Chat
def main():
    print("ChatBot - Mistral.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "salir":
            print(" Gracias por conversar 👋. ¡Recuerda que no estás solo y que pedir ayuda es una fortaleza! 💪")
            break
        salida = chat_con_mistral(entrada)
        print("Chatbot:", salida, "\n")


if __name__ == "__main__":
    main()
