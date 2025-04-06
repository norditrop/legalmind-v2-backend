from fastapi import APIRouter

router = APIRouter()

@router.get("/web/pesquisa-local")
def pesquisa_local_basica():
    return {
        "status": "ok",
        "descricao": "Simula uma coleta de dados locais com base em palavras-chave de negócios jurídicos.",
        "exemplo": {
            "cidade": "Itumbiara",
            "palavras_chave": ["advogado trabalhista", "isenção IPVA", "regularização MEI"],
            "fontes": ["Google Search", "Facebook Ads Library", "TikTok trends locais"],
            "observacao": "Retorna tendências e formatos de anúncios ativos na região alvo."
        }
    }

@router.get("/web/meta-ads")
def meta_ads_busca_simulada():
    return {
        "status": "ok",
        "descricao": "Retorna simulação de anúncios encontrados via Meta Ads Library.",
        "resultados": [
            {
                "titulo": "Revisão de Contrato de Financiamento",
                "plataforma": "Instagram",
                "formato": "Story vertical com CTA para WhatsApp",
                "publico": "Homens e mulheres, 25-45 anos, interessados em carros e crédito"
            },
            {
                "titulo": "Aposentadoria Especial",
                "plataforma": "Facebook",
                "formato": "Vídeo curto explicativo",
                "publico": "Trabalhadores da saúde e indústria com 50+ anos"
            }
        ]
    }