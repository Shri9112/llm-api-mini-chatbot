import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = """ 
My name is Shri. I'm 21 years old and I'm studying Computer Science and Data Science. I enjoy machine learning and I want to become an AI engineer.
"""

response = client.models.generate_content(
    model= "gemini-3.7-flash",
    contents= prompt,
)

print("Raw response:")
print(response.text)

data = json.loads(response.text)

print("\nParsed data:")
print(data)

print("\nName:", data["name"])
print("Age:", data["age"])
print("Field:", data["field"])