# services/image_processing_service.py
import httpx
import json
import logging
import os
from fastapi import UploadFile, HTTPException
from typing import Dict, Any

logger = logging.getLogger(__name__)

class ImageProcessingService:
    def __init__(self):
        # Đọc từ environment variables
        self.host = os.getenv("NUTRITION_EXTRACTOR_HOST", "localhost")
        self.port = os.getenv("NUTRITION_EXTRACTOR_PORT", "8000")
        self.upload_image_base_url = f"http://{self.host}:{self.port}/api/v1/image"
        self.ocr_base_url = f"http://{self.host}:{self.port}/api/v1/ocr"
        self.timeout = 60.0
        
    
    async def process_image_complete(self, file: UploadFile) -> Dict[str, Any]:
        try:
            # Bước 1: Upload image
            metadata_schema = await self._upload_image(file)
            
            # Bước 2: Extract text
            extract_result = await self._extract_text(metadata_schema)
            
            return extract_result
            
        except Exception as e:
            logger.error(f"Image processing failed: {str(e)}")
            raise e
    
    async def _upload_image(self, file: UploadFile) -> str:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                # Đọc file content
                await file.seek(0)
                file_content = await file.read()
                
                files = {
                    "file": (file.filename, file_content, file.content_type or "application/octet-stream")
                }
                
                response = await client.post(f"{self.upload_image_base_url}/upload-image/", files=files)
                response.raise_for_status()
                
                result = response.json()
                return result["metadata"]["path"]
                
            except httpx.HTTPError as e:
                logger.error(f"Upload failed: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Upload service error: {str(e)}")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON response: {str(e)}")
                raise HTTPException(status_code=500, detail="Invalid JSON response from upload service")
            except Exception as e:
                logger.error(f"Upload processing error: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Upload processing failed: {str(e)}")
        
    async def _extract_text(self, metadata_path: str) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(
                    f"{self.ocr_base_url}/extract-text/",
                    params={"path": metadata_path}
                )
                response.raise_for_status()
                
                result = response.json()
                return result
                
            except httpx.HTTPError as e:
                logger.error(f"Text extraction failed: {str(e)}")
                raise HTTPException(status_code=500, detail=f"OCR service error: {str(e)}")
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON response from OCR service: {str(e)}")
                raise HTTPException(status_code=500, detail="Invalid OCR service response")