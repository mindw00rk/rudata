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

class EfirDataHubModelsModelsRiskVarDataResponse(object):
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
        'type_rf': 'int',
        'rf': 'int',
        'cur': 'str',
        'type_rfc': 'int',
        'rfc': 'int',
        'r_o_isin': 'float',
        'r_o_cur': 'float',
        'sigma_rf': 'float',
        'sigma_rfc': 'float',
        'cor_rf_rfc': 'float',
        'va_r_mult': 'float',
        'e_s_mult': 'float',
        'unit_isin': 'float',
        'unit_cur': 'float',
        'error': 'str'
    }

    attribute_map = {
        'type_rf': 'typeRF',
        'rf': 'rf',
        'cur': 'cur',
        'type_rfc': 'type_RFC',
        'rfc': 'rfc',
        'r_o_isin': 'rO_ISIN',
        'r_o_cur': 'rO_CUR',
        'sigma_rf': 'sigma_RF',
        'sigma_rfc': 'sigma_RFC',
        'cor_rf_rfc': 'cor_RF_RFC',
        'va_r_mult': 'vaR_mult',
        'e_s_mult': 'eS_mult',
        'unit_isin': 'unit_ISIN',
        'unit_cur': 'unit_CUR',
        'error': 'error'
    }

    def __init__(self, type_rf=None, rf=None, cur=None, type_rfc=None, rfc=None, r_o_isin=None, r_o_cur=None, sigma_rf=None, sigma_rfc=None, cor_rf_rfc=None, va_r_mult=None, e_s_mult=None, unit_isin=None, unit_cur=None, error=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskVarDataResponse - a model defined in Swagger"""  # noqa: E501
        self._type_rf = None
        self._rf = None
        self._cur = None
        self._type_rfc = None
        self._rfc = None
        self._r_o_isin = None
        self._r_o_cur = None
        self._sigma_rf = None
        self._sigma_rfc = None
        self._cor_rf_rfc = None
        self._va_r_mult = None
        self._e_s_mult = None
        self._unit_isin = None
        self._unit_cur = None
        self._error = None
        self.discriminator = None
        if type_rf is not None:
            self.type_rf = type_rf
        if rf is not None:
            self.rf = rf
        if cur is not None:
            self.cur = cur
        if type_rfc is not None:
            self.type_rfc = type_rfc
        if rfc is not None:
            self.rfc = rfc
        if r_o_isin is not None:
            self.r_o_isin = r_o_isin
        if r_o_cur is not None:
            self.r_o_cur = r_o_cur
        if sigma_rf is not None:
            self.sigma_rf = sigma_rf
        if sigma_rfc is not None:
            self.sigma_rfc = sigma_rfc
        if cor_rf_rfc is not None:
            self.cor_rf_rfc = cor_rf_rfc
        if va_r_mult is not None:
            self.va_r_mult = va_r_mult
        if e_s_mult is not None:
            self.e_s_mult = e_s_mult
        if unit_isin is not None:
            self.unit_isin = unit_isin
        if unit_cur is not None:
            self.unit_cur = unit_cur
        if error is not None:
            self.error = error

    @property
    def type_rf(self):
        """Gets the type_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Тип фактора риска инструмента (0 – облигации, 1 – валюты, 2 - акции)  # noqa: E501

        :return: The type_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._type_rf

    @type_rf.setter
    def type_rf(self, type_rf):
        """Sets the type_rf of this EfirDataHubModelsModelsRiskVarDataResponse.

        Тип фактора риска инструмента (0 – облигации, 1 – валюты, 2 - акции)  # noqa: E501

        :param type_rf: The type_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: int
        """

        self._type_rf = type_rf

    @property
    def rf(self):
        """Gets the rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Фактор риска инструмента  # noqa: E501

        :return: The rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._rf

    @rf.setter
    def rf(self, rf):
        """Sets the rf of this EfirDataHubModelsModelsRiskVarDataResponse.

        Фактор риска инструмента  # noqa: E501

        :param rf: The rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: int
        """

        self._rf = rf

    @property
    def cur(self):
        """Gets the cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Код валюты. Если входной инструмент – валюта, то CUR = ID.  # noqa: E501

        :return: The cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._cur

    @cur.setter
    def cur(self, cur):
        """Sets the cur of this EfirDataHubModelsModelsRiskVarDataResponse.

        Код валюты. Если входной инструмент – валюта, то CUR = ID.  # noqa: E501

        :param cur: The cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: str
        """

        self._cur = cur

    @property
    def type_rfc(self):
        """Gets the type_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Тип фактора риска валюты (0-2)  # noqa: E501

        :return: The type_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._type_rfc

    @type_rfc.setter
    def type_rfc(self, type_rfc):
        """Sets the type_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.

        Тип фактора риска валюты (0-2)  # noqa: E501

        :param type_rfc: The type_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: int
        """

        self._type_rfc = type_rfc

    @property
    def rfc(self):
        """Gets the rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Фактор риска валюты (1-29)  # noqa: E501

        :return: The rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._rfc

    @rfc.setter
    def rfc(self, rfc):
        """Sets the rfc of this EfirDataHubModelsModelsRiskVarDataResponse.

        Фактор риска валюты (1-29)  # noqa: E501

        :param rfc: The rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: int
        """

        self._rfc = rfc

    @property
    def r_o_isin(self):
        """Gets the r_o_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель риска по инструменту  # noqa: E501

        :return: The r_o_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._r_o_isin

    @r_o_isin.setter
    def r_o_isin(self, r_o_isin):
        """Sets the r_o_isin of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель риска по инструменту  # noqa: E501

        :param r_o_isin: The r_o_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._r_o_isin = r_o_isin

    @property
    def r_o_cur(self):
        """Gets the r_o_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель риска по валюте  # noqa: E501

        :return: The r_o_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._r_o_cur

    @r_o_cur.setter
    def r_o_cur(self, r_o_cur):
        """Sets the r_o_cur of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель риска по валюте  # noqa: E501

        :param r_o_cur: The r_o_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._r_o_cur = r_o_cur

    @property
    def sigma_rf(self):
        """Gets the sigma_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Волатильность фактора риска инструмента  # noqa: E501

        :return: The sigma_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._sigma_rf

    @sigma_rf.setter
    def sigma_rf(self, sigma_rf):
        """Sets the sigma_rf of this EfirDataHubModelsModelsRiskVarDataResponse.

        Волатильность фактора риска инструмента  # noqa: E501

        :param sigma_rf: The sigma_rf of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._sigma_rf = sigma_rf

    @property
    def sigma_rfc(self):
        """Gets the sigma_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Волатильность фактора риска валюты  # noqa: E501

        :return: The sigma_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._sigma_rfc

    @sigma_rfc.setter
    def sigma_rfc(self, sigma_rfc):
        """Sets the sigma_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.

        Волатильность фактора риска валюты  # noqa: E501

        :param sigma_rfc: The sigma_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._sigma_rfc = sigma_rfc

    @property
    def cor_rf_rfc(self):
        """Gets the cor_rf_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Коэффициент корреляции между факторами риска инструмента и валюты(из корреляционной матрицы)  # noqa: E501

        :return: The cor_rf_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._cor_rf_rfc

    @cor_rf_rfc.setter
    def cor_rf_rfc(self, cor_rf_rfc):
        """Sets the cor_rf_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.

        Коэффициент корреляции между факторами риска инструмента и валюты(из корреляционной матрицы)  # noqa: E501

        :param cor_rf_rfc: The cor_rf_rfc of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._cor_rf_rfc = cor_rf_rfc

    @property
    def va_r_mult(self):
        """Gets the va_r_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель VaR с учетом временного горизонта прогноза  # noqa: E501

        :return: The va_r_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._va_r_mult

    @va_r_mult.setter
    def va_r_mult(self, va_r_mult):
        """Sets the va_r_mult of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель VaR с учетом временного горизонта прогноза  # noqa: E501

        :param va_r_mult: The va_r_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._va_r_mult = va_r_mult

    @property
    def e_s_mult(self):
        """Gets the e_s_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель ES с учетом временного горизонта прогноза  # noqa: E501

        :return: The e_s_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._e_s_mult

    @e_s_mult.setter
    def e_s_mult(self, e_s_mult):
        """Sets the e_s_mult of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель ES с учетом временного горизонта прогноза  # noqa: E501

        :param e_s_mult: The e_s_mult of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._e_s_mult = e_s_mult

    @property
    def unit_isin(self):
        """Gets the unit_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель риска на единицу позиции (составляющая по инструменту)  # noqa: E501

        :return: The unit_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._unit_isin

    @unit_isin.setter
    def unit_isin(self, unit_isin):
        """Sets the unit_isin of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель риска на единицу позиции (составляющая по инструменту)  # noqa: E501

        :param unit_isin: The unit_isin of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._unit_isin = unit_isin

    @property
    def unit_cur(self):
        """Gets the unit_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Множитель риска на единицу позиции (составляющая по валюте)  # noqa: E501

        :return: The unit_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: float
        """
        return self._unit_cur

    @unit_cur.setter
    def unit_cur(self, unit_cur):
        """Sets the unit_cur of this EfirDataHubModelsModelsRiskVarDataResponse.

        Множитель риска на единицу позиции (составляющая по валюте)  # noqa: E501

        :param unit_cur: The unit_cur of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :type: float
        """

        self._unit_cur = unit_cur

    @property
    def error(self):
        """Gets the error of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501

        Текст ошибки, если она произошла  # noqa: E501

        :return: The error of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EfirDataHubModelsModelsRiskVarDataResponse.

        Текст ошибки, если она произошла  # noqa: E501

        :param error: The error of this EfirDataHubModelsModelsRiskVarDataResponse.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsRiskVarDataResponse, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskVarDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
