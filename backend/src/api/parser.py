from fastapi import APIRouter

from pathlib import Path

from src.parser.repository_parser import RepositoryParser

router = APIRouter(
    prefix="/parser",
    tags=["Parser"]
)


@router.get("/test")
def test_parser():

    repository = Path("workspace/fastapi")

    parsed = RepositoryParser.parse(repository)

    return parsed