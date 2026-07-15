import ast

from pathlib import Path

from src.models.parsed_file import ParsedFile


class PythonParser:

    @staticmethod
    def parse(file_path: Path):

        source = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

        classes = []

        functions = []

        imports = []

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.Import):

                for alias in node.names:

                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    imports.append(node.module)

        return ParsedFile(

            file_path=str(file_path),

            language="Python",

            content=source,

            classes=classes,

            functions=functions,

            imports=imports

        )