import nltk

def setup_nltk():
    """
    Faz o download dos pacotes necessários do NLTK
    para processamento de linguagem natural.
    """
    packages = ["punkt", "stopwords", "punkt_tab"]

    for pkg in packages:
        try:
            nltk.data.find(f"tokenizers/{pkg}") if pkg == "punkt" else nltk.data.find(f"corpora/{pkg}")
            print(f"Pacote '{pkg}' já está disponível.")
        except LookupError:
            print(f"Baixando pacote '{pkg}'...")
            nltk.download(pkg)

if __name__ == "__main__":
    setup_nltk()
