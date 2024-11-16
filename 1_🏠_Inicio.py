import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Configuração da pagina.
st.set_page_config(
    page_title = 'Início',
    page_icon = '🏠',
    layout = 'centered'
)

# Aqui, o código verifica se 'data' não é uma chave presente no st.session_state.
# Essa lógica evita recarregar os dados do CSV repetidamente, o que seria desnecessário e ineficiente.
if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    # Filtro para mostrar só jogadores com contrato valido.
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    # Excluindo jogadores que não possue valor valido.
    df_data = df_data[df_data['Value(£)'] > 0]
    # Ordenando por overall.
    df_data = df_data.sort_values(by = 'Overall', ascending = False)
    # Persistindo os dados.
    st.session_state['data'] = df_data

# Título da pagína inicial.
st.markdown('# FIFA23 OFFICIAL DATASET! ⚽️')
st.sidebar.markdown("Desenvolvido por [Gilberto Gil Inácio](https://www.linkedin.com/in/gilberto-gil-in%C3%A1cio-591a45a9/)")

# Cliando um botão com derecionamento para o dataset.
btn = st.link_button('Acesse os dados no Kaggle', 
                     'https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset')

# Texto da tela inicial
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)