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

class EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest(object):
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
        'fintool_ids': 'list[int]',
        'codes': 'list[str]',
        '_date': 'datetime',
        'position_open_date': 'datetime',
        'use_frozen_dates': 'bool',
        'covered_by646_p': 'bool',
        'reorg_part': 'bool',
        'has_market_risk511_p': 'bool',
        'has_risk647_p': 'bool',
        'non2732u_depos': 'bool',
        'not_derecognized_securities': 'bool',
        'funding': 'bool'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        'codes': 'codes',
        '_date': 'date',
        'position_open_date': 'positionOpenDate',
        'use_frozen_dates': 'useFrozenDates',
        'covered_by646_p': 'coveredBy646P',
        'reorg_part': 'reorgPart',
        'has_market_risk511_p': 'hasMarketRisk511P',
        'has_risk647_p': 'hasRisk647P',
        'non2732u_depos': 'non2732uDepos',
        'not_derecognized_securities': 'notDerecognizedSecurities',
        'funding': 'funding'
    }

    def __init__(self, fintool_ids=None, codes=None, _date=None, position_open_date=None, use_frozen_dates=None, covered_by646_p=False, reorg_part=False, has_market_risk511_p=False, has_risk647_p=False, non2732u_depos=False, not_derecognized_securities=False, funding=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self._codes = None
        self.__date = None
        self._position_open_date = None
        self._use_frozen_dates = None
        self._covered_by646_p = None
        self._reorg_part = None
        self._has_market_risk511_p = None
        self._has_risk647_p = None
        self._non2732u_depos = None
        self._not_derecognized_securities = None
        self._funding = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if codes is not None:
            self.codes = codes
        if _date is not None:
            self._date = _date
        if position_open_date is not None:
            self.position_open_date = position_open_date
        if use_frozen_dates is not None:
            self.use_frozen_dates = use_frozen_dates
        if covered_by646_p is not None:
            self.covered_by646_p = covered_by646_p
        if reorg_part is not None:
            self.reorg_part = reorg_part
        if has_market_risk511_p is not None:
            self.has_market_risk511_p = has_market_risk511_p
        if has_risk647_p is not None:
            self.has_risk647_p = has_risk647_p
        if non2732u_depos is not None:
            self.non2732u_depos = non2732u_depos
        if not_derecognized_securities is not None:
            self.not_derecognized_securities = not_derecognized_securities
        if funding is not None:
            self.funding = funding

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Массив идентификаторов финансовых инструментов в БД Интерфакс, не более 20 значений.  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Массив идентификаторов финансовых инструментов в БД Интерфакс, не более 20 значений.  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Массив кодов инструментов - (ISIN). Используется, если не задан fintoolIds. Не более 20 значений.  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Массив кодов инструментов - (ISIN). Используется, если не задан fintoolIds. Не более 20 значений.  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Дата расчета норматива. Необязательная. Если не задана, то принимается как текущая.  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Дата расчета норматива. Необязательная. Если не задана, то принимается как текущая.  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def position_open_date(self):
        """Gets the position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Дата открытия (покупки) позиции. Необязательная. Если не задана, то принимается как текущая.  # noqa: E501

        :return: The position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """Sets the position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Дата открытия (покупки) позиции. Необязательная. Если не задана, то принимается как текущая.  # noqa: E501

        :param position_open_date: The position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: datetime
        """

        self._position_open_date = position_open_date

    @property
    def use_frozen_dates(self):
        """Gets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Использовать даты заморозки рейтингов. Необязательный. Если не задан, то принимается как true.  # noqa: E501

        :return: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_frozen_dates

    @use_frozen_dates.setter
    def use_frozen_dates(self, use_frozen_dates):
        """Sets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Использовать даты заморозки рейтингов. Необязательный. Если не задан, то принимается как true.  # noqa: E501

        :param use_frozen_dates: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._use_frozen_dates = use_frozen_dates

    @property
    def covered_by646_p(self):
        """Gets the covered_by646_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг \"актив уменьшает капитал в целях 646-П\" (актив уменьшает сумму источников базового капитала, добавочного капитала,  дополнительного капитала и сумму основного и дополнительного капитала, определенных в соответствии с 646-П).  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :return: The covered_by646_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._covered_by646_p

    @covered_by646_p.setter
    def covered_by646_p(self, covered_by646_p):
        """Sets the covered_by646_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг \"актив уменьшает капитал в целях 646-П\" (актив уменьшает сумму источников базового капитала, добавочного капитала,  дополнительного капитала и сумму основного и дополнительного капитала, определенных в соответствии с 646-П).  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :param covered_by646_p: The covered_by646_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._covered_by646_p = covered_by646_p

    @property
    def reorg_part(self):
        """Gets the reorg_part of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг \"актив является частью мероприятий по финансовому оздоровлению (Банк России или АСВ)\".  Необязательный. Если не задан, то принимается как false  # noqa: E501

        :return: The reorg_part of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reorg_part

    @reorg_part.setter
    def reorg_part(self, reorg_part):
        """Sets the reorg_part of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг \"актив является частью мероприятий по финансовому оздоровлению (Банк России или АСВ)\".  Необязательный. Если не задан, то принимается как false  # noqa: E501

        :param reorg_part: The reorg_part of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._reorg_part = reorg_part

    @property
    def has_market_risk511_p(self):
        """Gets the has_market_risk511_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг «по активу рассчитывается рыночный риск в соответствии с 511-П».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :return: The has_market_risk511_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_market_risk511_p

    @has_market_risk511_p.setter
    def has_market_risk511_p(self, has_market_risk511_p):
        """Sets the has_market_risk511_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг «по активу рассчитывается рыночный риск в соответствии с 511-П».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :param has_market_risk511_p: The has_market_risk511_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._has_market_risk511_p = has_market_risk511_p

    @property
    def has_risk647_p(self):
        """Gets the has_risk647_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг «по активу рассчитывается риск в соответствии с 647-П».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :return: The has_risk647_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._has_risk647_p

    @has_risk647_p.setter
    def has_risk647_p(self, has_risk647_p):
        """Sets the has_risk647_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг «по активу рассчитывается риск в соответствии с 647-П».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :param has_risk647_p: The has_risk647_p of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._has_risk647_p = has_risk647_p

    @property
    def non2732u_depos(self):
        """Gets the non2732u_depos of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг «депозитарий, удостоверяющий активы, не удовлетворяет условиям 2732-У».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :return: The non2732u_depos of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._non2732u_depos

    @non2732u_depos.setter
    def non2732u_depos(self, non2732u_depos):
        """Sets the non2732u_depos of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг «депозитарий, удостоверяющий активы, не удовлетворяет условиям 2732-У».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :param non2732u_depos: The non2732u_depos of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._non2732u_depos = non2732u_depos

    @property
    def not_derecognized_securities(self):
        """Gets the not_derecognized_securities of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг «ценные бумаги, переданные без прекращения признания».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :return: The not_derecognized_securities of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._not_derecognized_securities

    @not_derecognized_securities.setter
    def not_derecognized_securities(self, not_derecognized_securities):
        """Sets the not_derecognized_securities of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг «ценные бумаги, переданные без прекращения признания».  Необязательный. Если не задан, то принимается как false.  # noqa: E501

        :param not_derecognized_securities: The not_derecognized_securities of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._not_derecognized_securities = not_derecognized_securities

    @property
    def funding(self):
        """Gets the funding of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501

        Флаг фондирования в валюте номинала.  Необязательный. Если не задан, то принимается как true.  # noqa: E501

        :return: The funding of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.

        Флаг фондирования в валюте номинала.  Необязательный. Если не задан, то принимается как true.  # noqa: E501

        :param funding: The funding of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest.  # noqa: E501
        :type: bool
        """

        self._funding = funding

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
        if issubclass(EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RiskCapitalAdequacyFinalizedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
