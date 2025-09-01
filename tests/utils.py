import io
from reportlab.pdfgen import canvas

def make_pdf_bytes(text: str) -> bytes:
    """Gera um PDF em memória com o texto passado (para testes)."""
    pdf_bytes = io.BytesIO()
    c = canvas.Canvas(pdf_bytes)
    c.drawString(100, 750, text)
    c.save()
    pdf_bytes.seek(0)
    return pdf_bytes.read()

def make_txt_bytes(text: str) -> bytes:
    """
    Gera um arquivo TXT em memória com o texto passado.
    Retorna os bytes do TXT.
    """
    return text.encode("utf-8")
