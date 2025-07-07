from services.file_service import FileService
import json
from enums.http_error import HttpError
from llm.ocr_extractor import NutritionFactExtractor

class OCRService:
    def __init__(self):
        self.file_service = FileService()
        self.nutrition_extractor = NutritionFactExtractor()
        
    
    async def extract_text(self, metadata_path: str) -> str:
        if not metadata_path:
            return HttpError.METADATA_NOT_FOUND.value
        output = self.nutrition_extractor.extract_from_image(image_path=metadata_path)
        return output