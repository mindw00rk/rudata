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

class EfirDataHubModelsModelsEmitentBurdeningOrgData(object):
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
        'full_name': 'str'
    }

    attribute_map = {
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'full_name': 'full_name'
    }

    def __init__(self, fininst_id=None, inn=None, ogrn=None, full_name=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentBurdeningOrgData - a model defined in Swagger"""  # noqa: E501
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._full_name = None
        self.discriminator = None
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if full_name is not None:
            self.full_name = full_name

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501

        ID компании в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentBurdeningOrgData.

        ID компании в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501

        ИНН организации  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.

        ИНН организации  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501

        ОГРН организации  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.

        ОГРН организации  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def full_name(self):
        """Gets the full_name of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501

        Полное наименование организации  # noqa: E501

        :return: The full_name of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this EfirDataHubModelsModelsEmitentBurdeningOrgData.

        Полное наименование организации  # noqa: E501

        :param full_name: The full_name of this EfirDataHubModelsModelsEmitentBurdeningOrgData.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

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
        if issubclass(EfirDataHubModelsModelsEmitentBurdeningOrgData, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentBurdeningOrgData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
