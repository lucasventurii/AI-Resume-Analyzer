AI Resume Analyzer 📄
Intelligent Resume Analysis with Artificial Intelligence

O AI Resume Analyzer é uma aplicação desenvolvida em Python que utiliza Inteligência Artificial para analisar currículos e comparar as competências do candidato com os requisitos de uma vaga de emprego.

O sistema utiliza modelos de linguagem locais para identificar habilidades, estimar compatibilidade e gerar recomendações de melhoria profissional.

🚀 Funcionalidades
Upload de currículos em PDF.
Extração automática de texto.
Análise inteligente utilizando LLM.
Comparação entre currículo e descrição da vaga.
Estimativa de compatibilidade.
Identificação de habilidades.
Identificação de competências não mencionadas.
Recomendações de melhoria.
Resultados estruturados com validação.
🛠️ Tecnologias utilizadas
Tecnologia	Aplicação
Python	Linguagem principal
Ollama	Execução de modelos locais
Llama 3.2	Modelo de linguagem
Pydantic AI	Agente e saídas estruturadas
LangGraph	Orquestração do fluxo
Streamlit	Interface web
PyPDF	Extração de texto de PDFs
🏗️ Arquitetura
O usuário envia um currículo em PDF.
O sistema extrai o texto utilizando PyPDF.
O usuário informa a descrição da vaga.
O Ollama executa o modelo de linguagem.
O Pydantic AI estrutura e valida os resultados.
O LangGraph controla o fluxo de análise e validação.
O Streamlit apresenta os resultados.
💻 Como executar o projeto
1. Clonar o repositório
bash
git clone https://github.com/SEU-USUARIO/AI-Resume-Analyzer.git

2. Entrar na pasta
bash
cd AI-Resume-Analyzer

3. Criar ambiente virtual
bash
python -m venv .venv

4. Ativar o ambiente

Windows:

powershell
.venv\Scripts\Activate.ps1

5. Instalar dependências
bash
pip install -r requirements.txt

6. Instalar e iniciar o Ollama

Baixe o Ollama em https://ollama.com/

Execute:

bash
ollama pull llama3.2:3b

7. Executar a aplicação
bash
streamlit run app.py

📌 Objetivo do projeto

Projeto desenvolvido para demonstrar conhecimentos práticos em desenvolvimento Python, integração com LLMs, agentes de IA, validação de dados e orquestração de fluxos inteligentes.

⚠️ Observações

O percentual de compatibilidade é uma estimativa gerada por IA e não representa garantia de contratação ou avaliação profissional objetiva.

Os documentos enviados devem ser tratados como informações confidenciais. Utilize currículos fictícios ou anonimizados em demonstrações.

👨‍💻 Autor

Desenvolvido como projeto de portfólio na área de Inteligência Artificial e desenvolvimento Python.