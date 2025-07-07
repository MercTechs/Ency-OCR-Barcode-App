from fastapi import FastAPI
from uvicorn import run
from Router.image_router import router as image_router

# Initialize FastAPI app
app = FastAPI()

# Include the image router with prefix and tags
app.include_router(image_router, prefix="/api/v1/image", tags=["Image"])

# Run the FastAPI app using uvicorn
if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=8000, reload=True)
