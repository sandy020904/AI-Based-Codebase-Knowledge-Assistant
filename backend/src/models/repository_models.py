from pydantic import BaseModel, HttpUrl

class GithubRepositoryRequest(BaseModel):
    github_url: HttpUrl