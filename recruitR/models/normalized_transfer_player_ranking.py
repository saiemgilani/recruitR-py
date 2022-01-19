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

class NormalizedTransferPlayerRanking(object):
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
        'status': 'str',
        'source': 'PlayerSource',
        'destination': 'PlayerDestination',
        'ranking_key': 'int',
        'key': 'int',
        'index': 'int',
        'order': 'int',
        'current_rating': 'int',
        'rating': 'int',
        'current_group_rank': 'int',
        'previous_group_rank': 'int',
        'current_group_composite_rank': 'int',
        'current_overall_rank': 'int',
        'current_overall_composite_rank': 'int',
        'player_sport_rating': 'int',
        'under_evaluation': 'bool',
        'first_name': 'str',
        'last_name': 'str',
        'player_key': 'int',
        'player_institution_key': 'int',
        'position': 'str',
        'city': 'str',
        'state': 'str',
        'current_order': 'str',
        'has_eval': 'bool',
        'current_star_rating': 'int',
        'star_rating': 'int',
        'player_sport_star_rating': 'int',
        'height': 'float',
        'weight': 'float',
        'move': 'int',
        'current_temp_rank': 'int',
        'previous_temp_rank': 'int'
    }

    attribute_map = {
        'status': 'status',
        'source': 'source',
        'destination': 'destination',
        'ranking_key': 'rankingKey',
        'key': 'key',
        'index': 'index',
        'order': 'order',
        'current_rating': 'currentRating',
        'rating': 'rating',
        'current_group_rank': 'currentGroupRank',
        'previous_group_rank': 'previousGroupRank',
        'current_group_composite_rank': 'currentGroupCompositeRank',
        'current_overall_rank': 'currentOverallRank',
        'current_overall_composite_rank': 'currentOverallCompositeRank',
        'player_sport_rating': 'playerSportRating',
        'under_evaluation': 'underEvaluation',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'player_key': 'playerKey',
        'player_institution_key': 'playerInstitutionKey',
        'position': 'position',
        'city': 'city',
        'state': 'state',
        'current_order': 'currentOrder',
        'has_eval': 'hasEval',
        'current_star_rating': 'currentStarRating',
        'star_rating': 'starRating',
        'player_sport_star_rating': 'playerSportStarRating',
        'height': 'height',
        'weight': 'weight',
        'move': 'move',
        'current_temp_rank': 'currentTempRank',
        'previous_temp_rank': 'previousTempRank'
    }

    def __init__(self, status=None, source=None, destination=None, ranking_key=None, key=None, index=None, order=None, current_rating=None, rating=None, current_group_rank=None, previous_group_rank=None, current_group_composite_rank=None, current_overall_rank=None, current_overall_composite_rank=None, player_sport_rating=None, under_evaluation=None, first_name=None, last_name=None, player_key=None, player_institution_key=None, position=None, city=None, state=None, current_order=None, has_eval=None, current_star_rating=None, star_rating=None, player_sport_star_rating=None, height=None, weight=None, move=None, current_temp_rank=None, previous_temp_rank=None):  # noqa: E501
        """NormalizedTransferPlayerRanking - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._source = None
        self._destination = None
        self._ranking_key = None
        self._key = None
        self._index = None
        self._order = None
        self._current_rating = None
        self._rating = None
        self._current_group_rank = None
        self._previous_group_rank = None
        self._current_group_composite_rank = None
        self._current_overall_rank = None
        self._current_overall_composite_rank = None
        self._player_sport_rating = None
        self._under_evaluation = None
        self._first_name = None
        self._last_name = None
        self._player_key = None
        self._player_institution_key = None
        self._position = None
        self._city = None
        self._state = None
        self._current_order = None
        self._has_eval = None
        self._current_star_rating = None
        self._star_rating = None
        self._player_sport_star_rating = None
        self._height = None
        self._weight = None
        self._move = None
        self._current_temp_rank = None
        self._previous_temp_rank = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination
        if ranking_key is not None:
            self.ranking_key = ranking_key
        if key is not None:
            self.key = key
        if index is not None:
            self.index = index
        if order is not None:
            self.order = order
        if current_rating is not None:
            self.current_rating = current_rating
        if rating is not None:
            self.rating = rating
        if current_group_rank is not None:
            self.current_group_rank = current_group_rank
        if previous_group_rank is not None:
            self.previous_group_rank = previous_group_rank
        if current_group_composite_rank is not None:
            self.current_group_composite_rank = current_group_composite_rank
        if current_overall_rank is not None:
            self.current_overall_rank = current_overall_rank
        if current_overall_composite_rank is not None:
            self.current_overall_composite_rank = current_overall_composite_rank
        if player_sport_rating is not None:
            self.player_sport_rating = player_sport_rating
        if under_evaluation is not None:
            self.under_evaluation = under_evaluation
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if player_key is not None:
            self.player_key = player_key
        if player_institution_key is not None:
            self.player_institution_key = player_institution_key
        if position is not None:
            self.position = position
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if current_order is not None:
            self.current_order = current_order
        if has_eval is not None:
            self.has_eval = has_eval
        if current_star_rating is not None:
            self.current_star_rating = current_star_rating
        if star_rating is not None:
            self.star_rating = star_rating
        if player_sport_star_rating is not None:
            self.player_sport_star_rating = player_sport_star_rating
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if move is not None:
            self.move = move
        if current_temp_rank is not None:
            self.current_temp_rank = current_temp_rank
        if previous_temp_rank is not None:
            self.previous_temp_rank = previous_temp_rank

    @property
    def status(self):
        """Gets the status of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The status of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NormalizedTransferPlayerRanking.


        :param status: The status of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def source(self):
        """Gets the source of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The source of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: PlayerSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NormalizedTransferPlayerRanking.


        :param source: The source of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: PlayerSource
        """

        self._source = source

    @property
    def destination(self):
        """Gets the destination of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The destination of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: PlayerDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this NormalizedTransferPlayerRanking.


        :param destination: The destination of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: PlayerDestination
        """

        self._destination = destination

    @property
    def ranking_key(self):
        """Gets the ranking_key of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The ranking_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._ranking_key

    @ranking_key.setter
    def ranking_key(self, ranking_key):
        """Sets the ranking_key of this NormalizedTransferPlayerRanking.


        :param ranking_key: The ranking_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._ranking_key = ranking_key

    @property
    def key(self):
        """Gets the key of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NormalizedTransferPlayerRanking.


        :param key: The key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def index(self):
        """Gets the index of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The index of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this NormalizedTransferPlayerRanking.


        :param index: The index of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def order(self):
        """Gets the order of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The order of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this NormalizedTransferPlayerRanking.


        :param order: The order of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def current_rating(self):
        """Gets the current_rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_rating

    @current_rating.setter
    def current_rating(self, current_rating):
        """Sets the current_rating of this NormalizedTransferPlayerRanking.


        :param current_rating: The current_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_rating = current_rating

    @property
    def rating(self):
        """Gets the rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this NormalizedTransferPlayerRanking.


        :param rating: The rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._rating = rating

    @property
    def current_group_rank(self):
        """Gets the current_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_group_rank

    @current_group_rank.setter
    def current_group_rank(self, current_group_rank):
        """Sets the current_group_rank of this NormalizedTransferPlayerRanking.


        :param current_group_rank: The current_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_group_rank = current_group_rank

    @property
    def previous_group_rank(self):
        """Gets the previous_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The previous_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._previous_group_rank

    @previous_group_rank.setter
    def previous_group_rank(self, previous_group_rank):
        """Sets the previous_group_rank of this NormalizedTransferPlayerRanking.


        :param previous_group_rank: The previous_group_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._previous_group_rank = previous_group_rank

    @property
    def current_group_composite_rank(self):
        """Gets the current_group_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_group_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_group_composite_rank

    @current_group_composite_rank.setter
    def current_group_composite_rank(self, current_group_composite_rank):
        """Sets the current_group_composite_rank of this NormalizedTransferPlayerRanking.


        :param current_group_composite_rank: The current_group_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_group_composite_rank = current_group_composite_rank

    @property
    def current_overall_rank(self):
        """Gets the current_overall_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_overall_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_overall_rank

    @current_overall_rank.setter
    def current_overall_rank(self, current_overall_rank):
        """Sets the current_overall_rank of this NormalizedTransferPlayerRanking.


        :param current_overall_rank: The current_overall_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_overall_rank = current_overall_rank

    @property
    def current_overall_composite_rank(self):
        """Gets the current_overall_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_overall_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_overall_composite_rank

    @current_overall_composite_rank.setter
    def current_overall_composite_rank(self, current_overall_composite_rank):
        """Sets the current_overall_composite_rank of this NormalizedTransferPlayerRanking.


        :param current_overall_composite_rank: The current_overall_composite_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_overall_composite_rank = current_overall_composite_rank

    @property
    def player_sport_rating(self):
        """Gets the player_sport_rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The player_sport_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._player_sport_rating

    @player_sport_rating.setter
    def player_sport_rating(self, player_sport_rating):
        """Sets the player_sport_rating of this NormalizedTransferPlayerRanking.


        :param player_sport_rating: The player_sport_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._player_sport_rating = player_sport_rating

    @property
    def under_evaluation(self):
        """Gets the under_evaluation of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The under_evaluation of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: bool
        """
        return self._under_evaluation

    @under_evaluation.setter
    def under_evaluation(self, under_evaluation):
        """Sets the under_evaluation of this NormalizedTransferPlayerRanking.


        :param under_evaluation: The under_evaluation of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: bool
        """

        self._under_evaluation = under_evaluation

    @property
    def first_name(self):
        """Gets the first_name of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The first_name of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this NormalizedTransferPlayerRanking.


        :param first_name: The first_name of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The last_name of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this NormalizedTransferPlayerRanking.


        :param last_name: The last_name of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def player_key(self):
        """Gets the player_key of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The player_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._player_key

    @player_key.setter
    def player_key(self, player_key):
        """Sets the player_key of this NormalizedTransferPlayerRanking.


        :param player_key: The player_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._player_key = player_key

    @property
    def player_institution_key(self):
        """Gets the player_institution_key of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The player_institution_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._player_institution_key

    @player_institution_key.setter
    def player_institution_key(self, player_institution_key):
        """Sets the player_institution_key of this NormalizedTransferPlayerRanking.


        :param player_institution_key: The player_institution_key of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._player_institution_key = player_institution_key

    @property
    def position(self):
        """Gets the position of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The position of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this NormalizedTransferPlayerRanking.


        :param position: The position of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def city(self):
        """Gets the city of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The city of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this NormalizedTransferPlayerRanking.


        :param city: The city of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The state of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NormalizedTransferPlayerRanking.


        :param state: The state of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def current_order(self):
        """Gets the current_order of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_order of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: str
        """
        return self._current_order

    @current_order.setter
    def current_order(self, current_order):
        """Sets the current_order of this NormalizedTransferPlayerRanking.


        :param current_order: The current_order of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: str
        """

        self._current_order = current_order

    @property
    def has_eval(self):
        """Gets the has_eval of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The has_eval of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: bool
        """
        return self._has_eval

    @has_eval.setter
    def has_eval(self, has_eval):
        """Sets the has_eval of this NormalizedTransferPlayerRanking.


        :param has_eval: The has_eval of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: bool
        """

        self._has_eval = has_eval

    @property
    def current_star_rating(self):
        """Gets the current_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_star_rating

    @current_star_rating.setter
    def current_star_rating(self, current_star_rating):
        """Sets the current_star_rating of this NormalizedTransferPlayerRanking.


        :param current_star_rating: The current_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_star_rating = current_star_rating

    @property
    def star_rating(self):
        """Gets the star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._star_rating

    @star_rating.setter
    def star_rating(self, star_rating):
        """Sets the star_rating of this NormalizedTransferPlayerRanking.


        :param star_rating: The star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._star_rating = star_rating

    @property
    def player_sport_star_rating(self):
        """Gets the player_sport_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The player_sport_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._player_sport_star_rating

    @player_sport_star_rating.setter
    def player_sport_star_rating(self, player_sport_star_rating):
        """Sets the player_sport_star_rating of this NormalizedTransferPlayerRanking.


        :param player_sport_star_rating: The player_sport_star_rating of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._player_sport_star_rating = player_sport_star_rating

    @property
    def height(self):
        """Gets the height of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The height of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this NormalizedTransferPlayerRanking.


        :param height: The height of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The weight of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this NormalizedTransferPlayerRanking.


        :param weight: The weight of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def move(self):
        """Gets the move of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The move of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._move

    @move.setter
    def move(self, move):
        """Sets the move of this NormalizedTransferPlayerRanking.


        :param move: The move of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._move = move

    @property
    def current_temp_rank(self):
        """Gets the current_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The current_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._current_temp_rank

    @current_temp_rank.setter
    def current_temp_rank(self, current_temp_rank):
        """Sets the current_temp_rank of this NormalizedTransferPlayerRanking.


        :param current_temp_rank: The current_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._current_temp_rank = current_temp_rank

    @property
    def previous_temp_rank(self):
        """Gets the previous_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501


        :return: The previous_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :rtype: int
        """
        return self._previous_temp_rank

    @previous_temp_rank.setter
    def previous_temp_rank(self, previous_temp_rank):
        """Sets the previous_temp_rank of this NormalizedTransferPlayerRanking.


        :param previous_temp_rank: The previous_temp_rank of this NormalizedTransferPlayerRanking.  # noqa: E501
        :type: int
        """

        self._previous_temp_rank = previous_temp_rank

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
        if issubclass(NormalizedTransferPlayerRanking, dict):
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
        if not isinstance(other, NormalizedTransferPlayerRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
