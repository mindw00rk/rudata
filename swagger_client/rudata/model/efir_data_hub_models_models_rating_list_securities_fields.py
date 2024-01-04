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

class EfirDataHubModelsModelsRatingListSecuritiesFields(object):
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
        'id': 'int',
        'name': 'str',
        'shortname_rus': 'str',
        'secname': 'str',
        'isin': 'str',
        'cfi_ifx': 'str',
        'exch': 'int',
        'seccode': 'str',
        'symbol_ts': 'str',
        'code_issuer': 'str',
        'lotsize': 'int',
        'mat_date': 'str',
        'status': 'int',
        'issuer': 'str',
        'sector': 'str',
        'currency': 'str',
        'reg_num': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'shortname_rus': 'shortname_rus',
        'secname': 'secname',
        'isin': 'isin',
        'cfi_ifx': 'cfi_ifx',
        'exch': 'exch',
        'seccode': 'seccode',
        'symbol_ts': 'symbol_ts',
        'code_issuer': 'code_issuer',
        'lotsize': 'lotsize',
        'mat_date': 'mat_date',
        'status': 'status',
        'issuer': 'issuer',
        'sector': 'sector',
        'currency': 'currency',
        'reg_num': 'reg_num'
    }

    def __init__(self, id=None, name=None, shortname_rus=None, secname=None, isin=None, cfi_ifx=None, exch=None, seccode=None, symbol_ts=None, code_issuer=None, lotsize=None, mat_date=None, status=None, issuer=None, sector=None, currency=None, reg_num=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingListSecuritiesFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._shortname_rus = None
        self._secname = None
        self._isin = None
        self._cfi_ifx = None
        self._exch = None
        self._seccode = None
        self._symbol_ts = None
        self._code_issuer = None
        self._lotsize = None
        self._mat_date = None
        self._status = None
        self._issuer = None
        self._sector = None
        self._currency = None
        self._reg_num = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if secname is not None:
            self.secname = secname
        if isin is not None:
            self.isin = isin
        if cfi_ifx is not None:
            self.cfi_ifx = cfi_ifx
        if exch is not None:
            self.exch = exch
        if seccode is not None:
            self.seccode = seccode
        if symbol_ts is not None:
            self.symbol_ts = symbol_ts
        if code_issuer is not None:
            self.code_issuer = code_issuer
        if lotsize is not None:
            self.lotsize = lotsize
        if mat_date is not None:
            self.mat_date = mat_date
        if status is not None:
            self.status = status
        if issuer is not None:
            self.issuer = issuer
        if sector is not None:
            self.sector = sector
        if currency is not None:
            self.currency = currency
        if reg_num is not None:
            self.reg_num = reg_num

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Идентификатор инструмента  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Идентификатор инструмента  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501


        :return: The name of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EfirDataHubModelsModelsRatingListSecuritiesFields.


        :param name: The name of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Краткое русское наименование  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Краткое русское наименование  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def secname(self):
        """Gets the secname of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Наименование поля  # noqa: E501

        :return: The secname of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._secname

    @secname.setter
    def secname(self, secname):
        """Sets the secname of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Наименование поля  # noqa: E501

        :param secname: The secname of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._secname = secname

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Код ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Код ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def cfi_ifx(self):
        """Gets the cfi_ifx of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :return: The cfi_ifx of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._cfi_ifx

    @cfi_ifx.setter
    def cfi_ifx(self, cfi_ifx):
        """Sets the cfi_ifx of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :param cfi_ifx: The cfi_ifx of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._cfi_ifx = cfi_ifx

    @property
    def exch(self):
        """Gets the exch of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Наименование площадки/субплощадки, на которой торгуется инструмент  # noqa: E501

        :return: The exch of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._exch

    @exch.setter
    def exch(self, exch):
        """Sets the exch of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Наименование площадки/субплощадки, на которой торгуется инструмент  # noqa: E501

        :param exch: The exch of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._exch = exch

    @property
    def seccode(self):
        """Gets the seccode of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Торговый код  # noqa: E501

        :return: The seccode of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._seccode

    @seccode.setter
    def seccode(self, seccode):
        """Sets the seccode of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Торговый код  # noqa: E501

        :param seccode: The seccode of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._seccode = seccode

    @property
    def symbol_ts(self):
        """Gets the symbol_ts of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Краткое торговое наименование на торговой площадке  # noqa: E501

        :return: The symbol_ts of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._symbol_ts

    @symbol_ts.setter
    def symbol_ts(self, symbol_ts):
        """Sets the symbol_ts of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Краткое торговое наименование на торговой площадке  # noqa: E501

        :param symbol_ts: The symbol_ts of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._symbol_ts = symbol_ts

    @property
    def code_issuer(self):
        """Gets the code_issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Символьный код эмитента  # noqa: E501

        :return: The code_issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._code_issuer

    @code_issuer.setter
    def code_issuer(self, code_issuer):
        """Sets the code_issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Символьный код эмитента  # noqa: E501

        :param code_issuer: The code_issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._code_issuer = code_issuer

    @property
    def lotsize(self):
        """Gets the lotsize of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Размер лота  # noqa: E501

        :return: The lotsize of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._lotsize

    @lotsize.setter
    def lotsize(self, lotsize):
        """Sets the lotsize of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Размер лота  # noqa: E501

        :param lotsize: The lotsize of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._lotsize = lotsize

    @property
    def mat_date(self):
        """Gets the mat_date of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Дата погашения (экспирации)  # noqa: E501

        :return: The mat_date of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._mat_date

    @mat_date.setter
    def mat_date(self, mat_date):
        """Sets the mat_date of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Дата погашения (экспирации)  # noqa: E501

        :param mat_date: The mat_date of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._mat_date = mat_date

    @property
    def status(self):
        """Gets the status of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Статус  # noqa: E501

        :return: The status of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Статус  # noqa: E501

        :param status: The status of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def issuer(self):
        """Gets the issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Эмитент  # noqa: E501

        :return: The issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Эмитент  # noqa: E501

        :param issuer: The issuer of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def sector(self):
        """Gets the sector of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Сектор  # noqa: E501

        :return: The sector of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Сектор  # noqa: E501

        :param sector: The sector of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def currency(self):
        """Gets the currency of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Валюта  # noqa: E501

        :return: The currency of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Валюта  # noqa: E501

        :param currency: The currency of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def reg_num(self):
        """Gets the reg_num of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501

        Регистрационный номер  # noqa: E501

        :return: The reg_num of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_num

    @reg_num.setter
    def reg_num(self, reg_num):
        """Sets the reg_num of this EfirDataHubModelsModelsRatingListSecuritiesFields.

        Регистрационный номер  # noqa: E501

        :param reg_num: The reg_num of this EfirDataHubModelsModelsRatingListSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._reg_num = reg_num

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
        if issubclass(EfirDataHubModelsModelsRatingListSecuritiesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingListSecuritiesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
