import os
from langchain_google_vertexai import ChatVertexAI

# Définir la clé API (assurez-vous d'avoir téléchargé le fichier JSON de votre clé API depuis Google Cloud)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chemin/vers/votre/clé-api.json"

# Initialiser le modèle Gemini
model = ChatVertexAI(model="gemini-1.5-flash")

# Lancer l'invocation du modèle avec une entrée
response = model.invoke("Hello, world!")

# Afficher la réponse du modèle
print(response)
