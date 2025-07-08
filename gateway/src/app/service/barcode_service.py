from fastapi import UploadFile, HTTPException, status
import httpx
from config.api_config import APIConfig

apiConfig = APIConfig()

class BarcodeAPIService:
    def __init__(self):
        self.upload_img_url = apiConfig.barcode_upload_img_api_url
        self.read_barcode_url = apiConfig.barcode_read_api_url
        self.timeout = 30.0 
        
    async def _make_request(self, method: str, url: str, **kwargs) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    error_detail = response.json().get("detail", "API request failed")
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=f"API error: {error_detail}"
                    )
                    
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Unable to connect to service: {str(e)}"
            )
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unexpected error: {str(e)}"
            )
    
    async def upload_image(self, file: UploadFile) -> str:
        file_content = await file.read()
        await file.seek(0)
        
        files = {
            "file": (file.filename, file_content, file.content_type)
        }
        
        result = await self._make_request("POST", self.upload_img_url, files=files)
        return result["file_path"]
    
    async def read_barcode(self, file_path: str) -> list:
        params = {"file_path": file_path}
        result = await self._make_request("GET", self.read_barcode_url, params=params)
        return result["barcodes"]
    
    async def upload_and_read_barcode(self, file: UploadFile) -> list:
        file_path = await self.upload_image(file)
        barcodes = await self.read_barcode(file_path)
        return barcodes