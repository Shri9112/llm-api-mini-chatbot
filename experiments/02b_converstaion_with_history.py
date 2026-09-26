import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    history.append({
        "role": "user",
        "text": user_input
    })

    conversation = ""

    for message in history:
        conversation += f'{message["role"]}: {message["text"]}\n'

    response = client.models.generate_content(
        model = 'gemini-3.5-flash',
        contents = conversation
    )

    print("AI: ", response.text)

    # history.append({
    #     "role" : "user",
    #     "text" : user_input
    # })

    history.append({
        "role" : "assistant",
        "text" : response.text
    })