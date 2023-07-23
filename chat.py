import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")  # Replace with your OpenAI API key

history=[
            {"role": "system", "content": "Hi. Your name is Ro'za and you are created by a programmer called Endie to help people."},
            {"role": "assistant", "content": "OK."},
        ]

def req(message):
    otm=history.copy()
    otm.append({'role':'user','content':message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=otm
    )
    if response['choices'][0]['message']['content']:
        history.append(otm[-1])
        history.append(response['choices'][0]['message'])
        return response['choices'][0]['message']['content']
    else:
        return "Kechirasiz, savolingizni tushunmadim"

def gen_img(t):
    response = openai.Image.create(
        prompt=t,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url
