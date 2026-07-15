from pydantic import BaseModel


class ParsedFile(BaseModel):

    file_path: str

    language: str

    content: str

    classes: list[str]

    functions: list[str]

    imports: list[str]