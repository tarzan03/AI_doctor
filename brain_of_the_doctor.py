#Step 1: Setup Groq API key
import os
# import getpass
from dotenv import load_dotenv
load_dotenv()

# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Step 2: Convert image to required format
import base64

image_path = "OIP-4288977931.jpeg"
image_file = open(image_path,'rb')
encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup Multimodal LLM

from groq import Groq

Client = Groq()

query = "What is this on my back skin?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
# model="llama-3.3-70b-versatile"
messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]





chat_completion = Client.chat.completions.create(
    model=model,
    messages=messages
)

print(chat_completion.choices[0].message.content)

