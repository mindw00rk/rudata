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

class EfirDataHubModelsModelsEmitentEmitentShortInfoFields(object):
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
        'shortname_rus': 'str',
        'shortname_eng': 'str'
    }

    attribute_map = {
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'shortname_rus': 'shortname_rus',
        'shortname_eng': 'shortname_eng'
    }

    def __init__(self, fininst_id=None, inn=None, ogrn=None, shortname_rus=None, shortname_eng=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentEmitentShortInfoFields - a model defined in Swagger"""  # noqa: E501
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._shortname_rus = None
        self._shortname_eng = None
        self.discriminator = None
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if shortname_eng is not None:
            self.shortname_eng = shortname_eng

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501


        :return: The fininst_id of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.


        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501


        :return: The inn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.


        :param inn: The inn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501


        :return: The ogrn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.


        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501


        :return: The shortname_rus of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.


        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def shortname_eng(self):
        """Gets the shortname_eng of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501


        :return: The shortname_eng of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_eng

    @shortname_eng.setter
    def shortname_eng(self, shortname_eng):
        """Sets the shortname_eng of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.


        :param shortname_eng: The shortname_eng of this EfirDataHubModelsModelsEmitentEmitentShortInfoFields.  # noqa: E501
        :type: str
        """

        self._shortname_eng = shortname_eng

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
        if issubclass(EfirDataHubModelsModelsEmitentEmitentShortInfoFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentEmitentShortInfoFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other