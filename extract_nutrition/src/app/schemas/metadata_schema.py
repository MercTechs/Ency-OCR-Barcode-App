from pydantic import BaseModel
from uuid import UUID
class MetadataSchema(BaseModel):
    filename: str
    path: str
    is_valid: bool
    file_size: float

class MetadataValidationSchema(BaseModel):
    metadata_id: str
