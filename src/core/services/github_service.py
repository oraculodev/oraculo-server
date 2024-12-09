import logging
import os

import requests
from git import Repo

from core.utils.check_arguments import check_argument_is_not_none_or_empty
from config import settings

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

    def clone_repo(
        self,
        repo_url,
        repo_dir,
    ):
        check_argument_is_not_none_or_empty(repo_url, "repo_url")
        check_argument_is_not_none_or_empty(repo_dir, "repo_dir")

        # create base folder for clone repos
        os.makedirs("repos", exist_ok=True)

        if not os.path.exists(repo_dir):
            print("clonning repo")
            git_ssh_identity_file = os.path.join(
                os.getcwd(), self._get_ssh_key_path("id_ed25519")
            )
            git_ssh_cmd = "ssh -i %s" % git_ssh_identity_file
            Repo.clone_from(repo_url, repo_dir, env=dict(GIT_SSH_COMMAND=git_ssh_cmd))

        return None

    def _get_ssh_key_path(self, ssh_key_name):
        ssh_key = settings.GITHUB["DEPLOY_SSH_KEY"]

        check_argument_is_not_none_or_empty(ssh_key, "ssh_key")
        check_argument_is_not_none_or_empty(ssh_key_name, "ssh_key_name")

        # create base folder for ssh keys
        os.makedirs("ssh", exist_ok=True)

        # create ssh key
        ssh_key_path = os.path.join(os.getcwd(), "ssh", ssh_key_name)
        with open(ssh_key_path, "w") as f:
            f.write(ssh_key)

        # set ssh key permissions
        os.chmod(ssh_key_path, 0o600)

        return ssh_key_path
