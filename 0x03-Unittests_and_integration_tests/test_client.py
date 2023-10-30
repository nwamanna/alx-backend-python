#!/usr/bin/env python3
""" contains TestGithubOrgClient class and implement
    the test_org method.
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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

    def test_public_repos_url(self):
        """ method to unit-test GithubOrgClient._public_repos_url """
        client = GithubOrgClient('google')
        known_payload = {'name': 'google', 'repos_url': '1'}
        with patch.object(GithubOrgClient, 'org',
                          new=known_payload) as mock_org:
            expected = known_payload['repos_url']
            result = client._public_repos_url
            self.assertEqual(result, expected)
