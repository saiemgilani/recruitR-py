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

class PublishedRankingDto(object):
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
        'status': 'bool',
        'type': 'Types',
        'year': 'int'
    }

    attribute_map = {
        'key': 'key',
        'status': 'status',
        'type': 'type',
        'year': 'year'
    }

    def __init__(self, key=None, status=None, type=None, year=None):  # noqa: E501
        """PublishedRankingDto - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._status = None
        self._type = None
        self._year = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if year is not None:
            self.year = year

    @property
    def key(self):
        """Gets the key of this PublishedRankingDto.  # noqa: E501


        :return: The key of this PublishedRankingDto.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PublishedRankingDto.


        :param key: The key of this PublishedRankingDto.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def status(self):
        """Gets the status of this PublishedRankingDto.  # noqa: E501


        :return: The status of this PublishedRankingDto.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublishedRankingDto.


        :param status: The status of this PublishedRankingDto.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this PublishedRankingDto.  # noqa: E501


        :return: The type of this PublishedRankingDto.  # noqa: E501
        :rtype: Types
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublishedRankingDto.


        :param type: The type of this PublishedRankingDto.  # noqa: E501
        :type: Types
        """

        self._type = type

    @property
    def year(self):
        """Gets the year of this PublishedRankingDto.  # noqa: E501


        :return: The year of this PublishedRankingDto.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PublishedRankingDto.


        :param year: The year of this PublishedRankingDto.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if issubclass(PublishedRankingDto, dict):
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
        if not isinstance(other, PublishedRankingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
