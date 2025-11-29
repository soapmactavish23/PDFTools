import tempfile
from pathlib import Path

import pypdf
import streamlit as st

from utilidades import pegar_dados_pdf


def exibir_menu_marca_dagua(coluna):
    with coluna:
        st.markdown("""
            # Aridionar marca d'água
            
            Selecione um arquivo PDF e uma marca d'água nos seletores abaixo:
        """)

        arquivo_pdf = st.file_uploader(
            label='Selecione o arquivo PDF...',
            type=['pdf'],
            accept_multiple_files=False,
        )

        arquivo_marca = st.file_uploader(
            label="Selecione o arquivo contendo a marca d'água...",
            type=['pdf'],
            accept_multiple_files=False,
        )

        if arquivo_pdf and arquivo_marca:
            botoes_desativados = False
        else:
            botoes_desativados = True

        clicou_processar = st.button(
            'Clique para processar o arquivo PDF',
            use_container_width=True,
            disabled=botoes_desativados)

        if clicou_processar:
            dados_pdf = adicionar_marca_dagua(arquivo_pdf=arquivo_pdf, arquivo_marca=arquivo_marca)
            nome_arquivo = f'{Path(arquivo_pdf.name).stem}_marca.pdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )

def adicionar_marca_dagua(arquivo_pdf, arquivo_marca):
    leitor = pypdf.PdfReader(arquivo_pdf)
    pagina_marca = pypdf.PdfReader(arquivo_marca).pages[0]

    escritor = pypdf.PdfWriter()

    for pagina in leitor.pages:
        # Tamanhos como float para evitar problemas de tipo
        w_pag = float(pagina.mediabox.width)
        h_pag = float(pagina.mediabox.height)
        w_marca = float(pagina_marca.mediabox.width)
        h_marca = float(pagina_marca.mediabox.height)

        # Mantém proporção e "cobre" a página (ou use max/min conforme preferir)
        escala = min(w_pag / w_marca, h_pag / h_marca)

        # Centraliza a marca d'água
        tx = (w_pag - w_marca * escala) / 2
        ty = (h_pag - h_marca * escala) / 2

        transf = pypdf.Transformation().scale(escala).translate(tx, ty)

        # Sobrepõe por cima do conteúdo existente
        pagina.merge_transformed_page(pagina_marca, transf, over=True)

        escritor.add_page(pagina)

    dados_pdf = pegar_dados_pdf(escritor=escritor)
    return dados_pdf
