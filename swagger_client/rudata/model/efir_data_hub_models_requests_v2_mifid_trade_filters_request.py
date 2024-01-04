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

class EfirDataHubModelsRequestsV2MifidTradeFiltersRequest(object):
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
        'trade_date_start': 'datetime',
        'trade_date_end': 'datetime',
        'actual_on_date': 'datetime',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        'codes': 'codes',
        'trade_date_start': 'tradeDateStart',
        'trade_date_end': 'tradeDateEnd',
        'actual_on_date': 'actualOnDate',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, fintool_ids=None, codes=None, trade_date_start=None, trade_date_end=None, actual_on_date=None, page_num=None, page_size=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2MifidTradeFiltersRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self._codes = None
        self._trade_date_start = None
        self._trade_date_end = None
        self._actual_on_date = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if codes is not None:
            self.codes = codes
        self.trade_date_start = trade_date_start
        if trade_date_end is not None:
            self.trade_date_end = trade_date_end
        if actual_on_date is not None:
            self.actual_on_date = actual_on_date
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Идентификатор финансового инструмента в базе Интерфакс (не более 100)  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Идентификатор финансового инструмента в базе Интерфакс (не более 100)  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Иные идентификаторы облигации (ISIN, RegCode, NRDCode; не более 100).  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Иные идентификаторы облигации (ISIN, RegCode, NRDCode; не более 100).  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def trade_date_start(self):
        """Gets the trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Дата начала отрезка отбора свойств фильтров  # noqa: E501

        :return: The trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._trade_date_start

    @trade_date_start.setter
    def trade_date_start(self, trade_date_start):
        """Sets the trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Дата начала отрезка отбора свойств фильтров  # noqa: E501

        :param trade_date_start: The trade_date_start of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: datetime
        """
        if trade_date_start is None:
            raise ValueError("Invalid value for `trade_date_start`, must not be `None`")  # noqa: E501

        self._trade_date_start = trade_date_start

    @property
    def trade_date_end(self):
        """Gets the trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Дата окончания отрезка отбора свойств фильтров  # noqa: E501

        :return: The trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._trade_date_end

    @trade_date_end.setter
    def trade_date_end(self, trade_date_end):
        """Sets the trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Дата окончания отрезка отбора свойств фильтров  # noqa: E501

        :param trade_date_end: The trade_date_end of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: datetime
        """

        self._trade_date_end = trade_date_end

    @property
    def actual_on_date(self):
        """Gets the actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Дата расчета (по умолчанию - текущая)  # noqa: E501

        :return: The actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_on_date

    @actual_on_date.setter
    def actual_on_date(self, actual_on_date):
        """Sets the actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Дата расчета (по умолчанию - текущая)  # noqa: E501

        :param actual_on_date: The actual_on_date of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_on_date = actual_on_date

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2MifidTradeFiltersRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(EfirDataHubModelsRequestsV2MifidTradeFiltersRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2MifidTradeFiltersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
