from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Metadata
from sqlalchemy import select


class MetadataRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_metadata(self, metadata_id: str):
        stmt = select(Metadata).filter_by(id=metadata_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def create_metadata(self, metadata_data: Metadata):
        self.db.add(metadata_data)
        await self.db.commit()
        await self.db.refresh(metadata_data)
        return metadata_data

    async def update_metadata(self, metadata_id: str, updated_data: dict):
        metadata = await self.get_metadata(metadata_id)
        if metadata:
            for key, value in updated_data.items():
                setattr(metadata, key, value)
            await self.db.commit()
            await self.db.refresh(metadata)
            return metadata
        return None

    async def delete_metadata(self, metadata_id: str):
        metadata = await self.get_metadata(metadata_id)
        if metadata:
            await self.db.delete(metadata)
            await self.db.commit()
        return metadata