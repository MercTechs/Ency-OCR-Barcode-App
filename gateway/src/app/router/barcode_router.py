from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from service.barcode_service import BarcodeAPIService
from auth.api_key_auth import get_api_key

router = APIRouter()
image_service = BarcodeAPIService()

@router.post("/upload-and-read-barcode")
async def upload_and_read_barcode(file: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    """
    Upload image và đọc barcode
    """
    try:
        barcodes = await image_service.upload_and_read_barcode(file)
        return {
            "success": True,
            "barcodes": barcodes,
            "count": len(barcodes)
        }
    except HTTPException:
        # Re-raise HTTPException từ service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )