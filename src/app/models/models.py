from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class Metadata(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    path: str
    filename: str
    is_valid: bool
    file_size: float = Field()
    created_at: datetime = Field(default_factory=datetime.utcnow)

class OCR(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    metadata_id: UUID = Field(foreign_key="metadata.id")
    text_extracted: str
    created_at: datetime = Field(default_factory=datetime.utcnow)