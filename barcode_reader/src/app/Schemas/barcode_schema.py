from pydantic import BaseModel

class BarcodeSchema(BaseModel):
    barcode_type: str
    value: str