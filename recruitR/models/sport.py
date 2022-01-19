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

class Sport(object):
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
        'abbreviation': 'str',
        'pro_abbreviation': 'str',
        'cbs_key': 'int',
        'current_schedule_year': 'int',
        'current_recruiting_year': 'int',
        'rankings': 'list[Ranking]',
        'platoons': 'list[Platoon]',
        'teams': 'list[Team]'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'pro_abbreviation': 'proAbbreviation',
        'cbs_key': 'cbsKey',
        'current_schedule_year': 'currentScheduleYear',
        'current_recruiting_year': 'currentRecruitingYear',
        'rankings': 'rankings',
        'platoons': 'platoons',
        'teams': 'teams'
    }

    def __init__(self, key=None, name=None, abbreviation=None, pro_abbreviation=None, cbs_key=None, current_schedule_year=None, current_recruiting_year=None, rankings=None, platoons=None, teams=None):  # noqa: E501
        """Sport - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._abbreviation = None
        self._pro_abbreviation = None
        self._cbs_key = None
        self._current_schedule_year = None
        self._current_recruiting_year = None
        self._rankings = None
        self._platoons = None
        self._teams = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        self.pro_abbreviation = pro_abbreviation
        if cbs_key is not None:
            self.cbs_key = cbs_key
        if current_schedule_year is not None:
            self.current_schedule_year = current_schedule_year
        if current_recruiting_year is not None:
            self.current_recruiting_year = current_recruiting_year
        if rankings is not None:
            self.rankings = rankings
        if platoons is not None:
            self.platoons = platoons
        if teams is not None:
            self.teams = teams

    @property
    def key(self):
        """Gets the key of this Sport.  # noqa: E501


        :return: The key of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Sport.


        :param key: The key of this Sport.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Sport.  # noqa: E501


        :return: The name of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sport.


        :param name: The name of this Sport.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Sport.  # noqa: E501


        :return: The abbreviation of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Sport.


        :param abbreviation: The abbreviation of this Sport.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def pro_abbreviation(self):
        """Gets the pro_abbreviation of this Sport.  # noqa: E501


        :return: The pro_abbreviation of this Sport.  # noqa: E501
        :rtype: str
        """
        return self._pro_abbreviation

    @pro_abbreviation.setter
    def pro_abbreviation(self, pro_abbreviation):
        """Sets the pro_abbreviation of this Sport.


        :param pro_abbreviation: The pro_abbreviation of this Sport.  # noqa: E501
        :type: str
        """
        if pro_abbreviation is None:
            raise ValueError("Invalid value for `pro_abbreviation`, must not be `None`")  # noqa: E501

        self._pro_abbreviation = pro_abbreviation

    @property
    def cbs_key(self):
        """Gets the cbs_key of this Sport.  # noqa: E501


        :return: The cbs_key of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._cbs_key

    @cbs_key.setter
    def cbs_key(self, cbs_key):
        """Sets the cbs_key of this Sport.


        :param cbs_key: The cbs_key of this Sport.  # noqa: E501
        :type: int
        """

        self._cbs_key = cbs_key

    @property
    def current_schedule_year(self):
        """Gets the current_schedule_year of this Sport.  # noqa: E501


        :return: The current_schedule_year of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._current_schedule_year

    @current_schedule_year.setter
    def current_schedule_year(self, current_schedule_year):
        """Sets the current_schedule_year of this Sport.


        :param current_schedule_year: The current_schedule_year of this Sport.  # noqa: E501
        :type: int
        """

        self._current_schedule_year = current_schedule_year

    @property
    def current_recruiting_year(self):
        """Gets the current_recruiting_year of this Sport.  # noqa: E501


        :return: The current_recruiting_year of this Sport.  # noqa: E501
        :rtype: int
        """
        return self._current_recruiting_year

    @current_recruiting_year.setter
    def current_recruiting_year(self, current_recruiting_year):
        """Sets the current_recruiting_year of this Sport.


        :param current_recruiting_year: The current_recruiting_year of this Sport.  # noqa: E501
        :type: int
        """

        self._current_recruiting_year = current_recruiting_year

    @property
    def rankings(self):
        """Gets the rankings of this Sport.  # noqa: E501


        :return: The rankings of this Sport.  # noqa: E501
        :rtype: list[Ranking]
        """
        return self._rankings

    @rankings.setter
    def rankings(self, rankings):
        """Sets the rankings of this Sport.


        :param rankings: The rankings of this Sport.  # noqa: E501
        :type: list[Ranking]
        """

        self._rankings = rankings

    @property
    def platoons(self):
        """Gets the platoons of this Sport.  # noqa: E501


        :return: The platoons of this Sport.  # noqa: E501
        :rtype: list[Platoon]
        """
        return self._platoons

    @platoons.setter
    def platoons(self, platoons):
        """Sets the platoons of this Sport.


        :param platoons: The platoons of this Sport.  # noqa: E501
        :type: list[Platoon]
        """

        self._platoons = platoons

    @property
    def teams(self):
        """Gets the teams of this Sport.  # noqa: E501


        :return: The teams of this Sport.  # noqa: E501
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this Sport.


        :param teams: The teams of this Sport.  # noqa: E501
        :type: list[Team]
        """

        self._teams = teams

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
        if issubclass(Sport, dict):
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
        if not isinstance(other, Sport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other