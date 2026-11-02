
import streamlit as st

from analyzer import extract_resume_text
from workflow import run_workflow


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.caption(
    "Análise inteligente de currículos utilizando IA"
)

st.divider()


# Upload do currículo

st.subheader("1. Envie seu currículo")

uploaded_file = st.file_uploader(
    "Selecione seu currículo em PDF",
    type=["pdf"]
)


# Descrição da vaga

st.subheader("2. Informe a vaga")

job_description = st.text_area(
    "Descrição da vaga",
    placeholder="Cole aqui a descrição da vaga...",
    height=200
)


# Executar análise

if st.button("🚀 Analisar currículo", type="primary"):

    if uploaded_file is None:

        st.warning("Envie um currículo em PDF.")

    elif not job_description.strip():

        st.warning("Informe a descrição da vaga.")

    else:

        try:

            with st.spinner(
                "A inteligência artificial está analisando..."
            ):

                resume_text = extract_resume_text(
                    uploaded_file
                )

                if not resume_text.strip():

                    st.error(
                        "Não foi possível extrair texto do PDF."
                    )

                else:

                    workflow_result = run_workflow(
                        resume_text,
                        job_description
                    )

                    if workflow_result["error"]:

                        st.error(workflow_result["error"])

                    else:

                        result = workflow_result["result"]

                    st.success(
                        "Análise concluída com sucesso!"
                    )

                    # Compatibilidade

                    st.subheader("📊 Compatibilidade")

                    st.metric(
                        "Compatibilidade estimada",
                        f"{result.compatibility_score}%"
                    )

                    st.progress(
                        result.compatibility_score / 100
                    )

                    # Habilidades

                    col1, col2 = st.columns(2)

                    with col1:

                        st.subheader(
                            "✅ Habilidades identificadas"
                        )

                        for skill in result.identified_skills:
                            st.write(f"• {skill}")

                    with col2:

                        st.subheader(
                            "⚠️ Habilidades não identificadas"
                        )

                        for skill in result.missing_skills:
                            st.write(f"• {skill}")

                    st.divider()

                    # Pontos fortes

                    st.subheader("💪 Pontos fortes")

                    for item in result.strengths:
                        st.write(f"• {item}")

                    # Melhorias

                    st.subheader("🔧 Pontos de melhoria")

                    for item in result.improvements:
                        st.write(f"• {item}")

                    # Recomendações

                    st.subheader("🚀 Recomendações")

                    for item in result.recommendations:
                        st.write(f"• {item}")

                    # Resumo

                    st.subheader("📝 Resumo da análise")

                    st.write(result.summary)

        except Exception as error:

            st.error(
                f"Erro durante a análise: {error}"
            )
