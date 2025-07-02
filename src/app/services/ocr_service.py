from services.file_service import FileService
from repositories.metadata_repository import MetadataRepository
import json
from enums.http_error import HttpError
from llm.ocr_extractor import NutritionFactExtractor

class OCRService:
    def __init__(self, db):
        self.metadata_repository = MetadataRepository(db)
        self.file_service = FileService()
        self.nutrition_extractor = NutritionFactExtractor()
        
    
    async def extract_text(self, metadata_id: str) -> str:
        metadata = await self.metadata_repository.get_metadata(metadata_id)
        if not metadata:
            return HttpError.METADATA_NOT_FOUND.value
        if not metadata.is_valid:
            return HttpError.IMAGE_NOT_VALIDATED_FOR_OCR.value
        output = self.nutrition_extractor.extract_from_image(image_path=metadata.path)
        return output