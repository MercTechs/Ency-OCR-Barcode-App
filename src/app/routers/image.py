
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from services.image_service import ImageService
from services.file_service import FileService
from database.connection import DatabaseConnection
from schemas.metadata_schema import MetadataValidationSchema
from tasks.example_task import upload_image_task, validate_image_task
from enums.http_error import HttpError
from fastapi import HTTPException

router = APIRouter()
db = DatabaseConnection()

@router.post("/upload-image/")
async def upload_image(file: UploadFile):
    file_service = FileService()
    metadata_schema = await file_service.save_image(file)
    task_result = await upload_image_task.aio_run(metadata_schema)
    return {"metadata": task_result}

@router.post("/validate-image/")
async def validate_image(metadata: MetadataValidationSchema):
    result = await validate_image_task.aio_run(metadata)
    match result:
        case HttpError.METADATA_NOT_FOUND.value:
            raise HTTPException(status_code=404, detail={"transformed_message": "Metadata not found"})
        case HttpError.IMAGE_NOT_VALIDATED_FOR_OCR.value:
            raise HTTPException(status_code=400, detail={"transformed_message": "Image not validated for OCR"})
        case _:
            return {"transformed_message": "Image validated successfully"}
