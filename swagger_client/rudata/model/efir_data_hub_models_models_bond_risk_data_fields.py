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

class EfirDataHubModelsModelsBondRiskDataFields(object):
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
        'id_fintool': 'int',
        'oecd': 'str',
        'jurisdiction': 'str',
        'currency': 'str',
        'government': 'int',
        'bank': 'int',
        'name_government': 'int',
        'cis': 'int',
        'srf': 'int',
        'ifo': 'int',
        'investmentrating': 'float',
        'isregion': 'float',
        'fininstid': 'int',
        'jurisdiction_oksm': 'str',
        'counter': 'int'
    }

    attribute_map = {
        'id_fintool': 'id_fintool',
        'oecd': 'oecd',
        'jurisdiction': 'jurisdiction',
        'currency': 'currency',
        'government': 'government',
        'bank': 'bank',
        'name_government': 'name_government',
        'cis': 'cis',
        'srf': 'srf',
        'ifo': 'ifo',
        'investmentrating': 'investmentrating',
        'isregion': 'isregion',
        'fininstid': 'fininstid',
        'jurisdiction_oksm': 'jurisdiction_oksm',
        'counter': 'counter'
    }

    def __init__(self, id_fintool=None, oecd=None, jurisdiction=None, currency=None, government=None, bank=None, name_government=None, cis=None, srf=None, ifo=None, investmentrating=None, isregion=None, fininstid=None, jurisdiction_oksm=None, counter=None):  # noqa: E501
        """EfirDataHubModelsModelsBondRiskDataFields - a model defined in Swagger"""  # noqa: E501
        self._id_fintool = None
        self._oecd = None
        self._jurisdiction = None
        self._currency = None
        self._government = None
        self._bank = None
        self._name_government = None
        self._cis = None
        self._srf = None
        self._ifo = None
        self._investmentrating = None
        self._isregion = None
        self._fininstid = None
        self._jurisdiction_oksm = None
        self._counter = None
        self.discriminator = None
        if id_fintool is not None:
            self.id_fintool = id_fintool
        if oecd is not None:
            self.oecd = oecd
        if jurisdiction is not None:
            self.jurisdiction = jurisdiction
        if currency is not None:
            self.currency = currency
        if government is not None:
            self.government = government
        if bank is not None:
            self.bank = bank
        if name_government is not None:
            self.name_government = name_government
        if cis is not None:
            self.cis = cis
        if srf is not None:
            self.srf = srf
        if ifo is not None:
            self.ifo = ifo
        if investmentrating is not None:
            self.investmentrating = investmentrating
        if isregion is not None:
            self.isregion = isregion
        if fininstid is not None:
            self.fininstid = fininstid
        if jurisdiction_oksm is not None:
            self.jurisdiction_oksm = jurisdiction_oksm
        if counter is not None:
            self.counter = counter

    @property
    def id_fintool(self):
        """Gets the id_fintool of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Идентификатор облигации  # noqa: E501

        :return: The id_fintool of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._id_fintool

    @id_fintool.setter
    def id_fintool(self, id_fintool):
        """Sets the id_fintool of this EfirDataHubModelsModelsBondRiskDataFields.

        Идентификатор облигации  # noqa: E501

        :param id_fintool: The id_fintool of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._id_fintool = id_fintool

    @property
    def oecd(self):
        """Gets the oecd of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Значение уровня риска в стране эмитента, по данным классификации ОЭСР  # noqa: E501

        :return: The oecd of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: str
        """
        return self._oecd

    @oecd.setter
    def oecd(self, oecd):
        """Sets the oecd of this EfirDataHubModelsModelsBondRiskDataFields.

        Значение уровня риска в стране эмитента, по данным классификации ОЭСР  # noqa: E501

        :param oecd: The oecd of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: str
        """

        self._oecd = oecd

    @property
    def jurisdiction(self):
        """Gets the jurisdiction of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Название страны, в которой зарегистрирован эмитент выпуска  # noqa: E501

        :return: The jurisdiction of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, jurisdiction):
        """Sets the jurisdiction of this EfirDataHubModelsModelsBondRiskDataFields.

        Название страны, в которой зарегистрирован эмитент выпуска  # noqa: E501

        :param jurisdiction: The jurisdiction of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: str
        """

        self._jurisdiction = jurisdiction

    @property
    def currency(self):
        """Gets the currency of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Трехбуквенное стандартное обозначение валюты страны, в которой зарегистрирован эмитент выпуска  # noqa: E501

        :return: The currency of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EfirDataHubModelsModelsBondRiskDataFields.

        Трехбуквенное стандартное обозначение валюты страны, в которой зарегистрирован эмитент выпуска  # noqa: E501

        :param currency: The currency of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def government(self):
        """Gets the government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что эмитент правительство или ЦБ страны(0/1)  # noqa: E501

        :return: The government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._government

    @government.setter
    def government(self, government):
        """Sets the government of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что эмитент правительство или ЦБ страны(0/1)  # noqa: E501

        :param government: The government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._government = government

    @property
    def bank(self):
        """Gets the bank of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что эмитент – банк(0/1)  # noqa: E501

        :return: The bank of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что эмитент – банк(0/1)  # noqa: E501

        :param bank: The bank of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._bank = bank

    @property
    def name_government(self):
        """Gets the name_government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что эмитент имеет право осуществлять эмиссии от имени государства(0/1)  # noqa: E501

        :return: The name_government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._name_government

    @name_government.setter
    def name_government(self, name_government):
        """Sets the name_government of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что эмитент имеет право осуществлять эмиссии от имени государства(0/1)  # noqa: E501

        :param name_government: The name_government of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._name_government = name_government

    @property
    def cis(self):
        """Gets the cis of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что страна входит в СНГ(за исключением России) (0/1)  # noqa: E501

        :return: The cis of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._cis

    @cis.setter
    def cis(self, cis):
        """Sets the cis of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что страна входит в СНГ(за исключением России) (0/1)  # noqa: E501

        :param cis: The cis of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._cis = cis

    @property
    def srf(self):
        """Gets the srf of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что эмитент субъект РФ или муниципальное объединение(0/1)  # noqa: E501

        :return: The srf of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._srf

    @srf.setter
    def srf(self, srf):
        """Sets the srf of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что эмитент субъект РФ или муниципальное объединение(0/1)  # noqa: E501

        :param srf: The srf of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._srf = srf

    @property
    def ifo(self):
        """Gets the ifo of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак, что эмитент – международная банковская организация(0/1)  # noqa: E501

        :return: The ifo of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._ifo

    @ifo.setter
    def ifo(self, ifo):
        """Sets the ifo of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак, что эмитент – международная банковская организация(0/1)  # noqa: E501

        :param ifo: The ifo of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._ifo = ifo

    @property
    def investmentrating(self):
        """Gets the investmentrating of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Признак низкого риска инвестирования(0/1)  # noqa: E501

        :return: The investmentrating of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: float
        """
        return self._investmentrating

    @investmentrating.setter
    def investmentrating(self, investmentrating):
        """Sets the investmentrating of this EfirDataHubModelsModelsBondRiskDataFields.

        Признак низкого риска инвестирования(0/1)  # noqa: E501

        :param investmentrating: The investmentrating of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: float
        """

        self._investmentrating = investmentrating

    @property
    def isregion(self):
        """Gets the isregion of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Выпуск субъекта федерации: 0 – муниципальный выпуск; 1 – выпуск субъекта федерации; пусто – другое.  # noqa: E501

        :return: The isregion of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: float
        """
        return self._isregion

    @isregion.setter
    def isregion(self, isregion):
        """Sets the isregion of this EfirDataHubModelsModelsBondRiskDataFields.

        Выпуск субъекта федерации: 0 – муниципальный выпуск; 1 – выпуск субъекта федерации; пусто – другое.  # noqa: E501

        :param isregion: The isregion of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: float
        """

        self._isregion = isregion

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Идентификатор эмитента в базе Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsBondRiskDataFields.

        Идентификатор эмитента в базе Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def jurisdiction_oksm(self):
        """Gets the jurisdiction_oksm of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Двухбуквенный код страны в соответствии с ОКСМ  # noqa: E501

        :return: The jurisdiction_oksm of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: str
        """
        return self._jurisdiction_oksm

    @jurisdiction_oksm.setter
    def jurisdiction_oksm(self, jurisdiction_oksm):
        """Sets the jurisdiction_oksm of this EfirDataHubModelsModelsBondRiskDataFields.

        Двухбуквенный код страны в соответствии с ОКСМ  # noqa: E501

        :param jurisdiction_oksm: The jurisdiction_oksm of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: str
        """

        self._jurisdiction_oksm = jurisdiction_oksm

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsBondRiskDataFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsBondRiskDataFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

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
        if issubclass(EfirDataHubModelsModelsBondRiskDataFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondRiskDataFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other