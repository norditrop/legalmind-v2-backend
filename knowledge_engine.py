import json
from typing import List, Dict
from utils import load_json_file, search_in_json_blocks

class KnowledgeEngine:
    def __init__(self, knowledge_base_path: str):
        self.knowledge_base_path = knowledge_base_path
        self.data = self.load_knowledge_base()

    def load_knowledge_base(self) -> List[Dict]:
        try:
            with open(self.knowledge_base_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            print(f"Erro ao carregar a base de conhecimento: {e}")
            return []

    def search(self, query: str) -> List[Dict]:
        return search_in_json_blocks(self.data, query)

    def get_all_topics(self) -> List[str]:
        return [block.get("descricao", "") for block in self.data]

# Exemplo de uso
if __name__ == "__main__":
    engine = KnowledgeEngine("data/knowledge.json")
    resultados = engine.search("funil de conversão")
    for item in resultados:
        print(json.dumps(item, indent=2, ensure_ascii=False))