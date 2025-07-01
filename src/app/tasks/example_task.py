from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from services.image_service import ImageService
from hatchet_sdk import Hatchet, Context
from hatchet_client import hatchet
from pydantic import BaseModel
from database.connection import DatabaseConnection
from schemas.metadata_schema import MetadataSchema, MetadataValidationSchema
from services.image_service import ImageService
from services.ocr_service import OCRService
from enums.http_error import HttpError
from fastapi import HTTPException

db = DatabaseConnection()

class SimpleInput(BaseModel):
    txt: str

@hatchet.task(
    name="upload_image_task",
    input_validator=MetadataSchema,
)
async def upload_image_task(input: MetadataSchema, ctx: Context) -> str:
    """
    Task to process and save an uploaded image.
    """
    async with db.get_session() as session:
        image_service = ImageService(session)
        metadata = await image_service.save_metadata(input)
        metadata_id = metadata.id
        return {"transformed_message": metadata_id} 
    
@hatchet.task(
    name="validate_image_task",
    input_validator=MetadataValidationSchema,
)
async def validate_image_task(input: MetadataValidationSchema, ctx: Context) -> bool:
    """
    Task to process and save an uploaded image.
    """
    async with db.get_session() as session:
        image_service = ImageService(session)
        result = await image_service.validate_image(input.metadata_id)
        return result
    
@hatchet.task(
    name="extract_text_task",
    input_validator=MetadataValidationSchema,
)
async def extract_text_task(input: MetadataValidationSchema, ctx: Context) -> bool:
    """
    Task to process and save an uploaded image.
    """
    async with db.get_session() as session:
        ocr_service = OCRService(session)
        result = await ocr_service.extract_text(input.metadata_id)
        return result
        
       