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

class EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, fintool_ids=None, start_date=None, end_date=None, page_num=1, page_size=100):  # noqa: E501
        """EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self._start_date = None
        self._end_date = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501

        Необязательный параметр. Идентификаторы инструмента в БД Интерфакс.  Если не задан FintoolIds и даты периода, то результат содержит все актуальные индикаторы.  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.

        Необязательный параметр. Идентификаторы инструмента в БД Интерфакс.  Если не задан FintoolIds и даты периода, то результат содержит все актуальные индикаторы.  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def start_date(self):
        """Gets the start_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501

        Необязательный параметр. Дата начала диапазона дат.  # noqa: E501

        :return: The start_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.

        Необязательный параметр. Дата начала диапазона дат.  # noqa: E501

        :param start_date: The start_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501

        Необязательный параметр. Дата окончания диапазона дат.  # noqa: E501

        :return: The end_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.

        Необязательный параметр. Дата окончания диапазона дат.  # noqa: E501

        :param end_date: The end_date of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501

        Номер страницы для выборки. Если не задан или меньше 1, то устанавливается в 1.  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.

        Номер страницы для выборки. Если не задан или меньше 1, то устанавливается в 1.  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501

        Размер страницы выборки. Если не задан или меньше 1, то устанавливается в 1000.  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.

        Размер страницы выборки. Если не задан или меньше 1, то устанавливается в 1000.  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest.  # noqa: E501
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
        if issubclass(EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
