
import json
import os

def load_knowledge(directory='knowledge'):
    knowledge_base = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    key = os.path.splitext(filename)[0]
                    knowledge_base[key] = data
                except json.JSONDecodeError as e:
                    print(f'Erro ao carregar {filename}: {e}')
    return knowledge_base

if __name__ == '__main__':
    kb = load_knowledge()
    print(f'Base de conhecimento carregada com {len(kb)} segmentos.')
