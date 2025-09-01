from pydantic import BaseModel
from typing import Optional, Literal


class Classification(BaseModel):
    category: Literal["produtivo", "improdutivo"]
    confidence: float


class Analysis(BaseModel):
    processingTime: float  # em ms
    wordCount: int


class ClassifyData(BaseModel):
    classification: Classification
    analysis: Analysis
    response: str


class ClassifyResponse(BaseModel):
    success: bool
    data: Optional[ClassifyData] = None
    error: Optional[str] = None
