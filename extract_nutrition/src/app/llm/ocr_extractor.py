from llm.llm_singleton import LLMSingleton
import easyocr
from llm.llm_singleton import LLMSingleton
from marker.converters.pdf import PdfConverter  # Change this
from marker.converters.ocr import OCRConverter  # Change this

class OCREngine:
    def __init__(self):
        # Initialize with both English and Vietnamese
        self.reader = easyocr.Reader(['en', 'vi'])  # Both English and Vietnamese

    def extract_text(self, img_path):
        # Use EasyOCR to read the image
        result = self.reader.readtext(img_path)
        
        # Extract text with confidence scores
        extracted_text = []
        for (bbox, text, confidence) in result:
            if confidence > 0.3:  # Filter low confidence results
                extracted_text.append(text)
        
        # Join all text
        full_text = "\n".join(extracted_text)
        return full_text
    
    

class NutritionFactExtractor:
    def __init__(self):
        self.ocr_engine = OCREngine()
        self.nutrition_model = LLMSingleton.get_instance()

    def extract_from_image(self, image_path):
        ocr_text = self.ocr_engine.extract_text(image_path)
        result = self.nutrition_model.extract_nutrition(ocr_text)
        return result