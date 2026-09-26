from google.genai import _api_client
from google.genai import _api_client
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = API_key)

prompt = """
Give defination of chemistry.
"""

response = client.models.generate_content_stream(
    model = "gemini-3.7-flash",
    contents=prompt,
)

for chunk in response:
    print(chunk.text, end="", flush=True)

print()
