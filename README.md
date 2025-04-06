# LegalMind Web Investigation API

LegalMind é um sistema backend que permite investigações web automatizadas, interpretações estratégicas e suporte inteligente à captação de clientes jurídicos e administrativos, baseado nos princípios das 80 Leis do Sucesso e arquivos JSON segmentados.

## Funcionalidades Principais

- **/investigate**: executa investigações com scraping ou API externa para identificar estratégias de mercado, concorrentes e oportunidades jurídicas.
- **/web-search**: realiza buscas diretas na web com retorno de links e conteúdo analisado.
- **Modularização inteligente** com arquitetura FastAPI.
- **Customização via .env** para variáveis sensíveis e opções de API externas.
- **Resposta com base em JSONs segmentados** e aplicação de heurísticas interpretativas via LegalMind.

---

## Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- python-dotenv

---

## Instalação

```bash
git clone https://github.com/seuusuario/legalmind-api
cd legalmind-api
pip install -r requirements.txt
cp env.example .env
```

Preencha o arquivo `.env` com suas chaves de API e configurações locais.

---

## Executando o servidor

```bash
uvicorn main:app --reload
```

---

## Requisição de Exemplo (via Postman ou Insomnia)

**POST /investigate**

```json
{
  "tipo": "advocacia_local",
  "preferencias": {
    "regiao": "Centro-Oeste",
    "formato": "anuncios"
  }
}
```

**POST /web-search**

```json
{
  "query": "captação de clientes advocacia previdenciária 2024"
}
```

---

## Próximas Integrações

- Respostas por voz via ElevenLabs
- Salvamento de relatórios investigativos em PDF
- Bot Telegram para disparo remoto de investigações
- Modo ofensivo: escaneamento reverso de concorrência