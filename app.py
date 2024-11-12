import openai
import os
import time

# Configura tu clave API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Asegúrate de establecer la variable de entorno
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Puedes cambiar a otro modelo si lo deseas
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit"]:
            break
        try:
            response = chat_with_gpt(user_input)
            print(f"ChatGPT: {response}")
        except openai.error.RateLimitError:

            print("Has excedido tu cuota de uso. Esperando 60 segundos antes de intentar nuevamente...")
            time.sleep(60)