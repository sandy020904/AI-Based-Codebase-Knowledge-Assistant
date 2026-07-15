from src.config import WORKSPACE_DIR
from src.repository.github import clone_repository
from src.repository.scanner import RepositoryScanner
from src.core.logger import logger


class RepositoryManager:

    @staticmethod
    def clone(repo_url: str):

        repository_name = repo_url.split("/")[-1]

        destination = WORKSPACE_DIR / repository_name

        if not destination.exists():

            logger.info(f"Cloning repository: {repo_url}")

            clone_repository(repo_url, destination)

        else:

            logger.info("Repository already exists. Using cached version.")

        metadata = RepositoryScanner.scan(destination)

        logger.info("Repository scanned successfully")

        return {
            "repository": repository_name,
            "path": str(destination),
            "metadata": metadata
        }