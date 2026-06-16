import streamlit as st
import pandas as pd
from datetime import datetime
import os

ARQUIVO = "relatorios.xlsx"

st.set_page_config(
    page_title="Painel de Relatórios",
    layout="wide"
)

st.markdown("""
<style>

.block-container{
max-width:1100px;
padding-top:25px;
}

.relatorio{
padding:14px;
border:1px solid #E5E7EB;
border-radius:10px;
margin-bottom:12px;
background:white;
}

[data-testid="stMetric"]{
border:1px solid #E5E7EB;
padding:12px;
border-radius:10px;
}

.stButton button{
width:100%;
height:40px;
border-radius:8px;
}

</style>
""",
unsafe_allow_html=True
)

st.title("Painel de Relatórios")
st.caption("Visualização e gerenciamento dos relatórios enviados")

hoje = datetime.now().strftime("%d/%m/%Y")

if os.path.exists(ARQUIVO):

    df = pd.read_excel(ARQUIVO)

    df_hoje = df[
        df["Data"] == hoje
    ]

    m1, m2 = st.columns(2)

    with m1:
        st.metric(
            "Relatórios Recebidos",
            len(df_hoje)
        )

    with m2:
        st.metric(
            "Data",
            hoje
        )

    st.divider()

    if len(df_hoje):

        for indice, linha in df_hoje.iterrows():

            st.markdown(
                '<div class="relatorio">',
                unsafe_allow_html=True
            )

            c1, c2, c3, c4 = st.columns(
                [5,2,2,1]
            )

            with c1:

                st.write(
                    f"**{linha['Nome']}**"
                )

            with c2:

                st.write(
                    linha["Hora"]
                )

            with c3:

                abrir = st.button(
                    "Abrir",
                    key=f"abrir{indice}"
                )

            with c4:

                excluir = st.button(
                    "🗑",
                    key=f"excluir{indice}",
                    help="Excluir relatório"
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

            if abrir:

                st.markdown(
                    "---"
                )

                st.subheader(
                    "Atividades"
                )

                st.write(
                    linha["Atividades"]
                )

                st.subheader(
                    "Pendências"
                )

                valor = linha[
                    "Pendências"
                ]

                if str(valor) != "nan":

                    st.write(
                        valor
                    )

                else:

                    st.write(
                        "-"
                    )

                st.subheader(
                    "Observações"
                )

                valor = linha[
                    "Observações"
                ]

                if str(valor) != "nan":

                    st.write(
                        valor
                    )

                else:

                    st.write(
                        "-"
                    )

                st.divider()

            if excluir:

                df = df.drop(
                    indice
                )

                df.to_excel(
                    ARQUIVO,
                    index=False
                )

                st.success(
                    "Relatório excluído."
                )

                st.rerun()

    else:

        st.info(
            "Nenhum relatório enviado hoje."
        )

else:

    st.warning(
        "Arquivo de relatórios não encontrado."
    )