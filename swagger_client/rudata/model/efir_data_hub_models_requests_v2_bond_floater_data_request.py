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

class EfirDataHubModelsRequestsV2BondFloaterDataRequest(object):
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
        '_date': 'datetime',
        'show_future_periods': 'bool'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        '_date': 'date',
        'show_future_periods': 'showFuturePeriods'
    }

    def __init__(self, fintool_ids=None, _date=None, show_future_periods=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2BondFloaterDataRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self.__date = None
        self._show_future_periods = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if _date is not None:
            self._date = _date
        if show_future_periods is not None:
            self.show_future_periods = show_future_periods

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501

        Числовые идентификаторы в базе Интерфакс. Обязательный параметр;   Максимальное количество элементов: 100  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.

        Числовые идентификаторы в базе Интерфакс. Обязательный параметр;   Максимальное количество элементов: 100  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501

        Дата, на которую актуально описание правила расчета флоатера  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.

        Дата, на которую актуально описание правила расчета флоатера  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def show_future_periods(self):
        """Gets the show_future_periods of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501

        Показывать правила для последующих периодов  # noqa: E501

        :return: The show_future_periods of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_future_periods

    @show_future_periods.setter
    def show_future_periods(self, show_future_periods):
        """Sets the show_future_periods of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.

        Показывать правила для последующих периодов  # noqa: E501

        :param show_future_periods: The show_future_periods of this EfirDataHubModelsRequestsV2BondFloaterDataRequest.  # noqa: E501
        :type: bool
        """

        self._show_future_periods = show_future_periods

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
        if issubclass(EfirDataHubModelsRequestsV2BondFloaterDataRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2BondFloaterDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
