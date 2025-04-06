import json
from typing import List, Dict
from config import KNOWLEDGE_BASE_PATH

class KnowledgeAnalyzer:
    def __init__(self):
        self.knowledge_base_path = KNOWLEDGE_BASE_PATH

    def carregar_blocos(self) -> List[Dict]:
        blocos = []
        for path in sorted(self.knowledge_base_path.glob("*.json")):
            with open(path, "r", encoding="utf-8") as file:
                blocos.append(json.load(file))
        return blocos

    def encontrar_segmento_por_descricao(self, termo: str) -> List[Dict]:
        blocos = self.carregar_blocos()
        resultados = []
        for bloco in blocos:
            for chave, segmento in bloco.items():
                if termo.lower() in segmento.get("descricao", "").lower():
                    resultados.append({chave: segmento})
        return resultados

    def listar_todos_segmentos(self) -> List[str]:
        blocos = self.carregar_blocos()
        descricoes = []
        for bloco in blocos:
            for segmento in bloco.values():
                descricoes.append(segmento.get("descricao", "Sem descrição"))
        return descricoes