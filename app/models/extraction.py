"""Pydantic models for structured information extraction."""

from pydantic import BaseModel, Field


class ExtractedInformation(BaseModel):
    """Structured extraction result model for v0.1 AI Information Extractor."""

    topic: str = Field(
        ...,
        description="The primary topic or subject of the analyzed text.",
    )
    summary: str = Field(
        ...,
        description="A concise summary of the key information in the text.",
    )
    key_points: list[str] = Field(
        default_factory=list,
        description="List of significant points, findings, or takeaways.",
    )
    entities: list[str] = Field(
        default_factory=list,
        description="Important named entities, technologies, people, or organizations mentioned.",
    )
    category: str = Field(
        default="General",
        description="Classification category for the content (e.g. Technical, Research, News).",
    )
