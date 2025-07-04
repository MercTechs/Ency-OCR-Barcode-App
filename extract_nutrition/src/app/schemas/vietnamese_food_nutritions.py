from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VietnameseFoodNutrition(BaseModel):
    # Basic food information
    food_group: str = Field(..., description="Food group in Vietnamese")
    code: int = Field(..., description="Unique food code identifier")
    vietnamese_name: str = Field(..., description="Vietnamese name of the food")
    english_name: str = Field(..., description="English name of the food")
    edible_portion: float = Field(..., description="Percentage of edible portion")
    
    # Basic nutrients
    nutrients_energy: Optional[float] = Field(None, alias="nutrients.energy", description="Energy content (kcal)")
    nutrients_water: Optional[float] = Field(None, alias="nutrients.water", description="Water content (g)")
    nutrients_procnt: Optional[float] = Field(None, alias="nutrients.procnt", description="Protein content (g)")
    nutrients_fat: Optional[float] = Field(None, alias="nutrients.fat", description="Total fat content (g)")
    nutrients_chocdf: Optional[float] = Field(None, alias="nutrients.chocdf", description="Carbohydrate content (g)")
    nutrients_fibc: Optional[float] = Field(None, alias="nutrients.fibc", description="Fiber content (g)")
    nutrients_ash: Optional[float] = Field(None, alias="nutrients.ash", description="Ash content (g)")
    
    # Minerals
    minerals_ca: Optional[float] = Field(None, alias="minerals.ca", description="Calcium (mg)")
    minerals_p: Optional[float] = Field(None, alias="minerals.p", description="Phosphorus (mg)")
    minerals_fe: Optional[float] = Field(None, alias="minerals.fe", description="Iron (mg)")
    minerals_zn: Optional[float] = Field(None, alias="minerals.zn", description="Zinc (mg)")
    minerals_na: Optional[float] = Field(None, alias="minerals.na", description="Sodium (mg)")
    minerals_k: Optional[float] = Field(None, alias="minerals.k", description="Potassium (mg)")
    minerals_mg: Optional[float] = Field(None, alias="minerals.mg", description="Magnesium (mg)")
    minerals_mn: Optional[float] = Field(None, alias="minerals.mn", description="Manganese (mg)")
    minerals_cu: Optional[float] = Field(None, alias="minerals.cu", description="Copper (mg)")
    minerals_se: Optional[float] = Field(None, alias="minerals.se", description="Selenium (mcg)")
    
    # Vitamins
    vitamins_vitc: Optional[float] = Field(None, alias="vitamins.vitc", description="Vitamin C (mg)")
    vitamins_thia: Optional[float] = Field(None, alias="vitamins.thia", description="Thiamine/B1 (mg)")
    vitamins_ribf: Optional[float] = Field(None, alias="vitamins.ribf", description="Riboflavin/B2 (mg)")
    vitamins_nia: Optional[float] = Field(None, alias="vitamins.nia", description="Niacin/B3 (mg)")
    vitamins_pantac: Optional[float] = Field(None, alias="vitamins.pantac", description="Pantothenic acid/B5 (mg)")
    vitamins_vitb6: Optional[float] = Field(None, alias="vitamins.vitb6", description="Vitamin B6 (mg)")
    vitamins_fol: Optional[float] = Field(None, alias="vitamins.fol", description="Folate (mcg)")
    vitamins_folac: Optional[float] = Field(None, alias="vitamins.folac", description="Folic acid (mcg)")
    vitamins_biot: Optional[float] = Field(None, alias="vitamins.biot", description="Biotin (mcg)")
    vitamins_vitb12: Optional[float] = Field(None, alias="vitamins.vitb12", description="Vitamin B12 (mcg)")
    vitamins_retol: Optional[float] = Field(None, alias="vitamins.retol", description="Retinol (mcg)")
    vitamins_vita: Optional[float] = Field(None, alias="vitamins.vita", description="Vitamin A activity (mcg RAE)")
    vitamins_vitd: Optional[float] = Field(None, alias="vitamins.vitd", description="Vitamin D (mcg)")
    vitamins_vite: Optional[float] = Field(None, alias="vitamins.vite", description="Vitamin E (mg)")
    vitamins_vitk: Optional[float] = Field(None, alias="vitamins.vitk", description="Vitamin K (mcg)")
    vitamins_cartb: Optional[float] = Field(None, alias="vitamins.cartb", description="Beta-carotene (mcg)")
    vitamins_carta: Optional[float] = Field(None, alias="vitamins.carta", description="Alpha-carotene (mcg)")
    vitamins_crypxb: Optional[float] = Field(None, alias="vitamins.crypxb", description="Cryptoxanthin beta (mcg)")
    
    # Amino acids
    amino_acids_lys: Optional[float] = Field(None, alias="amino_acids.lys", description="Lysine (mg)")
    amino_acids_met: Optional[float] = Field(None, alias="amino_acids.met", description="Methionine (mg)")
    amino_acids_trp: Optional[float] = Field(None, alias="amino_acids.trp", description="Tryptophan (mg)")
    amino_acids_phe: Optional[float] = Field(None, alias="amino_acids.phe", description="Phenylalanine (mg)")
    amino_acids_thr: Optional[float] = Field(None, alias="amino_acids.thr", description="Threonine (mg)")
    amino_acids_val: Optional[float] = Field(None, alias="amino_acids.val", description="Valine (mg)")
    amino_acids_leu: Optional[float] = Field(None, alias="amino_acids.leu", description="Leucine (mg)")
    amino_acids_ile: Optional[float] = Field(None, alias="amino_acids.ile", description="Isoleucine (mg)")
    amino_acids_arg: Optional[float] = Field(None, alias="amino_acids.arg", description="Arginine (mg)")
    amino_acids_his: Optional[float] = Field(None, alias="amino_acids.his", description="Histidine (mg)")
    amino_acids_cys: Optional[float] = Field(None, alias="amino_acids.cys", description="Cysteine (mg)")
    amino_acids_tyr: Optional[float] = Field(None, alias="amino_acids.tyr", description="Tyrosine (mg)")
    amino_acids_ala: Optional[float] = Field(None, alias="amino_acids.ala", description="Alanine (mg)")
    amino_acids_asp: Optional[float] = Field(None, alias="amino_acids.asp", description="Aspartic acid (mg)")
    amino_acids_glu: Optional[float] = Field(None, alias="amino_acids.glu", description="Glutamic acid (mg)")
    amino_acids_gly: Optional[float] = Field(None, alias="amino_acids.gly", description="Glycine (mg)")
    amino_acids_pro: Optional[float] = Field(None, alias="amino_acids.pro", description="Proline (mg)")
    amino_acids_ser: Optional[float] = Field(None, alias="amino_acids.ser", description="Serine (mg)")
    
    # Saturated fatty acids
    saturated_fatty_acids_sfa: Optional[float] = Field(None, alias="saturated_fatty_acids.sfa", description="Total saturated fatty acids (g)")
    saturated_fatty_acids_f16d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f16d0", description="Palmitic acid (g)")
    saturated_fatty_acids_f17d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f17d0", description="Margaric acid (g)")
    saturated_fatty_acids_f18d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f18d0", description="Stearic acid (g)")
    saturated_fatty_acids_f20d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f20d0", description="Arachidic acid (g)")
    saturated_fatty_acids_f22d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f22d0", description="Behenic acid (g)")
    saturated_fatty_acids_f24d0: Optional[float] = Field(None, alias="saturated_fatty_acids.f24d0", description="Lignoceric acid (g)")
    
    # Monounsaturated fatty acids
    mono_unsaturated_fatty_acids_mufa: Optional[float] = Field(None, alias="mono_unsaturated_fatty_acids.mufa", description="Total monounsaturated fatty acids (g)")
    mono_unsaturated_fatty_acids_f14d1: Optional[float] = Field(None, alias="mono_unsaturated_fatty_acids.f14d1", description="Myristoleic acid (g)")
    mono_unsaturated_fatty_acids_f16d1: Optional[float] = Field(None, alias="mono_unsaturated_fatty_acids.f16d1", description="Palmitoleic acid (g)")
    mono_unsaturated_fatty_acids_f18d1: Optional[float] = Field(None, alias="mono_unsaturated_fatty_acids.f18d1", description="Oleic acid (g)")
    
    # Polyunsaturated fatty acids
    poly_unsaturated_fatty_acids_pufa: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.pufa", description="Total polyunsaturated fatty acids (g)")
    poly_unsaturated_fatty_acids_f18d2: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.f18d2", description="Linoleic acid (g)")
    poly_unsaturated_fatty_acids_f18d3: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.f18d3", description="Linolenic acid (g)")
    poly_unsaturated_fatty_acids_f20d4: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.f20d4", description="Arachidonic acid (g)")
    poly_unsaturated_fatty_acids_f20d5cn3: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.f20d5cn3", description="EPA (g)")
    poly_unsaturated_fatty_acids_f22d6cn3: Optional[float] = Field(None, alias="poly_unsaturated_fatty_acids.f22d6cn3", description="DHA (g)")
    
    # Other fatty acid properties
    other_fatty_acid_properties_trans: Optional[float] = Field(None, alias="other_fatty_acid_properties.trans", description="Trans fatty acids (g)")
    other_fatty_acid_properties_chol: Optional[float] = Field(None, alias="other_fatty_acid_properties.chol", description="Cholesterol (mg)")
    
    # Sugars
    sugars_sugar: Optional[float] = Field(None, alias="sugars.sugar", description="Total sugars (g)")
    sugars_gals: Optional[float] = Field(None, alias="sugars.gals", description="Galactose (g)")
    sugars_mals: Optional[float] = Field(None, alias="sugars.mals", description="Maltose (g)")
    sugars_lacs: Optional[float] = Field(None, alias="sugars.lacs", description="Lactose (g)")
    sugars_frus: Optional[float] = Field(None, alias="sugars.frus", description="Fructose (g)")
    sugars_glus: Optional[float] = Field(None, alias="sugars.glus", description="Glucose (g)")
    sugars_sucs: Optional[float] = Field(None, alias="sugars.sucs", description="Sucrose (g)")
    
    # Carotenoids
    carotenoids_lycpn: Optional[float] = Field(None, alias="carotenoids.lycpn", description="Lycopene (mcg)")
    carotenoids_lutnzea: Optional[float] = Field(None, alias="carotenoids.lutnzea", description="Lutein + zeaxanthin (mcg)")
    
    # Isoflavones
    isoflavones_total_isoflavone: Optional[float] = Field(None, alias="isoflavones.total_isoflavone", description="Total isoflavones (mg)")
    isoflavones_daidzein: Optional[float] = Field(None, alias="isoflavones.daidzein", description="Daidzein (mg)")
    isoflavones_genistein: Optional[float] = Field(None, alias="isoflavones.genistein", description="Genistein (mg)")
    isoflavones_glycetin: Optional[float] = Field(None, alias="isoflavones.glycetin", description="Glycitein (mg)")
    
    # Other components
    other_components_phytosterol: Optional[float] = Field(None, alias="other_components.phytosterol", description="Phytosterols (mg)")
    other_components_purine: Optional[float] = Field(None, alias="other_components.purine", description="Purines (mg)")
    
    # Database metadata
    created_at: datetime
    updated_at: datetime
    food_group_id: int

    class Config:
        allow_population_by_field_name = True  # Allows using either field name or alias
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        schema_extra = {
            "example": {
                "food_group": "Quả chín",
                "code": 5039,
                "vietnamese_name": "Nhót",
                "english_name": "Silver berry",
                "edible_portion": 76.00,
                "nutrients.energy": 22.00,
                "nutrients.water": 94.00,
                "nutrients.procnt": 1.20,
                "nutrients.fat": None,
                "nutrients.chocdf": 4.40,
                "nutrients.fibc": 2.30,
                "nutrients.ash": 0.40,
                "minerals.ca": 27.00,
                "minerals.p": 30.00,
                "minerals.fe": 0.20,
                "minerals.zn": None,
                "created_at": "2025-06-18T03:51:03.799534",
                "updated_at": "2025-06-30T16:36:22.651658",
                "food_group_id": 15
            }
        }

from datetime import datetime

# Complete sample data (all required fields included)
food_data = {
    "food_group": "Quả chín",
    "code": 5039,
    "vietnamese_name": "Nhót",  # This was missing in your test!
    "english_name": "Silver berry",  # This was missing in your test!
    "edible_portion": 76.00,  # This was missing in your test!
    "nutrients.energy": 22.00,
    "nutrients.water": 94.00,
    "nutrients.procnt": 1.20,
    "nutrients.fat": None,
    "nutrients.chocdf": 4.40,
    "nutrients.fibc": 2.30,
    "nutrients.ash": 0.40,
    "minerals.ca": 27.00,
    "minerals.p": 30.00,
    "minerals.fe": 0.20,
    "minerals.zn": None,
    # ... all the other null fields from your sample
    "created_at": "2025-06-18 03:51:03.799534",  # This was missing!
    "updated_at": "2025-06-30 16:36:22.651658",  # This was missing!
    "food_group_id": 15  # This was missing!
}

# Now this will work:
food_item = VietnameseFoodNutrition(**food_data)
print(food_item.model_dump())