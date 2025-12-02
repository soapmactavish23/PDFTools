import streamlit as st
from streamlit_option_menu import option_menu

import menu_combinar
import menu_extrair
import menu_imagens
import menu_marca_dagua

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

_, col2, _ = st.columns(3)
with col2:
    match escolha:
        case 'Extrair página':
            menu_extrair.exibir_menu_extrair(col2)
        case 'Combinar PDFs':
            menu_combinar.exibir_menu_combinar(col2)
        case "Adicionar marca d'água":
            menu_marca_dagua.exibir_menu_marca_dagua(col2)
        case "Imagens para PDF":
            menu_imagens.exibir_menu_imagens(col2)
        case _:
            st.warning('Implementar página')
#        case "Excel para PDF":
#            st.write('Clicou excel para PDF')