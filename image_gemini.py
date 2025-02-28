import PIL.Image

import io
import base64
import pathlib
import textwrap
import google.generativeai as genai

img = PIL.Image.open('image.jpg')


# Convertir l'image en base64 (si le modèle attend une telle entrée)
buffered = io.BytesIO()
img.save(buffered, format="JPEG")
img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

GOOGLE_API_KEY='AIzaSyA0CCYiBGQPGy3ZC99ZoMgoVRCnGKXKRhw'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

#response = model.generate_content(img)

# Appel à l'API avec l'image en base64 (ou toute autre méthode requise par l'API)
response = model.generate_content(img_base64)

print(response.text)