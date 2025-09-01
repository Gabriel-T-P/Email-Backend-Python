from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.classify import router as classify_router
from app.api.v1.upload import router as upload_router

app = FastAPI(
    title="Email Classifier API",
    version="1.0.0",
    description="API para classificar emails e sugerir respostas automáticas."
)

# CORS
origins = [
    "http://localhost:3000",
    "https://email-frontend-nu.vercel.app",
    "https://*.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    """
    Rota raiz da API. Retorna uma mensagem de boas-vindas e status.
    """
    return {
        "status": "ok",
        "message": "Bem-vindo! Visite /docs para ver a documentação interativa da API."
    }


# Inclui rotas da API
app.include_router(classify_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
