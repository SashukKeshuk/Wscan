import openai
from config import OAI
openai.api_key = OAI

def gpt(msg):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": msg}]
    )
    return res['choices'][0]['message']['content']