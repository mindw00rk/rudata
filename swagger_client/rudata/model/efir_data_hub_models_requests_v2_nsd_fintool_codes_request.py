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

class EfirDataHubModelsRequestsV2NsdFintoolCodesRequest(object):
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
        'filter': 'str',
        'count': 'int'
    }

    attribute_map = {
        'filter': 'filter',
        'count': 'count'
    }

    def __init__(self, filter=None, count=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2NsdFintoolCodesRequest - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._count = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if count is not None:
            self.count = count

    @property
    def filter(self):
        """Gets the filter of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501

        Строка фильтрации. (необязательный)  # noqa: E501

        :return: The filter of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.

        Строка фильтрации. (необязательный)  # noqa: E501

        :param filter: The filter of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def count(self):
        """Gets the count of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501

        Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000.  # noqa: E501

        :return: The count of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.

        Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000.  # noqa: E501

        :param count: The count of this EfirDataHubModelsRequestsV2NsdFintoolCodesRequest.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(EfirDataHubModelsRequestsV2NsdFintoolCodesRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2NsdFintoolCodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
