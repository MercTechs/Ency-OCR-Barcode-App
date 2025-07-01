import os
import uuid
from repositories.metadata_repository import MetadataRepository
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Metadata
from services.file_service import FileService
from schemas.metadata_schema import MetadataSchema
from openai_client.openai_client import openai_client
from openai_client.openai_prompt import validate_image_prompt, create_image_message, validate_image_message
import base64
import json
from enums.http_error import HttpError
class ImageService:
    def __init__(self, db: AsyncSession):
        self.metadata_repository = MetadataRepository(db)
        self.file_service = FileService()
        self.db = db
        
    async def save_metadata(self, metadata: MetadataSchema) -> Metadata:
        # Convert schema to model and use repository to save to the database
        metadata_model = Metadata(
            filename=metadata.filename,
            path=metadata.path,
            is_valid=metadata.is_valid,
            file_size=metadata.file_size
        )
        return await self.metadata_repository.create_metadata(metadata_model)

    async def process_and_save(self, file: UploadFile) -> int:
        # Save the image and get metadata
        metadata = await self.file_service.save_image(file)

        # Save metadata to the database
        metadata_model = await self.save_metadata(metadata)

        # Return the metadata ID
        return metadata_model.id
    
    
    async def validate_image(self, metadata_id: str):
        # Retrieve metadata from the database
        metadata = await self.metadata_repository.get_metadata(metadata_id)
        if not metadata:
            return HttpError.METADATA_NOT_FOUND.value
        
        image_base64 = self.file_service.read_image_as_base64(metadata.path)

        # Update the metadata in the database
        response = openai_client.chat.completions.create(
            model="gpt-4.1",
            messages=create_image_message(validate_image_message, image_base64),
            tools=validate_image_prompt
        )

        tool_call = response.choices[0].message.tool_calls[0]
        function_args_json = tool_call.function.arguments
        args = json.loads(function_args_json)

        is_valid = args["is_nutrition_facts"]
        if is_valid:
            await self.metadata_repository.update_metadata(
            metadata_id,
            {"is_valid": is_valid}
            )
            return "Image is valid"
        return HttpError.IMAGE_NOT_VALID.value
        