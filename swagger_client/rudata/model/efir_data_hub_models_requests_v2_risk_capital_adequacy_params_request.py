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

class EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest(object):
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
        'use_frozen_dates': 'bool',
        'cbr_instructions': 'list[EfirDataHubModelsRequestsV2NameValuePair]',
        'position_open_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        '_date': 'date',
        'use_frozen_dates': 'useFrozenDates',
        'cbr_instructions': 'cbrInstructions',
        'position_open_date': 'positionOpenDate'
    }

    def __init__(self, id=None, _date=None, use_frozen_dates=None, cbr_instructions=None, position_open_date=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__date = None
        self._use_frozen_dates = None
        self._cbr_instructions = None
        self._position_open_date = None
        self.discriminator = None
        self.id = id
        self._date = _date
        if use_frozen_dates is not None:
            self.use_frozen_dates = use_frozen_dates
        if cbr_instructions is not None:
            self.cbr_instructions = cbr_instructions
        if position_open_date is not None:
            self.position_open_date = position_open_date

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501

        Идентификатор инструмента – ISIN (обязательный)  # noqa: E501

        :return: The id of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.

        Идентификатор инструмента – ISIN (обязательный)  # noqa: E501

        :param id: The id of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501

        Дата расчета (обязательный)  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.

        Дата расчета (обязательный)  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def use_frozen_dates(self):
        """Gets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501

        Флаг заморозки рейтингов (необязательный)  # noqa: E501

        :return: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_frozen_dates

    @use_frozen_dates.setter
    def use_frozen_dates(self, use_frozen_dates):
        """Sets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.

        Флаг заморозки рейтингов (необязательный)  # noqa: E501

        :param use_frozen_dates: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :type: bool
        """

        self._use_frozen_dates = use_frozen_dates

    @property
    def cbr_instructions(self):
        """Gets the cbr_instructions of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501

        Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \"Положение о порядке расчета показателя краткосрочной ликвидности\"  - marketRiskEdition - для положений \"О порядке расчета кредитными организациями величины рыночного риска\"  - bankNormEdition - для положений \"Об обязательных нормативах банков\"  # noqa: E501

        :return: The cbr_instructions of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :rtype: list[EfirDataHubModelsRequestsV2NameValuePair]
        """
        return self._cbr_instructions

    @cbr_instructions.setter
    def cbr_instructions(self, cbr_instructions):
        """Sets the cbr_instructions of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.

        Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \"Положение о порядке расчета показателя краткосрочной ликвидности\"  - marketRiskEdition - для положений \"О порядке расчета кредитными организациями величины рыночного риска\"  - bankNormEdition - для положений \"Об обязательных нормативах банков\"  # noqa: E501

        :param cbr_instructions: The cbr_instructions of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :type: list[EfirDataHubModelsRequestsV2NameValuePair]
        """

        self._cbr_instructions = cbr_instructions

    @property
    def position_open_date(self):
        """Gets the position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501

        Дата открытия (покупки) позиции  # noqa: E501

        :return: The position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """Sets the position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.

        Дата открытия (покупки) позиции  # noqa: E501

        :param position_open_date: The position_open_date of this EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest.  # noqa: E501
        :type: datetime
        """

        self._position_open_date = position_open_date

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
        if issubclass(EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
