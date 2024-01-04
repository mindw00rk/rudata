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

class EfirDataHubModelsModelsRiskRiskGroupParamsRequest(object):
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
        'params': 'list[str]',
        'offer_enable': 'bool',
        'use_frozen_dates': 'bool',
        'edition': 'str'
    }

    attribute_map = {
        'isin': 'isin',
        '_date': 'date',
        'params': 'params',
        'offer_enable': 'offerEnable',
        'use_frozen_dates': 'useFrozenDates',
        'edition': 'edition'
    }

    def __init__(self, isin=None, _date=None, params=None, offer_enable=None, use_frozen_dates=None, edition=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskRiskGroupParamsRequest - a model defined in Swagger"""  # noqa: E501
        self._isin = None
        self.__date = None
        self._params = None
        self._offer_enable = None
        self._use_frozen_dates = None
        self._edition = None
        self.discriminator = None
        self.isin = isin
        self._date = _date
        if params is not None:
            self.params = params
        if offer_enable is not None:
            self.offer_enable = offer_enable
        if use_frozen_dates is not None:
            self.use_frozen_dates = use_frozen_dates
        if edition is not None:
            self.edition = edition

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: str
        """
        if isin is None:
            raise ValueError("Invalid value for `isin`, must not be `None`")  # noqa: E501

        self._isin = isin

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        Дата расчета  # noqa: E501

        :return: The _date of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        Дата расчета  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def params(self):
        """Gets the params of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        Список параметров  # noqa: E501

        :return: The params of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        Список параметров  # noqa: E501

        :param params: The params of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: list[str]
        """

        self._params = params

    @property
    def offer_enable(self):
        """Gets the offer_enable of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        Использовать оферты  # noqa: E501

        :return: The offer_enable of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._offer_enable

    @offer_enable.setter
    def offer_enable(self, offer_enable):
        """Sets the offer_enable of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        Использовать оферты  # noqa: E501

        :param offer_enable: The offer_enable of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: bool
        """

        self._offer_enable = offer_enable

    @property
    def use_frozen_dates(self):
        """Gets the use_frozen_dates of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        Использовать даты заморозки рейтингов  # noqa: E501

        :return: The use_frozen_dates of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_frozen_dates

    @use_frozen_dates.setter
    def use_frozen_dates(self, use_frozen_dates):
        """Sets the use_frozen_dates of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        Использовать даты заморозки рейтингов  # noqa: E501

        :param use_frozen_dates: The use_frozen_dates of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: bool
        """

        self._use_frozen_dates = use_frozen_dates

    @property
    def edition(self):
        """Gets the edition of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501

        Редакция инструкции ЦБ  # noqa: E501

        :return: The edition of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.

        Редакция инструкции ЦБ  # noqa: E501

        :param edition: The edition of this EfirDataHubModelsModelsRiskRiskGroupParamsRequest.  # noqa: E501
        :type: str
        """

        self._edition = edition

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
        if issubclass(EfirDataHubModelsModelsRiskRiskGroupParamsRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskRiskGroupParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
