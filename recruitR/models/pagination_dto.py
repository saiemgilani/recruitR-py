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

class PaginationDto(object):
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
        'count': 'int',
        'offset': 'int',
        'limit': 'int',
        'items_per_page': 'int',
        'current_page': 'int',
        'page_count': 'int'
    }

    attribute_map = {
        'count': 'count',
        'offset': 'offset',
        'limit': 'limit',
        'items_per_page': 'itemsPerPage',
        'current_page': 'currentPage',
        'page_count': 'pageCount'
    }

    def __init__(self, count=None, offset=None, limit=None, items_per_page=None, current_page=None, page_count=None):  # noqa: E501
        """PaginationDto - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._offset = None
        self._limit = None
        self._items_per_page = None
        self._current_page = None
        self._page_count = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if current_page is not None:
            self.current_page = current_page
        if page_count is not None:
            self.page_count = page_count

    @property
    def count(self):
        """Gets the count of this PaginationDto.  # noqa: E501


        :return: The count of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PaginationDto.


        :param count: The count of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def offset(self):
        """Gets the offset of this PaginationDto.  # noqa: E501


        :return: The offset of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PaginationDto.


        :param offset: The offset of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PaginationDto.  # noqa: E501


        :return: The limit of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaginationDto.


        :param limit: The limit of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def items_per_page(self):
        """Gets the items_per_page of this PaginationDto.  # noqa: E501


        :return: The items_per_page of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this PaginationDto.


        :param items_per_page: The items_per_page of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._items_per_page = items_per_page

    @property
    def current_page(self):
        """Gets the current_page of this PaginationDto.  # noqa: E501


        :return: The current_page of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this PaginationDto.


        :param current_page: The current_page of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def page_count(self):
        """Gets the page_count of this PaginationDto.  # noqa: E501


        :return: The page_count of this PaginationDto.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this PaginationDto.


        :param page_count: The page_count of this PaginationDto.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

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
        if issubclass(PaginationDto, dict):
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
        if not isinstance(other, PaginationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
