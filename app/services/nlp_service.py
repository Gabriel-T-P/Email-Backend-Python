import io
import re
# import string
from PyPDF2 import PdfReader
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import SnowballStemmer

# STOPWORDS = set(stopwords.words("portuguese"))
# STEMMER = SnowballStemmer("portuguese")


def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """
    Extrai texto de arquivos .txt ou .pdf
    """
    text = ""
    if filename.endswith(".txt"):
        text = file_bytes.decode("utf-8", errors="ignore")
    elif filename.endswith(".pdf"):
        pdf_reader = PdfReader(io.BytesIO(file_bytes))
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


def preprocess_text(text: str) -> str:
    """
    Pré-processamento de texto:
    - lowercase
    - remove pontuação
    - remove stopwords
    - aplica stemming

    Versão Atual não faz as opções acima, somente retira espaços duplos,
    pois esse pre-processamento estava quebrando o meu model que foi treinado
    sem isso.
    """

    text = re.sub(r"\s+", " ", text)  # remove espaços duplicados
    return text.strip()

    # 1. lowercase
    # text = text.lower()

    # 2. remove pontuação
    # text = text.translate(str.maketrans("", "", string.punctuation))

    # 3. tokenização simples
    # tokens = nltk.word_tokenize(text, language="portuguese")

    # 4. remove stopwords e aplica stemming
    # processed_tokens = [STEMMER.stem(t) for t in tokens if t not in STOPWORDS]

    # return " ".join(processed_tokens)


def process_file(file_bytes: bytes, filename: str) -> str:
    """
    Extrai o texto do arquivo e aplica NLP
    """
    raw_text = extract_text_from_file(file_bytes, filename)
    processed_text = preprocess_text(raw_text)
    return processed_text
