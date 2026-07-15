from fastapi import APIRouter, HTTPException

from src.models.repository_models import GithubRepositoryRequest
from src.repository.repository_manager import RepositoryManager

router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)


@router.post("/clone")
def clone_repository(request: GithubRepositoryRequest):

    try:

        return RepositoryManager.clone(
            str(request.github_url)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )