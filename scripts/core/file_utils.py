"""core/file_utils.py"""

import shutil
from pathlib import Path
from typing import Iterator


def reset_dir(dir_path: Path) -> None:
    """empty and recreate the directory"""
    if dir_path.exists():
        if not dir_path.is_dir():
            raise ValueError(f"{dir_path} is not a directory")
        shutil.rmtree(dir_path)
    dir_path.mkdir(parents=True)


def collect_markdown_files(dir_path: Path) -> Iterator[Path]:
    """recursively get all markdown files under the directory"""
    if not dir_path.exists():
        raise FileNotFoundError(f"{dir_path} does not exist")
    for file_path in dir_path.rglob("*.md"):
        yield file_path


def read_file(input_path: Path) -> str:
    """reads the file and returns a string"""
    path = input_path
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(output_path: Path, content: str) -> None:
    """write the string to the file"""
    path = output_path
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
