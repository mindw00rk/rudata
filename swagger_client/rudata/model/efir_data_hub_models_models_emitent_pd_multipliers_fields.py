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

class EfirDataHubModelsModelsEmitentPDMultipliersFields(object):
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
        'rt_num': 'int',
        'years': 'int',
        'multiplier': 'float'
    }

    attribute_map = {
        'rt_num': 'rt_num',
        'years': 'years',
        'multiplier': 'multiplier'
    }

    def __init__(self, rt_num=None, years=None, multiplier=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentPDMultipliersFields - a model defined in Swagger"""  # noqa: E501
        self._rt_num = None
        self._years = None
        self._multiplier = None
        self.discriminator = None
        if rt_num is not None:
            self.rt_num = rt_num
        if years is not None:
            self.years = years
        if multiplier is not None:
            self.multiplier = multiplier

    @property
    def rt_num(self):
        """Gets the rt_num of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501

        Порядковый номер значения по рейтинговой шкале,  # noqa: E501

        :return: The rt_num of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :rtype: int
        """
        return self._rt_num

    @rt_num.setter
    def rt_num(self, rt_num):
        """Sets the rt_num of this EfirDataHubModelsModelsEmitentPDMultipliersFields.

        Порядковый номер значения по рейтинговой шкале,  # noqa: E501

        :param rt_num: The rt_num of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :type: int
        """

        self._rt_num = rt_num

    @property
    def years(self):
        """Gets the years of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501

        Горизонт выдачи прогнозных мультипликаторов, лет  # noqa: E501

        :return: The years of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :rtype: int
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this EfirDataHubModelsModelsEmitentPDMultipliersFields.

        Горизонт выдачи прогнозных мультипликаторов, лет  # noqa: E501

        :param years: The years of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :type: int
        """

        self._years = years

    @property
    def multiplier(self):
        """Gets the multiplier of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501

        Мультипликатор расчета pd  # noqa: E501

        :return: The multiplier of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this EfirDataHubModelsModelsEmitentPDMultipliersFields.

        Мультипликатор расчета pd  # noqa: E501

        :param multiplier: The multiplier of this EfirDataHubModelsModelsEmitentPDMultipliersFields.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

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
        if issubclass(EfirDataHubModelsModelsEmitentPDMultipliersFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentPDMultipliersFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other