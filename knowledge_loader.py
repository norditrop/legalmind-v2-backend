
import os
import json

KNOWLEDGE_PATH = "knowledge"

def load_knowledge():
    knowledge_data = {}
    for filename in os.listdir(KNOWLEDGE_PATH):
        if filename.endswith(".json"):
            path = os.path.join(KNOWLEDGE_PATH, filename)
            with open(path, "r", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                    knowledge_data[filename] = content
                except json.JSONDecodeError:
                    print(f"Erro ao ler {filename}")
    return knowledge_data
