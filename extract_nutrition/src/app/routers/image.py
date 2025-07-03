
from fastapi import APIRouter, Depends, UploadFile
from services.file_service import FileService
router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile):
    file_service = FileService()
    metadata_schema = await file_service.save_image(file)
    return {"metadata": metadata_schema}

