"""Extraction prompt templates for structured output."""

EXTRACTION_SYSTEM_PROMPT = """You are an expert AI Research Assistant specializing in information extraction.
Your task is to analyze the provided text carefully and extract structured information according to the requested schema.

Guidelines:
1. Identify the core topic accurately.
2. Provide a clear, factual, and concise summary.
3. Extract bulleted key points highlighting significant insights or findings.
4. Extract key entities (people, organizations, technologies, concepts).
5. Assign a relevant content category.
6. Do not fabricate facts; stay faithful to the provided source text.
"""

EXTRACTION_USER_PROMPT_TEMPLATE = """Please analyze the following text and extract structured information:

--- SOURCE TEXT ---
{text}
-------------------
"""
