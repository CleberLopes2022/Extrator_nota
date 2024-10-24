import streamlit as st
import pypdf
import re

def extract_nf_key(pdf_file):
    # Lê o arquivo PDF
    reader = PyPDF2.PdfReader(pdf_file)
    key = None
    
    # Procura pela chave da nota fiscal no texto das páginas
    for page in reader.pages:
        text = page.extract_text()
        if text:
            # Usando regex para encontrar a chave da nota fiscal (44 dígitos separados por espaços a cada 4 dígitos)
            match = re.search(r'(\d{4}\s){10}\d{4}', text)
            if match:
                # Remove os espaços para retornar a chave com os 44 dígitos
                key = match.group(0).replace(' ', '')
                break
                
    return key

st.title("Extrator de Chave da Nota Fiscal")
st.write("Carregue sua nota fiscal em PDF para extrair a chave.")

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    # Extrai a chave da nota fiscal
    nf_key = extract_nf_key(uploaded_file)
    
    if nf_key:
        st.success("Chave da Nota Fiscal extraída com sucesso!")
        
        # Exibe a chave da nota fiscal em um campo de entrada para facilitar a cópia
        st.text_input("Selecione a chave abaixo e pressione Ctrl+C para copiá-la", value=nf_key)
        
        st.info("Selecione o texto acima e use Ctrl+C para copiar")
    else:
        st.error("Chave da Nota Fiscal não encontrada no documento.")



