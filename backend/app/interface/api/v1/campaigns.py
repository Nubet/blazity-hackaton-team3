from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.application.dto import CampaignView
from app.application.use_cases.generate_campaign import (
    GenerateCampaignInput,
    GenerateCampaignUseCase,
    GetCampaignUseCase,
    ListCampaignsUseCase,
)
from app.domain.value_objects import Platform
from app.interface.dependencies import (
    get_generate_campaign_use_case,
    get_get_campaign_use_case,
    get_list_campaigns_use_case,
)
from app.interface.schemas import (
    CampaignListResponse,
    CampaignResponse,
    GeneratedContentResponse,
    GenerateCampaignRequest,
)

router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.post(
    "",
    response_model=CampaignResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Generate platform-tailored posts from a brief",
)
async def create_campaign(
    payload: GenerateCampaignRequest,
    use_case: GenerateCampaignUseCase = Depends(get_generate_campaign_use_case),
) -> CampaignResponse:
    try:
        platforms = [Platform(p.lower()) for p in payload.platforms]
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported platform: {exc}",
        ) from exc

    view = await use_case.execute(
        GenerateCampaignInput(
            raw_text=payload.raw_text,
            platforms=platforms,
            file_ids=payload.file_ids,
        )
    )
    return _to_response(view)


@router.get("/{campaign_id}", response_model=CampaignResponse)
async def get_campaign(
    campaign_id: UUID,
    use_case: GetCampaignUseCase = Depends(get_get_campaign_use_case),
) -> CampaignResponse:
    view = await use_case.execute(campaign_id)
    if view is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found")
    return _to_response(view)


@router.get("", response_model=CampaignListResponse)
async def list_campaigns(
    use_case: ListCampaignsUseCase = Depends(get_list_campaigns_use_case),
) -> CampaignListResponse:
    views = await use_case.execute()
    return CampaignListResponse(campaigns=[_to_response(v) for v in views])


def _to_response(view: CampaignView) -> CampaignResponse:
    return CampaignResponse(
        id=view.id,
        raw_text=view.raw_text,
        platforms=view.platforms,
        file_ids=view.file_ids,
        status=view.status,
        error=view.error,
        generated=[
            GeneratedContentResponse(
                id=g.id,
                platform=g.platform,
                copy=g.copy,
                hashtags=g.hashtags,
                asset_curation=g.asset_curation,
                created_at=g.created_at,
            )
            for g in view.generated
        ],
        created_at=view.created_at,
    )
