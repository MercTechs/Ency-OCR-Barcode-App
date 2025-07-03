from fastapi import APIRouter
from schemas.metadata_schema import MetadataValidationSchema
from services.ocr_service import OCRService
import json
import re
router = APIRouter()


@router.post("/extract-text/")
async def extract_text(path: str):
    ocr_service = OCRService()
    output = await ocr_service.extract_text(metadata_path=path)

    # Loại bỏ markdown code block ```json ... ```
    cleaned_output = re.sub(r"^```json\s*|\s*```$", "", output.strip())

    try:
        parsed_output = json.loads(cleaned_output)
        return {"output": parsed_output}
    except json.JSONDecodeError:
        return {"error": "Still not valid JSON", "cleaned_output": cleaned_output}


