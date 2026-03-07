"""main.py"""

import tomllib
from pathlib import Path
from scripts.core import file_utils
from scripts.core import parser
from scripts.core import templater
from scripts.core import generators

BASE_DIR = Path.cwd()
CONTENT_DIR = BASE_DIR / "content"
TEMPLATE_DIR = BASE_DIR / "templates"
PUBLIC_DIR = BASE_DIR / "public"

RENDERER = templater.TemplateRenderer(TEMPLATE_DIR)

CONFIG_FILE = BASE_DIR / "config.toml"


def load_config():
    with open(CONFIG_FILE, "rb") as f:
        config = tomllib.load(f)

    return config


def main():
    """main"""

    config = load_config()

    file_utils.reset_dir(PUBLIC_DIR)

    all_articles = []
    for md_file in file_utils.collect_markdown_files(CONTENT_DIR):
        text = file_utils.read_file(md_file)
        article = parser.parse_markdown(md_file, text)
        all_articles.append(article)

    article_gen = generators.ArticleGenerator(RENDERER)
    article_gen.generate(all_articles, PUBLIC_DIR)

    index_gen = generators.IndexGenerator(RENDERER)
    index_gen.generate(all_articles, PUBLIC_DIR)

    return
