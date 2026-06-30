import json
from uuid import uuid4

from anthropic import AsyncAnthropic

from app.application.ports import ContentGenerator
from app.application.prompts.platform_prompts import SYSTEM_PROMPT, build_user_prompt
from app.domain.entities import GeneratedContent
from app.domain.exceptions import ContentGenerationError
from app.domain.value_objects import Platform


class AnthropicContentGenerator(ContentGenerator):
    def __init__(
        self,
        api_key: str,
        model: str,
        max_tokens: int,
        temperature: float,
    ) -> None:
        if not api_key:
            raise ContentGenerationError(platform="*", reason="ANTHROPIC_API_KEY is not configured")
        self._client = AsyncAnthropic(api_key=api_key)
        self._model = model
        self._max_tokens = max_tokens
        self._temperature = temperature

    async def generate(
        self,
        platform: Platform,
        raw_text: str,
        image_urls: list[str],
    ) -> GeneratedContent:
        try:
            response = await self._client.messages.create(
                model=self._model,
                max_tokens=self._max_tokens,
                temperature=self._temperature,
                system=SYSTEM_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": build_user_prompt(raw_text, image_urls, platform),
                    }
                ],
            )
        except Exception as exc:
            raise ContentGenerationError(platform=platform.value, reason=str(exc)) from exc

        text = self._extract_text(response)
        payload = self._parse_json(text, platform)

        return GeneratedContent(
            id=uuid4(),
            platform=platform,
            copy=str(payload.get("copy", "")).strip(),
            hashtags=[
                str(tag).lstrip("#").strip().lower()
                for tag in payload.get("hashtags", [])
                if str(tag).strip()
            ],
            asset_curation=str(payload.get("asset_curation", "")).strip(),
        )

    @staticmethod
    def _extract_text(response) -> str:
        parts: list[str] = []
        for block in response.content:
            if getattr(block, "type", None) == "text":
                parts.append(block.text)
        return "".join(parts).strip()

    @staticmethod
    def _parse_json(text: str, platform: Platform) -> dict:
        cleaned = text.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`")
            if cleaned.lower().startswith("json"):
                cleaned = cleaned[4:].strip()
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start == -1 or end == -1:
            raise ContentGenerationError(
                platform=platform.value, reason=f"Model returned non-JSON output: {text[:200]}"
            )
        try:
            return json.loads(cleaned[start : end + 1])
        except json.JSONDecodeError as exc:
            raise ContentGenerationError(
                platform=platform.value, reason=f"Invalid JSON from model: {exc}"
            ) from exc
