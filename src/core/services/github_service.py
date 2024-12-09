import logging

import requests

from core.utils.check_arguments import check_argument_is_not_none_or_empty

logger = logging.getLogger(__name__)


class GithubService:
    GIT_API_BASE_URL = "https://api.github.com"

    def __init__(self, org, api_token):
        check_argument_is_not_none_or_empty(org, "org")
        check_argument_is_not_none_or_empty(api_token, "api_token")

        self.org = org
        self.api_token = api_token

    def _get(self, url, params):
        check_argument_is_not_none_or_empty(url, "url")

        try:
            url = self.GIT_API_BASE_URL + url
            headers = {"Authorization": f"Bearer {self.api_token}"}
            res = requests.get(url, headers=headers, params=params)
            if res.status_code != 200:
                logger.exception(
                    "Failed to get api request status code: %s", res.status_code
                )
                raise Exception("Failed to get GITHUB api request")

            return res.json()
        except Exception:
            logger.exception("Failed to get api request from %s", url)

    def get_all_repos(self):
        page = 1
        all_repos = []
        partial_repos = self._get(
            f"/orgs/{self.org}/repos", {"per_page": 100, "page": page}
        )

        while partial_repos:
            page += 1
            all_repos.extend(partial_repos)
            partial_repos = self._get(
                f"/orgs/{self.org}/repos", {"per_page": 100, "page": page}
            )

        return all_repos
