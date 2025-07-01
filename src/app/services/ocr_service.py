from openai_client.openai_client import openai_client
from openai_client.openai_prompt import extract_text_message, create_image_message
from services.file_service import FileService
from repositories.metadata_repository import MetadataRepository
import json
from enums.http_error import HttpError

class OCRService:
    def __init__(self, db):
        self.metadata_repository = MetadataRepository(db)
        self.file_service = FileService()
    
    async def extract_text(self, metadata_id: str) -> str:
        metadata = await self.metadata_repository.get_metadata(metadata_id)
        if not metadata:
            return HttpError.METADATA_NOT_FOUND.value
        if not metadata.is_valid:
            return HttpError.IMAGE_NOT_VALIDATED_FOR_OCR.value
        
        image_base64 = self.file_service.read_image_as_base64(metadata.path)

        # Update the metadata in the database
        response = openai_client.chat.completions.create(
            model="gpt-4.1",
            messages=create_image_message(extract_text_message, image_base64),
        )

        tool_call = response.choices[0].message.content
        return json.loads(tool_call)