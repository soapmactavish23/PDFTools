import tempfile
from pathlib import Path

import pypdf
import streamlit as st

from utilidades import pegar_dados_pdf


def exibir_menu_relatorio(coluna):
    with coluna:
        st.markdown("""
            # Gerar relatório PDF
            
            Escolha um arquivo Excel para gerar um relatório: 
        """)

        arquivo_excel = st.file_uploader(
            label='Selecione o arquivo Excel...',
            type=['xlsx'],
            accept_multiple_files=False,
        )

        if arquivo_excel:
            botoes_desativados = False
        else:
            botoes_desativados = True

        col1, col2 = st.columns(2)
        with col1:
            seletor_ano = st.selectbox('Ano', range(2020, 2024), disabled=botoes_desativados)
        with col2:
            seletor_mes = st.selectbox("Mês", range(1, 13), disabled=botoes_desativados)

        clicou_processar = st.button(
            'Clique para processar o arquivo Excel...',
            use_container_width=True,
            disabled=botoes_desativados)

        if clicou_processar:
            dados_pdf = pegar_dados_do_relatorio_pdf(arquivo_excel)

            if dados_pdf is None:
                st.warning(f'Excel não possui dados para ano {seletor_ano} e mês {seletor_mes}')
                return

            nome_arquivo = 'relatorio.pdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )

def pegar_dados_do_relatorio_pdf(arquivo_excel, seletor_ano, seletor_mes):
    print(arquivo_excel)
    print(seletor_ano)
    print(seletor_mes)