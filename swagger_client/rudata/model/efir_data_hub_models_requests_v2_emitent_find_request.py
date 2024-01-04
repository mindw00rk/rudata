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

class EfirDataHubModelsRequestsV2EmitentFindRequest(object):
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
        'codes': 'list[str]'
    }

    attribute_map = {
        'codes': 'codes'
    }

    def __init__(self, codes=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2EmitentFindRequest - a model defined in Swagger"""  # noqa: E501
        self._codes = None
        self.discriminator = None
        self.codes = codes

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2EmitentFindRequest.  # noqa: E501

        FininstId, ИНН, ОГРН, ShortName  Максимум 1000 элементов.  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2EmitentFindRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2EmitentFindRequest.

        FininstId, ИНН, ОГРН, ShortName  Максимум 1000 элементов.  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2EmitentFindRequest.  # noqa: E501
        :type: list[str]
        """
        if codes is None:
            raise ValueError("Invalid value for `codes`, must not be `None`")  # noqa: E501

        self._codes = codes

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
        if issubclass(EfirDataHubModelsRequestsV2EmitentFindRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2EmitentFindRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
