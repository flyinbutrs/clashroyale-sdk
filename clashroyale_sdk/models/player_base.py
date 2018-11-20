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

from clashroyale_sdk.models.arena import Arena  # noqa: F401,E501


class PlayerBase(object):
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
        'tag': 'str',
        'name': 'str',
        'exp_level': 'int',
        'trophies': 'int',
        'arena': 'Arena'
    }

    attribute_map = {
        'tag': 'tag',
        'name': 'name',
        'exp_level': 'expLevel',
        'trophies': 'trophies',
        'arena': 'arena'
    }

    def __init__(self, tag=None, name=None, exp_level=None, trophies=None, arena=None):  # noqa: E501
        """PlayerBase - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._name = None
        self._exp_level = None
        self._trophies = None
        self._arena = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if exp_level is not None:
            self.exp_level = exp_level
        if trophies is not None:
            self.trophies = trophies
        if arena is not None:
            self.arena = arena

    @property
    def tag(self):
        """Gets the tag of this PlayerBase.  # noqa: E501


        :return: The tag of this PlayerBase.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PlayerBase.


        :param tag: The tag of this PlayerBase.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this PlayerBase.  # noqa: E501


        :return: The name of this PlayerBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerBase.


        :param name: The name of this PlayerBase.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def exp_level(self):
        """Gets the exp_level of this PlayerBase.  # noqa: E501


        :return: The exp_level of this PlayerBase.  # noqa: E501
        :rtype: int
        """
        return self._exp_level

    @exp_level.setter
    def exp_level(self, exp_level):
        """Sets the exp_level of this PlayerBase.


        :param exp_level: The exp_level of this PlayerBase.  # noqa: E501
        :type: int
        """

        self._exp_level = exp_level

    @property
    def trophies(self):
        """Gets the trophies of this PlayerBase.  # noqa: E501


        :return: The trophies of this PlayerBase.  # noqa: E501
        :rtype: int
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this PlayerBase.


        :param trophies: The trophies of this PlayerBase.  # noqa: E501
        :type: int
        """

        self._trophies = trophies

    @property
    def arena(self):
        """Gets the arena of this PlayerBase.  # noqa: E501


        :return: The arena of this PlayerBase.  # noqa: E501
        :rtype: Arena
        """
        return self._arena

    @arena.setter
    def arena(self, arena):
        """Sets the arena of this PlayerBase.


        :param arena: The arena of this PlayerBase.  # noqa: E501
        :type: Arena
        """

        self._arena = arena

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
        if not isinstance(other, PlayerBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
