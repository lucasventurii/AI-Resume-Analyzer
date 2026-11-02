
# 📄 AI Resume Analyzer

### Intelligent Resume Analysis with Artificial Intelligence

O **AI Resume Analyzer** é uma aplicação desenvolvida em Python que utiliza Inteligência Artificial para analisar currículos e comparar as competências do candidato com os requisitos de uma vaga de emprego.

O sistema utiliza modelos de linguagem locais (LLMs) para identificar habilidades, estimar compatibilidade e gerar recomendações de melhoria profissional.

---

## 🚀 Funcionalidades

- 📄 Upload de currículos em PDF.
- 🔍 Extração automática de texto utilizando PyPDF.
- 🤖 Análise inteligente utilizando LLM.
- 🎯 Comparação entre currículo e descrição da vaga.
- 📊 Estimativa de compatibilidade entre candidato e vaga.
- ✅ Identificação de habilidades encontradas.
- ⚠️ Identificação de competências não mencionadas.
- 💡 Recomendações de melhoria profissional.
- 📋 Resultados estruturados e validados com Pydantic.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| Ollama | Execução de modelos de IA localmente |
| Llama 3.2 | Modelo de linguagem utilizado |
| Pydantic AI | Criação de agentes e saídas estruturadas |
| LangGraph | Orquestração do fluxo de análise |
| Streamlit | Desenvolvimento da interface web |
| PyPDF | Extração de texto de arquivos PDF |
| Pydantic | Validação e estruturação de dados |

---

## 🏗️ Arquitetura do projeto

O funcionamento da aplicação acontece nas seguintes etapas:

1. O usuário envia um currículo em PDF.
2. O sistema extrai o texto utilizando PyPDF.
3. O usuário informa a descrição da vaga de emprego.
4. O Ollama executa o modelo de linguagem Llama 3.2.
5. O Pydantic AI processa a solicitação e estrutura os resultados.
6. O LangGraph controla o fluxo de análise e validação.
7. O Streamlit apresenta os resultados em uma interface interativa.

### Fluxo da aplicação

```text
          CURRÍCULO PDF
                |
                v
          EXTRAÇÃO DE TEXTO
              (PyPDF)
                |
                v
        DESCRIÇÃO DA VAGA
                |
                v
          OLLAMA + LLM
                |
                v
           PYDANTIC AI
       (Análise estruturada)
                |
                v
           LANGGRAPH
       (Fluxo e validação)
                |
                v
            STREAMLIT
       (Exibição dos resultados)
```

---

## 📂 Estrutura do projeto

```text
AI-Resume-Analyzer/
│
├── app.py
├── analyzer.py
├── ai_agent.py
├── llm_service.py
├── schemas.py
├── workflow.py
│
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
│
└── .venv/
```

### Responsabilidade dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| app.py | Interface principal da aplicação |
| analyzer.py | Extração de texto dos currículos PDF |
| ai_agent.py | Configuração do agente Pydantic AI |
| llm_service.py | Serviço de análise com IA |
| schemas.py | Modelos e validação dos resultados |
| workflow.py | Fluxo de execução utilizando LangGraph |
| requirements.txt | Dependências do projeto |
| .env.example | Exemplo das variáveis de ambiente |

---

## 💻 Como executar o projeto

### Pré-requisitos

Antes de começar, você precisará instalar:

- Python 3.11 ou superior.
- Visual Studio Code.
- Ollama.
- Git.

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/AI-Resume-Analyzer.git
```

### 2. Entrar na pasta do projeto

```bash
cd AI-Resume-Analyzer
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Instalar o Ollama

Acesse:

https://ollama.com/

Faça o download e instale o Ollama no seu computador.

### 7. Baixar o modelo de linguagem

```bash
ollama pull llama3.2:3b
```

### 8. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_MODEL=llama3.2:3b
OLLAMA_BASE_URL=http://localhost:11434
```

### 9. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador.

---

## 🧠 Conceitos de Inteligência Artificial aplicados

### LLM (Large Language Model)

Utilização de modelos de linguagem para interpretar currículos e comparar informações com os requisitos de vagas.

### Ollama

Execução de modelos de linguagem localmente, permitindo realizar análises sem depender de uma API externa de LLM.

### Pydantic AI

Utilizado para criar um agente de IA que produz resultados estruturados, facilitando a validação e o consumo dos dados pela aplicação.

### LangGraph

Responsável por organizar e controlar o fluxo de execução da análise, utilizando nós e estado compartilhado.

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de aplicar conhecimentos práticos em:

- Desenvolvimento Python.
- Inteligência Artificial Generativa.
- Large Language Models (LLMs).
- Engenharia de prompts.
- Agentes de IA.
- Estruturação e validação de dados.
- Orquestração de fluxos inteligentes.
- Integração entre diferentes tecnologias.

---

## 🔮 Melhorias futuras

Algumas funcionalidades que podem ser adicionadas em versões futuras:

- Exportação dos resultados em PDF.
- Histórico de análises realizadas.
- Suporte para múltiplos formatos de currículo.
- Reconhecimento de texto em PDFs digitalizados utilizando OCR.
- Dashboard com gráficos e indicadores.
- Comparação entre múltiplas vagas.
- Testes automatizados.

---

## ⚠️ Observações

- O percentual de compatibilidade é uma estimativa produzida por IA, não uma avaliação objetiva ou garantia de contratação.
- Habilidades não mencionadas no currículo não significam necessariamente que o candidato não as possui.
- Os documentos enviados devem ser tratados como informações confidenciais.
- Recomenda-se utilizar currículos fictícios ou anonimizados durante demonstrações.

---

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio na área de **Inteligência Artificial, Python e desenvolvimento de aplicações com LLMs**.

⭐ Se este projeto foi interessante, considere deixar uma estrela no repositório!
