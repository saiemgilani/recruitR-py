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

class ImageDto(object):
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
        'source_key': 'int',
        '_date': 'datetime',
        'name': 'str',
        'description': 'str',
        'thumbnail': 'str',
        'file_type': 'str',
        'height': 'int',
        'width': 'int',
        'duration': 'int',
        'url': 'str'
    }

    attribute_map = {
        'key': 'key',
        'user_key': 'userKey',
        'source_key': 'sourceKey',
        '_date': 'date',
        'name': 'name',
        'description': 'description',
        'thumbnail': 'thumbnail',
        'file_type': 'fileType',
        'height': 'height',
        'width': 'width',
        'duration': 'duration',
        'url': 'url'
    }

    def __init__(self, key=None, user_key=None, source_key=None, _date=None, name=None, description=None, thumbnail=None, file_type=None, height=None, width=None, duration=None, url=None):  # noqa: E501
        """ImageDto - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._user_key = None
        self._source_key = None
        self.__date = None
        self._name = None
        self._description = None
        self._thumbnail = None
        self._file_type = None
        self._height = None
        self._width = None
        self._duration = None
        self._url = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if user_key is not None:
            self.user_key = user_key
        if source_key is not None:
            self.source_key = source_key
        if _date is not None:
            self._date = _date
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if file_type is not None:
            self.file_type = file_type
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if duration is not None:
            self.duration = duration
        if url is not None:
            self.url = url

    @property
    def key(self):
        """Gets the key of this ImageDto.  # noqa: E501


        :return: The key of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ImageDto.


        :param key: The key of this ImageDto.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def user_key(self):
        """Gets the user_key of this ImageDto.  # noqa: E501


        :return: The user_key of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this ImageDto.


        :param user_key: The user_key of this ImageDto.  # noqa: E501
        :type: int
        """

        self._user_key = user_key

    @property
    def source_key(self):
        """Gets the source_key of this ImageDto.  # noqa: E501


        :return: The source_key of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._source_key

    @source_key.setter
    def source_key(self, source_key):
        """Sets the source_key of this ImageDto.


        :param source_key: The source_key of this ImageDto.  # noqa: E501
        :type: int
        """

        self._source_key = source_key

    @property
    def _date(self):
        """Gets the _date of this ImageDto.  # noqa: E501


        :return: The _date of this ImageDto.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ImageDto.


        :param _date: The _date of this ImageDto.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def name(self):
        """Gets the name of this ImageDto.  # noqa: E501


        :return: The name of this ImageDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageDto.


        :param name: The name of this ImageDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ImageDto.  # noqa: E501


        :return: The description of this ImageDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageDto.


        :param description: The description of this ImageDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def thumbnail(self):
        """Gets the thumbnail of this ImageDto.  # noqa: E501


        :return: The thumbnail of this ImageDto.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this ImageDto.


        :param thumbnail: The thumbnail of this ImageDto.  # noqa: E501
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def file_type(self):
        """Gets the file_type of this ImageDto.  # noqa: E501


        :return: The file_type of this ImageDto.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ImageDto.


        :param file_type: The file_type of this ImageDto.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def height(self):
        """Gets the height of this ImageDto.  # noqa: E501


        :return: The height of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImageDto.


        :param height: The height of this ImageDto.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this ImageDto.  # noqa: E501


        :return: The width of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImageDto.


        :param width: The width of this ImageDto.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def duration(self):
        """Gets the duration of this ImageDto.  # noqa: E501


        :return: The duration of this ImageDto.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ImageDto.


        :param duration: The duration of this ImageDto.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def url(self):
        """Gets the url of this ImageDto.  # noqa: E501


        :return: The url of this ImageDto.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageDto.


        :param url: The url of this ImageDto.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ImageDto, dict):
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
        if not isinstance(other, ImageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other