from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.ports import CampaignRepository, FileRepository
from app.domain.entities import Campaign, GeneratedContent, UploadedFile
from app.domain.value_objects import CampaignStatus, ImageContentType, Platform
from app.infrastructure.db.models import (
    CampaignModel,
    GeneratedContentModel,
    UploadedFileModel,
)


class SqlAlchemyFileRepository(FileRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, file: UploadedFile) -> None:
        assert file.content_type is not None
        model = UploadedFileModel(
            id=file.id,
            original_filename=file.original_filename,
            storage_key=file.storage_key,
            content_type=file.content_type.value,
            extension=file.content_type.extension,
            size_bytes=file.size_bytes,
            created_at=file.created_at,
        )
        self._session.add(model)
        await self._session.commit()

    async def get(self, file_id: UUID) -> UploadedFile | None:
        result = await self._session.execute(
            select(UploadedFileModel).where(UploadedFileModel.id == file_id)
        )
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def list_recent(self, limit: int = 50) -> list[UploadedFile]:
        result = await self._session.execute(
            select(UploadedFileModel)
            .order_by(UploadedFileModel.created_at.desc())
            .limit(limit)
        )
        return [self._to_entity(m) for m in result.scalars().all()]

    async def delete(self, file_id: UUID) -> bool:
        result = await self._session.execute(
            delete(UploadedFileModel).where(UploadedFileModel.id == file_id)
        )
        await self._session.commit()
        return result.rowcount > 0

    @staticmethod
    def _to_entity(model: UploadedFileModel) -> UploadedFile:
        return UploadedFile(
            id=model.id,
            original_filename=model.original_filename,
            storage_key=model.storage_key,
            content_type=ImageContentType(value=model.content_type, extension=model.extension),
            size_bytes=model.size_bytes,
            created_at=model.created_at,
        )


class SqlAlchemyCampaignRepository(CampaignRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, campaign: Campaign) -> None:
        model = CampaignModel(
            id=campaign.id,
            raw_text=campaign.raw_text,
            platforms=[p.value for p in campaign.platforms],
            file_ids=list(campaign.file_ids),
            status=campaign.status.value,
            error=campaign.error,
            created_at=campaign.created_at,
        )
        self._session.add(model)
        await self._session.commit()

    async def update(self, campaign: Campaign) -> None:
        model = await self._session.get(CampaignModel, campaign.id)
        if model is None:
            return
        model.status = campaign.status.value
        model.error = campaign.error
        model.generated.clear()
        for gen in campaign.generated:
            model.generated.append(
                GeneratedContentModel(
                    id=gen.id,
                    campaign_id=campaign.id,
                    platform=gen.platform.value,
                    copy=gen.copy,
                    hashtags=list(gen.hashtags),
                    asset_curation=gen.asset_curation,
                    created_at=gen.created_at,
                )
            )
        await self._session.commit()

    async def get(self, campaign_id: UUID) -> Campaign | None:
        model = await self._session.get(CampaignModel, campaign_id)
        return self._to_entity(model) if model else None

    async def list_recent(self, limit: int = 50) -> list[Campaign]:
        result = await self._session.execute(
            select(CampaignModel).order_by(CampaignModel.created_at.desc()).limit(limit)
        )
        return [self._to_entity(m) for m in result.scalars().all()]

    @staticmethod
    def _to_entity(model: CampaignModel) -> Campaign:
        return Campaign(
            id=model.id,
            raw_text=model.raw_text,
            platforms=[Platform(p) for p in model.platforms],
            file_ids=list(model.file_ids),
            status=CampaignStatus(model.status),
            error=model.error,
            generated=[
                GeneratedContent(
                    id=g.id,
                    campaign_id=g.campaign_id,
                    platform=Platform(g.platform),
                    copy=g.copy,
                    hashtags=list(g.hashtags),
                    asset_curation=g.asset_curation,
                    created_at=g.created_at,
                )
                for g in model.generated
            ],
            created_at=model.created_at,
        )
