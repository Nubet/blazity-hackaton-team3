from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UploadedFileResponse(BaseModel):
    id: UUID
    filename: str = Field(..., description="Original filename provided by client")
    content_type: str
    size_bytes: int
    url: str = Field(..., description="Presigned GET URL valid for 1 hour")
    created_at: datetime


class UploadResponse(BaseModel):
    files: list[UploadedFileResponse]


class ErrorResponse(BaseModel):
    detail: str
    code: str


class GenerateCampaignRequest(BaseModel):
    raw_text: str = Field(default="", description="Free-form brief from the user")
    platforms: list[str] = Field(..., min_length=1, description="linkedin | instagram | twitter")
    file_ids: list[UUID] = Field(default_factory=list)


class GeneratedContentResponse(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    id: UUID
    platform: str
    copy: str
    hashtags: list[str]
    asset_curation: str
    created_at: datetime


class CampaignResponse(BaseModel):
    id: UUID
    raw_text: str
    platforms: list[str]
    file_ids: list[UUID]
    status: str
    error: str | None
    generated: list[GeneratedContentResponse]
    created_at: datetime


class CampaignListResponse(BaseModel):
    campaigns: list[CampaignResponse]
