from dataclasses import dataclass

from .exceptions import UnsupportedFileTypeError

ALLOWED_IMAGE_TYPES: dict[str, str] = {
    "image/jpeg": "jpg",
    "image/png": "png",
    "image/webp": "webp",
    "image/gif": "gif",
    "image/svg+xml": "svg",
    "image/heic": "heic",
    "image/heif": "heif",
}


@dataclass(frozen=True)
class ImageContentType:
    value: str
    extension: str

    @classmethod
    def from_mime(cls, mime: str, filename: str) -> "ImageContentType":
        normalized = mime.lower().split(";")[0].strip()
        ext = ALLOWED_IMAGE_TYPES.get(normalized)
        if ext is None:
            raise UnsupportedFileTypeError(filename=filename, content_type=mime)
        return cls(value=normalized, extension=ext)
