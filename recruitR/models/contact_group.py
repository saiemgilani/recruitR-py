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

class ContactGroup(object):
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
        'site': 'Site',
        'group_alerts': 'list[GroupAlert]',
        'group_contacts': 'list[GroupContact]'
    }

    attribute_map = {
        'key': 'key',
        'site_key': 'siteKey',
        'site': 'site',
        'group_alerts': 'groupAlerts',
        'group_contacts': 'groupContacts'
    }

    def __init__(self, key=None, site_key=None, site=None, group_alerts=None, group_contacts=None):  # noqa: E501
        """ContactGroup - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._site_key = None
        self._site = None
        self._group_alerts = None
        self._group_contacts = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if site_key is not None:
            self.site_key = site_key
        if site is not None:
            self.site = site
        if group_alerts is not None:
            self.group_alerts = group_alerts
        if group_contacts is not None:
            self.group_contacts = group_contacts

    @property
    def key(self):
        """Gets the key of this ContactGroup.  # noqa: E501


        :return: The key of this ContactGroup.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ContactGroup.


        :param key: The key of this ContactGroup.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def site_key(self):
        """Gets the site_key of this ContactGroup.  # noqa: E501


        :return: The site_key of this ContactGroup.  # noqa: E501
        :rtype: int
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this ContactGroup.


        :param site_key: The site_key of this ContactGroup.  # noqa: E501
        :type: int
        """

        self._site_key = site_key

    @property
    def site(self):
        """Gets the site of this ContactGroup.  # noqa: E501


        :return: The site of this ContactGroup.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this ContactGroup.


        :param site: The site of this ContactGroup.  # noqa: E501
        :type: Site
        """

        self._site = site

    @property
    def group_alerts(self):
        """Gets the group_alerts of this ContactGroup.  # noqa: E501


        :return: The group_alerts of this ContactGroup.  # noqa: E501
        :rtype: list[GroupAlert]
        """
        return self._group_alerts

    @group_alerts.setter
    def group_alerts(self, group_alerts):
        """Sets the group_alerts of this ContactGroup.


        :param group_alerts: The group_alerts of this ContactGroup.  # noqa: E501
        :type: list[GroupAlert]
        """

        self._group_alerts = group_alerts

    @property
    def group_contacts(self):
        """Gets the group_contacts of this ContactGroup.  # noqa: E501


        :return: The group_contacts of this ContactGroup.  # noqa: E501
        :rtype: list[GroupContact]
        """
        return self._group_contacts

    @group_contacts.setter
    def group_contacts(self, group_contacts):
        """Sets the group_contacts of this ContactGroup.


        :param group_contacts: The group_contacts of this ContactGroup.  # noqa: E501
        :type: list[GroupContact]
        """

        self._group_contacts = group_contacts

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
        if issubclass(ContactGroup, dict):
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
        if not isinstance(other, ContactGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other