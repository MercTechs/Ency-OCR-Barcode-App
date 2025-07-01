from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from services.image_service import ImageService
from database.connection import DatabaseConnection
from schemas.metadata_schema import MetadataValidationSchema
from tasks.example_task import extract_text_task
from enums.http_error import HttpError
from fastapi import HTTPException
router = APIRouter()
db = DatabaseConnection()

@router.post("/extract-text/")
async def extract_text(metadata: MetadataValidationSchema):
    result = await extract_text_task.aio_run(metadata)
    match result:
        case HttpError.METADATA_NOT_FOUND.value:
            raise HTTPException(status_code=404, detail={"transformed_message": "Metadata not found"})
        case HttpError.IMAGE_NOT_VALIDATED_FOR_OCR.value:
            raise HTTPException(status_code=400, detail={"transformed_message": "Image not validated for OCR"})
        case _:
            return {"transformed_message": result} 
