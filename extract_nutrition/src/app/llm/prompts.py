def create_extract_nutrition_prompt(ocr_text: str) -> str:
    return f"""
Extract nutritional information from the nutrition facts label text below.
Return the result as a JSON object with ALL these exact field names and NUMERIC VALUES ONLY (no units).
For fields not found in the label, use null.

Required format (ALL fields must be included):
{{
    "nutrients.energy": numeric_value_or_null,
    "nutrients.water": null,
    "nutrients.procnt": numeric_value_or_null,
    "nutrients.fat": numeric_value_or_null,
    "nutrients.chocdf": numeric_value_or_null,
    "nutrients.fibc": numeric_value_or_null,
    "nutrients.ash": null,
    
    "minerals.ca": numeric_value_or_null,
    "minerals.p": null,
    "minerals.fe": numeric_value_or_null,
    "minerals.zn": null,
    "minerals.na": numeric_value_or_null,
    "minerals.k": numeric_value_or_null,
    "minerals.mg": null,
    "minerals.mn": null,
    "minerals.cu": null,
    "minerals.se": null,
    
    "vitamins.vitc": null,
    "vitamins.thia": null,
    "vitamins.ribf": null,
    "vitamins.nia": null,
    "vitamins.pantac": null,
    "vitamins.vitb6": null,
    "vitamins.fol": null,
    "vitamins.folac": null,
    "vitamins.biot": null,
    "vitamins.vitb12": null,
    "vitamins.retol": null,
    "vitamins.vita": null,
    "vitamins.vitd": numeric_value_or_null,
    "vitamins.vite": null,
    "vitamins.vitk": null,
    "vitamins.cartb": null,
    "vitamins.carta": null,
    "vitamins.crypxb": null,
    
    "amino_acids.lys": null,
    "amino_acids.met": null,
    "amino_acids.trp": null,
    "amino_acids.phe": null,
    "amino_acids.thr": null,
    "amino_acids.val": null,
    "amino_acids.leu": null,
    "amino_acids.ile": null,
    "amino_acids.arg": null,
    "amino_acids.his": null,
    "amino_acids.cys": null,
    "amino_acids.tyr": null,
    "amino_acids.ala": null,
    "amino_acids.asp": null,
    "amino_acids.glu": null,
    "amino_acids.gly": null,
    "amino_acids.pro": null,
    "amino_acids.ser": null,
    
    "saturated_fatty_acids.sfa": numeric_value_or_null,
    "saturated_fatty_acids.f16d0": null,
    "saturated_fatty_acids.f17d0": null,
    "saturated_fatty_acids.f18d0": null,
    "saturated_fatty_acids.f20d0": null,
    "saturated_fatty_acids.f22d0": null,
    "saturated_fatty_acids.f24d0": null,
    
    "mono_unsaturated_fatty_acids.mufa": null,
    "mono_unsaturated_fatty_acids.f14d1": null,
    "mono_unsaturated_fatty_acids.f16d1": null,
    "mono_unsaturated_fatty_acids.f18d1": null,
    
    "poly_unsaturated_fatty_acids.pufa": null,
    "poly_unsaturated_fatty_acids.f18d2": null,
    "poly_unsaturated_fatty_acids.f18d3": null,
    "poly_unsaturated_fatty_acids.f20d4": null,
    "poly_unsaturated_fatty_acids.f20d5cn3": null,
    "poly_unsaturated_fatty_acids.f22d6cn3": null,
    
    "other_fatty_acid_properties.trans": numeric_value_or_null,
    "other_fatty_acid_properties.chol": numeric_value_or_null,
    
    "sugars.sugar": numeric_value_or_null,
    "sugars.gals": null,
    "sugars.mals": null,
    "sugars.lacs": null,
    "sugars.frus": null,
    "sugars.glus": null,
    "sugars.sucs": null,
    
    "carotenoids.lycpn": null,
    "carotenoids.lutnzea": null,
    
    "isoflavones.total_isoflavone": null,
    "isoflavones.daidzein": null,
    "isoflavones.genistein": null,
    "isoflavones.glycetin": null,
    
    "other_components.phytosterol": null,
    "other_components.purine": null
}}

EXTRACTION RULES:
1. OCR often reads 'g' as '9'. Fix these errors:
   - "19" → extract as 1
   - "29" → extract as 2  
   - "39" → extract as 3
   - "129" → extract as 12
   - "169" → extract as 16
   - "09" → extract as 0

2. Unit conversions (extract number only, no units):
   - Calories/Energy → convert to kcal (just the number)
   - Protein, Fat, Carbs, Fiber, Sugars, Saturated Fat, Trans Fat → convert to grams (just the number)
   - Calcium, Iron, Sodium, Potassium, Cholesterol → convert to mg (just the number)  
   - Vitamin D → convert to mcg (just the number)

3. Value extraction:
   - Extract ONLY the numeric value, strip all units (g, mg, mcg, kcal, etc.)
   - If value is "0g" or "0mg" → extract as 0
   - If nutrient not shown → use null
   - Ignore % Daily Value percentages

4. Field mapping for extractable nutrients:
   - "Calories" → nutrients.energy
   - "Protein" → nutrients.procnt
   - "Total Fat" → nutrients.fat
   - "Total Carbohydrate" → nutrients.chocdf
   - "Dietary Fiber" → nutrients.fibc
   - "Calcium" → minerals.ca
   - "Iron" → minerals.fe
   - "Sodium" → minerals.na
   - "Potassium" → minerals.k
   - "Vitamin D" → vitamins.vitd
   - "Saturated Fat" → saturated_fatty_acids.sfa
   - "Trans Fat" → other_fatty_acid_properties.trans
   - "Cholesterol" → other_fatty_acid_properties.chol
   - "Total Sugars" → sugars.sugar

5. IMPORTANT: You MUST include ALL fields in the response, even if they are null. Do not omit any fields.

Only extract nutrients explicitly shown in the label. For all other fields, use null.

Nutrition label text:
\"\"\"
{ocr_text}
\"\"\"
Return ONLY the flat JSON object. All required fields must be returned even if they're null or 0. No explanations.
"""