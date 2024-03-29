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

class EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest(object):
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
        'actual_on_date': 'datetime',
        'trade_date_start': 'datetime',
        'trade_date_end': 'datetime',
        'trade_group_code': 'int',
        'use_filters': 'bool',
        'use_restored_volumes': 'bool'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        'codes': 'codes',
        'actual_on_date': 'actualOnDate',
        'trade_date_start': 'tradeDateStart',
        'trade_date_end': 'tradeDateEnd',
        'trade_group_code': 'tradeGroupCode',
        'use_filters': 'useFilters',
        'use_restored_volumes': 'useRestoredVolumes'
    }

    def __init__(self, fintool_ids=None, codes=None, actual_on_date=None, trade_date_start=None, trade_date_end=None, trade_group_code=None, use_filters=None, use_restored_volumes=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self._codes = None
        self._actual_on_date = None
        self._trade_date_start = None
        self._trade_date_end = None
        self._trade_group_code = None
        self._use_filters = None
        self._use_restored_volumes = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if codes is not None:
            self.codes = codes
        if actual_on_date is not None:
            self.actual_on_date = actual_on_date
        self.trade_date_start = trade_date_start
        if trade_date_end is not None:
            self.trade_date_end = trade_date_end
        if trade_group_code is not None:
            self.trade_group_code = trade_group_code
        if use_filters is not None:
            self.use_filters = use_filters
        if use_restored_volumes is not None:
            self.use_restored_volumes = use_restored_volumes

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 100  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 100  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode);  Максимальное количество элементов: 100  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode);  Максимальное количество элементов: 100  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def actual_on_date(self):
        """Gets the actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Дата расчета  # noqa: E501

        :return: The actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_on_date

    @actual_on_date.setter
    def actual_on_date(self, actual_on_date):
        """Sets the actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Дата расчета  # noqa: E501

        :param actual_on_date: The actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_on_date = actual_on_date

    @property
    def trade_date_start(self):
        """Gets the trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Дата начала отрезка отбора фильтров  # noqa: E501

        :return: The trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._trade_date_start

    @trade_date_start.setter
    def trade_date_start(self, trade_date_start):
        """Sets the trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Дата начала отрезка отбора фильтров  # noqa: E501

        :param trade_date_start: The trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: datetime
        """
        if trade_date_start is None:
            raise ValueError("Invalid value for `trade_date_start`, must not be `None`")  # noqa: E501

        self._trade_date_start = trade_date_start

    @property
    def trade_date_end(self):
        """Gets the trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Дата окончания отрезка отбора фильтров  # noqa: E501

        :return: The trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._trade_date_end

    @trade_date_end.setter
    def trade_date_end(self, trade_date_end):
        """Sets the trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Дата окончания отрезка отбора фильтров  # noqa: E501

        :param trade_date_end: The trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: datetime
        """

        self._trade_date_end = trade_date_end

    @property
    def trade_group_code(self):
        """Gets the trade_group_code of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Код групп сделок для формирования статистик:  1 - Биржевые сделки (основной режим)  12 - Биржевые сделки (основной и прочие режимы)  3 - Внебиржевые сделки  123 - Биржевые и небиржевые сделки   1234 - Биржевые, небиржевые и пока неопределенные сделки  # noqa: E501

        :return: The trade_group_code of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: int
        """
        return self._trade_group_code

    @trade_group_code.setter
    def trade_group_code(self, trade_group_code):
        """Sets the trade_group_code of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Код групп сделок для формирования статистик:  1 - Биржевые сделки (основной режим)  12 - Биржевые сделки (основной и прочие режимы)  3 - Внебиржевые сделки  123 - Биржевые и небиржевые сделки   1234 - Биржевые, небиржевые и пока неопределенные сделки  # noqa: E501

        :param trade_group_code: The trade_group_code of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: int
        """

        self._trade_group_code = trade_group_code

    @property
    def use_filters(self):
        """Gets the use_filters of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Использовать фильтры для исключения ценовых 'выбросов'  # noqa: E501

        :return: The use_filters of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_filters

    @use_filters.setter
    def use_filters(self, use_filters):
        """Sets the use_filters of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Использовать фильтры для исключения ценовых 'выбросов'  # noqa: E501

        :param use_filters: The use_filters of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: bool
        """

        self._use_filters = use_filters

    @property
    def use_restored_volumes(self):
        """Gets the use_restored_volumes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501

        Включать сделки с восстановленными объемами. По-умолчанию - true  # noqa: E501

        :return: The use_restored_volumes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_restored_volumes

    @use_restored_volumes.setter
    def use_restored_volumes(self, use_restored_volumes):
        """Sets the use_restored_volumes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.

        Включать сделки с восстановленными объемами. По-умолчанию - true  # noqa: E501

        :param use_restored_volumes: The use_restored_volumes of this EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest.  # noqa: E501
        :type: bool
        """

        self._use_restored_volumes = use_restored_volumes

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
        if issubclass(EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
