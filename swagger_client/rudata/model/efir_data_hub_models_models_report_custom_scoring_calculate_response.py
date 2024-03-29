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

class EfirDataHubModelsModelsReportCustomScoringCalculateResponse(object):
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
        'calculation_id': 'str'
    }

    attribute_map = {
        'calculation_id': 'calculation_id'
    }

    def __init__(self, calculation_id=None):  # noqa: E501
        """EfirDataHubModelsModelsReportCustomScoringCalculateResponse - a model defined in Swagger"""  # noqa: E501
        self._calculation_id = None
        self.discriminator = None
        if calculation_id is not None:
            self.calculation_id = calculation_id

    @property
    def calculation_id(self):
        """Gets the calculation_id of this EfirDataHubModelsModelsReportCustomScoringCalculateResponse.  # noqa: E501

        GUID расчета  # noqa: E501

        :return: The calculation_id of this EfirDataHubModelsModelsReportCustomScoringCalculateResponse.  # noqa: E501
        :rtype: str
        """
        return self._calculation_id

    @calculation_id.setter
    def calculation_id(self, calculation_id):
        """Sets the calculation_id of this EfirDataHubModelsModelsReportCustomScoringCalculateResponse.

        GUID расчета  # noqa: E501

        :param calculation_id: The calculation_id of this EfirDataHubModelsModelsReportCustomScoringCalculateResponse.  # noqa: E501
        :type: str
        """

        self._calculation_id = calculation_id

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
        if issubclass(EfirDataHubModelsModelsReportCustomScoringCalculateResponse, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsReportCustomScoringCalculateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
