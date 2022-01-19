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

class QuickLink(object):
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
        'site_key': 'int',
        'link': 'str',
        'name': 'str',
        'type': 'LinkType',
        'site': 'Site'
    }

    attribute_map = {
        'key': 'key',
        'site_key': 'siteKey',
        'link': 'link',
        'name': 'name',
        'type': 'type',
        'site': 'site'
    }

    def __init__(self, key=None, site_key=None, link=None, name=None, type=None, site=None):  # noqa: E501
        """QuickLink - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._site_key = None
        self._link = None
        self._name = None
        self._type = None
        self._site = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.site_key = site_key
        if link is not None:
            self.link = link
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if site is not None:
            self.site = site

    @property
    def key(self):
        """Gets the key of this QuickLink.  # noqa: E501


        :return: The key of this QuickLink.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this QuickLink.


        :param key: The key of this QuickLink.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def site_key(self):
        """Gets the site_key of this QuickLink.  # noqa: E501


        :return: The site_key of this QuickLink.  # noqa: E501
        :rtype: int
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this QuickLink.


        :param site_key: The site_key of this QuickLink.  # noqa: E501
        :type: int
        """
        if site_key is None:
            raise ValueError("Invalid value for `site_key`, must not be `None`")  # noqa: E501

        self._site_key = site_key

    @property
    def link(self):
        """Gets the link of this QuickLink.  # noqa: E501


        :return: The link of this QuickLink.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this QuickLink.


        :param link: The link of this QuickLink.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def name(self):
        """Gets the name of this QuickLink.  # noqa: E501


        :return: The name of this QuickLink.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QuickLink.


        :param name: The name of this QuickLink.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this QuickLink.  # noqa: E501


        :return: The type of this QuickLink.  # noqa: E501
        :rtype: LinkType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuickLink.


        :param type: The type of this QuickLink.  # noqa: E501
        :type: LinkType
        """

        self._type = type

    @property
    def site(self):
        """Gets the site of this QuickLink.  # noqa: E501


        :return: The site of this QuickLink.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this QuickLink.


        :param site: The site of this QuickLink.  # noqa: E501
        :type: Site
        """

        self._site = site

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
        if issubclass(QuickLink, dict):
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
        if not isinstance(other, QuickLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
