import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from ai-agent!")

if __name__ == "__main__":
    main()

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error, please provide an input!")
    sys.exit(1)
else:
    content = sys.argv[1]

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=content
)

print(response.text)
print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)