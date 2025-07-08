# main.py
from fastapi import FastAPI
from router.ocr_router import router as ocr_router
from router.barcode_router import router as barcode_router
import logging
import os
import uvicorn
# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Image Processing Gateway")

app.include_router(ocr_router, prefix="/api/v1", tags=["OCR"])
app.include_router(barcode_router, prefix="/api/v1", tags=["Barcode"])

if __name__ == "__main__":
    
    # Đọc từ environment variables
    host = os.getenv("GATEWAY_HOST", "0.0.0.0")
    port = int(os.getenv("GATEWAY_PORT", "8001"))
    
    # Log configuration
    logging.info(f"Starting Gateway Server on {host}:{port}")
    
    uvicorn.run(
        "main:app",  # Module:app format for reload
        host=host,
        port=port,
        reload=True,  # Enable auto-reload
        log_level="info"
    )