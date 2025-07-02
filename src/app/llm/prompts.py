def create_extract_nutrition_prompt(ocr_text: str) -> str:
    return f"""
                    Extract nutritional information from the nutrition facts label text below.
                    Return the result as a list of items, each in this format:
                    {{
                    "name": "Nutrient name as shown in label",
                    "amount": "value with unit, or null if not shown",
                    "daily_value_percent": "percent value or null if not shown"
                    }}
                    Only include data explicitly shown in the label text. Do not guess or invent missing fields.
                    Units and naming must match exactly as in the label.

                    IMPORTANT:
                    The OCR process often misreads the letter 'g' (for grams) as the number '9', so values like:
                    - "19" should be interpreted as "1g"
                    - "29" → "2g"
                    - "39" → "3g"
                    - ...
                    - "129" → "12g"
                    - "139" → "13g"
                    - "169" → "16g"
                    - "09" → "0g"
                    Any amount that ends with '9' but does NOT have a valid unit like "g", "mg", "kcal", etc., is likely intended to be a value with a unit letter, and the final '9' should actually be 'g'.

                    The value for amount **must always** end with a valid unit like "g", "mg", "mcg", "IU", "kcal" and not %.
                    The unit end with % must be daily value percent and never put in the amount field.
                    If amount is % unit, then amount must be null and daily_value_percent must be the value.

                    Nutrition label text:
                    \"\"\"
                    {ocr_text}
                    \"\"\"
                    """