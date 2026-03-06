"""core/generators.py"""

from pathlib import Path
from . import file_utils


class ArticleGenerator:
    def __init__(self, renderer):
        self.renderer = renderer

    def generate(self, articles: list, output_dir: Path):
        for article in articles:
            context = article.get_context()
            full_html = self.renderer.render("article.html", context)
            output_path = article.get_output_path(output_dir)

            file_utils.write_file(output_path, full_html)
            print(f"    Generated: {output_path}")


class IndexGenerator:
    def __init__(self, renderer):
        self.renderer = renderer

    def generate(self, articles: list, output_dir: Path):
        context = {"articles": articles}
        full_html = self.renderer.render("index.html", context)
        output_path = output_dir / "index.html"

        file_utils.write_file(output_path, full_html)
        print(f"    Generated: {output_path} (Index Page)")
