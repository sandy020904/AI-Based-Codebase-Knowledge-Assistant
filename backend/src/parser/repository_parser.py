from pathlib import Path

from src.parser.python_parser import PythonParser


class RepositoryParser:

    @staticmethod
    def parse(repository_path: Path):

        parsed_files = []

        for file in repository_path.rglob("*.py"):

            parsed = PythonParser.parse(file)

            parsed_files.append(parsed)

        return parsed_files