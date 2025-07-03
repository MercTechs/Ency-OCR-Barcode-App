from pathlib import Path
from fastapi import UploadFile
import cv2
from pyzbar import pyzbar


class ImageService:
    def __init__(self):
        self.save_directory="barcode_reader/src/media/"
        self.save_directory = Path(self.save_directory)
        self.save_directory.mkdir(parents=True, exist_ok=True)

    def save_image(self, file: UploadFile) -> str:
        file_path = self.save_directory / file.filename
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return str(file_path)
    
    def read_barcode(self, image_path):
    # Load image
        image = cv2.imread(image_path)
        
        # Decode barcodes
        barcodes = pyzbar.decode(image)
        
        for barcode in barcodes:
            # Extract barcode data and type
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            
            print(f"Found {barcode_type} barcode: {barcode_data}")
            
            # Get barcode coordinates
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        return barcodes