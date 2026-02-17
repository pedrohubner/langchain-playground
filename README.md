# LangChain Playground

Projeto de estudos com exemplos práticos de LangChain focados em:

- `PromptTemplate`
- `Chains` e composição com operador `|`
- sumarização (`stuff` e `map_reduce`)
- gerenciamento de memória em chat
- agente ReAct com ferramenta customizada

## Estrutura

```text
agent/
chain/
memorymanagement/
prompttemplate/
summarize/
requirements.txt
```

## Pré-requisitos

- Python 3.12 (ou compatível)
- Chave de API da OpenAI

## Configuração do ambiente

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o arquivo `.env` na raiz:

```env
OPENAI_API_KEY=seu_token_aqui
```

Opcional (recomendado para usar Hub/observabilidade da LangSmith):

```env
LANGSMITH_API_KEY=seu_token_langsmith
```

## Como executar

Com o ambiente virtual ativo, rode os exemplos com:

### Prompt templates

```bash
python prompttemplate/prompt_template_basics.py
python prompttemplate/prompt_template_open_ai.py
```

### Chains

```bash
python chain/chain_basics.py
python chain/chain_pipeline.py
python chain/chain_decorator
```

### Summarization

```bash
python summarize/summarize_stuff_type.py
python summarize/summarize_map_reduce_type.py
```

### Memory management

```bash
python memorymanagement/in_memory_chat.py
python memorymanagement/sliding_window_memory_chat.py
```

### Agent (ReAct + tool)

```bash
python agent/react_agent.py
```

## Observações

- O projeto usa modelos como `gpt-5.2` e `gpt-4.1-mini`. Se não estiverem disponíveis na sua conta, troque o nome do modelo nos arquivos.
- O exemplo `agent/react_agent.py` usa `eval` na tool `calculator`; mantenha esse padrão apenas para estudo local.
- Os scripts são independentes: você pode executar cada arquivo separadamente para testar um conceito.
