import streamlit as st
import openai

st.set_page_config(page_title="MedPrompt AI", layout="centered")

st.title("MedPrompt AI – Diagnóstico e Conduta Médica")
st.markdown("Insira abaixo o caso clínico do paciente para análise com base nas diretrizes médicas mais recentes.")

caso_clinico = st.text_area("Caso Clínico", placeholder="Ex: Homem, 62 anos, dor torácica em aperto, sudorese, PA 90x60 mmHg, FC 112 bpm...")

if st.button("Analisar com IA"):
    if caso_clinico.strip() == "":
        st.warning("Por favor, insira um caso clínico.")
    else:
        openai.api_key = "sk-..."  # <- sua chave vai aqui depois

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um médico emergencista especializado. Responda com base nas diretrizes clínicas mais atualizadas (AHA/ESC/SSC 2025)."},
                {"role": "user", "content": caso_clinico}
            ]
        )
        resposta_ia = response["choices"][0]["message"]["content"]
        st.markdown(resposta_ia)
