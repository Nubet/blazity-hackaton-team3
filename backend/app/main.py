from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import get_settings
from app.domain.exceptions import (
    EmptyFileError,
    FileTooLargeError,
    TooManyFilesError,
    UnsupportedFileTypeError,
)
from app.interface.api.v1.router import api_router
from app.interface.dependencies import _database, _storage


@asynccontextmanager
async def lifespan(_: FastAPI):
    await _storage().ensure_bucket()
    yield
    await _database().dispose()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="FlowForge Backend",
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(TooManyFilesError)
    async def _too_many(_: Request, exc: TooManyFilesError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc), "code": "too_many_files"},
        )

    @app.exception_handler(FileTooLargeError)
    async def _too_large(_: Request, exc: FileTooLargeError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            content={"detail": str(exc), "code": "file_too_large"},
        )

    @app.exception_handler(UnsupportedFileTypeError)
    async def _unsupported(_: Request, exc: UnsupportedFileTypeError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            content={"detail": str(exc), "code": "unsupported_file_type"},
        )

    @app.exception_handler(EmptyFileError)
    async def _empty(_: Request, exc: EmptyFileError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(exc), "code": "empty_file"},
        )

    @app.get("/health", tags=["meta"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(api_router)
    return app


app = create_app()
