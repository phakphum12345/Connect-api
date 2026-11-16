import os
import requests

from dotenv import load_dotenv

load_dotenv()


class GithubService:

    TOKEN = os.getenv(
        "GITHUB_TOKEN"
    )

    HEADERS = {
        "Authorization":
        f"Bearer {TOKEN}",
        "Accept":
        "application/vnd.github+json"
    }

    @staticmethod
    def get_repo(
        owner,
        repo
    ):
        response = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}",
            headers=GithubService.HEADERS
        )

        return response.json()

    @staticmethod
    def get_contents(
        owner,
        repo,
        path=""
    ):
        response = requests.get(
            f"https://api.github.com/repos/"
            f"{owner}/{repo}/contents/{path}",
            headers=GithubService.HEADERS
        )

        return response.json()
