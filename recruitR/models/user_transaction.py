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

class UserTransaction(object):
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
        'user_subscription_key': 'int',
        'type': 'TransactionTypes',
        '_date': 'datetime',
        'amount': 'float',
        'tref': 'str',
        'submit': 'str',
        'response': 'str',
        'card_key': 'int',
        'success': 'int',
        'admin_user_key': 'int',
        'subscription_key': 'int',
        'subscription_price': 'float',
        'zip_code': 'str',
        'state_key': 'int',
        'card': 'Card',
        'user': 'User',
        'admin_user': 'User',
        'subscription': 'Subscription',
        'user_subscription': 'UserSubscription',
        'revenues': 'list[Revenue]',
        'is_recurty_transaction': 'bool',
        'generate_recurly_links': 'bool',
        'charge_back_submit': 'str'
    }

    attribute_map = {
        'key': 'key',
        'user_key': 'userKey',
        'user_subscription_key': 'userSubscriptionKey',
        'type': 'type',
        '_date': 'date',
        'amount': 'amount',
        'tref': 'tref',
        'submit': 'submit',
        'response': 'response',
        'card_key': 'cardKey',
        'success': 'success',
        'admin_user_key': 'adminUserKey',
        'subscription_key': 'subscriptionKey',
        'subscription_price': 'subscriptionPrice',
        'zip_code': 'zipCode',
        'state_key': 'stateKey',
        'card': 'card',
        'user': 'user',
        'admin_user': 'adminUser',
        'subscription': 'subscription',
        'user_subscription': 'userSubscription',
        'revenues': 'revenues',
        'is_recurty_transaction': 'isRecurtyTransaction',
        'generate_recurly_links': 'generateRecurlyLinks',
        'charge_back_submit': 'chargeBackSubmit'
    }

    def __init__(self, key=None, user_key=None, user_subscription_key=None, type=None, _date=None, amount=None, tref=None, submit=None, response=None, card_key=None, success=None, admin_user_key=None, subscription_key=None, subscription_price=None, zip_code=None, state_key=None, card=None, user=None, admin_user=None, subscription=None, user_subscription=None, revenues=None, is_recurty_transaction=None, generate_recurly_links=None, charge_back_submit=None):  # noqa: E501
        """UserTransaction - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._user_key = None
        self._user_subscription_key = None
        self._type = None
        self.__date = None
        self._amount = None
        self._tref = None
        self._submit = None
        self._response = None
        self._card_key = None
        self._success = None
        self._admin_user_key = None
        self._subscription_key = None
        self._subscription_price = None
        self._zip_code = None
        self._state_key = None
        self._card = None
        self._user = None
        self._admin_user = None
        self._subscription = None
        self._user_subscription = None
        self._revenues = None
        self._is_recurty_transaction = None
        self._generate_recurly_links = None
        self._charge_back_submit = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if user_key is not None:
            self.user_key = user_key
        if user_subscription_key is not None:
            self.user_subscription_key = user_subscription_key
        if type is not None:
            self.type = type
        if _date is not None:
            self._date = _date
        if amount is not None:
            self.amount = amount
        if tref is not None:
            self.tref = tref
        if submit is not None:
            self.submit = submit
        if response is not None:
            self.response = response
        if card_key is not None:
            self.card_key = card_key
        if success is not None:
            self.success = success
        if admin_user_key is not None:
            self.admin_user_key = admin_user_key
        if subscription_key is not None:
            self.subscription_key = subscription_key
        if subscription_price is not None:
            self.subscription_price = subscription_price
        if zip_code is not None:
            self.zip_code = zip_code
        if state_key is not None:
            self.state_key = state_key
        if card is not None:
            self.card = card
        if user is not None:
            self.user = user
        if admin_user is not None:
            self.admin_user = admin_user
        if subscription is not None:
            self.subscription = subscription
        if user_subscription is not None:
            self.user_subscription = user_subscription
        if revenues is not None:
            self.revenues = revenues
        if is_recurty_transaction is not None:
            self.is_recurty_transaction = is_recurty_transaction
        if generate_recurly_links is not None:
            self.generate_recurly_links = generate_recurly_links
        if charge_back_submit is not None:
            self.charge_back_submit = charge_back_submit

    @property
    def key(self):
        """Gets the key of this UserTransaction.  # noqa: E501


        :return: The key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UserTransaction.


        :param key: The key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._key = key

    @property
    def user_key(self):
        """Gets the user_key of this UserTransaction.  # noqa: E501


        :return: The user_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this UserTransaction.


        :param user_key: The user_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._user_key = user_key

    @property
    def user_subscription_key(self):
        """Gets the user_subscription_key of this UserTransaction.  # noqa: E501


        :return: The user_subscription_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._user_subscription_key

    @user_subscription_key.setter
    def user_subscription_key(self, user_subscription_key):
        """Sets the user_subscription_key of this UserTransaction.


        :param user_subscription_key: The user_subscription_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._user_subscription_key = user_subscription_key

    @property
    def type(self):
        """Gets the type of this UserTransaction.  # noqa: E501


        :return: The type of this UserTransaction.  # noqa: E501
        :rtype: TransactionTypes
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserTransaction.


        :param type: The type of this UserTransaction.  # noqa: E501
        :type: TransactionTypes
        """

        self._type = type

    @property
    def _date(self):
        """Gets the _date of this UserTransaction.  # noqa: E501


        :return: The _date of this UserTransaction.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this UserTransaction.


        :param _date: The _date of this UserTransaction.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this UserTransaction.  # noqa: E501


        :return: The amount of this UserTransaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UserTransaction.


        :param amount: The amount of this UserTransaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def tref(self):
        """Gets the tref of this UserTransaction.  # noqa: E501


        :return: The tref of this UserTransaction.  # noqa: E501
        :rtype: str
        """
        return self._tref

    @tref.setter
    def tref(self, tref):
        """Sets the tref of this UserTransaction.


        :param tref: The tref of this UserTransaction.  # noqa: E501
        :type: str
        """

        self._tref = tref

    @property
    def submit(self):
        """Gets the submit of this UserTransaction.  # noqa: E501


        :return: The submit of this UserTransaction.  # noqa: E501
        :rtype: str
        """
        return self._submit

    @submit.setter
    def submit(self, submit):
        """Sets the submit of this UserTransaction.


        :param submit: The submit of this UserTransaction.  # noqa: E501
        :type: str
        """

        self._submit = submit

    @property
    def response(self):
        """Gets the response of this UserTransaction.  # noqa: E501


        :return: The response of this UserTransaction.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this UserTransaction.


        :param response: The response of this UserTransaction.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def card_key(self):
        """Gets the card_key of this UserTransaction.  # noqa: E501


        :return: The card_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._card_key

    @card_key.setter
    def card_key(self, card_key):
        """Sets the card_key of this UserTransaction.


        :param card_key: The card_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._card_key = card_key

    @property
    def success(self):
        """Gets the success of this UserTransaction.  # noqa: E501


        :return: The success of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UserTransaction.


        :param success: The success of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._success = success

    @property
    def admin_user_key(self):
        """Gets the admin_user_key of this UserTransaction.  # noqa: E501


        :return: The admin_user_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._admin_user_key

    @admin_user_key.setter
    def admin_user_key(self, admin_user_key):
        """Sets the admin_user_key of this UserTransaction.


        :param admin_user_key: The admin_user_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._admin_user_key = admin_user_key

    @property
    def subscription_key(self):
        """Gets the subscription_key of this UserTransaction.  # noqa: E501


        :return: The subscription_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._subscription_key

    @subscription_key.setter
    def subscription_key(self, subscription_key):
        """Sets the subscription_key of this UserTransaction.


        :param subscription_key: The subscription_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._subscription_key = subscription_key

    @property
    def subscription_price(self):
        """Gets the subscription_price of this UserTransaction.  # noqa: E501


        :return: The subscription_price of this UserTransaction.  # noqa: E501
        :rtype: float
        """
        return self._subscription_price

    @subscription_price.setter
    def subscription_price(self, subscription_price):
        """Sets the subscription_price of this UserTransaction.


        :param subscription_price: The subscription_price of this UserTransaction.  # noqa: E501
        :type: float
        """

        self._subscription_price = subscription_price

    @property
    def zip_code(self):
        """Gets the zip_code of this UserTransaction.  # noqa: E501


        :return: The zip_code of this UserTransaction.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this UserTransaction.


        :param zip_code: The zip_code of this UserTransaction.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def state_key(self):
        """Gets the state_key of this UserTransaction.  # noqa: E501


        :return: The state_key of this UserTransaction.  # noqa: E501
        :rtype: int
        """
        return self._state_key

    @state_key.setter
    def state_key(self, state_key):
        """Sets the state_key of this UserTransaction.


        :param state_key: The state_key of this UserTransaction.  # noqa: E501
        :type: int
        """

        self._state_key = state_key

    @property
    def card(self):
        """Gets the card of this UserTransaction.  # noqa: E501


        :return: The card of this UserTransaction.  # noqa: E501
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this UserTransaction.


        :param card: The card of this UserTransaction.  # noqa: E501
        :type: Card
        """

        self._card = card

    @property
    def user(self):
        """Gets the user of this UserTransaction.  # noqa: E501


        :return: The user of this UserTransaction.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserTransaction.


        :param user: The user of this UserTransaction.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def admin_user(self):
        """Gets the admin_user of this UserTransaction.  # noqa: E501


        :return: The admin_user of this UserTransaction.  # noqa: E501
        :rtype: User
        """
        return self._admin_user

    @admin_user.setter
    def admin_user(self, admin_user):
        """Sets the admin_user of this UserTransaction.


        :param admin_user: The admin_user of this UserTransaction.  # noqa: E501
        :type: User
        """

        self._admin_user = admin_user

    @property
    def subscription(self):
        """Gets the subscription of this UserTransaction.  # noqa: E501


        :return: The subscription of this UserTransaction.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this UserTransaction.


        :param subscription: The subscription of this UserTransaction.  # noqa: E501
        :type: Subscription
        """

        self._subscription = subscription

    @property
    def user_subscription(self):
        """Gets the user_subscription of this UserTransaction.  # noqa: E501


        :return: The user_subscription of this UserTransaction.  # noqa: E501
        :rtype: UserSubscription
        """
        return self._user_subscription

    @user_subscription.setter
    def user_subscription(self, user_subscription):
        """Sets the user_subscription of this UserTransaction.


        :param user_subscription: The user_subscription of this UserTransaction.  # noqa: E501
        :type: UserSubscription
        """

        self._user_subscription = user_subscription

    @property
    def revenues(self):
        """Gets the revenues of this UserTransaction.  # noqa: E501


        :return: The revenues of this UserTransaction.  # noqa: E501
        :rtype: list[Revenue]
        """
        return self._revenues

    @revenues.setter
    def revenues(self, revenues):
        """Sets the revenues of this UserTransaction.


        :param revenues: The revenues of this UserTransaction.  # noqa: E501
        :type: list[Revenue]
        """

        self._revenues = revenues

    @property
    def is_recurty_transaction(self):
        """Gets the is_recurty_transaction of this UserTransaction.  # noqa: E501


        :return: The is_recurty_transaction of this UserTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_recurty_transaction

    @is_recurty_transaction.setter
    def is_recurty_transaction(self, is_recurty_transaction):
        """Sets the is_recurty_transaction of this UserTransaction.


        :param is_recurty_transaction: The is_recurty_transaction of this UserTransaction.  # noqa: E501
        :type: bool
        """

        self._is_recurty_transaction = is_recurty_transaction

    @property
    def generate_recurly_links(self):
        """Gets the generate_recurly_links of this UserTransaction.  # noqa: E501


        :return: The generate_recurly_links of this UserTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._generate_recurly_links

    @generate_recurly_links.setter
    def generate_recurly_links(self, generate_recurly_links):
        """Sets the generate_recurly_links of this UserTransaction.


        :param generate_recurly_links: The generate_recurly_links of this UserTransaction.  # noqa: E501
        :type: bool
        """

        self._generate_recurly_links = generate_recurly_links

    @property
    def charge_back_submit(self):
        """Gets the charge_back_submit of this UserTransaction.  # noqa: E501


        :return: The charge_back_submit of this UserTransaction.  # noqa: E501
        :rtype: str
        """
        return self._charge_back_submit

    @charge_back_submit.setter
    def charge_back_submit(self, charge_back_submit):
        """Sets the charge_back_submit of this UserTransaction.


        :param charge_back_submit: The charge_back_submit of this UserTransaction.  # noqa: E501
        :type: str
        """

        self._charge_back_submit = charge_back_submit

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
        if issubclass(UserTransaction, dict):
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
        if not isinstance(other, UserTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
