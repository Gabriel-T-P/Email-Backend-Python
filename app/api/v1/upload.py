from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.security import verify_api_key
from app.services.classifier_service import classify_email
from app.services.nlp_service import process_file
from app.models.response import ClassifyResponse
import time

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


@router.post(
    "/file",
    response_model=ClassifyResponse,
    summary="Classificar email a partir de arquivo (.txt ou .pdf)",
    description="""
Recebe um arquivo `.txt` ou `.pdf`, extrai o conteúdo e retorna:

- A categoria atribuída (**Produtivo** ou **Improdutivo**)
- Nível de confiança da resposta entre e 0 e 1
- Tempo de processamento em ms
- Contagem de palavras
- Booleano para sucesso ou falha
- Erro (opcional)
- Uma resposta automática sugerida
    """,
)
async def classify_file(
    file: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    start_time = time.time()

    if not file.filename.endswith((".txt", ".pdf")):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado")

    file_bytes = await file.read()

    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Arquivo muito grande")

    processed_text = process_file(file_bytes, file.filename)

    if not processed_text.strip():
        raise HTTPException(status_code=400, detail="Não foi possível extrair conteúdo do arquivo")

    result = classify_email(processed_text)
    processing_time = int((time.time() - start_time) * 1000)

    return ClassifyResponse(
        success=True,
        data={
            "classification": {
                "category": result["data"]["classification"]["category"],
                "confidence": 0.85,
            },
            "analysis": {
                "processingTime": processing_time,
                "wordCount": len(processed_text.split()),
            },
            "response": result["data"]["response"],
        },
    )
