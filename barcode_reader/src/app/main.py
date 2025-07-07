import os
from fastapi import FastAPI
from uvicorn import run
from dotenv import load_dotenv
from Router.image_router import router as image_router

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Include the image router with prefix and tags
app.include_router(image_router, prefix="/api/v1/image", tags=["Image"])

# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    host = os.getenv("BARCODE_READER_HOST", "127.0.0.1")  # Default fallback
    port = int(os.getenv("BARCODE_READER_PORT", "8000"))   # Default fallback
    debug = os.getenv("BARCODE_READER_DEBUG", "True").lower() == "true"
    
    run("main:app", host=host, port=port, reload=debug)