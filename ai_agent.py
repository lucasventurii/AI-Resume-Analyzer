
from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.output import NativeOutput

from schemas import ResumeAnalysis


# Conexão com o modelo local
model = OllamaModel(
    "llama3.2:3b",
    provider=OllamaProvider(
        base_url="http://localhost:11434/v1"
    )
)


# Criação do agente
resume_agent = Agent(
    model,
    output_type=NativeOutput(ResumeAnalysis),
    instructions="""
    Você é um especialista em recrutamento.

    Compare o currículo com a descrição da vaga.

    Analise:
    - Compatibilidade estimada.
    - Habilidades identificadas.
    - Habilidades exigidas que não aparecem no currículo.
    - Pontos fortes.
    - Pontos de melhoria.
    - Recomendações.

    Responda em português.

    Não invente experiências ou qualificações.
    Não considere automaticamente que uma habilidade
    não mencionada seja uma habilidade que o candidato
    definitivamente não possui.

    O percentual deve ser uma estimativa baseada
    nas evidências disponíveis.
    """
)


def analyze_resume(resume, job_description):

    prompt = f"""
    Analise o currículo abaixo em comparação
    com a descrição da vaga.

    CURRÍCULO:
    {resume}

    DESCRIÇÃO DA VAGA:
    {job_description}
    """

    result = resume_agent.run_sync(prompt)

    return result.output
