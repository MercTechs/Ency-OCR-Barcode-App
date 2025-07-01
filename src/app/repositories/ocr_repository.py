from sqlalchemy.ext.asyncio import AsyncSession
from ..models.models import OCR

class OCRRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_ocr(self, ocr_id: str):
        result = await self.db.execute(
            self.db.query(OCR).filter_by(id=ocr_id)
        )
        return result.scalar_one_or_none()

    async def create_ocr(self, ocr_data: OCR):
        self.db.add(ocr_data)
        await self.db.commit()
        await self.db.refresh(ocr_data)
        return ocr_data

    async def update_ocr(self, ocr_id: str, updated_data: dict):
        ocr = await self.get_ocr(ocr_id)
        if ocr:
            for key, value in updated_data.items():
                setattr(ocr, key, value)
            await self.db.commit()
            await self.db.refresh(ocr)
        return ocr

    async def delete_ocr(self, ocr_id: str):
        ocr = await self.get_ocr(ocr_id)
        if ocr:
            await self.db.delete(ocr)
            await self.db.commit()
        return ocr