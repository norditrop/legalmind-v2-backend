from typing import List, Dict
from utils import summarize_text, extract_keywords
from config import EXPLAINER_SUMMARY_MAX_LEN


class KnowledgeExplainer:
    def __init__(self, knowledge_base: List[Dict]):
        self.knowledge_base = knowledge_base

    def explain_segment(self, segmento_id: str) -> str:
        segment = next((s for s in self.knowledge_base if s.get("id") == segmento_id), None)
        if not segment:
            return f"Segmento com ID '{segmento_id}' não encontrado."

        explicacao = []
        explicacao.append(f"Segmento: {segment.get('descricao', 'Descrição não disponível')}")

        if 'servicos_viaveis' in segment:
            explicacao.append("Serviços viáveis:")
            for chave, dados in segment['servicos_viaveis'].items():
                titulo = dados.get("descricao", chave)
                resumo = summarize_text(titulo, max_length=EXPLAINER_SUMMARY_MAX_LEN)
                explicacao.append(f" - {chave}: {resumo}")

        if 'modelos_negocio' in segment:
            explicacao.append("Modelos de negócio destacados:")
            for chave, modelo in segment['modelos_negocio'].items():
                desc = modelo.get("descricao", chave)
                resumo = summarize_text(desc, max_length=EXPLAINER_SUMMARY_MAX_LEN)
                explicacao.append(f" - {chave}: {resumo}")

        if 'desafios_comuns' in segment:
            explicacao.append("Principais desafios enfrentados:")
            for desafio in segment['desafios_comuns']:
                explicacao.append(f" - {desafio}")

        if 'estrategias_comerciais' in segment:
            explicacao.append("Estratégias comerciais utilizadas:")
            for k, v in segment['estrategias_comerciais'].items():
                if isinstance(v, dict):
                    explicacao.append(f" - {k}: {v.get('descricao', '')}")
                else:
                    explicacao.append(f" - {k}: {v}")

        if 'indicadores_validade_negocio' in segment:
            explicacao.append("Critérios de validação do modelo:")
            for crit, val in segment['indicadores_validade_negocio'].items():
                explicacao.append(f" - {crit}: {val}")

        if 'alertas_eticos' in segment:
            explicacao.append("Cuidados e alertas éticos:")
            for alert, val in segment['alertas_eticos'].items():
                explicacao.append(f" - {alert}: {val}")

        return "\n".join(explicacao)

    def list_available_segments(self) -> List[str]:
        return [seg.get("id", "sem_id") + " - " + seg.get("descricao", "") for seg in self.knowledge_base]