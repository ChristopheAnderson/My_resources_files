import re

def replace_text_in_file(file_path, patterns_and_functions):
    # Lire le contenu du fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fonction de remplacement
    def repl_func(match, modify_function):
        old_value = match.group(1)  # Récupérer la valeur capturée dans le pattern
        
        if old_value.startswith("https://"):
            return match.group(0)  # Retourner le texte original sans modification
        
        new_value = modify_function(old_value)  # Modifier la valeur
        return new_value  # Construire la nouvelle chaîne
    
    # Appliquer la modification pour chaque pattern/fonction
    for pattern, modify_function in patterns_and_functions:
        content = re.sub(pattern, lambda match: repl_func(match, modify_function), content)
    
    # Générer un nouveau fichier avec le même type d'extension
    new_file_path = file_path.rsplit('.', 1)[0] + "_modifie." + file_path.rsplit('.', 1)[1]
    
    # Écrire les modifications dans le nouveau fichier
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"✅ Remplacement terminé. Nouveau fichier enregistré sous '{new_file_path}'")


# Fonction qui modifie la valeur extraite
def modify_function1(old_value):
    texte1 = "href=\"{% static '"
    texte2 = "' %}\""
    resultat = texte1 + old_value + texte2
    return resultat  

def modify_function2(old_value):
    texte1 = "src=\"{% static '"
    texte2 = "' %}\""
    resultat = texte1 + old_value + texte2
    return resultat  


# Exemple d'utilisation
file_path = "polls/templates/polls/Blog.html"  # Remplacez par le chemin de votre fichier
patterns_and_functions = [
    (r"href=\"(.*?)\"", modify_function1),  # Remplacement pour les liens
    (r"src=\"(.*?)\"", modify_function2),  # Remplacement pour les titres (juste un exemple)
]

replace_text_in_file(file_path, patterns_and_functions)

