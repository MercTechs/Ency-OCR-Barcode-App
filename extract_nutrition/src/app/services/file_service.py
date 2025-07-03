from fastapi import UploadFile
import os
import uuid
import base64
from schemas.metadata_schema import MetadataSchema
class FileService:
    async def save_image(self, file: UploadFile) -> MetadataSchema:
        # Generate a random file name
        file_extension = file.filename.split(".")[-1]
        file_name = f"{uuid.uuid4()}.{file_extension}"
        media_dir = "src/media"
        file_path = os.path.join(media_dir, file_name)

        os.makedirs(media_dir, exist_ok=True)

        # Save the file to the media directory
        try:
            with open(file_path, "wb") as f:
                content = await file.read()
                f.write(content)
                # Create metadata
                metadata = MetadataSchema(
                    filename=file_name,
                    path=file_path,
                    is_valid=False,
                    file_size=os.path.getsize(file_path)
                )
                return metadata
        except Exception as e:
            return None
        
    def read_image_as_base64(self, path: str) -> str:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")