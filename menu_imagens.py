import streamlit as st
from PIL import Image

def exibir_menu_imagens(coluna):
    with coluna:
        st.markdown("""
            # Imagens para PDF
            
            Selecione as imagens para gerar um PDF com elas: 
        """)

        imagens = st.file_uploader(
            label='Selecione as imagens que irão para o arquivo PDF...',
            type=['png', 'jpg', 'jpeg'],
            accept_multiple_files=True,
        )

        if imagens:
            botoes_desativados = False
        else:
            botoes_desativados = True

        clicou_processar = st.button(
            'Clique para processar o arquivo PDF',
            use_container_width=True,
            disabled=botoes_desativados)

        if clicou_processar:
            dados_pdf = gerar_arquivo_pdf_com_imagens(imagens=imagens)

            nome_arquivo = f'imagenspdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )

def gerar_arquivo_pdf_com_imagens(imagens):
    imagens_pillow = []
    for imagem in imagens:
        dados_imagem = Image.open(imagem)
        imagens_pillow.append(dados_imagem)

    primeira_imagem = imagens_pillow[0]
    demais_imagens = imagens_pillow[1:]

    primeira_imagem.save('imagens.pdf', save_all=True, append_image=demais_imagens)
    return ''