from llm.llm_singleton import LLMSingleton
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

class OCREngine:
    def __init__(self):
        # Load marker-pdf models
        self.models = create_model_dict()
        self.pdf_converter = PdfConverter(
            artifact_dict=self.models,
        )

    def extract_text(self, img_path):
        # Use marker-pdf converter to read the image/PDF
        rendered = self.pdf_converter(img_path)
        full_text, _, images = text_from_rendered(rendered)
        return full_text
    

class NutritionFactExtractor:
    def __init__(self):
        self.ocr_engine = OCREngine()
        self.nutrition_model = LLMSingleton.get_instance()

    def extract_from_image(self, image_path):
        ocr_text = self.ocr_engine.extract_text(image_path)
        result = self.nutrition_model.extract_nutrition(ocr_text)
        return result