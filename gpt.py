import time

import openai
from config import OAI
openai.api_key = OAI

def gpt(msg):
    REP = ""
    for i in range(0, len(msg), 9000):
        s = msg[i : i + 9000]
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": f"Сформулируй очень краткий и понятный отчет по результатам web сканнера:\n{s}"}]
        )
        REP += res['choices'][0]['message']['content']
        time.sleep(10)
    return REP