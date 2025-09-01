from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    text: str = Field(
        ...,
        description="Texto bruto do email recebido.",
        example="Preciso de atualização do meu chamado #12345"
    )
