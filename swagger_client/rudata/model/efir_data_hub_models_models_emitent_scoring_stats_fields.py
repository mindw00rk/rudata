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

class EfirDataHubModelsModelsEmitentScoringStatsFields(object):
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
        'sector': 'str',
        'source': 'str',
        'actualondate': 'datetime',
        'key_name': 'str',
        'mean': 'float',
        'median': 'float',
        'q1': 'float',
        'q3': 'float',
        'top10': 'float',
        'top90': 'float',
        'max': 'float',
        'min': 'float'
    }

    attribute_map = {
        'sector': 'sector',
        'source': 'source',
        'actualondate': 'actualondate',
        'key_name': 'key_name',
        'mean': 'mean',
        'median': 'median',
        'q1': 'q1',
        'q3': 'q3',
        'top10': 'top10',
        'top90': 'top90',
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, sector=None, source=None, actualondate=None, key_name=None, mean=None, median=None, q1=None, q3=None, top10=None, top90=None, max=None, min=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentScoringStatsFields - a model defined in Swagger"""  # noqa: E501
        self._sector = None
        self._source = None
        self._actualondate = None
        self._key_name = None
        self._mean = None
        self._median = None
        self._q1 = None
        self._q3 = None
        self._top10 = None
        self._top90 = None
        self._max = None
        self._min = None
        self.discriminator = None
        if sector is not None:
            self.sector = sector
        if source is not None:
            self.source = source
        if actualondate is not None:
            self.actualondate = actualondate
        if key_name is not None:
            self.key_name = key_name
        if mean is not None:
            self.mean = mean
        if median is not None:
            self.median = median
        if q1 is not None:
            self.q1 = q1
        if q3 is not None:
            self.q3 = q3
        if top10 is not None:
            self.top10 = top10
        if top90 is not None:
            self.top90 = top90
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def sector(self):
        """Gets the sector of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Наименование сектора рынка  # noqa: E501

        :return: The sector of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Наименование сектора рынка  # noqa: E501

        :param sector: The sector of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Наименование типа отчетности  # noqa: E501

        :return: The source of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Наименование типа отчетности  # noqa: E501

        :param source: The source of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def actualondate(self):
        """Gets the actualondate of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Дата вызова метода  # noqa: E501

        :return: The actualondate of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: datetime
        """
        return self._actualondate

    @actualondate.setter
    def actualondate(self, actualondate):
        """Sets the actualondate of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Дата вызова метода  # noqa: E501

        :param actualondate: The actualondate of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: datetime
        """

        self._actualondate = actualondate

    @property
    def key_name(self):
        """Gets the key_name of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Наименование поля, по которому сформирована статистика  # noqa: E501

        :return: The key_name of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Наименование поля, по которому сформирована статистика  # noqa: E501

        :param key_name: The key_name of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def mean(self):
        """Gets the mean of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Среднее арифметическое значений  # noqa: E501

        :return: The mean of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Среднее арифметическое значений  # noqa: E501

        :param mean: The mean of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def median(self):
        """Gets the median of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Медиана  # noqa: E501

        :return: The median of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        """Sets the median of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Медиана  # noqa: E501

        :param median: The median of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._median = median

    @property
    def q1(self):
        """Gets the q1 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        25 перцентиль  # noqa: E501

        :return: The q1 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._q1

    @q1.setter
    def q1(self, q1):
        """Sets the q1 of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        25 перцентиль  # noqa: E501

        :param q1: The q1 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._q1 = q1

    @property
    def q3(self):
        """Gets the q3 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        75 перцентиль  # noqa: E501

        :return: The q3 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._q3

    @q3.setter
    def q3(self, q3):
        """Sets the q3 of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        75 перцентиль  # noqa: E501

        :param q3: The q3 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._q3 = q3

    @property
    def top10(self):
        """Gets the top10 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        10 перцентиль  # noqa: E501

        :return: The top10 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._top10

    @top10.setter
    def top10(self, top10):
        """Sets the top10 of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        10 перцентиль  # noqa: E501

        :param top10: The top10 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._top10 = top10

    @property
    def top90(self):
        """Gets the top90 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        90 перцентиль  # noqa: E501

        :return: The top90 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._top90

    @top90.setter
    def top90(self, top90):
        """Sets the top90 of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        90 перцентиль  # noqa: E501

        :param top90: The top90 of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._top90 = top90

    @property
    def max(self):
        """Gets the max of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Максимальное значение  # noqa: E501

        :return: The max of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Максимальное значение  # noqa: E501

        :param max: The max of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501

        Минимальное значение  # noqa: E501

        :return: The min of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this EfirDataHubModelsModelsEmitentScoringStatsFields.

        Минимальное значение  # noqa: E501

        :param min: The min of this EfirDataHubModelsModelsEmitentScoringStatsFields.  # noqa: E501
        :type: float
        """

        self._min = min

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
        if issubclass(EfirDataHubModelsModelsEmitentScoringStatsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentScoringStatsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
