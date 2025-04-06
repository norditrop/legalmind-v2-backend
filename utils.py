
from fastapi.responses import JSONResponse

def format_response(success: bool, message: str, data: dict = None):
    response = {
        "success": success,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return JSONResponse(content=response)

def extract_keywords(text: str, max_keywords: int = 5):
    words = text.lower().split()
    keywords = list(set(words))[:max_keywords]
    return keywords
