import streamlit as st

def exibir_manu_extrair(coluna):
    with coluna:
        st.markdown("""
            # Extrair página PDF
            
            Escolha um arquivo PDF para extrair uma página: 
        """)

        arquivo_pdf = st.file_uploader(
            label='Selecione o arquivo PDF...',
            type=['pdf'],
            accept_multiple_files=False,
        )

        if arquivo_pdf:
            botoes_desativados = False
        else:
            botoes_desativados = True

        numero_pagina = st.number_input('Página para extrair', min_value=1, disabled=botoes_desativados)
        clicou_processar = st.button(
            'Clique para processar o arquivo PDF',
            use_container_width=True,
            disabled=botoes_desativados)

        if clicou_processar:
            #dados_pdf = exibir_manu_extrair(arquivo_pdf=arquivo_pdf, numero_pagina=numero_pagina)
            dados_pdf = ''
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name='teste.txt',
                use_container_width=True,
            )
