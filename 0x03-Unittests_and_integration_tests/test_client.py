#!/usr/bin/env python3
""" contains TestGithubOrgClient class and implement
    the test_org method.
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
import utils
from typing import Dict
from requests import HTTPError
from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ contains test for GithubOtgCLient.org """
    @parameterized.expand([('google', {'name': 'google', 'repos_url': 1}),
                           ('abc', {'name': 'abc', 'repos_url': 2})])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, val, expected, mock_org):
        """ test that GithubOrgClient.org
            returns the correct value.
        """
        mock_org.return_value = expected
        self.assertEqual(GithubOrgClient.org(), expected)

    # def test_public_repos_url(self):
    #     """ method to unit-test GithubOrgClient._public_repos_url """
    #     client = GithubOrgClient('google')
    #     known_payload = {'name': 'google', 'repos_url': '1'}
    #     with patch.object(GithubOrgClient, 'org',
    #                       new=known_payload) as mock_org:
    #         expected = known_payload['repos_url']
    #         result = client._public_repos_url
    #         self.assertEqual(result, expected)

    # known_payload = [{'name': 'google', 'license': 'MIT'},
    #                         {'name': 'repo2', 'license': 'Apache'},
    #                         {'name': 'repo3', 'license': 'GPL'}]
    # @patch('utils.get_json', return_value=known_payload)
    # def test_public_repos(self, mock_get_json):
    #     with patch.object(GithubOrgClient, '_public_repos_url',
    #                       new_callable=PropertyMock) as mock_repo_url:
    #         mock_repo_url.return_value = 'http://google.com'
    #         repos_payload = mock_get_json(mock_repo_url)
    #         client = GithubOrgClient('google')
    #         expected = ['google']
    #         result = client.public_repos('MIT')
    #         self.assertEqual(result, expected)
    #         # mock_repo.return_value = 'google.com'
    #         # mock_get_json(mock_repo.return_value)
    #         # client = GithubOrgClient('google')
    #         # expected = ['google']
    #         # result = client.public_repos('MIT')
    #         # self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """test for public_repo url """
        obj = GithubOrgClient('abc')
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            payload = {"payload": True, "repos_url": "success"}
            mock_org.return_value = payload
            self.assertEqual(obj._public_repos_url, 'success')

    @patch('client.get_json')  # patching request.get will do same thing
    def test_public_repos(self, mock_get_json):
        """unit-test for GithubOrgClient.public_repos."""
        mock_payload = [{'name': 'google'}]
        mock_get_json.return_value = mock_payload
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub:
            expected_pub_rep_url = 'http://spacedigit.tech'
            mock_pub.return_value = expected_pub_rep_url
            new_org = GithubOrgClient('holberton')
            self.assertEqual(new_org.public_repos(), ['google'])

            mock_pub.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    @patch.object(GithubOrgClient, 'has_license')
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected_result: bool, mock_has_lincense) -> None:
        """Unit-test for GithubOrgClient.has_license."""
        mock_has_lincense.return_value = expected_result
        org = GithubOrgClient('holberton')
        result = org.has_license(repo, license_key)
        self.assertEqual(expected_result, result)


# class TestIntegrationGithubOrgClient(unittest.TestCase):
#     """Performs integration tests for the `GithubOrgClient` class."""
#     @classmethod
#     def setUpClass(cls) -> None:
#         """Sets up class fixtures before running tests."""
#         route_payload = {
#             'https://api.github.com/orgs/google': cls.org_payload,
#             'https://api.github.com/orgs/google/repos': cls.repos_payload,
#             }

#         def get_payload(url):
#             if url in route_payload:
#                 return Mock(**{'json.return_value': route_payload[url]})
#             return HTTPError

#         cls.get_patcher = patch("requests.get", side_effect=get_payload)
#         cls.get_patcher.start()

#     def test_public_repos(self) -> None:
#         """Tests the `public_repos` method."""
#         self.assertEqual(
#             GithubOrgClient("google").public_repos(),
#             self.expected_repos,
#         )

#     def test_public_repos_with_license(self) -> None:
#         """Tests the `public_repos` method with a license."""
#         self.assertEqual(
#             GithubOrgClient("google").public_repos(license="apache-2.0"),
#             self.apache2_repos,
#         )

#     @classmethod
#     def tearDownClass(cls) -> None:
#         """Removes the class fixtures after running all tests."""
#         cls.get_patcher.stop()
