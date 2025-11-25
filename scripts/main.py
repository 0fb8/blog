"""main.py"""

from pathlib import Path
import shutil

BASE_DIR = Path.cwd()
PUBLIC_DIR = BASE_DIR / "public"


def main():
    """main"""

    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir()

    html_content = """
    <h1>hello</h1>
    """

    output_path = PUBLIC_DIR / "index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return
