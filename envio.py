import streamlit as st
import pandas as pd
from datetime import datetime
import os

ARQUIVO = "relatorios.xlsx"

st.set_page_config(
    page_title="Relatórios",
    layout="wide"
)

st.markdown("""
<style>

.block-container{
max-width:1000px;
padding-top:30px;
}

h1{
font-size:32px !important;
font-weight:700 !important;
}

[data-testid="stForm"]{
border:1px solid #E5E7EB;
padding:35px;
border-radius:16px;
background:#FFFFFF;
}

.stTextInput input{
border-radius:8px;
}

.stTextArea textarea{
border-radius:8px;
}

.stButton button{
width:100%;
height:54px;
border-radius:8px;
font-size:16px;
font-weight:600;
}

.linha{
padding:12px;
background:#F8FAFC;
border-radius:8px;
margin-bottom:20px;
}

.rodape{
margin-top:40px;
text-align:center;
font-size:13px;
color:#6B7280;
}

</style>
""", unsafe_allow_html=True)

st.title("Sistema de Relatórios")

st.caption(
"Registro diário de atividades"
)

col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("""
<div class='linha'>
Preencha o relatório e envie para disponibilizar no painel.
</div>
""", unsafe_allow_html=True)

with col2:
    st.metric(
        "Data",
        datetime.now().strftime("%d/%m/%Y")
    )

with st.form("envio"):

    nome = st.text_input(
        "Responsável"
    )

    atividades = st.text_area(
        "Atividades realizadas",
        height=220
    )

    pendencias = st.text_area(
        "Pendências",
        height=120
    )

    observacoes = st.text_area(
        "Observações",
        height=120
    )

    enviar = st.form_submit_button(
        "Enviar Relatório"
    )

if enviar:

    if not nome.strip():

        st.error(
            "Informe o responsável."
        )

    elif not atividades.strip():

        st.error(
            "Preencha as atividades."
        )

    else:

        registro = {

            "Data":
            datetime.now().strftime(
                "%d/%m/%Y"
            ),

            "Hora":
            datetime.now().strftime(
                "%H:%M"
            ),

            "Nome":
            nome,

            "Atividades":
            atividades,

            "Pendências":
            pendencias,

            "Observações":
            observacoes
        }

        if os.path.exists(
            ARQUIVO
        ):

            df = pd.read_excel(
                ARQUIVO
            )

        else:

            df = pd.DataFrame()

        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    [registro]
                )
            ],
            ignore_index=True
        )

        df.to_excel(
            ARQUIVO,
            index=False
        )

        st.success(
            "Relatório enviado com sucesso."
        )

st.balloons()

st.markdown("""
<div class='rodape'>
Painel interno de acompanhamento
</div>
""", unsafe_allow_html=True)