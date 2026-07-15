from pathlib import Path

from src.parser.language_detector import LanguageDetector
from src.parser.file_filter import FileFilter

IGNORE_FOLDERS = {
    ".git",
    "__pycache__",
    "node_modules",
    "venv",
    ".idea",
    ".vscode",
    "dist",
    "build"
}


class RepositoryScanner:

    @staticmethod
    def scan(repository_path: Path):

        total_files = 0

        languages = {}

        for file in repository_path.rglob("*"):

            if file.is_dir():

                if file.name in IGNORE_FOLDERS:
                    continue

                continue

            if not FileFilter.is_supported(file):
                continue

            language = LanguageDetector.detect(file)

            languages[language] = languages.get(language, 0) + 1

            total_files += 1

        return {
            "total_files": total_files,
            "languages": languages
        }