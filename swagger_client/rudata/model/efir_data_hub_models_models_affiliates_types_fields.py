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

class EfirDataHubModelsModelsAffiliatesTypesFields(object):
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
        'affiliates_type_id': 'int',
        'shortname_rus': 'str',
        'fullname_rus': 'str'
    }

    attribute_map = {
        'affiliates_type_id': 'affiliates_type_id',
        'shortname_rus': 'shortname_rus',
        'fullname_rus': 'fullname_rus'
    }

    def __init__(self, affiliates_type_id=None, shortname_rus=None, fullname_rus=None):  # noqa: E501
        """EfirDataHubModelsModelsAffiliatesTypesFields - a model defined in Swagger"""  # noqa: E501
        self._affiliates_type_id = None
        self._shortname_rus = None
        self._fullname_rus = None
        self.discriminator = None
        if affiliates_type_id is not None:
            self.affiliates_type_id = affiliates_type_id
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus

    @property
    def affiliates_type_id(self):
        """Gets the affiliates_type_id of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501

        Идентификатор типа аффилированности  # noqa: E501

        :return: The affiliates_type_id of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :rtype: int
        """
        return self._affiliates_type_id

    @affiliates_type_id.setter
    def affiliates_type_id(self, affiliates_type_id):
        """Sets the affiliates_type_id of this EfirDataHubModelsModelsAffiliatesTypesFields.

        Идентификатор типа аффилированности  # noqa: E501

        :param affiliates_type_id: The affiliates_type_id of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :type: int
        """

        self._affiliates_type_id = affiliates_type_id

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501

        Краткое наименование типа  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.

        Краткое наименование типа  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501

        Полное наименование типа  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.

        Полное наименование типа  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsAffiliatesTypesFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

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
        if issubclass(EfirDataHubModelsModelsAffiliatesTypesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsAffiliatesTypesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
