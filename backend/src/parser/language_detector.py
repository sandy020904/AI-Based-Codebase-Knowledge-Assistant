from pathlib import Path

EXTENSION_TO_LANGUAGE = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go",
    ".html": "HTML",
    ".css": "CSS",
    ".json": "JSON",
    ".md": "Markdown",
    ".xml": "XML",
    ".yml": "YAML",
    ".yaml": "YAML",
}


class LanguageDetector:

    @staticmethod
    def detect(file: Path):

        return EXTENSION_TO_LANGUAGE.get(
            file.suffix.lower(),
            "Unknown"
        )