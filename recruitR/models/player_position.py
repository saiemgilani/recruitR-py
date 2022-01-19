# coding: utf-8

"""
    Recruit Database

    Groups of services that manage the data for the 247Sports recruiting database.<br>                                         Documentation for this silo can be found here:                                         <a target=\"_blank\" href=\"https://atlassian.cbsi.com/confluence/display/TWOSPORTS/RDB+Information\">                                         Recruit Database Documentation</a>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlayerPosition(object):
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
        'key': 'int',
        'player_sport_key': 'int',
        'position_key': 'int',
        'player_sport': 'PlayerSport',
        'position': 'Position'
    }

    attribute_map = {
        'key': 'key',
        'player_sport_key': 'playerSportKey',
        'position_key': 'positionKey',
        'player_sport': 'playerSport',
        'position': 'position'
    }

    def __init__(self, key=None, player_sport_key=None, position_key=None, player_sport=None, position=None):  # noqa: E501
        """PlayerPosition - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._player_sport_key = None
        self._position_key = None
        self._player_sport = None
        self._position = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if player_sport_key is not None:
            self.player_sport_key = player_sport_key
        if position_key is not None:
            self.position_key = position_key
        if player_sport is not None:
            self.player_sport = player_sport
        if position is not None:
            self.position = position

    @property
    def key(self):
        """Gets the key of this PlayerPosition.  # noqa: E501


        :return: The key of this PlayerPosition.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PlayerPosition.


        :param key: The key of this PlayerPosition.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def player_sport_key(self):
        """Gets the player_sport_key of this PlayerPosition.  # noqa: E501


        :return: The player_sport_key of this PlayerPosition.  # noqa: E501
        :rtype: int
        """
        return self._player_sport_key

    @player_sport_key.setter
    def player_sport_key(self, player_sport_key):
        """Sets the player_sport_key of this PlayerPosition.


        :param player_sport_key: The player_sport_key of this PlayerPosition.  # noqa: E501
        :type: int
        """

        self._player_sport_key = player_sport_key

    @property
    def position_key(self):
        """Gets the position_key of this PlayerPosition.  # noqa: E501


        :return: The position_key of this PlayerPosition.  # noqa: E501
        :rtype: int
        """
        return self._position_key

    @position_key.setter
    def position_key(self, position_key):
        """Sets the position_key of this PlayerPosition.


        :param position_key: The position_key of this PlayerPosition.  # noqa: E501
        :type: int
        """

        self._position_key = position_key

    @property
    def player_sport(self):
        """Gets the player_sport of this PlayerPosition.  # noqa: E501


        :return: The player_sport of this PlayerPosition.  # noqa: E501
        :rtype: PlayerSport
        """
        return self._player_sport

    @player_sport.setter
    def player_sport(self, player_sport):
        """Sets the player_sport of this PlayerPosition.


        :param player_sport: The player_sport of this PlayerPosition.  # noqa: E501
        :type: PlayerSport
        """

        self._player_sport = player_sport

    @property
    def position(self):
        """Gets the position of this PlayerPosition.  # noqa: E501


        :return: The position of this PlayerPosition.  # noqa: E501
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerPosition.


        :param position: The position of this PlayerPosition.  # noqa: E501
        :type: Position
        """

        self._position = position

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
        if issubclass(PlayerPosition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other