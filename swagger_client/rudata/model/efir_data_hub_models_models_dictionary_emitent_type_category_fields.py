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

class EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields(object):
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
        'shortname_rus': 'str',
        'fullname_rus': 'str',
        'is_given_country': 'int',
        'counter': 'int'
    }

    attribute_map = {
        'id': 'id',
        'shortname_rus': 'shortname_rus',
        'fullname_rus': 'fullname_rus',
        'is_given_country': 'is_given_country',
        'counter': 'counter'
    }

    def __init__(self, id=None, shortname_rus=None, fullname_rus=None, is_given_country=None, counter=None):  # noqa: E501
        """EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._shortname_rus = None
        self._fullname_rus = None
        self._is_given_country = None
        self._counter = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus
        if is_given_country is not None:
            self.is_given_country = is_given_country
        if counter is not None:
            self.counter = counter

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501

        ID типа  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.

        ID типа  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501

        Краткое наименование типа  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.

        Краткое наименование типа  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501

        Полное наименование типа  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.

        Полное наименование типа  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

    @property
    def is_given_country(self):
        """Gets the is_given_country of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501

        Признак, что тип категории связан со странами (каждой категории в типе должна быть сопоставлена одна страна)  # noqa: E501

        :return: The is_given_country of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :rtype: int
        """
        return self._is_given_country

    @is_given_country.setter
    def is_given_country(self, is_given_country):
        """Sets the is_given_country of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.

        Признак, что тип категории связан со странами (каждой категории в типе должна быть сопоставлена одна страна)  # noqa: E501

        :param is_given_country: The is_given_country of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :type: int
        """

        self._is_given_country = is_given_country

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsDictionaryEmitentTypeCategoryFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other