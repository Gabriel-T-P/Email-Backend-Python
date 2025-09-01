import time
from IA.models.gemini_gen import generate_response
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import TextClassificationPipeline

# Carregar modelo e tokenizer uma vez no backend
MODEL_PATH = "IA/models/best_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

classifier = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    device="cpu"
)


def classify_email(text: str) -> dict:
    start_time = time.time()
    word_count = len(text.split())

    result = classifier(text, truncation=True, padding=True, max_length=512)[0]
    category = result["label"].lower()  # "produtivo" ou "improdutivo"
    confidence = round(float(result["score"]), 4)

    response = generate_response(category, text)

    processing_time = (time.time() - start_time) * 1000  # ms

    return {
        "success": True,
        "data": {
            "classification": {
                "category": category,
                "confidence": confidence
            },
            "analysis": {
                "processingTime": round(processing_time, 2),
                "wordCount": word_count
            },
            "response": response
        },
        "error": None
    }
