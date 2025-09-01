# 📧 Email Classifier API

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Gabriel-T-P/Email-Backend-Python)

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)

Este projeto é uma API construída em **FastAPI** para classificar emails em **Produtivo** ou **Improdutivo** e sugerir respostas automáticas.  
Agora a API também suporta **upload de arquivos .txt e .pdf**, extraindo o conteúdo e processando-o.

---

## 🚀 Funcionalidades

- Endpoint `/api/v1/text/` que recebe texto bruto de email e retorna:
  - Categoria (`Produtivo` ou `Improdutivo`)
  - Resposta sugerida

- Endpoint `/api/v1/file/` que permite enviar arquivos `.txt` ou `.pdf` e retorna:
  - Texto extraído do arquivo
  - Categoria e resposta sugerida

- Documentação automática via **Swagger UI** em `/docs`.

- Testes unitários básicos com **pytest**.

- Tinha pré-processamento de texto com **NLTK** (remoção de stopwords, lematização), removido no final do projeto.

---

## 🛠️ Instalação e Setup

**Pré-requisitos:**
- Python 3.9+

### 1. Clonar o repositório
```bash
git clone git@github.com:Gabriel-T-P/Email-Backend-Python.git
cd Email-Backend-Python
```

### 2. Criar e ativar ambiente virtual
```bash
# Criar o ambiente virtual
python3 -m venv venv_email

# Ativar no Linux/Mac
source venv_email/bin/activate

# Ativar no Windows (PowerShell)
venv_email\Scripts\activate
```

Você saberá que está ativo quando aparecer `(venv_email)` no início da linha do terminal.

### 3. Configurar variáveis de ambiente
Este projeto usa um arquivo `.env` para gerenciar chaves de API e outras configurações.

```bash
# Crie uma cópia do arquivo de exemplo e complete as informações

# Linux
cp .env.example .env

# Windows
copy .env.example .env
```

### 4. Instalar dependências
Existem 3 arquivos diferentes de dependência: Deploy, Desenvolvimento e IA

- **Deploy (FastAPI, uvicorn, pydantic, ...):**
```bash
pip install -r requirements.txt
```

- **Desenvolvimento (pytest, flake8, ...):**
```bash
pip install -r requirements-dev.txt
```

- **Treinamento da IA (transformes, dataset, ...):**
```bash
pip install -r requirements-ia.txt
```

### 5. Baixar recursos do NLTK
Antes de rodar a aplicação pela primeira vez, inicialize os recursos do NLTK:
Esse passo pode ser ignorado por enquanto.
```bash
python3 setup_nltk.py
```

---

## ▶️ Rodando a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:
- **API Root:** http://127.0.0.1:8000  
- **Swagger Docs:** http://127.0.0.1:8000/docs  

- **Classificação de Texto:** Endpoint `/api/v1/text/` que recebe texto bruto.
- **Classificação de Arquivos:** Endpoint `/api/v1/file/` que aceita arquivos `.txt` e `.pdf`.
- **Documentação Interativa:** Interface Swagger UI em `/docs` e ReDoc em `/redoc`.

---

## 🧪 Rodando os testes

```bash
pytest
```

---

## 📂 Estrutura do Projeto

```
project/
│
├── app/                  
│   ├── api/
│   │    └── v1/
│   │        ├── classify.py         # Endpoints da API
│   │        └── upload.py           # Endpoint para upload de arquivos
│   │
│   ├── core/
│   │   └── config.py               # Configurações do projeto
│   │
│   ├── models/
│   │   └── email.py                # Schema Pydantic de request
│   │   └── response.py             # Schema Pydantic de response
│   │
│   ├── services/
│   │   ├── classifier_service.py   # Lógica de classificação (mock inicial)
│   │   └── nlp_service.py          # Lógica de pré-processamento NLP
│   ├── main.py                     # Ponto de entrada da aplicação
│   └── security.py                 # Arquivo de configuração da chave da API
│
├── IA/
│   ├── models/                     # Modelos usados no projeto
│   ├── dataset.csv                 # Dataset utilizado para treinamento do modelo
│   └── train.ipynb                 # Arquivo Jupyter Notebook com script do treinamento
│
├── tests/
│   ├── conftest.py                 # Arquivo de configuração de testes
│   ├── test_classify.py            # Testes unitários para classificação de texto
│   ├── test_upload.py              # Testes unitários para upload de arquivos
│   ├── test_nlp_service.py         # Testes unitários para o serviço de Processamento de Linguagem Natural
│   └── utils.py                    # Helpers reutilizáveis nos testes
│
├── .env.example                    # Formato do .env
├── setup_nltk.py                   # Script para baixar recursos do NLTK
├── .flake8                         # Script para regular o lint dessa biblioteca
├── .python-version                 # especificação da versão do python para deploy no render
├── pytest.ini                      # Arquivo de configuração inicial do pytest
├── render.yaml                     # Arquivo de configuração de deploy
├── requirements.txt                # API
├── requirements-dev.txt            # DEV
└── requirements-ia.txt             # IA
```