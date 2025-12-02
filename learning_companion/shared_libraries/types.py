"""Common data schema and types."""

from pydantic import BaseModel, Field
# from typing import List

class TextBreakdown(BaseModel):
    """Represents a text unit, usually a word, in the sentence analysis."""
    text: str = Field(..., description="The actual text.")
    pronunciation: str = Field(..., description="The pronunciation of the word, it can be pinyin, IPA, or another more relevant representation.")
    translation: str = Field(..., description="The translation in the target language.")
    role: str = Field(..., description="The grammatical role of the text.")

class SentenceAnalysis(BaseModel):
    """Represents the complete analysis of a sentence."""
    original_sentence: str = Field(..., description="The original, full sentence.")
    translated_sentence: str = Field(..., description="The translated sentence, not literal but in a meaningful way.")
    source_language: str = Field(default="zh-CN", description="The language code of the sentence.")
    target_language: str = Field(default="en-US", description="The language code of the analysis.")
    words: list[TextBreakdown] = Field(..., description="A list of text elements that form the sentence.")
