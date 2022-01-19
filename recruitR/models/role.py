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

class Role(object):
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
        'name': 'str',
        'role_group': 'RoleGroup',
        'user_roles': 'list[UserRole]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'role_group': 'roleGroup',
        'user_roles': 'userRoles'
    }

    def __init__(self, key=None, name=None, role_group=None, user_roles=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._role_group = None
        self._user_roles = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if role_group is not None:
            self.role_group = role_group
        if user_roles is not None:
            self.user_roles = user_roles

    @property
    def key(self):
        """Gets the key of this Role.  # noqa: E501


        :return: The key of this Role.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Role.


        :param key: The key of this Role.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501


        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.


        :param name: The name of this Role.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role_group(self):
        """Gets the role_group of this Role.  # noqa: E501


        :return: The role_group of this Role.  # noqa: E501
        :rtype: RoleGroup
        """
        return self._role_group

    @role_group.setter
    def role_group(self, role_group):
        """Sets the role_group of this Role.


        :param role_group: The role_group of this Role.  # noqa: E501
        :type: RoleGroup
        """

        self._role_group = role_group

    @property
    def user_roles(self):
        """Gets the user_roles of this Role.  # noqa: E501


        :return: The user_roles of this Role.  # noqa: E501
        :rtype: list[UserRole]
        """
        return self._user_roles

    @user_roles.setter
    def user_roles(self, user_roles):
        """Sets the user_roles of this Role.


        :param user_roles: The user_roles of this Role.  # noqa: E501
        :type: list[UserRole]
        """

        self._user_roles = user_roles

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other