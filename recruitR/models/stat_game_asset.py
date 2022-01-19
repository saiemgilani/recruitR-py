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

class StatGameAsset(object):
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
        'stat_game_key': 'int',
        'stat_game': 'StatGame',
        'asset_key': 'int',
        'asset': 'Asset',
        'tag': 'ITaggable',
        'tag_key': 'int'
    }

    attribute_map = {
        'key': 'key',
        'stat_game_key': 'statGameKey',
        'stat_game': 'statGame',
        'asset_key': 'assetKey',
        'asset': 'asset',
        'tag': 'tag',
        'tag_key': 'tagKey'
    }

    def __init__(self, key=None, stat_game_key=None, stat_game=None, asset_key=None, asset=None, tag=None, tag_key=None):  # noqa: E501
        """StatGameAsset - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._stat_game_key = None
        self._stat_game = None
        self._asset_key = None
        self._asset = None
        self._tag = None
        self._tag_key = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.stat_game_key = stat_game_key
        if stat_game is not None:
            self.stat_game = stat_game
        if asset_key is not None:
            self.asset_key = asset_key
        if asset is not None:
            self.asset = asset
        if tag is not None:
            self.tag = tag
        if tag_key is not None:
            self.tag_key = tag_key

    @property
    def key(self):
        """Gets the key of this StatGameAsset.  # noqa: E501


        :return: The key of this StatGameAsset.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this StatGameAsset.


        :param key: The key of this StatGameAsset.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def stat_game_key(self):
        """Gets the stat_game_key of this StatGameAsset.  # noqa: E501


        :return: The stat_game_key of this StatGameAsset.  # noqa: E501
        :rtype: int
        """
        return self._stat_game_key

    @stat_game_key.setter
    def stat_game_key(self, stat_game_key):
        """Sets the stat_game_key of this StatGameAsset.


        :param stat_game_key: The stat_game_key of this StatGameAsset.  # noqa: E501
        :type: int
        """
        if stat_game_key is None:
            raise ValueError("Invalid value for `stat_game_key`, must not be `None`")  # noqa: E501

        self._stat_game_key = stat_game_key

    @property
    def stat_game(self):
        """Gets the stat_game of this StatGameAsset.  # noqa: E501


        :return: The stat_game of this StatGameAsset.  # noqa: E501
        :rtype: StatGame
        """
        return self._stat_game

    @stat_game.setter
    def stat_game(self, stat_game):
        """Sets the stat_game of this StatGameAsset.


        :param stat_game: The stat_game of this StatGameAsset.  # noqa: E501
        :type: StatGame
        """

        self._stat_game = stat_game

    @property
    def asset_key(self):
        """Gets the asset_key of this StatGameAsset.  # noqa: E501


        :return: The asset_key of this StatGameAsset.  # noqa: E501
        :rtype: int
        """
        return self._asset_key

    @asset_key.setter
    def asset_key(self, asset_key):
        """Sets the asset_key of this StatGameAsset.


        :param asset_key: The asset_key of this StatGameAsset.  # noqa: E501
        :type: int
        """

        self._asset_key = asset_key

    @property
    def asset(self):
        """Gets the asset of this StatGameAsset.  # noqa: E501


        :return: The asset of this StatGameAsset.  # noqa: E501
        :rtype: Asset
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this StatGameAsset.


        :param asset: The asset of this StatGameAsset.  # noqa: E501
        :type: Asset
        """

        self._asset = asset

    @property
    def tag(self):
        """Gets the tag of this StatGameAsset.  # noqa: E501


        :return: The tag of this StatGameAsset.  # noqa: E501
        :rtype: ITaggable
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this StatGameAsset.


        :param tag: The tag of this StatGameAsset.  # noqa: E501
        :type: ITaggable
        """

        self._tag = tag

    @property
    def tag_key(self):
        """Gets the tag_key of this StatGameAsset.  # noqa: E501


        :return: The tag_key of this StatGameAsset.  # noqa: E501
        :rtype: int
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this StatGameAsset.


        :param tag_key: The tag_key of this StatGameAsset.  # noqa: E501
        :type: int
        """

        self._tag_key = tag_key

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
        if issubclass(StatGameAsset, dict):
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
        if not isinstance(other, StatGameAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
