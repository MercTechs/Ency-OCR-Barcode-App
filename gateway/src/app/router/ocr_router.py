# routers/gateway_router.py
from fastapi import APIRouter, UploadFile, HTTPException, Depends
from service.ocr_service import ImageProcessingService
from auth.api_key_auth import get_api_key
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

# Khởi tạo service
image_service = ImageProcessingService()

@router.post("/process-image/")
async def process_image(file: UploadFile, api_key: str = Depends(get_api_key)):
    """
    Gateway endpoint để xử lý image hoàn chỉnh
    """
    try:
        result = await image_service.process_image_complete(file)
        return result
        
    except HTTPException:
        # Re-raise HTTPException từ service
        raise
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected error in gateway: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")