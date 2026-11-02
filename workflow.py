
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from ai_agent import analyze_resume


# Estado compartilhado do processo
class ResumeState(TypedDict):

    resume: str

    job_description: str

    result: object

    error: str



# Primeiro nó: análise do currículo
def analysis_node(state: ResumeState):

    try:

        result = analyze_resume(
            state["resume"],
            state["job_description"]
        )

        return {
            "result": result,
            "error": ""
        }

    except Exception as error:

        return {
            "result": None,
            "error": str(error)
        }


# Segundo nó: validação do resultado
def validation_node(state: ResumeState):

    result = state["result"]

    if result is None:

        return {
            "error": state["error"] or "Análise não gerou resultado."
        }

    if not 0 <= result.compatibility_score <= 100:

        return {
            "error": "Percentual de compatibilidade inválido."
        }

    if not result.summary.strip():

        return {
            "error": "O resumo da análise está vazio."
        }

    return {
        "error": ""
    }

# Construção do fluxo
builder = StateGraph(ResumeState)


# Adicionando os nós
builder.add_node(
    "analysis",
    analysis_node
)

builder.add_node(
    "validation",
    validation_node
)


# Definindo a sequência
builder.add_edge(
    START,
    "analysis"
)

builder.add_edge(
    "analysis",
    "validation"
)

builder.add_edge(
    "validation",
    END
)


# Compilando o grafo
resume_workflow = builder.compile()


# Função utilizada pela aplicação
def run_workflow(resume, job_description):

    return resume_workflow.invoke({
        "resume": resume,
        "job_description": job_description,
        "result": None,
        "error": ""
    })
