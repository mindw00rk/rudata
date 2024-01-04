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

class EfirDataHubModelsModelsEmitentKmvPdFields(object):
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
        'fininstid': 'int',
        'pd_kmv': 'float',
        'calcdate': 'datetime'
    }

    attribute_map = {
        'fininstid': 'fininstid',
        'pd_kmv': 'pd_kmv',
        'calcdate': 'calcdate'
    }

    def __init__(self, fininstid=None, pd_kmv=None, calcdate=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentKmvPdFields - a model defined in Swagger"""  # noqa: E501
        self._fininstid = None
        self._pd_kmv = None
        self._calcdate = None
        self.discriminator = None
        if fininstid is not None:
            self.fininstid = fininstid
        if pd_kmv is not None:
            self.pd_kmv = pd_kmv
        if calcdate is not None:
            self.calcdate = calcdate

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501

        Id компании в БД Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsEmitentKmvPdFields.

        Id компании в БД Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def pd_kmv(self):
        """Gets the pd_kmv of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501

        Вероятность дефолта в процентах по Килхоферу, МакКоуну, Васичеку  # noqa: E501

        :return: The pd_kmv of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :rtype: float
        """
        return self._pd_kmv

    @pd_kmv.setter
    def pd_kmv(self, pd_kmv):
        """Sets the pd_kmv of this EfirDataHubModelsModelsEmitentKmvPdFields.

        Вероятность дефолта в процентах по Килхоферу, МакКоуну, Васичеку  # noqa: E501

        :param pd_kmv: The pd_kmv of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :type: float
        """

        self._pd_kmv = pd_kmv

    @property
    def calcdate(self):
        """Gets the calcdate of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501

        Дата формирования значения  # noqa: E501

        :return: The calcdate of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :rtype: datetime
        """
        return self._calcdate

    @calcdate.setter
    def calcdate(self, calcdate):
        """Sets the calcdate of this EfirDataHubModelsModelsEmitentKmvPdFields.

        Дата формирования значения  # noqa: E501

        :param calcdate: The calcdate of this EfirDataHubModelsModelsEmitentKmvPdFields.  # noqa: E501
        :type: datetime
        """

        self._calcdate = calcdate

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
        if issubclass(EfirDataHubModelsModelsEmitentKmvPdFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentKmvPdFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
