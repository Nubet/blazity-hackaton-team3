import asyncio
from dataclasses import dataclass
from uuid import UUID

from app.application.dto import CampaignView, GeneratedContentView
from app.application.ports import (
    CampaignRepository,
    ContentGenerator,
    FileRepository,
    ObjectStorage,
)
from app.domain.entities import Campaign, GeneratedContent
from app.domain.exceptions import (
    ContentGenerationError,
    InvalidCampaignInputError,
)
from app.domain.value_objects import CampaignStatus, Platform


@dataclass
class GenerateCampaignInput:
    raw_text: str
    platforms: list[Platform]
    file_ids: list[UUID]


class GenerateCampaignUseCase:
    def __init__(
        self,
        generator: ContentGenerator,
        campaigns: CampaignRepository,
        files: FileRepository,
        storage: ObjectStorage,
    ) -> None:
        self._generator = generator
        self._campaigns = campaigns
        self._files = files
        self._storage = storage

    async def execute(self, payload: GenerateCampaignInput) -> CampaignView:
        if not payload.platforms:
            raise InvalidCampaignInputError("At least one platform is required")
        if not payload.raw_text.strip() and not payload.file_ids:
            raise InvalidCampaignInputError("Provide raw_text, file_ids, or both")

        image_urls: list[str] = []
        for fid in payload.file_ids:
            entity = await self._files.get(fid)
            if entity is None:
                raise InvalidCampaignInputError(f"File '{fid}' not found")
            image_urls.append(await self._storage.presigned_get_url(entity.storage_key))

        campaign = Campaign(
            raw_text=payload.raw_text,
            platforms=list(payload.platforms),
            file_ids=list(payload.file_ids),
            status=CampaignStatus.GENERATING,
        )
        await self._campaigns.add(campaign)

        results = await asyncio.gather(
            *(
                self._generator.generate(p, payload.raw_text, image_urls)
                for p in payload.platforms
            ),
            return_exceptions=True,
        )

        generated: list[GeneratedContent] = []
        errors: list[str] = []
        for platform, result in zip(payload.platforms, results):
            if isinstance(result, Exception):
                reason = (
                    result.reason
                    if isinstance(result, ContentGenerationError)
                    else str(result)
                )
                errors.append(f"{platform.value}: {reason}")
                continue
            result.campaign_id = campaign.id
            generated.append(result)

        campaign.generated = generated
        if errors and not generated:
            campaign.status = CampaignStatus.FAILED
            campaign.error = " | ".join(errors)
        elif errors:
            campaign.status = CampaignStatus.COMPLETED
            campaign.error = " | ".join(errors)
        else:
            campaign.status = CampaignStatus.COMPLETED
            campaign.error = None

        await self._campaigns.update(campaign)
        return _to_view(campaign)


class GetCampaignUseCase:
    def __init__(self, campaigns: CampaignRepository) -> None:
        self._campaigns = campaigns

    async def execute(self, campaign_id: UUID) -> CampaignView | None:
        campaign = await self._campaigns.get(campaign_id)
        return _to_view(campaign) if campaign else None


class ListCampaignsUseCase:
    def __init__(self, campaigns: CampaignRepository) -> None:
        self._campaigns = campaigns

    async def execute(self, limit: int = 50) -> list[CampaignView]:
        campaigns = await self._campaigns.list_recent(limit)
        return [_to_view(c) for c in campaigns]


def _to_view(campaign: Campaign) -> CampaignView:
    return CampaignView(
        id=campaign.id,
        raw_text=campaign.raw_text,
        platforms=[p.value for p in campaign.platforms],
        file_ids=list(campaign.file_ids),
        status=campaign.status.value,
        error=campaign.error,
        generated=[
            GeneratedContentView(
                id=g.id,
                platform=g.platform.value,
                copy=g.copy,
                hashtags=list(g.hashtags),
                asset_curation=g.asset_curation,
                created_at=g.created_at,
            )
            for g in campaign.generated
        ],
        created_at=campaign.created_at,
    )
