from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


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
