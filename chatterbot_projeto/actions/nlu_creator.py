import json
import os

directory = r"C:/Cadeira Facul/TCC/projeto_completo/chatterbot_projeto/actions"
file_name = "output.json"
file_path = os.path.join(directory, file_name)

with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)

# Extrai os dados relevantes
intents = []
responses = []
intent_counts = {}
for obj in data:
    for section in obj['sections']:
        intent_name = section['title']
        if intent_name in intent_counts:
            intent_counts[intent_name] += 1
            intent_name = f"{intent_name}_{intent_counts[intent_name]}"
        else:
            intent_counts[intent_name] = 1
        intents.append(intent_name)
        responses.append(section['content'])

# Usar apenas uma vez para criar o nlu.yml

with open('data/nlu.yml', 'w', encoding='utf-8') as f:
    f.write('version: "3.1"\n\n')
    f.write('nlu:\n\n')


    for intent in intents:
        intent_name = intent.replace(" ", "_")
        f.write('  - intent: 'f'{intent_name}\n')
        f.write('    examples: | \n')
        f.write('      - \n')
        f.write('      - \n\n')