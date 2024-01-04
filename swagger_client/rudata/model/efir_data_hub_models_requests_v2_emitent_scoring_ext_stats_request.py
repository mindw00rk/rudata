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

class EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest(object):
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
        'horizon': 'int',
        'sector': 'str',
        'source': 'AllOfEfirDataHubModelsRequestsV2EmitentScoringExtStatsRequestSource',
        'actual_on_date': 'datetime'
    }

    attribute_map = {
        'horizon': 'horizon',
        'sector': 'sector',
        'source': 'source',
        'actual_on_date': 'actualOnDate'
    }

    def __init__(self, horizon=None, sector=None, source=None, actual_on_date=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest - a model defined in Swagger"""  # noqa: E501
        self._horizon = None
        self._sector = None
        self._source = None
        self._actual_on_date = None
        self.discriminator = None
        if horizon is not None:
            self.horizon = horizon
        self.sector = sector
        if source is not None:
            self.source = source
        if actual_on_date is not None:
            self.actual_on_date = actual_on_date

    @property
    def horizon(self):
        """Gets the horizon of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501

        Значение горизонта прогнозирования.  # noqa: E501

        :return: The horizon of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :rtype: int
        """
        return self._horizon

    @horizon.setter
    def horizon(self, horizon):
        """Sets the horizon of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.

        Значение горизонта прогнозирования.  # noqa: E501

        :param horizon: The horizon of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :type: int
        """

        self._horizon = horizon

    @property
    def sector(self):
        """Gets the sector of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501

        Наименование сектора рынка  # noqa: E501

        :return: The sector of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.

        Наименование сектора рынка  # noqa: E501

        :param sector: The sector of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :type: str
        """
        if sector is None:
            raise ValueError("Invalid value for `sector`, must not be `None`")  # noqa: E501

        self._sector = sector

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501

        Код базы расчета (RSBU = 0,IFRS = 1)  0 = RSBU  1 = IFRS  # noqa: E501

        :return: The source of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsRequestsV2EmitentScoringExtStatsRequestSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.

        Код базы расчета (RSBU = 0,IFRS = 1)  0 = RSBU  1 = IFRS  # noqa: E501

        :param source: The source of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :type: AllOfEfirDataHubModelsRequestsV2EmitentScoringExtStatsRequestSource
        """

        self._source = source

    @property
    def actual_on_date(self):
        """Gets the actual_on_date of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501

        Дата вызова, на которую актуальна статистика  # noqa: E501

        :return: The actual_on_date of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_on_date

    @actual_on_date.setter
    def actual_on_date(self, actual_on_date):
        """Sets the actual_on_date of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.

        Дата вызова, на которую актуальна статистика  # noqa: E501

        :param actual_on_date: The actual_on_date of this EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_on_date = actual_on_date

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
        if issubclass(EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2EmitentScoringExtStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
