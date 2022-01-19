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

class Player(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'zip_code_key': 'int',
        'default_asset_key': 'int',
        'cbs_key': 'int',
        'last_player_institution_key': 'int',
        'last_recruitment_player_institution_key': 'int',
        'modified_date': 'datetime',
        'default_asset': 'Asset',
        'name': 'str',
        'cbs_annotation': 'str',
        'player_assets': 'list[PlayerAsset]',
        'player_contents': 'list[PlayerContent]',
        'player_institutions': 'list[PlayerInstitution]',
        'zip_code': 'ZipCode'
    }

    attribute_map = {
        'key': 'key',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'zip_code_key': 'zipCodeKey',
        'default_asset_key': 'defaultAssetKey',
        'cbs_key': 'cbsKey',
        'last_player_institution_key': 'lastPlayerInstitutionKey',
        'last_recruitment_player_institution_key': 'lastRecruitmentPlayerInstitutionKey',
        'modified_date': 'modifiedDate',
        'default_asset': 'defaultAsset',
        'name': 'name',
        'cbs_annotation': 'cbsAnnotation',
        'player_assets': 'playerAssets',
        'player_contents': 'playerContents',
        'player_institutions': 'playerInstitutions',
        'zip_code': 'zipCode'
    }

    def __init__(self, key=None, first_name=None, last_name=None, zip_code_key=None, default_asset_key=None, cbs_key=None, last_player_institution_key=None, last_recruitment_player_institution_key=None, modified_date=None, default_asset=None, name=None, cbs_annotation=None, player_assets=None, player_contents=None, player_institutions=None, zip_code=None):  # noqa: E501
        """Player - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._first_name = None
        self._last_name = None
        self._zip_code_key = None
        self._default_asset_key = None
        self._cbs_key = None
        self._last_player_institution_key = None
        self._last_recruitment_player_institution_key = None
        self._modified_date = None
        self._default_asset = None
        self._name = None
        self._cbs_annotation = None
        self._player_assets = None
        self._player_contents = None
        self._player_institutions = None
        self._zip_code = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if zip_code_key is not None:
            self.zip_code_key = zip_code_key
        if default_asset_key is not None:
            self.default_asset_key = default_asset_key
        if cbs_key is not None:
            self.cbs_key = cbs_key
        if last_player_institution_key is not None:
            self.last_player_institution_key = last_player_institution_key
        if last_recruitment_player_institution_key is not None:
            self.last_recruitment_player_institution_key = last_recruitment_player_institution_key
        if modified_date is not None:
            self.modified_date = modified_date
        if default_asset is not None:
            self.default_asset = default_asset
        if name is not None:
            self.name = name
        if cbs_annotation is not None:
            self.cbs_annotation = cbs_annotation
        if player_assets is not None:
            self.player_assets = player_assets
        if player_contents is not None:
            self.player_contents = player_contents
        if player_institutions is not None:
            self.player_institutions = player_institutions
        if zip_code is not None:
            self.zip_code = zip_code

    @property
    def key(self):
        """Gets the key of this Player.  # noqa: E501


        :return: The key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Player.


        :param key: The key of this Player.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def first_name(self):
        """Gets the first_name of this Player.  # noqa: E501


        :return: The first_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Player.


        :param first_name: The first_name of this Player.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Player.  # noqa: E501


        :return: The last_name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Player.


        :param last_name: The last_name of this Player.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def zip_code_key(self):
        """Gets the zip_code_key of this Player.  # noqa: E501


        :return: The zip_code_key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._zip_code_key

    @zip_code_key.setter
    def zip_code_key(self, zip_code_key):
        """Sets the zip_code_key of this Player.


        :param zip_code_key: The zip_code_key of this Player.  # noqa: E501
        :type: int
        """

        self._zip_code_key = zip_code_key

    @property
    def default_asset_key(self):
        """Gets the default_asset_key of this Player.  # noqa: E501


        :return: The default_asset_key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._default_asset_key

    @default_asset_key.setter
    def default_asset_key(self, default_asset_key):
        """Sets the default_asset_key of this Player.


        :param default_asset_key: The default_asset_key of this Player.  # noqa: E501
        :type: int
        """

        self._default_asset_key = default_asset_key

    @property
    def cbs_key(self):
        """Gets the cbs_key of this Player.  # noqa: E501


        :return: The cbs_key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._cbs_key

    @cbs_key.setter
    def cbs_key(self, cbs_key):
        """Sets the cbs_key of this Player.


        :param cbs_key: The cbs_key of this Player.  # noqa: E501
        :type: int
        """

        self._cbs_key = cbs_key

    @property
    def last_player_institution_key(self):
        """Gets the last_player_institution_key of this Player.  # noqa: E501


        :return: The last_player_institution_key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._last_player_institution_key

    @last_player_institution_key.setter
    def last_player_institution_key(self, last_player_institution_key):
        """Sets the last_player_institution_key of this Player.


        :param last_player_institution_key: The last_player_institution_key of this Player.  # noqa: E501
        :type: int
        """

        self._last_player_institution_key = last_player_institution_key

    @property
    def last_recruitment_player_institution_key(self):
        """Gets the last_recruitment_player_institution_key of this Player.  # noqa: E501


        :return: The last_recruitment_player_institution_key of this Player.  # noqa: E501
        :rtype: int
        """
        return self._last_recruitment_player_institution_key

    @last_recruitment_player_institution_key.setter
    def last_recruitment_player_institution_key(self, last_recruitment_player_institution_key):
        """Sets the last_recruitment_player_institution_key of this Player.


        :param last_recruitment_player_institution_key: The last_recruitment_player_institution_key of this Player.  # noqa: E501
        :type: int
        """

        self._last_recruitment_player_institution_key = last_recruitment_player_institution_key

    @property
    def modified_date(self):
        """Gets the modified_date of this Player.  # noqa: E501


        :return: The modified_date of this Player.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this Player.


        :param modified_date: The modified_date of this Player.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def default_asset(self):
        """Gets the default_asset of this Player.  # noqa: E501


        :return: The default_asset of this Player.  # noqa: E501
        :rtype: Asset
        """
        return self._default_asset

    @default_asset.setter
    def default_asset(self, default_asset):
        """Sets the default_asset of this Player.


        :param default_asset: The default_asset of this Player.  # noqa: E501
        :type: Asset
        """

        self._default_asset = default_asset

    @property
    def name(self):
        """Gets the name of this Player.  # noqa: E501


        :return: The name of this Player.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Player.


        :param name: The name of this Player.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cbs_annotation(self):
        """Gets the cbs_annotation of this Player.  # noqa: E501


        :return: The cbs_annotation of this Player.  # noqa: E501
        :rtype: str
        """
        return self._cbs_annotation

    @cbs_annotation.setter
    def cbs_annotation(self, cbs_annotation):
        """Sets the cbs_annotation of this Player.


        :param cbs_annotation: The cbs_annotation of this Player.  # noqa: E501
        :type: str
        """

        self._cbs_annotation = cbs_annotation

    @property
    def player_assets(self):
        """Gets the player_assets of this Player.  # noqa: E501


        :return: The player_assets of this Player.  # noqa: E501
        :rtype: list[PlayerAsset]
        """
        return self._player_assets

    @player_assets.setter
    def player_assets(self, player_assets):
        """Sets the player_assets of this Player.


        :param player_assets: The player_assets of this Player.  # noqa: E501
        :type: list[PlayerAsset]
        """

        self._player_assets = player_assets

    @property
    def player_contents(self):
        """Gets the player_contents of this Player.  # noqa: E501


        :return: The player_contents of this Player.  # noqa: E501
        :rtype: list[PlayerContent]
        """
        return self._player_contents

    @player_contents.setter
    def player_contents(self, player_contents):
        """Sets the player_contents of this Player.


        :param player_contents: The player_contents of this Player.  # noqa: E501
        :type: list[PlayerContent]
        """

        self._player_contents = player_contents

    @property
    def player_institutions(self):
        """Gets the player_institutions of this Player.  # noqa: E501


        :return: The player_institutions of this Player.  # noqa: E501
        :rtype: list[PlayerInstitution]
        """
        return self._player_institutions

    @player_institutions.setter
    def player_institutions(self, player_institutions):
        """Sets the player_institutions of this Player.


        :param player_institutions: The player_institutions of this Player.  # noqa: E501
        :type: list[PlayerInstitution]
        """

        self._player_institutions = player_institutions

    @property
    def zip_code(self):
        """Gets the zip_code of this Player.  # noqa: E501


        :return: The zip_code of this Player.  # noqa: E501
        :rtype: ZipCode
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Player.


        :param zip_code: The zip_code of this Player.  # noqa: E501
        :type: ZipCode
        """

        self._zip_code = zip_code

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
        if issubclass(Player, dict):
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
        if not isinstance(other, Player):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other