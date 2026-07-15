from pathlib import Path
from git import Repo
from git.exc import GitCommandError


def clone_repository(repo_url: str, destination: Path):

    try:

        Repo.clone_from(repo_url, destination)

        return destination

    except GitCommandError as e:

        raise Exception(
            f"Failed to clone repository : {e}"
        )