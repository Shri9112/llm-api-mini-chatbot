import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = """
Give me a name for a Python project.Return only the project name..
"""

temperatures =[0.0, 0.5, 1.0, 1.5]

for temperature in temperatures:

    print("\n" + "=" * 60)
    print(f"Temperature: {temperature}")
    print("=" * 60)

    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
        )
    )
    print(response.text)
    
    
    


