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

class EfirDataHubModelsModelsRiskPfiParamsResponse(object):
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
        'isin_base': 'str',
        'currency_code': 'str',
        'lot_size': 'int',
        'expiration_date': 'str',
        'expiration_date_dt': 'datetime',
        'currency_rate': 'float',
        'price': 'float',
        'point': 'float',
        'error': 'str',
        'nominal': 'float',
        'market_price': 'float',
        'accrued_interest': 'float',
        'delivery_ai': 'float',
        'conversion_factor': 'float',
        'instrument_type': 'int',
        'isin_base_rate': 'float',
        'rate_period': 'str',
        'quotation_price': 'float',
        'basic_asset_code': 'str',
        'risk_type': 'str'
    }

    attribute_map = {
        'isin_base': 'isinBase',
        'currency_code': 'currencyCode',
        'lot_size': 'lotSize',
        'expiration_date': 'expirationDate',
        'expiration_date_dt': 'expirationDateDt',
        'currency_rate': 'currencyRate',
        'price': 'price',
        'point': 'point',
        'error': 'error',
        'nominal': 'nominal',
        'market_price': 'marketPrice',
        'accrued_interest': 'accruedInterest',
        'delivery_ai': 'deliveryAi',
        'conversion_factor': 'conversionFactor',
        'instrument_type': 'instrumentType',
        'isin_base_rate': 'isinBaseRate',
        'rate_period': 'ratePeriod',
        'quotation_price': 'quotationPrice',
        'basic_asset_code': 'basicAssetCode',
        'risk_type': 'riskType'
    }

    def __init__(self, isin_base=None, currency_code=None, lot_size=None, expiration_date=None, expiration_date_dt=None, currency_rate=None, price=None, point=None, error=None, nominal=None, market_price=None, accrued_interest=None, delivery_ai=None, conversion_factor=None, instrument_type=None, isin_base_rate=None, rate_period=None, quotation_price=None, basic_asset_code=None, risk_type=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskPfiParamsResponse - a model defined in Swagger"""  # noqa: E501
        self._isin_base = None
        self._currency_code = None
        self._lot_size = None
        self._expiration_date = None
        self._expiration_date_dt = None
        self._currency_rate = None
        self._price = None
        self._point = None
        self._error = None
        self._nominal = None
        self._market_price = None
        self._accrued_interest = None
        self._delivery_ai = None
        self._conversion_factor = None
        self._instrument_type = None
        self._isin_base_rate = None
        self._rate_period = None
        self._quotation_price = None
        self._basic_asset_code = None
        self._risk_type = None
        self.discriminator = None
        if isin_base is not None:
            self.isin_base = isin_base
        if currency_code is not None:
            self.currency_code = currency_code
        if lot_size is not None:
            self.lot_size = lot_size
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if expiration_date_dt is not None:
            self.expiration_date_dt = expiration_date_dt
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if price is not None:
            self.price = price
        if point is not None:
            self.point = point
        if error is not None:
            self.error = error
        if nominal is not None:
            self.nominal = nominal
        if market_price is not None:
            self.market_price = market_price
        if accrued_interest is not None:
            self.accrued_interest = accrued_interest
        if delivery_ai is not None:
            self.delivery_ai = delivery_ai
        if conversion_factor is not None:
            self.conversion_factor = conversion_factor
        if instrument_type is not None:
            self.instrument_type = instrument_type
        if isin_base_rate is not None:
            self.isin_base_rate = isin_base_rate
        if rate_period is not None:
            self.rate_period = rate_period
        if quotation_price is not None:
            self.quotation_price = quotation_price
        if basic_asset_code is not None:
            self.basic_asset_code = basic_asset_code
        if risk_type is not None:
            self.risk_type = risk_type

    @property
    def isin_base(self):
        """Gets the isin_base of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        ISIN базового актива  # noqa: E501

        :return: The isin_base of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._isin_base

    @isin_base.setter
    def isin_base(self, isin_base):
        """Sets the isin_base of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        ISIN базового актива  # noqa: E501

        :param isin_base: The isin_base of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._isin_base = isin_base

    @property
    def currency_code(self):
        """Gets the currency_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Трехбуквенный код валюты  # noqa: E501

        :return: The currency_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Трехбуквенный код валюты  # noqa: E501

        :param currency_code: The currency_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def lot_size(self):
        """Gets the lot_size of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Размер лота  # noqa: E501

        :return: The lot_size of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Размер лота  # noqa: E501

        :param lot_size: The lot_size of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def expiration_date(self):
        """Gets the expiration_date of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Дата экспирации типа String  # noqa: E501

        :return: The expiration_date of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Дата экспирации типа String  # noqa: E501

        :param expiration_date: The expiration_date of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def expiration_date_dt(self):
        """Gets the expiration_date_dt of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Дата экспирации типа DateTime  # noqa: E501

        :return: The expiration_date_dt of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_dt

    @expiration_date_dt.setter
    def expiration_date_dt(self, expiration_date_dt):
        """Sets the expiration_date_dt of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Дата экспирации типа DateTime  # noqa: E501

        :param expiration_date_dt: The expiration_date_dt of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_dt = expiration_date_dt

    @property
    def currency_rate(self):
        """Gets the currency_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Курс валюты к рублю  # noqa: E501

        :return: The currency_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Курс валюты к рублю  # noqa: E501

        :param currency_rate: The currency_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def price(self):
        """Gets the price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Цена базового актива  # noqa: E501

        :return: The price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Цена базового актива  # noqa: E501

        :param price: The price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def point(self):
        """Gets the point of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Стоимость одного пункта цены контракта в валюте контракта  # noqa: E501

        :return: The point of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Стоимость одного пункта цены контракта в валюте контракта  # noqa: E501

        :param point: The point of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._point = point

    @property
    def error(self):
        """Gets the error of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Текст ошибки, если она есть  # noqa: E501

        :return: The error of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Текст ошибки, если она есть  # noqa: E501

        :param error: The error of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def nominal(self):
        """Gets the nominal of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Номинал ПФИ  # noqa: E501

        :return: The nominal of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._nominal

    @nominal.setter
    def nominal(self, nominal):
        """Sets the nominal of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Номинал ПФИ  # noqa: E501

        :param nominal: The nominal of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._nominal = nominal

    @property
    def market_price(self):
        """Gets the market_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Рыночная цена  # noqa: E501

        :return: The market_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._market_price

    @market_price.setter
    def market_price(self, market_price):
        """Sets the market_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Рыночная цена  # noqa: E501

        :param market_price: The market_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._market_price = market_price

    @property
    def accrued_interest(self):
        """Gets the accrued_interest of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        НКД облигации, наилучшей к поставке на дату расчета в процентах от номинала.  # noqa: E501

        :return: The accrued_interest of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._accrued_interest

    @accrued_interest.setter
    def accrued_interest(self, accrued_interest):
        """Sets the accrued_interest of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        НКД облигации, наилучшей к поставке на дату расчета в процентах от номинала.  # noqa: E501

        :param accrued_interest: The accrued_interest of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._accrued_interest = accrued_interest

    @property
    def delivery_ai(self):
        """Gets the delivery_ai of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        НКД облигации, наилучшей к поставке на дату экспирации фьючерса.Процент от номинала бонда в процентах от номинала.  # noqa: E501

        :return: The delivery_ai of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._delivery_ai

    @delivery_ai.setter
    def delivery_ai(self, delivery_ai):
        """Sets the delivery_ai of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        НКД облигации, наилучшей к поставке на дату экспирации фьючерса.Процент от номинала бонда в процентах от номинала.  # noqa: E501

        :param delivery_ai: The delivery_ai of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._delivery_ai = delivery_ai

    @property
    def conversion_factor(self):
        """Gets the conversion_factor of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Конверсионный коэффициент облигации, наилучшей к поставке.  # noqa: E501

        :return: The conversion_factor of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, conversion_factor):
        """Sets the conversion_factor of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Конверсионный коэффициент облигации, наилучшей к поставке.  # noqa: E501

        :param conversion_factor: The conversion_factor of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._conversion_factor = conversion_factor

    @property
    def instrument_type(self):
        """Gets the instrument_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Тип ПФИ:  0 – фьючерс на акции или индекс  1 – фьючерс на корзину облигаций  2 – товарный контракт  3 – валютный контракт  4 – фьючерс на процентную ставку  # noqa: E501

        :return: The instrument_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: int
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Тип ПФИ:  0 – фьючерс на акции или индекс  1 – фьючерс на корзину облигаций  2 – товарный контракт  3 – валютный контракт  4 – фьючерс на процентную ставку  # noqa: E501

        :param instrument_type: The instrument_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: int
        """

        self._instrument_type = instrument_type

    @property
    def isin_base_rate(self):
        """Gets the isin_base_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Курс базового актива для валютных контрактов  # noqa: E501

        :return: The isin_base_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._isin_base_rate

    @isin_base_rate.setter
    def isin_base_rate(self, isin_base_rate):
        """Sets the isin_base_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Курс базового актива для валютных контрактов  # noqa: E501

        :param isin_base_rate: The isin_base_rate of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._isin_base_rate = isin_base_rate

    @property
    def rate_period(self):
        """Gets the rate_period of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Дата для фьючерсов на процентную ставку  # noqa: E501

        :return: The rate_period of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._rate_period

    @rate_period.setter
    def rate_period(self, rate_period):
        """Sets the rate_period of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Дата для фьючерсов на процентную ставку  # noqa: E501

        :param rate_period: The rate_period of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._rate_period = rate_period

    @property
    def quotation_price(self):
        """Gets the quotation_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Котировка ПФИ  # noqa: E501

        :return: The quotation_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: float
        """
        return self._quotation_price

    @quotation_price.setter
    def quotation_price(self, quotation_price):
        """Sets the quotation_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Котировка ПФИ  # noqa: E501

        :param quotation_price: The quotation_price of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: float
        """

        self._quotation_price = quotation_price

    @property
    def basic_asset_code(self):
        """Gets the basic_asset_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Код базового актива  # noqa: E501

        :return: The basic_asset_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._basic_asset_code

    @basic_asset_code.setter
    def basic_asset_code(self, basic_asset_code):
        """Sets the basic_asset_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Код базового актива  # noqa: E501

        :param basic_asset_code: The basic_asset_code of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._basic_asset_code = basic_asset_code

    @property
    def risk_type(self):
        """Gets the risk_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501

        Тип риска  # noqa: E501

        :return: The risk_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.

        Тип риска  # noqa: E501

        :param risk_type: The risk_type of this EfirDataHubModelsModelsRiskPfiParamsResponse.  # noqa: E501
        :type: str
        """

        self._risk_type = risk_type

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
        if issubclass(EfirDataHubModelsModelsRiskPfiParamsResponse, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskPfiParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
