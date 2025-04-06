# Estrutura de Conhecimento (Knowledge)

Este diretório `knowledge/` armazena os blocos de conhecimento que alimentam o LegalMind GPT. Cada bloco corresponde a um segmento de atuação, modelo de negócio, técnica de marketing ou estrutura de funil validada.

## Estrutura dos Arquivos

- Os arquivos devem estar no formato `.json`.
- Cada arquivo deve conter um único `segmento_X` e pode incluir metainformações como `"legalmind_consultivo"` no final.
- Os nomes dos arquivos devem seguir o padrão: `bloco_X_nome_tematico.json`.

## Arquivo de Leitura

O script `knowledge_loader.py` varre automaticamente a pasta e carrega todos os arquivos `.json`, retornando seus conteúdos organizados para uso no backend.

## Padrões de Conteúdo

- Usar português técnico e claro.
- Evitar duplicidade de segmentos.
- Usar sempre o mesmo padrão de indentação e estrutura já definido nos blocos anteriores.

## Exemplo de Nome de Arquivo

- `bloco_1_segmentos_estrategias.json`
- `bloco_4_departamentos_juridicos.json`
- `bloco_7_modelos_validos.json`

---

**Importante**: Os arquivos de conhecimento devem ser considerados uma base viva. Sempre que houver evolução no mercado ou na prática investigativa do LegalMind, novos arquivos podem ser adicionados ou atualizados aqui.