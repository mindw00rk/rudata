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

class EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest(object):
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
        '_date': 'datetime',
        'curve_code': 'str',
        'num_decimals': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'curve_code': 'curveCode',
        'num_decimals': 'numDecimals'
    }

    def __init__(self, _date=None, curve_code=None, num_decimals=4):  # noqa: E501
        """EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._curve_code = None
        self._num_decimals = None
        self.discriminator = None
        self._date = _date
        self.curve_code = curve_code
        if num_decimals is not None:
            self.num_decimals = num_decimals

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501

        Дата, на которую возвращаются точки кривой.  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.

        Дата, на которую возвращаются точки кривой.  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def curve_code(self):
        """Gets the curve_code of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501

        Код кривой. Возможные значения:  - MOEX.RUB.ZCYC - Кривая бескупонной доходности Мосбиржи в рублях;  - UST.USD.DYCR - Дневные ставки кривой доходности US Treasuries;  - ECB.EUR.ZCYC - Дневные ставки кривой доходности ЕЦБ;  - CCDC.CNY.ZCYC - Дневные ставки кривой бескупонной доходности КИТАЙ;  # noqa: E501

        :return: The curve_code of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :rtype: str
        """
        return self._curve_code

    @curve_code.setter
    def curve_code(self, curve_code):
        """Sets the curve_code of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.

        Код кривой. Возможные значения:  - MOEX.RUB.ZCYC - Кривая бескупонной доходности Мосбиржи в рублях;  - UST.USD.DYCR - Дневные ставки кривой доходности US Treasuries;  - ECB.EUR.ZCYC - Дневные ставки кривой доходности ЕЦБ;  - CCDC.CNY.ZCYC - Дневные ставки кривой бескупонной доходности КИТАЙ;  # noqa: E501

        :param curve_code: The curve_code of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :type: str
        """
        if curve_code is None:
            raise ValueError("Invalid value for `curve_code`, must not be `None`")  # noqa: E501

        self._curve_code = curve_code

    @property
    def num_decimals(self):
        """Gets the num_decimals of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501

        Число знаков после запятой, до которых необходимо округлять значения доходности (поле rate).  Возможные значения - от 0 до 6 включительно.  По умолчанию 4.  # noqa: E501

        :return: The num_decimals of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_decimals

    @num_decimals.setter
    def num_decimals(self, num_decimals):
        """Sets the num_decimals of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.

        Число знаков после запятой, до которых необходимо округлять значения доходности (поле rate).  Возможные значения - от 0 до 6 включительно.  По умолчанию 4.  # noqa: E501

        :param num_decimals: The num_decimals of this EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest.  # noqa: E501
        :type: int
        """

        self._num_decimals = num_decimals

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
        if issubclass(EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
