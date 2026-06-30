from dataclasses import dataclass
from datetime import datetime
from typing import BinaryIO
from uuid import UUID


@dataclass
class IncomingFile:
    filename: str
    content_type: str
    size: int
    stream: BinaryIO


@dataclass
class UploadedFileView:
    id: UUID
    original_filename: str
    content_type: str
    size_bytes: int
    url: str
    created_at: datetime


@dataclass
class GeneratedContentView:
    id: UUID
    platform: str
    copy: str
    hashtags: list[str]
    asset_curation: str
    created_at: datetime


@dataclass
class CampaignView:
    id: UUID
    raw_text: str
    platforms: list[str]
    file_ids: list[UUID]
    status: str
    error: str | None
    generated: list[GeneratedContentView]
    created_at: datetime
