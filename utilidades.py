from pathlib import Path
import tempfile

def pegar_dados_pdf(escritor):
    with tempfile.TemporaryDirectory() as tempdir:
        temp_pdf_file = Path(tempdir) / 'temp.pdf'
        escritor.write(temp_pdf_file)
        with open(temp_pdf_file, 'rb') as output_pdf:
            pdf_data = output_pdf.read()
    return pdf_data