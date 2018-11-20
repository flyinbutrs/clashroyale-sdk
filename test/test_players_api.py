# coding: utf-8

"""
    Clash Royale API

    null  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import clashroyale_sdk
from clashroyale_sdk.api.players_api import PlayersApi  # noqa: E501
from clashroyale_sdk.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = clashroyale_sdk.api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_player(self):
        """Test case for get_player

        Get player information  # noqa: E501
        """
        pass

    def test_get_player_battles(self):
        """Test case for get_player_battles

        Get log of recent battles for a player  # noqa: E501
        """
        pass

    def test_get_player_upcoming_chests(self):
        """Test case for get_player_upcoming_chests

        Get information about player's upcoming chests  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()