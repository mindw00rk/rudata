# coding: utf-8

"""
    API Reference United Data (RU DATA) v2.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: DataHub: v2, Models: 1.23.21.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EfirDataHubModelsModelsBondDateOptionsResponse(object):
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
        'error': 'str',
        'coupon_date': 'datetime',
        'coupon_period': 'int',
        'coupon_rate': 'float',
        'pay_per_bond': 'float',
        'offer_date': 'datetime',
        'buy_back_price': 'float',
        'current_facevalue': 'float',
        'accrued_interest': 'float',
        'listing_level': 'int',
        'sum_coupons_mty': 'float',
        'sum_coupons_offer': 'float'
    }

    attribute_map = {
        'error': 'error',
        'coupon_date': 'couponDate',
        'coupon_period': 'couponPeriod',
        'coupon_rate': 'couponRate',
        'pay_per_bond': 'payPerBond',
        'offer_date': 'offerDate',
        'buy_back_price': 'buyBackPrice',
        'current_facevalue': 'currentFacevalue',
        'accrued_interest': 'accruedInterest',
        'listing_level': 'listingLevel',
        'sum_coupons_mty': 'sumCouponsMty',
        'sum_coupons_offer': 'sumCouponsOffer'
    }

    def __init__(self, error=None, coupon_date=None, coupon_period=None, coupon_rate=None, pay_per_bond=None, offer_date=None, buy_back_price=None, current_facevalue=None, accrued_interest=None, listing_level=None, sum_coupons_mty=None, sum_coupons_offer=None):  # noqa: E501
        """EfirDataHubModelsModelsBondDateOptionsResponse - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._coupon_date = None
        self._coupon_period = None
        self._coupon_rate = None
        self._pay_per_bond = None
        self._offer_date = None
        self._buy_back_price = None
        self._current_facevalue = None
        self._accrued_interest = None
        self._listing_level = None
        self._sum_coupons_mty = None
        self._sum_coupons_offer = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if coupon_date is not None:
            self.coupon_date = coupon_date
        if coupon_period is not None:
            self.coupon_period = coupon_period
        if coupon_rate is not None:
            self.coupon_rate = coupon_rate
        if pay_per_bond is not None:
            self.pay_per_bond = pay_per_bond
        if offer_date is not None:
            self.offer_date = offer_date
        if buy_back_price is not None:
            self.buy_back_price = buy_back_price
        if current_facevalue is not None:
            self.current_facevalue = current_facevalue
        if accrued_interest is not None:
            self.accrued_interest = accrued_interest
        if listing_level is not None:
            self.listing_level = listing_level
        if sum_coupons_mty is not None:
            self.sum_coupons_mty = sum_coupons_mty
        if sum_coupons_offer is not None:
            self.sum_coupons_offer = sum_coupons_offer

    @property
    def error(self):
        """Gets the error of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Текст ошибки при обработке запроса  # noqa: E501

        :return: The error of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Текст ошибки при обработке запроса  # noqa: E501

        :param error: The error of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def coupon_date(self):
        """Gets the coupon_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Дата текущего купона  # noqa: E501

        :return: The coupon_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._coupon_date

    @coupon_date.setter
    def coupon_date(self, coupon_date):
        """Sets the coupon_date of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Дата текущего купона  # noqa: E501

        :param coupon_date: The coupon_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: datetime
        """

        self._coupon_date = coupon_date

    @property
    def coupon_period(self):
        """Gets the coupon_period of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Купонный период  # noqa: E501

        :return: The coupon_period of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._coupon_period

    @coupon_period.setter
    def coupon_period(self, coupon_period):
        """Sets the coupon_period of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Купонный период  # noqa: E501

        :param coupon_period: The coupon_period of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: int
        """

        self._coupon_period = coupon_period

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Ставка текущего купона  # noqa: E501

        :return: The coupon_rate of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Ставка текущего купона  # noqa: E501

        :param coupon_rate: The coupon_rate of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._coupon_rate = coupon_rate

    @property
    def pay_per_bond(self):
        """Gets the pay_per_bond of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Выплата на облигацию  # noqa: E501

        :return: The pay_per_bond of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._pay_per_bond

    @pay_per_bond.setter
    def pay_per_bond(self, pay_per_bond):
        """Sets the pay_per_bond of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Выплата на облигацию  # noqa: E501

        :param pay_per_bond: The pay_per_bond of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._pay_per_bond = pay_per_bond

    @property
    def offer_date(self):
        """Gets the offer_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Дата ближайшей оферты  # noqa: E501

        :return: The offer_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._offer_date

    @offer_date.setter
    def offer_date(self, offer_date):
        """Sets the offer_date of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Дата ближайшей оферты  # noqa: E501

        :param offer_date: The offer_date of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: datetime
        """

        self._offer_date = offer_date

    @property
    def buy_back_price(self):
        """Gets the buy_back_price of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Цена выкупа  # noqa: E501

        :return: The buy_back_price of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._buy_back_price

    @buy_back_price.setter
    def buy_back_price(self, buy_back_price):
        """Sets the buy_back_price of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Цена выкупа  # noqa: E501

        :param buy_back_price: The buy_back_price of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._buy_back_price = buy_back_price

    @property
    def current_facevalue(self):
        """Gets the current_facevalue of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Текущий номинал  # noqa: E501

        :return: The current_facevalue of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._current_facevalue

    @current_facevalue.setter
    def current_facevalue(self, current_facevalue):
        """Sets the current_facevalue of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Текущий номинал  # noqa: E501

        :param current_facevalue: The current_facevalue of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._current_facevalue = current_facevalue

    @property
    def accrued_interest(self):
        """Gets the accrued_interest of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        НКД  # noqa: E501

        :return: The accrued_interest of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._accrued_interest

    @accrued_interest.setter
    def accrued_interest(self, accrued_interest):
        """Sets the accrued_interest of this EfirDataHubModelsModelsBondDateOptionsResponse.

        НКД  # noqa: E501

        :param accrued_interest: The accrued_interest of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._accrued_interest = accrued_interest

    @property
    def listing_level(self):
        """Gets the listing_level of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Листинг  # noqa: E501

        :return: The listing_level of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: int
        """
        return self._listing_level

    @listing_level.setter
    def listing_level(self, listing_level):
        """Sets the listing_level of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Листинг  # noqa: E501

        :param listing_level: The listing_level of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: int
        """

        self._listing_level = listing_level

    @property
    def sum_coupons_mty(self):
        """Gets the sum_coupons_mty of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Сумма купонов до погашения  # noqa: E501

        :return: The sum_coupons_mty of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._sum_coupons_mty

    @sum_coupons_mty.setter
    def sum_coupons_mty(self, sum_coupons_mty):
        """Sets the sum_coupons_mty of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Сумма купонов до погашения  # noqa: E501

        :param sum_coupons_mty: The sum_coupons_mty of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._sum_coupons_mty = sum_coupons_mty

    @property
    def sum_coupons_offer(self):
        """Gets the sum_coupons_offer of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501

        Сумма купонов до ближайшей оферты  # noqa: E501

        :return: The sum_coupons_offer of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._sum_coupons_offer

    @sum_coupons_offer.setter
    def sum_coupons_offer(self, sum_coupons_offer):
        """Sets the sum_coupons_offer of this EfirDataHubModelsModelsBondDateOptionsResponse.

        Сумма купонов до ближайшей оферты  # noqa: E501

        :param sum_coupons_offer: The sum_coupons_offer of this EfirDataHubModelsModelsBondDateOptionsResponse.  # noqa: E501
        :type: float
        """

        self._sum_coupons_offer = sum_coupons_offer

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
        if issubclass(EfirDataHubModelsModelsBondDateOptionsResponse, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondDateOptionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
