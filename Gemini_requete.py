import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
# from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyA0CCYiBGQPGy3ZC99ZoMgoVRCnGKXKRhw'

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is the meaning of life?")

print(response.text)

response.prompt_feedback

response.candidates

#model.count_tokens("What is the meaning of life?")

#model.count_tokens(chat.history)