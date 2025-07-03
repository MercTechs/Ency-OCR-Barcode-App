from llm.llm_singleton import LLMSingleton
from marker.converters.table import TableConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

class OCREngine:
    def __init__(self):
        self.converter = TableConverter(
            artifact_dict=create_model_dict(),
        )

    def extract_text(self, img_path):
        rendered = self.converter(img_path)
        text, _, images = text_from_rendered(rendered)
        return text

class NutritionFactExtractor:
    def __init__(self):
        self.ocr_engine = OCREngine()
        self.nutrition_model = LLMSingleton.get_instance()

    def extract_from_image(self, image_path):
        ocr_text = self.ocr_engine.extract_text(image_path)
        result = self.nutrition_model.extract_nutrition(ocr_text)
        return result