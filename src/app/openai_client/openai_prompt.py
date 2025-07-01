validate_image_prompt = [{
    "type": "function",
    "function": {
        "name": "is_nutrition_facts_image",
        "description": "Xác định ảnh có phải là bảng thành phần dinh dưỡng (nutrition facts) hay không.",
        "parameters": {
            "type": "object",
            "properties": {
                "is_nutrition_facts": {
                    "type": "boolean"
                }
            },
            "required": ["is_nutrition_facts"],
            "additionalProperties": False
        }
    }
}]

validate_image_message = "Is this a nutrition facts label?"
extract_text_message = """You are a nutrition facts label extractor.
The user will send you an image of a nutrition label. From this image, extract all visible nutritional components. For each component, return both the value (with units) and, if available, the % Daily Value.

Return the result as a list of items, each with the following format:
{
  "name": "Nutrient name as shown in label",
  "amount": "value with unit, or null if not shown",
  "daily_value_percent": "value or null if not shown"
}

Only include data explicitly shown in the label. Do not guess or infer missing values.
"""

def create_image_message(text: str, image_base64: str) -> list:
    """
    Create a message for the OpenAI API with an image.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"{text}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
            ]
        }
    ]
    return messages
# Prepare the messages

