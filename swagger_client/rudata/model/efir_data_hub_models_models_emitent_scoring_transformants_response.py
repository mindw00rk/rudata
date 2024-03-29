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

class EfirDataHubModelsModelsEmitentScoringTransformantsResponse(object):
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
        'source': 'str',
        'coeff_name_eng': 'str',
        'date_actual': 'datetime',
        'transformants': 'list[EfirDataHubModelsModelsEmitentScoringTransformant]'
    }

    attribute_map = {
        'source': 'source',
        'coeff_name_eng': 'coeff_name_eng',
        'date_actual': 'date_actual',
        'transformants': 'transformants'
    }

    def __init__(self, source=None, coeff_name_eng=None, date_actual=None, transformants=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentScoringTransformantsResponse - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._coeff_name_eng = None
        self._date_actual = None
        self._transformants = None
        self.discriminator = None
        if source is not None:
            self.source = source
        if coeff_name_eng is not None:
            self.coeff_name_eng = coeff_name_eng
        if date_actual is not None:
            self.date_actual = date_actual
        if transformants is not None:
            self.transformants = transformants

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501

        Тип отчетности  # noqa: E501

        :return: The source of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.

        Тип отчетности  # noqa: E501

        :param source: The source of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def coeff_name_eng(self):
        """Gets the coeff_name_eng of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501

        Англоязычное наименование коэффициента скоринговой модели  # noqa: E501

        :return: The coeff_name_eng of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :rtype: str
        """
        return self._coeff_name_eng

    @coeff_name_eng.setter
    def coeff_name_eng(self, coeff_name_eng):
        """Sets the coeff_name_eng of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.

        Англоязычное наименование коэффициента скоринговой модели  # noqa: E501

        :param coeff_name_eng: The coeff_name_eng of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :type: str
        """

        self._coeff_name_eng = coeff_name_eng

    @property
    def date_actual(self):
        """Gets the date_actual of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501

        Дата актуализации  # noqa: E501

        :return: The date_actual of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._date_actual

    @date_actual.setter
    def date_actual(self, date_actual):
        """Sets the date_actual of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.

        Дата актуализации  # noqa: E501

        :param date_actual: The date_actual of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :type: datetime
        """

        self._date_actual = date_actual

    @property
    def transformants(self):
        """Gets the transformants of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501

        Массив трансформант  # noqa: E501

        :return: The transformants of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsEmitentScoringTransformant]
        """
        return self._transformants

    @transformants.setter
    def transformants(self, transformants):
        """Sets the transformants of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.

        Массив трансформант  # noqa: E501

        :param transformants: The transformants of this EfirDataHubModelsModelsEmitentScoringTransformantsResponse.  # noqa: E501
        :type: list[EfirDataHubModelsModelsEmitentScoringTransformant]
        """

        self._transformants = transformants

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
        if issubclass(EfirDataHubModelsModelsEmitentScoringTransformantsResponse, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentScoringTransformantsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
