import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

PLANILHA = "Relatorios Empresa"

st.set_page_config(
    page_title="Painel de Relatórios",
    layout="wide"
)

escopos = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credenciais = Credentials.from_service_account_info(
    dict(st.secrets),
    scopes=escopos
)

cliente = gspread.authorize(
    credenciais
)

sheet = cliente.open(
    PLANILHA
).sheet1

dados = sheet.get_all_records()

st.title("Painel de Relatórios")

if len(dados) == 0:

    st.info("Nenhum relatório encontrado.")

else:

    df = pd.DataFrame(dados)

    st.metric(
        "Total de Relatórios",
        len(df)
    )

    st.divider()

    for i in range(len(df)-1, -1, -1):

        linha = df.iloc[i]

        with st.expander(
            f"{linha['Data']} | {linha['Nome']}"
        ):

            st.write(
                f"**Hora:** {linha['Hora']}"
            )

            st.write(
                f"**Atividades:**\n\n{linha['Atividades']}"
            )

            st.write(
                f"**Pendências:**\n\n{linha['Pendências']}"
            )

            st.write(
                f"**Observações:**\n\n{linha['Observações']}"
            )