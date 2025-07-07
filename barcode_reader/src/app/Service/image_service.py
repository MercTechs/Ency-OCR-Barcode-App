from pathlib import Path
from fastapi import UploadFile
import cv2
from pyzbar import pyzbar
from Schemas.barcode_schema import BarcodeSchema
import aiofiles
from Enums.image_exception import ImageProcessingError

class ImageService:
    def __init__(self):
        self.save_directory="barcode_reader/src/media/"
        self.save_directory = Path(self.save_directory)
        self.save_directory.mkdir(parents=True, exist_ok=True)

    async def save_image(self, file: UploadFile) -> str:
        file_path = self.save_directory / file.filename
        async with aiofiles.open(file_path, "wb") as f:
            content = await file.read()
            await f.write(content)
        return str(file_path)
    
    def read_barcode(self, image_path) -> list[BarcodeSchema]:
        # Validate file path
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Load image
        image = cv2.imread(str(image_path))
        
        # Check if image was loaded successfully
        if image is None:
            raise ImageProcessingError(f"Failed to load image: {image_path}. File may be corrupted or not a valid image format.")
        
        # Decode barcodes
        barcodes = pyzbar.decode(image)
        
        barcode_schemas = []
        for barcode in barcodes:
            try:
                # Extract barcode data and type
                barcode_data = barcode.data.decode('utf-8')
                barcode_type = barcode.type
                
                barcode_schemas.append(BarcodeSchema(barcode_type=barcode_type, value=barcode_data))
            except UnicodeDecodeError as e:
                raise ImageProcessingError(f"Failed to decode barcode data as UTF-8: {e}")
        
        return barcode_schemas