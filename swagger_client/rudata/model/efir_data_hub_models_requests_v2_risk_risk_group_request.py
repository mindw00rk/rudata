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

class EfirDataHubModelsRequestsV2RiskRiskGroupRequest(object):
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
        'isin': 'str',
        '_date': 'datetime',
        'funding': 'int',
        'offer_enable': 'bool',
        'use_frozen_dates': 'bool',
        'edition': 'str',
        'cbr_instructions': 'list[EfirDataHubModelsRequestsV2NameValuePair]',
        'position_open_date': 'datetime'
    }

    attribute_map = {
        'isin': 'isin',
        '_date': 'date',
        'funding': 'funding',
        'offer_enable': 'offerEnable',
        'use_frozen_dates': 'useFrozenDates',
        'edition': 'edition',
        'cbr_instructions': 'cbrInstructions',
        'position_open_date': 'positionOpenDate'
    }

    def __init__(self, isin=None, _date=None, funding=None, offer_enable=None, use_frozen_dates=None, edition=None, cbr_instructions=None, position_open_date=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RiskRiskGroupRequest - a model defined in Swagger"""  # noqa: E501
        self._isin = None
        self.__date = None
        self._funding = None
        self._offer_enable = None
        self._use_frozen_dates = None
        self._edition = None
        self._cbr_instructions = None
        self._position_open_date = None
        self.discriminator = None
        self.isin = isin
        self._date = _date
        if funding is not None:
            self.funding = funding
        if offer_enable is not None:
            self.offer_enable = offer_enable
        if use_frozen_dates is not None:
            self.use_frozen_dates = use_frozen_dates
        if edition is not None:
            self.edition = edition
        if cbr_instructions is not None:
            self.cbr_instructions = cbr_instructions
        if position_open_date is not None:
            self.position_open_date = position_open_date

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        ISIN (обязательный)  # noqa: E501

        :return: The isin of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        ISIN (обязательный)  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: str
        """
        if isin is None:
            raise ValueError("Invalid value for `isin`, must not be `None`")  # noqa: E501

        self._isin = isin

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        Дата (обязательный)  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        Дата (обязательный)  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def funding(self):
        """Gets the funding of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        1 – фондирование в валюте номинала. По умолчанию 0.  # noqa: E501

        :return: The funding of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """Sets the funding of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        1 – фондирование в валюте номинала. По умолчанию 0.  # noqa: E501

        :param funding: The funding of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: int
        """

        self._funding = funding

    @property
    def offer_enable(self):
        """Gets the offer_enable of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        Использовать оферты  # noqa: E501

        :return: The offer_enable of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._offer_enable

    @offer_enable.setter
    def offer_enable(self, offer_enable):
        """Sets the offer_enable of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        Использовать оферты  # noqa: E501

        :param offer_enable: The offer_enable of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: bool
        """

        self._offer_enable = offer_enable

    @property
    def use_frozen_dates(self):
        """Gets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501


        :return: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_frozen_dates

    @use_frozen_dates.setter
    def use_frozen_dates(self, use_frozen_dates):
        """Sets the use_frozen_dates of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.


        :param use_frozen_dates: The use_frozen_dates of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: bool
        """

        self._use_frozen_dates = use_frozen_dates

    @property
    def edition(self):
        """Gets the edition of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        Редакция инструкции ЦБ  # noqa: E501

        :return: The edition of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        Редакция инструкции ЦБ  # noqa: E501

        :param edition: The edition of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def cbr_instructions(self):
        """Gets the cbr_instructions of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \"Положение о порядке расчета показателя краткосрочной ликвидности\"  - marketRiskEdition - для положений \"О порядке расчета кредитными организациями величины рыночного риска\"  - bankNormEdition - для положений \"Об обязательных нормативах банков\"  # noqa: E501

        :return: The cbr_instructions of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: list[EfirDataHubModelsRequestsV2NameValuePair]
        """
        return self._cbr_instructions

    @cbr_instructions.setter
    def cbr_instructions(self, cbr_instructions):
        """Sets the cbr_instructions of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \"Положение о порядке расчета показателя краткосрочной ликвидности\"  - marketRiskEdition - для положений \"О порядке расчета кредитными организациями величины рыночного риска\"  - bankNormEdition - для положений \"Об обязательных нормативах банков\"  # noqa: E501

        :param cbr_instructions: The cbr_instructions of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :type: list[EfirDataHubModelsRequestsV2NameValuePair]
        """

        self._cbr_instructions = cbr_instructions

    @property
    def position_open_date(self):
        """Gets the position_open_date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501

        Дата открытия (покупки) позиции  # noqa: E501

        :return: The position_open_date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """Sets the position_open_date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.

        Дата открытия (покупки) позиции  # noqa: E501

        :param position_open_date: The position_open_date of this EfirDataHubModelsRequestsV2RiskRiskGroupRequest.  # noqa: E501
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
        if issubclass(EfirDataHubModelsRequestsV2RiskRiskGroupRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RiskRiskGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
