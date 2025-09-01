import google.generativeai as genai
import os
from dotenv import load_dotenv

# carregando api key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def generate_response(category: str, text: str) -> str:
    prompt = f"""
Você é um assistente de email automatizado em português. 

Categoria do email: {category}
Mensagem recebida: "{text}"

Instruções:
- Se a categoria for 'produtivo', responda de forma profissional confirmando recebimento e informando que o assunto será tratado com prioridade.
- Se a categoria for 'improdutivo', responda de forma simpática, curta, sem compromisso de retorno, agradecendo a mensagem.

Gere apenas a resposta do email, sem cabeçalhos ou cumprimentos extras.
"""
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text.strip()
