"""core/parser.py"""

from pathlib import Path
import markdown
from .models import Article


def parse_markdown(file_path: Path, md_text: str) -> Article:
    """convert markdown text into an article with html and metadata"""

    md = markdown.Markdown(
        extensions=[
            "meta",
            "fenced_code",
            "tables",
        ]
    )
    html = md.convert(md_text)
    meta = md.Meta if hasattr(md, "Meta") else {}

    return Article(
        source_path=file_path,
        html_content=html,
        metadata=meta,
    )
