def create_extract_nutrition_prompt(ocr_text: str) -> str:
   return f"""
You are extracting nutritional information from a Vietnamese nutrition facts table.

CRITICAL TABLE STRUCTURE UNDERSTANDING:
This appears to be a nutrition table with columns:
- Thành phần dinh dưỡng (Nutrients) 
- ĐV (Unit)
- Hàm lượng (Value) - THIS IS THE MAIN VALUE COLUMN
- TLTK (Source)

EXTRACTION RULES:

1. **FOCUS ON THE "Hàm lượng (Value)" COLUMN**: 
   - This contains the actual nutritional values
   - Ignore other numbers that might be reference codes or source indicators

2. **UNIT CONVERSIONS** (CRITICAL):
   - Energy: ALWAYS convert to kcal
     * If value shows KJ (like "111 KJ"), convert: KJ ÷ 4.184 = kcal
     * If value shows kcal (like "27 kcal"), use as-is
   - Protein, Fat, Carbs, Fiber, Ash, Water: grams (g)
   - Minerals: milligrams (mg) - keep as shown in table
     * Copper (Đồng): if in μg, convert to mg (÷1000)
     * Selenium (Selen): if in μg, convert to mg (÷1000)
     * Manganese: use exact value as shown (e.g., 16.000 → 16.0)
   - Vitamins: keep original units as specified in table

3. **SPECIFIC VALUE MAPPINGS** (extract these exact patterns):
   
   **SPECIFIC ENERGY CONVERSION EXAMPLE:**
   - If you see "Năng lượng (Energy) KCal 27" → nutrients.energy = 27
   - If you see "Năng lượng (Energy) KJ 111" → nutrients.energy = 111 ÷ 4.184 = 26.5
   - Always check the unit (KCal vs KJ) before extracting
   - Nước (Water): Look for water content in grams
   - Năng lượng (Energy): Look for energy in kcal or KJ
   - Protein: Look for protein content in grams  
   - Lipid (Fat): Look for fat content in grams
   - Glucid (Carbohydrate): Look for carbohydrate in grams
   - Celluloza (Fiber): Look for fiber in grams
   - Tro (Ash): Look for ash content in grams

   **MINERALS (EXACT VALUES FROM TABLE):**
   - Calci (Calcium): mg - use exact value from Hàm lượng column
   - Sắt (Iron): mg - use exact value 
   - Magiê (Magnesium): mg - use exact value
   - Mangan (Manganese): mg - use EXACT value as shown (e.g., if table shows "16.000", use 16.0)
   - Phospho (Phosphorous): mg - use exact value
   - Kali (Potassium): mg - use exact value  
   - Natri (Sodium): mg - use exact value
   - Kẽm (Zinc): mg - use exact value
   - Đồng (Copper): if in μg, convert to mg (÷1000); if in mg, use as-is
   - Selen (Selenium): if in μg, convert to mg (÷1000); if in mg, use as-is

   **VITAMINS:**
   - Vitamin C (Ascorbic acid): mg
   - Vitamin B1 (Thiamine): mg
   - Vitamin B2 (Riboflavin): mg
   - Vitamin PP (Niacin): mg
   - Vitamin B5 (Pantothenic acid): mg
   - Vitamin B6 (Pyridoxine): mg
   - Folat (Folate): μg
   - Vitamin B9 (Folic acid): μg
   - Vitamin H (Biotin): μg
   - Vitamin B12: μg
   - Vitamin A (Retinol): μg
   - Vitamin D: μg
   - Vitamin E: mg
   - Vitamin K: μg
   - Beta-caroten: μg
   - Alpha-caroten: μg
   - Beta-cryptoxanthin: μg

   **AMINO ACIDS (all in mg):**
   - Lysin, Methionin, Tryptophan, Phenylalanin, Threonin, Valin, Leucin, Isoleucin, Arginin, Histidin, Cystin, Tyrosin, Alanin, Acid aspartic, Acid glutamic, Glycin, Prolin, Serin

   **FATTY ACIDS:**
   - Look for saturated, monounsaturated, polyunsaturated fatty acid values
   - Specific fatty acids like C16:0, C18:0, C18:1, C18:2, etc.

4. **VALUE VALIDATION**:
   - If a value shows "-" or is blank, use null
   - If a value is "0" or "0.00", use 0
   - Convert units appropriately (μg to mg where needed)
   - Manganese values in mg should be reasonable (typically 0.1-20 mg)

5. **CONSERVATIVE EXTRACTION**:
   - Only extract values you can clearly identify
   - Do not guess or interpolate missing values
   - Use null for unclear or missing nutrients
   - Double-check that values make nutritional sense

6. **DEBUG APPROACH**:
   - Identify the table structure first
   - Find the "Hàm lượng" (Value) column
   - Extract values row by row, matching nutrient names to values
   - Apply appropriate unit conversions

Required JSON format (ALL fields must be included):
{{
    "nutrients.energy": numeric_value_or_null,
    "nutrients.water": numeric_value_or_null,
    "nutrients.procnt": numeric_value_or_null,
    "nutrients.fat": numeric_value_or_null,
    "nutrients.chocdf": numeric_value_or_null,
    "nutrients.fibc": numeric_value_or_null,
    "nutrients.ash": numeric_value_or_null,
    
    "minerals.ca": numeric_value_or_null,
    "minerals.p": numeric_value_or_null,
    "minerals.fe": numeric_value_or_null,
    "minerals.zn": numeric_value_or_null,
    "minerals.na": numeric_value_or_null,
    "minerals.k": numeric_value_or_null,
    "minerals.mg": numeric_value_or_null,
    "minerals.mn": numeric_value_or_null,
    "minerals.cu": numeric_value_or_null,
    "minerals.se": numeric_value_or_null,
    
    "vitamins.vitc": numeric_value_or_null,
    "vitamins.thia": numeric_value_or_null,
    "vitamins.ribf": numeric_value_or_null,
    "vitamins.nia": numeric_value_or_null,
    "vitamins.pantac": numeric_value_or_null,
    "vitamins.vitb6": numeric_value_or_null,
    "vitamins.fol": numeric_value_or_null,
    "vitamins.folac": numeric_value_or_null,
    "vitamins.biot": numeric_value_or_null,
    "vitamins.vitb12": numeric_value_or_null,
    "vitamins.retol": numeric_value_or_null,
    "vitamins.vita": numeric_value_or_null,
    "vitamins.vitd": numeric_value_or_null,
    "vitamins.vite": numeric_value_or_null,
    "vitamins.vitk": numeric_value_or_null,
    "vitamins.cartb": numeric_value_or_null,
    "vitamins.carta": numeric_value_or_null,
    "vitamins.crypxb": numeric_value_or_null,
    
    "amino_acids.lys": numeric_value_or_null,
    "amino_acids.met": numeric_value_or_null,
    "amino_acids.trp": numeric_value_or_null,
    "amino_acids.phe": numeric_value_or_null,
    "amino_acids.thr": numeric_value_or_null,
    "amino_acids.val": numeric_value_or_null,
    "amino_acids.leu": numeric_value_or_null,
    "amino_acids.ile": numeric_value_or_null,
    "amino_acids.arg": numeric_value_or_null,
    "amino_acids.his": numeric_value_or_null,
    "amino_acids.cys": numeric_value_or_null,
    "amino_acids.tyr": numeric_value_or_null,
    "amino_acids.ala": numeric_value_or_null,
    "amino_acids.asp": numeric_value_or_null,
    "amino_acids.glu": numeric_value_or_null,
    "amino_acids.gly": numeric_value_or_null,
    "amino_acids.pro": numeric_value_or_null,
    "amino_acids.ser": numeric_value_or_null,
    
    "saturated_fatty_acids.sfa": numeric_value_or_null,
    "saturated_fatty_acids.f16d0": numeric_value_or_null,
    "saturated_fatty_acids.f17d0": numeric_value_or_null,
    "saturated_fatty_acids.f18d0": numeric_value_or_null,
    "saturated_fatty_acids.f20d0": numeric_value_or_null,
    "saturated_fatty_acids.f22d0": numeric_value_or_null,
    "saturated_fatty_acids.f24d0": numeric_value_or_null,
    
    "mono_unsaturated_fatty_acids.mufa": numeric_value_or_null,
    "mono_unsaturated_fatty_acids.f14d1": numeric_value_or_null,
    "mono_unsaturated_fatty_acids.f16d1": numeric_value_or_null,
    "mono_unsaturated_fatty_acids.f18d1": numeric_value_or_null,
    
    "poly_unsaturated_fatty_acids.pufa": numeric_value_or_null,
    "poly_unsaturated_fatty_acids.f18d2": numeric_value_or_null,
    "poly_unsaturated_fatty_acids.f18d3": numeric_value_or_null,
    "poly_unsaturated_fatty_acids.f20d4": numeric_value_or_null,
    "poly_unsaturated_fatty_acids.f20d5cn3": numeric_value_or_null,
    "poly_unsaturated_fatty_acids.f22d6cn3": numeric_value_or_null,
    
    "other_fatty_acid_properties.trans": numeric_value_or_null,
    "other_fatty_acid_properties.chol": numeric_value_or_null,
    
    "sugars.sugar": numeric_value_or_null,
    "sugars.gals": numeric_value_or_null,
    "sugars.mals": numeric_value_or_null,
    "sugars.lacs": numeric_value_or_null,
    "sugars.frus": numeric_value_or_null,
    "sugars.glus": numeric_value_or_null,
    "sugars.sucs": numeric_value_or_null,
    
    "carotenoids.lycpn": numeric_value_or_null,
    "carotenoids.lutnzea": numeric_value_or_null,
    
    "isoflavones.total_isoflavone": numeric_value_or_null,
    "isoflavones.daidzein": numeric_value_or_null,
    "isoflavones.genistein": numeric_value_or_null,
    "isoflavones.glycetin": numeric_value_or_null,
    
    "other_components.phytosterol": numeric_value_or_null,
    "other_components.purine": numeric_value_or_null
}}

OCR Text:
\"\"\"
{ocr_text}
\"\"\"

IMPORTANT: 
- Extract values from the correct column (Hàm lượng/Value column)
- Apply proper unit conversions
- Use null for missing or unclear values
- Return ONLY the JSON object
"""