import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="PDFTools",
    page_icon=':page_facing_up:',
    layout='wide',
)

_, col2, _ = st.columns(3)

with col2:
    st.title("PDFTools")
    st.markdown("""
        ### Escolha a opção desejada abaixo: 
    """)

entradas_menu = {
    'Extrair página': 'file-earmark-pdf-fill',
    'Combinar PDFs': 'plus-square-fill',
    "Adicionar marca d'água": 'droplet-fill',
    'Imagens para PDF': 'file-earmark-richtext-fill',
    'Excel para PDF': 'file-earmark-spreadsheet-fill',
}

escolha = option_menu(
    menu_title=None,
    orientation='horizontal',
    options=list(entradas_menu.keys()),
    icons=list(entradas_menu.values()),
    default_index=0
)

match escolha:
    case 'Extrair página':
        st.write('Clicou extrair')
    case 'Combinar PDFs':
        st.write('Clicou combinar PDFs')
    case "Adicionar marca d'água":
        st.write('Clicou adicionar marca')
    case "Imagens para PDF":
        st.write('Clicou imagens para PDF')
    case "Excel para PDF":
        st.write('Clicou excel para PDF')