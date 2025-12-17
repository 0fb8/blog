"""core/models.py"""

from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Article:
    """
    represents a processed article with its source path, html content, and associated metadata
    """

    source_path: Path
    html_content: str
    metadata: Dict[str, Any]

    def get_output_path(self, public_dir: Path) -> Path:
        """build the output file path for the article"""
        stem = self.source_path.stem
        return public_dir / "posts" / stem / "index.html"

    def get_context(self) -> Dict[str, Any]:
        """construct a context dict for rendering the article in templates"""
        return {
            "content": self.html_content,
            "title": self.metadata.get("title", ["No Title"])[0],
            "date": self.metadata.get("date", [""])[0],
            "url": f"/posts/{self.source_path.stem}/",
        }
