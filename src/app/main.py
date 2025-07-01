from fastapi import FastAPI
from workers.hatchet_worker import upload_image_worker
from database.connection import DatabaseConnection
from routers.image import router as image_router
from routers.ocr import router as ocr_router
import uvicorn
import asyncio
app = FastAPI()
from hatchet_sdk import Hatchet

# Include the router
app.include_router(image_router, prefix="/api/v1/image", tags=["Image"])
app.include_router(ocr_router, prefix="/api/v1/ocr", tags=["OCR"])

async def main():
    db = DatabaseConnection()
    await db.create_db_and_tables()
    print("Tables created successfully.")
    uvicorn.run("main:app", reload=True)
    print("FastAPI app is running.")

if __name__ == "__main__":
    asyncio.run(main())
    