import streamlit as st

# Configuração da pagina.
st.set_page_config(
    page_title = 'Times',
    page_icon = '👥',
    layout = 'wide'
)

# Persistindo os dados.
df_data = st.session_state['data']

# Obtem os valores únicos.
clubs = df_data['Club'].unique()

# Cria o sidebar.
club = st.sidebar.selectbox('Clubes', clubs)

# Filtra o dataset com base na seleção do filtro.
df_filtered = df_data[df_data['Club'] == club].set_index('Name')

# Exibe a imagem do clube.
st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f'## {club}')

# Seleciona as colunas que serão filtradas.
columns = ['Age','Photo','Flag','Overall', 'Value(£)', 'Wage(£)', 'Joined','Height(cm.)','Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

# Agora realizamos os filtros.
st.dataframe(df_filtered[columns],
             column_config = {
                 "Overall": st.column_config.ProgressColumn("Overall", format = "%d", min_value = 0, max_value = 100),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format = "£%d", min_value = 0, max_value = df_filtered['Wage(£)'].max()),
                 "Photo": st.column_config.ImageColumn(),
                 "Club": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
             })