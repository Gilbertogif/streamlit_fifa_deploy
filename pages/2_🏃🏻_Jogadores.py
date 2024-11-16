import streamlit as st

# Configuração da pagina.
st.set_page_config(
    page_title = 'Players',
    page_icon = '🏃🏻',
    layout = 'wide'
)

# Recebe os dados carregados na pagina inicial.
df_data = st.session_state['data']

# Criando os sidebars.

# ----------- Clubes ---------------------------

# Filtro para os clubes.
clubes = df_data['Club'].unique()

# sidebar
club = st.sidebar.selectbox('Clubes', clubes)

# Cria o filtro dos clubes.
df_players = df_data[df_data['Club'] == club]

# --------------- Jogadores -------------------

# Filtro para os jogadores.
players = df_players['Name'].unique()

# sidebar
player = st.sidebar.selectbox('Jogadores', players)

# Cria o filtro por jogador. O iloc serve para pegar a primeira ocorrência do jogador.
# Caso ele apareça mais vezes no dataset.
player_stats = df_data[df_data['Name'] == player].iloc[0]

# Inserção da foto.
st.image(player_stats['Photo'])

# Inserindo um título com o nome do atleta.
st.title(player_stats['Name'])

# Inserindo os detalhes do atleta.
st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Posição:** {player_stats["Position"]}')

# Criando 3 novas colunas para dispor todas as outras informações.
col_1, col_2, col_3, col_4 = st.columns(4)
col_1.markdown(f'**Idade:** {player_stats["Age"]}')
col_2.markdown(f'**Altura:** {player_stats["Height(cm.)"] / 100}')
col_3.markdown(f'**Peso:** {player_stats["Weight(lbs.)"] * 0.453:.2f}')

# Adiciona uma linha ao final.
st.divider()

# Informações de Overall.
st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

# Informações de mercado.
# :, Indica que o valor será formatado com separadores de milhares (vírgulas no caso de números no padrão inglês).
col_1, col_2, col_3, col_4 = st.columns(4)
col_1.metric(label = 'Valor de Mercado', value = f'£ {player_stats["Value(£)"]:,}')
col_2.metric(label = 'Remuneração Semanal', value = f'£ {player_stats["Wage(£)"]:,}')
col_3.metric(label = 'Clásula de Rescisão', value = f'£ {player_stats["Release Clause(£)"]:,}')

