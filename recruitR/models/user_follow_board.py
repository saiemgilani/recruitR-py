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

class UserFollowBoard(object):
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
        'user_key': 'int',
        'board_key': 'int',
        'board': 'Board',
        'site_key': 'int',
        'site': 'Site',
        'user': 'User'
    }

    attribute_map = {
        'key': 'key',
        'user_key': 'userKey',
        'board_key': 'boardKey',
        'board': 'board',
        'site_key': 'siteKey',
        'site': 'site',
        'user': 'user'
    }

    def __init__(self, key=None, user_key=None, board_key=None, board=None, site_key=None, site=None, user=None):  # noqa: E501
        """UserFollowBoard - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._user_key = None
        self._board_key = None
        self._board = None
        self._site_key = None
        self._site = None
        self._user = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.user_key = user_key
        self.board_key = board_key
        if board is not None:
            self.board = board
        if site_key is not None:
            self.site_key = site_key
        if site is not None:
            self.site = site
        if user is not None:
            self.user = user

    @property
    def key(self):
        """Gets the key of this UserFollowBoard.  # noqa: E501


        :return: The key of this UserFollowBoard.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserFollowBoard.


        :param key: The key of this UserFollowBoard.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def user_key(self):
        """Gets the user_key of this UserFollowBoard.  # noqa: E501


        :return: The user_key of this UserFollowBoard.  # noqa: E501
        :rtype: int
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this UserFollowBoard.


        :param user_key: The user_key of this UserFollowBoard.  # noqa: E501
        :type: int
        """
        if user_key is None:
            raise ValueError("Invalid value for `user_key`, must not be `None`")  # noqa: E501

        self._user_key = user_key

    @property
    def board_key(self):
        """Gets the board_key of this UserFollowBoard.  # noqa: E501


        :return: The board_key of this UserFollowBoard.  # noqa: E501
        :rtype: int
        """
        return self._board_key

    @board_key.setter
    def board_key(self, board_key):
        """Sets the board_key of this UserFollowBoard.


        :param board_key: The board_key of this UserFollowBoard.  # noqa: E501
        :type: int
        """
        if board_key is None:
            raise ValueError("Invalid value for `board_key`, must not be `None`")  # noqa: E501

        self._board_key = board_key

    @property
    def board(self):
        """Gets the board of this UserFollowBoard.  # noqa: E501


        :return: The board of this UserFollowBoard.  # noqa: E501
        :rtype: Board
        """
        return self._board

    @board.setter
    def board(self, board):
        """Sets the board of this UserFollowBoard.


        :param board: The board of this UserFollowBoard.  # noqa: E501
        :type: Board
        """

        self._board = board

    @property
    def site_key(self):
        """Gets the site_key of this UserFollowBoard.  # noqa: E501


        :return: The site_key of this UserFollowBoard.  # noqa: E501
        :rtype: int
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this UserFollowBoard.


        :param site_key: The site_key of this UserFollowBoard.  # noqa: E501
        :type: int
        """

        self._site_key = site_key

    @property
    def site(self):
        """Gets the site of this UserFollowBoard.  # noqa: E501


        :return: The site of this UserFollowBoard.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this UserFollowBoard.


        :param site: The site of this UserFollowBoard.  # noqa: E501
        :type: Site
        """

        self._site = site

    @property
    def user(self):
        """Gets the user of this UserFollowBoard.  # noqa: E501


        :return: The user of this UserFollowBoard.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserFollowBoard.


        :param user: The user of this UserFollowBoard.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(UserFollowBoard, dict):
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
        if not isinstance(other, UserFollowBoard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other