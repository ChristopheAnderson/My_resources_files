import pathlib
import textwrap
import google.generativeai as genai

GOOGLE_API_KEY='AIzaSyA0CCYiBGQPGy3ZC99ZoMgoVRCnGKXKRhw'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
chat
response = chat.send_message("In one sentence, explain how a computer works to a young child.")

print(response.text)
#chat.history

response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

for chunk in response:
  print(chunk.text)
  print("_"*80)


for message in chat.history:
  print(f'**{message.role}**: {message.parts[0].text}')