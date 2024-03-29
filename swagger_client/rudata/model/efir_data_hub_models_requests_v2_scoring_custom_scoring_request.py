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

class EfirDataHubModelsRequestsV2ScoringCustomScoringRequest(object):
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
        'calculation_id': 'str',
        'codes': 'list[str]',
        'actual_on_date': 'datetime',
        'source': 'AllOfEfirDataHubModelsRequestsV2ScoringCustomScoringRequestSource'
    }

    attribute_map = {
        'calculation_id': 'calculationId',
        'codes': 'codes',
        'actual_on_date': 'actualOnDate',
        'source': 'source'
    }

    def __init__(self, calculation_id=None, codes=None, actual_on_date=None, source=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2ScoringCustomScoringRequest - a model defined in Swagger"""  # noqa: E501
        self._calculation_id = None
        self._codes = None
        self._actual_on_date = None
        self._source = None
        self.discriminator = None
        if calculation_id is not None:
            self.calculation_id = calculation_id
        if codes is not None:
            self.codes = codes
        if actual_on_date is not None:
            self.actual_on_date = actual_on_date
        if source is not None:
            self.source = source

    @property
    def calculation_id(self):
        """Gets the calculation_id of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501

        Идентификатор запроса на расчет пользовательского скоринга. Необязательный.  # noqa: E501

        :return: The calculation_id of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :rtype: str
        """
        return self._calculation_id

    @calculation_id.setter
    def calculation_id(self, calculation_id):
        """Sets the calculation_id of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.

        Идентификатор запроса на расчет пользовательского скоринга. Необязательный.  # noqa: E501

        :param calculation_id: The calculation_id of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :type: str
        """

        self._calculation_id = calculation_id

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501

        Коды компаний ИНН или ОГРН, не более 20 кодов. Необязательный.  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.

        Коды компаний ИНН или ОГРН, не более 20 кодов. Необязательный.  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def actual_on_date(self):
        """Gets the actual_on_date of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501

        Дата, на которую актуальны скоринги (вернется последний пользовательский скоринг за указанную дату).  По умолчанию - текущая дата.  # noqa: E501

        :return: The actual_on_date of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_on_date

    @actual_on_date.setter
    def actual_on_date(self, actual_on_date):
        """Sets the actual_on_date of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.

        Дата, на которую актуальны скоринги (вернется последний пользовательский скоринг за указанную дату).  По умолчанию - текущая дата.  # noqa: E501

        :param actual_on_date: The actual_on_date of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_on_date = actual_on_date

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501

        Тип отчетности: 0 - РСБУ, 1 – МСФО.  Если не задан, то будет получена наиболее актуальная на дату запись без учета типа отчетности.  0 = RSBU  1 = IFRS  # noqa: E501

        :return: The source of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsRequestsV2ScoringCustomScoringRequestSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.

        Тип отчетности: 0 - РСБУ, 1 – МСФО.  Если не задан, то будет получена наиболее актуальная на дату запись без учета типа отчетности.  0 = RSBU  1 = IFRS  # noqa: E501

        :param source: The source of this EfirDataHubModelsRequestsV2ScoringCustomScoringRequest.  # noqa: E501
        :type: AllOfEfirDataHubModelsRequestsV2ScoringCustomScoringRequestSource
        """

        self._source = source

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
        if issubclass(EfirDataHubModelsRequestsV2ScoringCustomScoringRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2ScoringCustomScoringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
