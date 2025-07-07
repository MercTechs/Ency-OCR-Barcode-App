from fastapi import APIRouter, UploadFile, HTTPException, Depends, status
from Service.image_service import ImageService
from Enums.image_exception import ImageProcessingError

router = APIRouter()

# Dependency to initialize ImageService
def get_image_service():
    return ImageService()

@router.post("/upload-image/")
async def upload_image(file: UploadFile, image_service: ImageService = Depends(get_image_service)):
    try:
        file_path = await image_service.save_image(file)
        return {"message": "Image uploaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/read-barcode/")
async def read_barcode(file_path: str, image_service: ImageService = Depends(get_image_service)):
    try:
        barcodes = image_service.read_barcode(image_path=file_path)
        return {"barcodes": barcodes}
    
    except FileNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Image file not found: {str(e)}"
        )
    
    except ImageProcessingError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail=f"Image processing failed: {str(e)}"
        )
    
    except PermissionError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"Permission denied accessing file: {str(e)}"
        )
    
    except Exception as e:
        # Log the unexpected error for debugging
        # logging.error(f"Unexpected error in read_barcode: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="An unexpected error occurred while processing the image"
        )
    
