from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py",
    ".java",
    ".js",
    ".ts",
    ".cpp",
    ".c",
    ".go",
    ".html",
    ".css",
    ".json",
    ".xml",
    ".yml",
    ".yaml",
    ".md"
}


class FileFilter:

    @staticmethod
    def is_supported(file: Path):

        return file.suffix.lower() in SUPPORTED_EXTENSIONS