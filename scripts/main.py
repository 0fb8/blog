"""main.py"""

from pathlib import Path
from scripts.core import file_utils
from scripts.core import parser

BASE_DIR = Path.cwd()
CONTENT_DIR = BASE_DIR / "content"
PUBLIC_DIR = BASE_DIR / "public"


def main():
    """main"""

    file_utils.reset_dir(PUBLIC_DIR)

    all_articles = []
    for md_file in file_utils.collect_markdown_files(CONTENT_DIR):
        text = file_utils.read_file(md_file)
        article = parser.parse_markdown(md_file, text)
        all_articles.append(article)

    for article in all_articles:
        context = article.get_context()
        full_html = f"<html><body>{context["content"]}</body></html>"
        output_path = article.get_output_path(PUBLIC_DIR)

        file_utils.write_file(output_path, full_html)
        print(f"    Generated: {output_path}")

    return
