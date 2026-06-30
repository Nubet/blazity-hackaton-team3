from collections.abc import AsyncIterator
from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.ports import FileRepository, ObjectStorage
from app.application.use_cases.upload_files import (
    DeleteFileUseCase,
    GetFileUseCase,
    UploadFilesUseCase,
    UploadLimits,
)
from app.core.config import Settings, get_settings
from app.infrastructure.db.repositories import SqlAlchemyFileRepository
from app.infrastructure.db.session import Database
from app.infrastructure.storage.minio_storage import MinioObjectStorage


@lru_cache
def _database() -> Database:
    return Database(get_settings().database_url)


@lru_cache
def _storage() -> MinioObjectStorage:
    s = get_settings()
    return MinioObjectStorage(
        endpoint=s.minio_endpoint,
        access_key=s.minio_access_key,
        secret_key=s.minio_secret_key,
        bucket=s.minio_bucket,
        secure=s.minio_secure,
        public_endpoint=s.minio_public_endpoint,
    )


def get_database() -> Database:
    return _database()


def get_object_storage() -> ObjectStorage:
    return _storage()


async def get_session() -> AsyncIterator[AsyncSession]:
    async for session in _database().session():
        yield session


def get_file_repository(session: AsyncSession = Depends(get_session)) -> FileRepository:
    return SqlAlchemyFileRepository(session)


def get_upload_limits(settings: Settings = Depends(get_settings)) -> UploadLimits:
    return UploadLimits(
        max_files=settings.upload_max_files,
        max_file_bytes=settings.upload_max_file_bytes,
    )


def get_upload_use_case(
    storage: ObjectStorage = Depends(get_object_storage),
    repo: FileRepository = Depends(get_file_repository),
    limits: UploadLimits = Depends(get_upload_limits),
) -> UploadFilesUseCase:
    return UploadFilesUseCase(storage=storage, repository=repo, limits=limits)


def get_get_use_case(
    storage: ObjectStorage = Depends(get_object_storage),
    repo: FileRepository = Depends(get_file_repository),
) -> GetFileUseCase:
    return GetFileUseCase(storage=storage, repository=repo)


def get_delete_use_case(
    storage: ObjectStorage = Depends(get_object_storage),
    repo: FileRepository = Depends(get_file_repository),
) -> DeleteFileUseCase:
    return DeleteFileUseCase(storage=storage, repository=repo)
