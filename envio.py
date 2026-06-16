import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

PLANILHA = "Relatorios Empresa"

escopos = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive"
]

credenciais = Credentials.from_service_account_file(
"credenciais.json",
scopes=escopos
)

cliente = gspread.authorize(
credenciais
)

planilha = cliente.open(
PLANILHA
).sheet1

st.set_page_config(
page_title="Sistema de Relatórios",
layout="centered"
)

st.title(
"Sistema de Relatório"
)

with st.form("relatorio"):

    nome = st.text_input(
        "Responsável"
    )

    atividades = st.text_area(
        "Atividades"
    )

    pendencias = st.text_area(
        "Pendências"
    )

    observacoes = st.text_area(
        "Observações"
    )

    enviar = st.form_submit_button(
        "Enviar Relatório"
    )

if enviar:

    planilha.append_row([

        datetime.now().strftime(
            "%d/%m/%Y"
        ),

        datetime.now().strftime(
            "%H:%M"
        ),

        nome,

        atividades,

        pendencias,

        observacoes

    ])

    st.success(
        "Relatório enviado."
    )

    st.balloons()