# coding: utf-8

"""
    Clash Royale API

    null  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clashroyale_sdk.models.tournament_base import TournamentBase  # noqa: F401,E501
from clashroyale_sdk.models.tournament_base_items import TournamentBaseItems  # noqa: F401,E501
from clashroyale_sdk.models.tournament_members_list import TournamentMembersList  # noqa: F401,E501


class Tournament(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[TournamentBaseItems]',
        'started_time': 'str',
        'members_list': 'list[TournamentMembersList]'
    }

    attribute_map = {
        'items': 'items',
        'started_time': 'startedTime',
        'members_list': 'membersList'
    }

    def __init__(self, items=None, started_time=None, members_list=None):  # noqa: E501
        """Tournament - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._started_time = None
        self._members_list = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if started_time is not None:
            self.started_time = started_time
        if members_list is not None:
            self.members_list = members_list

    @property
    def items(self):
        """Gets the items of this Tournament.  # noqa: E501


        :return: The items of this Tournament.  # noqa: E501
        :rtype: list[TournamentBaseItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Tournament.


        :param items: The items of this Tournament.  # noqa: E501
        :type: list[TournamentBaseItems]
        """

        self._items = items

    @property
    def started_time(self):
        """Gets the started_time of this Tournament.  # noqa: E501


        :return: The started_time of this Tournament.  # noqa: E501
        :rtype: str
        """
        return self._started_time

    @started_time.setter
    def started_time(self, started_time):
        """Sets the started_time of this Tournament.


        :param started_time: The started_time of this Tournament.  # noqa: E501
        :type: str
        """

        self._started_time = started_time

    @property
    def members_list(self):
        """Gets the members_list of this Tournament.  # noqa: E501


        :return: The members_list of this Tournament.  # noqa: E501
        :rtype: list[TournamentMembersList]
        """
        return self._members_list

    @members_list.setter
    def members_list(self, members_list):
        """Sets the members_list of this Tournament.


        :param members_list: The members_list of this Tournament.  # noqa: E501
        :type: list[TournamentMembersList]
        """

        self._members_list = members_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Tournament):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other