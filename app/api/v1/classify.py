from fastapi import APIRouter, Depends, HTTPException
from app.security import verify_api_key
from app.models.email import EmailRequest
from app.models.response import ClassifyResponse
from app.services.classifier_service import classify_email
from app.services.nlp_service import preprocess_text
import time

router = APIRouter()

MAX_TEXT_LENGTH = 5000  # limite máximo de caracteres
MIN_TEXT_LENGTH = 10    # limite mínimo de caracteres
MAX_WORDS = 800         # limite de palavras


@router.post(
    "/text",
    response_model=ClassifyResponse,
    summary="Classificar email a partir de texto puro",
    description="""
Recebe o conteúdo de um email como **texto simples** e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Nível de confiança da resposta entre e 0 e 1
- Tempo de processamento em ms
- Contagem de palavras
- Booleano para sucesso ou falha
- Erro (opcional)
- Uma resposta automática sugerida
    """,
)
async def classify_text(
    request: EmailRequest,
    api_key: str = Depends(verify_api_key)
):
    start_time = time.time()

    # validações extras
    if len(request.text) > MAX_TEXT_LENGTH:
        raise HTTPException(status_code=400, detail="Texto muito grande")
    if len(request.text) < MIN_TEXT_LENGTH:
        raise HTTPException(status_code=400, detail="Texto muito pequeno")
    if len(request.text.split()) > MAX_WORDS:
        raise HTTPException(status_code=400, detail="Texto com muitas palavras")

    processed_text = preprocess_text(request.text)
    result = classify_email(processed_text)
    processing_time = int((time.time() - start_time) * 1000)  # ms

    return ClassifyResponse(
        success=True,
        data={
            "classification": {
                "category": result["data"]["classification"]["category"],
                "confidence": result["data"]["classification"]["confidence"],
            },
            "analysis": {
                "processingTime": processing_time,
                "wordCount": len(request.text.split()),
            },
            "response": result["data"]["response"],
        },
    )
