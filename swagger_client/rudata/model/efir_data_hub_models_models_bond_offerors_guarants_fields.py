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

class EfirDataHubModelsModelsBondOfferorsGuarantsFields(object):
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
        'fintool_id': 'int',
        'fininstid_guarant': 'int',
        'fininstid_offeror': 'int',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fintool_id': 'fintoolId',
        'fininstid_guarant': 'fininstid_guarant',
        'fininstid_offeror': 'fininstid_offeror',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fintool_id=None, fininstid_guarant=None, fininstid_offeror=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsBondOfferorsGuarantsFields - a model defined in Swagger"""  # noqa: E501
        self._fintool_id = None
        self._fininstid_guarant = None
        self._fininstid_offeror = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if fininstid_guarant is not None:
            self.fininstid_guarant = fininstid_guarant
        if fininstid_offeror is not None:
            self.fininstid_offeror = fininstid_offeror
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501

        Идентификатор инструмента в БД Интерфакс  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.

        Идентификатор инструмента в БД Интерфакс  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def fininstid_guarant(self):
        """Gets the fininstid_guarant of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501

        Идентификатор лучшего гаранта/поручителя в БД Интерфакс  # noqa: E501

        :return: The fininstid_guarant of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid_guarant

    @fininstid_guarant.setter
    def fininstid_guarant(self, fininstid_guarant):
        """Sets the fininstid_guarant of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.

        Идентификатор лучшего гаранта/поручителя в БД Интерфакс  # noqa: E501

        :param fininstid_guarant: The fininstid_guarant of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :type: int
        """

        self._fininstid_guarant = fininstid_guarant

    @property
    def fininstid_offeror(self):
        """Gets the fininstid_offeror of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501

        Идентификатор лучшего оферента в БД Интерфакс  # noqa: E501

        :return: The fininstid_offeror of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid_offeror

    @fininstid_offeror.setter
    def fininstid_offeror(self, fininstid_offeror):
        """Sets the fininstid_offeror of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.

        Идентификатор лучшего оферента в БД Интерфакс  # noqa: E501

        :param fininstid_offeror: The fininstid_offeror of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :type: int
        """

        self._fininstid_offeror = fininstid_offeror

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsBondOfferorsGuarantsFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsBondOfferorsGuarantsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondOfferorsGuarantsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
