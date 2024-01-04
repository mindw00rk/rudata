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

class EfirDataHubModelsModelsEmitentEncumbranceListFields(object):
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
        'fininst_id': 'int',
        'inn': 'str',
        'ogrn': 'str',
        'full_name': 'str',
        'counterpartyid': 'int',
        'property_data': 'list[EfirDataHubModelsModelsEmitentPropertyData]',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'full_name': 'full_name',
        'counterpartyid': 'counterpartyid',
        'property_data': 'property_data',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fininst_id=None, inn=None, ogrn=None, full_name=None, counterpartyid=None, property_data=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentEncumbranceListFields - a model defined in Swagger"""  # noqa: E501
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._full_name = None
        self._counterpartyid = None
        self._property_data = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if full_name is not None:
            self.full_name = full_name
        if counterpartyid is not None:
            self.counterpartyid = counterpartyid
        if property_data is not None:
            self.property_data = property_data
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        ID компании в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        ID компании в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        ИНН организации  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        ИНН организации  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        ОГРН организации  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        ОГРН организации  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def full_name(self):
        """Gets the full_name of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        Полное наименование организации  # noqa: E501

        :return: The full_name of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        Полное наименование организации  # noqa: E501

        :param full_name: The full_name of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def counterpartyid(self):
        """Gets the counterpartyid of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The counterpartyid of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: int
        """
        return self._counterpartyid

    @counterpartyid.setter
    def counterpartyid(self, counterpartyid):
        """Sets the counterpartyid of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        Идентификатор контрагента  # noqa: E501

        :param counterpartyid: The counterpartyid of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: int
        """

        self._counterpartyid = counterpartyid

    @property
    def property_data(self):
        """Gets the property_data of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        Данные обремененного имущества  # noqa: E501

        :return: The property_data of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsEmitentPropertyData]
        """
        return self._property_data

    @property_data.setter
    def property_data(self, property_data):
        """Sets the property_data of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        Данные обремененного имущества  # noqa: E501

        :param property_data: The property_data of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: list[EfirDataHubModelsModelsEmitentPropertyData]
        """

        self._property_data = property_data

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsEmitentEncumbranceListFields.  # noqa: E501
        :type: int
        """

        self._rn = rn

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
        if issubclass(EfirDataHubModelsModelsEmitentEncumbranceListFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentEncumbranceListFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
