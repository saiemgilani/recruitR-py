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

class LeagueConference(object):
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
        'league_key': 'int',
        'conference_key': 'int',
        'level_key': 'int',
        'league': 'League',
        'conference': 'Conference'
    }

    attribute_map = {
        'key': 'key',
        'league_key': 'leagueKey',
        'conference_key': 'conferenceKey',
        'level_key': 'levelKey',
        'league': 'league',
        'conference': 'conference'
    }

    def __init__(self, key=None, league_key=None, conference_key=None, level_key=None, league=None, conference=None):  # noqa: E501
        """LeagueConference - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._league_key = None
        self._conference_key = None
        self._level_key = None
        self._league = None
        self._conference = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if league_key is not None:
            self.league_key = league_key
        if conference_key is not None:
            self.conference_key = conference_key
        if level_key is not None:
            self.level_key = level_key
        if league is not None:
            self.league = league
        if conference is not None:
            self.conference = conference

    @property
    def key(self):
        """Gets the key of this LeagueConference.  # noqa: E501


        :return: The key of this LeagueConference.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LeagueConference.


        :param key: The key of this LeagueConference.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def league_key(self):
        """Gets the league_key of this LeagueConference.  # noqa: E501


        :return: The league_key of this LeagueConference.  # noqa: E501
        :rtype: int
        """
        return self._league_key

    @league_key.setter
    def league_key(self, league_key):
        """Sets the league_key of this LeagueConference.


        :param league_key: The league_key of this LeagueConference.  # noqa: E501
        :type: int
        """

        self._league_key = league_key

    @property
    def conference_key(self):
        """Gets the conference_key of this LeagueConference.  # noqa: E501


        :return: The conference_key of this LeagueConference.  # noqa: E501
        :rtype: int
        """
        return self._conference_key

    @conference_key.setter
    def conference_key(self, conference_key):
        """Sets the conference_key of this LeagueConference.


        :param conference_key: The conference_key of this LeagueConference.  # noqa: E501
        :type: int
        """

        self._conference_key = conference_key

    @property
    def level_key(self):
        """Gets the level_key of this LeagueConference.  # noqa: E501


        :return: The level_key of this LeagueConference.  # noqa: E501
        :rtype: int
        """
        return self._level_key

    @level_key.setter
    def level_key(self, level_key):
        """Sets the level_key of this LeagueConference.


        :param level_key: The level_key of this LeagueConference.  # noqa: E501
        :type: int
        """

        self._level_key = level_key

    @property
    def league(self):
        """Gets the league of this LeagueConference.  # noqa: E501


        :return: The league of this LeagueConference.  # noqa: E501
        :rtype: League
        """
        return self._league

    @league.setter
    def league(self, league):
        """Sets the league of this LeagueConference.


        :param league: The league of this LeagueConference.  # noqa: E501
        :type: League
        """

        self._league = league

    @property
    def conference(self):
        """Gets the conference of this LeagueConference.  # noqa: E501


        :return: The conference of this LeagueConference.  # noqa: E501
        :rtype: Conference
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this LeagueConference.


        :param conference: The conference of this LeagueConference.  # noqa: E501
        :type: Conference
        """

        self._conference = conference

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
        if issubclass(LeagueConference, dict):
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
        if not isinstance(other, LeagueConference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
