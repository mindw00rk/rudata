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

class EfirDataHubModelsModelsRiskFintoolsRiskGroupParams(object):
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
        'fintool_id': 'int',
        'params': 'list[EfirDataHubModelsModelsRiskFintoolsRiskGroupParamsFields]',
        'error': 'str'
    }

    attribute_map = {
        'fintool_id': 'fintoolId',
        'params': 'params',
        'error': 'error'
    }

    def __init__(self, fintool_id=None, params=None, error=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskFintoolsRiskGroupParams - a model defined in Swagger"""  # noqa: E501
        self._fintool_id = None
        self._params = None
        self._error = None
        self.discriminator = None
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if params is not None:
            self.params = params
        if error is not None:
            self.error = error

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501

        fintoolId инструмента  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.

        fintoolId инструмента  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def params(self):
        """Gets the params of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501

        Список параметров  # noqa: E501

        :return: The params of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsRiskFintoolsRiskGroupParamsFields]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.

        Список параметров  # noqa: E501

        :param params: The params of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :type: list[EfirDataHubModelsModelsRiskFintoolsRiskGroupParamsFields]
        """

        self._params = params

    @property
    def error(self):
        """Gets the error of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501

        Описание ошибки  # noqa: E501

        :return: The error of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.

        Описание ошибки  # noqa: E501

        :param error: The error of this EfirDataHubModelsModelsRiskFintoolsRiskGroupParams.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(EfirDataHubModelsModelsRiskFintoolsRiskGroupParams, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskFintoolsRiskGroupParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other