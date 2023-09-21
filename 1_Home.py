import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="⚽",
    layout="wide"
)


if "data" not in st.session_state:
    df_data = pd.read_csv("archive\CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# DATASET OFICIAL FIFA 23! ⚽")
st.sidebar.markdown("Aula da [Asimov Academy](https://www.youtube.com/watch?v=0lYBYYHBT5k&ab_channel=AsimovAcademy)")
st.sidebar.markdown("Feito por [Ciro Menescal](https://github.com/Ciro125)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")

st.markdown(
    """
    O Conjunto de Dados de Jogadores de Futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla variedade de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contrato e filiações a clubes. 
\nCom mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento dos jogadores e desenvolvimento de jogadores ao longo do tempo.
"""
)