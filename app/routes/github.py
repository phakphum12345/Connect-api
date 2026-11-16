from fastapi import APIRouter

from app.services.github_service import (
    GithubService
)

router = APIRouter()


@router.get(
"/github/repo/{owner}/{repo}"
)
async def repo(
    owner:str,
    repo:str
):
    return (
        GithubService.get_repo(
            owner,
            repo
        )
    )


@router.get(
"/github/files/{owner}/{repo}"
)
async def files(
    owner:str,
    repo:str
):
    return (
        GithubService.get_contents(
            owner,
            repo
        )
    )
