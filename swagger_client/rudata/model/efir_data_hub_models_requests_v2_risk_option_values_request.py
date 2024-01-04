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

class EfirDataHubModelsRequestsV2RiskOptionValuesRequest(object):
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
        'id': 'str',
        '_date': 'datetime',
        'fields': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        '_date': 'date',
        'fields': 'fields'
    }

    def __init__(self, id=None, _date=None, fields=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RiskOptionValuesRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__date = None
        self._fields = None
        self.discriminator = None
        self.id = id
        self._date = _date
        if fields is not None:
            self.fields = fields

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501

        Идентификатор опциона (торговый код)  # noqa: E501

        :return: The id of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.

        Идентификатор опциона (торговый код)  # noqa: E501

        :param id: The id of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501

        Дата расчета  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.

        Дата расчета  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def fields(self):
        """Gets the fields of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501

        Список полей  # noqa: E501

        :return: The fields of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.

        Список полей  # noqa: E501

        :param fields: The fields of this EfirDataHubModelsRequestsV2RiskOptionValuesRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

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
        if issubclass(EfirDataHubModelsRequestsV2RiskOptionValuesRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RiskOptionValuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other