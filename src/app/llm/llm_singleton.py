import os
from PIL import Image
from llama_cpp import Llama
from marker.converters.table import TableConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from dotenv import load_dotenv
from prompts import create_extract_nutrition_prompt

load_dotenv()

class LLMSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if LLMSingleton.__instance is None:
            LLMSingleton()
        return LLMSingleton.__instance

    def __init__(self):
        if LLMSingleton.__instance is not None:
            raise Exception("This is a singleton class.")
        model_path = os.environ.get("LLM_MODEL_PATH")
        if not model_path:
            raise ValueError("LLM_MODEL_PATH environment variable not set")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_gpu_layers=33,
        )
        LLMSingleton.__instance = self

    def extract_nutrition(self, ocr_text):
        prompt = create_extract_nutrition_prompt(ocr_text)
        output = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
        )
        return output["choices"][0]["message"]["content"]





# def main():
#     # Bắt buộc phải export biến môi trường LLM_MODEL_PATH trước khi chạy file này
#     # export LLM_MODEL_PATH=/path/to/your/model.gguf
#     image_path = os.environ.get("IMAGE_PATH") or "/home/aidontknow/Projects/Nutrition-Fact-Reader/src/media/fda_ntfact.jpg"

#     extractor = NutritionFactExtractor()
#     print("=== STRUCTURED NUTRITION OUTPUT ===\n")
#     output = extractor.extract_from_image(image_path)
#     print(output)
#     print("\n=== END STRUCTURED OUTPUT ===")

# if __name__ == "__main__":
#     main()