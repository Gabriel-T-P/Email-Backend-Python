import io
import pytest
from tests.utils import make_pdf_bytes

from app.services.nlp_service import (
    extract_text_from_file,
    preprocess_text,
    process_file,
)

def test_extract_text_from_txt():
    content = "Este é um email de teste simples."
    file_bytes = content.encode("utf-8")

    result = extract_text_from_file(file_bytes, "teste.txt")
    assert "email de teste" in result


def test_extract_text_from_pdf():
    content = "Pedido de atualização do pedido 123"
    pdf_bytes = make_pdf_bytes(content)

    result = extract_text_from_file(pdf_bytes, "teste.pdf")
    assert "pedido" in result.lower()

'''
def test_preprocess_text_removes_stopwords_and_stems():
    text = "Os clientes estão comprando produtos rapidamente!"
    result = preprocess_text(text)

    # "os" e "estão" são stopwords em português
    assert "os" not in result
    assert "estão" not in result
    # "comprando" deve virar "compr"
    assert "compr" in result
'''

def test_process_file_txt_end_to_end():
    content = "O cliente fez uma reclamação sobre o produto."
    file_bytes = content.encode("utf-8")

    processed = process_file(file_bytes, "teste.txt")
    assert "client" in processed or "client"[:4] in processed  # stemming
    assert "reclam" in processed  # stemming de reclamação
