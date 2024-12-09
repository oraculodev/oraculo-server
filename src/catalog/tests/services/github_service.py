from unittest.mock import MagicMock, patch

from django.test import TestCase

from core.services.github_service import GithubService


class TestGithubService(TestCase):

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_none_url(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        with self.assertRaises(ValueError):
            github_service.clone_repo(None, "test_repo_dir")

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_empty_url(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        with self.assertRaises(ValueError):
            github_service.clone_repo("", "test_repo_dir")

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_none_dir(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        with self.assertRaises(ValueError):
            github_service.clone_repo("test_repo_url", None)

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_empty_dir(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        with self.assertRaises(ValueError):
            github_service.clone_repo("test_repo_url", "")

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_existing_dir(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        mock_os.path.exists.return_value = True
        result = github_service.clone_repo("test_repo_url", "existing_dir")
        self.assertIsNone(result)

    @patch("core.services.github_service.os")
    @patch("core.services.github_service.Repo")
    def test_clone_repo_success(self, mock_repo, mock_os):
        github_service = GithubService(org="test_org", api_token="test_token")
        mock_os.path.exists.return_value = False
        with patch("core.services.github_service.os.makedirs") as mock_makedirs:
            with patch("core.services.github_service.os.getcwd") as mock_getcwd:
                result = github_service.clone_repo("test_repo_url", "test_repo_dir")
                self.assertIsNone(result)
