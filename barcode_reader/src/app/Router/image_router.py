from fastapi import APIRouter, UploadFile, HTTPException, Depends
from Service.image_service import ImageService

router = APIRouter()

# Dependency to initialize ImageService
def get_image_service():
    return ImageService()

@router.post("/upload-image/")
async def upload_image(file: UploadFile, image_service: ImageService = Depends(get_image_service)):
    try:
        file_path = image_service.save_image(file)
        return {"message": "Image uploaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/read-barcode/")
async def read_barcode(file_path: str, image_service: ImageService = Depends(get_image_service)):
    try:
        barcodes = image_service.read_barcode(image_path=file_path)
        return {"barcodes": barcodes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
