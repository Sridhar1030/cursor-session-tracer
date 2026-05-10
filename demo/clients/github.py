"""
GitHub API client — PRE-refactor state.
Imports and uses APIKeyAuth directly. The agent needs to change this to BearerTokenAuth.
"""

from demo.auth import APIKeyAuth

GITHUB_API_BASE = "https://api.github.com"


class GitHubClient:
    def __init__(self):
        self.auth = APIKeyAuth()
        self.base_url = GITHUB_API_BASE

    def get_repo(self, owner: str, repo: str) -> dict:
        return {
            "owner": owner,
            "repo": repo,
            "auth_headers": self.auth.headers,
            "url": f"{self.base_url}/repos/{owner}/{repo}",
        }

    def list_issues(self, owner: str, repo: str) -> list:
        return []
