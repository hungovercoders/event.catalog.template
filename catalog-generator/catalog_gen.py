import os
import openai

openai.api_key = os.getenv("CHATGPT_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])