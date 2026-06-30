from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .value_objects import CampaignStatus, ImageContentType, Platform


@dataclass
class UploadedFile:
    id: UUID = field(default_factory=uuid4)
    original_filename: str = ""
    storage_key: str = ""
    content_type: ImageContentType | None = None
    size_bytes: int = 0
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class GeneratedContent:
    id: UUID = field(default_factory=uuid4)
    campaign_id: UUID = field(default_factory=uuid4)
    platform: Platform = Platform.LINKEDIN
    copy: str = ""
    hashtags: list[str] = field(default_factory=list)
    asset_curation: str = ""
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class Campaign:
    id: UUID = field(default_factory=uuid4)
    raw_text: str = ""
    platforms: list[Platform] = field(default_factory=list)
    file_ids: list[UUID] = field(default_factory=list)
    status: CampaignStatus = CampaignStatus.PENDING
    error: str | None = None
    generated: list[GeneratedContent] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
