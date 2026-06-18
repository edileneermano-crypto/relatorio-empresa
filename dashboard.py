import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

PLANILHA = "Relatorios Empresa"

st.set_page_config(
    page_title="Painel de Relatórios",
    layout="wide"
)

# GOOGLE SHEETS
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

    st.info(
        "Nenhum relatório encontrado."
    )

else:

    df = pd.DataFrame(
        dados
    )

    # FILTRO PELO LINK
    params = st.query_params

    if "data" in params:

        data_link = params["data"]

        df = df[
            df["Data"]
            .astype(str)
            .str.replace("/", "-")
            == data_link
        ]

        st.success(
            f"Exibindo relatórios do dia {data_link}"
        )

        if st.button(
            "Ver todos"
        ):

            st.query_params.clear()

            st.rerun()

    st.metric(
        "Total",
        len(df)
    )

    st.divider()

    for i in range(
        len(df)-1,
        -1,
        -1
    ):

        linha = df.iloc[i]

        data = str(
            linha["Data"]
        )

        link_dia = (
            "https://relatorio-empresa-gd2pcbuqe3mef2bowyzjtt.streamlit.app/"
            "?data="
            + data.replace("/", "-")
        )

        with st.expander(

            f"{linha['Data']} | "
            f"{linha['Nome']}"

        ):

            st.write(
                f"**Hora:** {linha['Hora']}"
            )

            st.markdown(
                "### Atividades"
            )

            st.write(
                linha["Atividades"]
            )

            st.markdown(
                "### Pendências"
            )

            texto = linha[
                "Pendências"
            ]

            st.write(
                texto
                if texto
                else "-"
            )

            st.markdown(
                "### Observações"
            )

            texto = linha[
                "Observações"
            ]

            st.write(
                texto
                if texto
                else "-"
            )

            st.text_input(
                "Link direto deste dia",
                value=link_dia,
                key=f"link{i}"
            )