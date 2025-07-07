import os
from fastapi import FastAPI
from routers.image import router as image_router
from routers.ocr import router as ocr_router
import uvicorn
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Include the routers
app.include_router(image_router, prefix="/api/v1/image", tags=["Image"])
app.include_router(ocr_router, prefix="/api/v1/ocr", tags=["OCR"])

async def main():
    print("Tables created successfully.")
    
    # Get host and port from environment variables
    host = os.getenv("NUTRITION_EXTRACTOR_HOST", "127.0.0.1")
    port = int(os.getenv("NUTRITION_EXTRACTOR_PORT", "8000"))
    reload = os.getenv("NUTRITION_EXTRACTOR_DEBUG", "True").lower() == "true"
    
    # Run uvicorn with environment variables
    uvicorn.run("main:app", host=host, port=port, reload=reload)
    print("FastAPI app is running.")

if __name__ == "__main__":
    asyncio.run(main())