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

class EfirDataHubModelsModelsDictionaryCategoryFields(object):
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
        'id_type_category': 'int',
        'id_category': 'int',
        'is_main': 'bool'
    }

    attribute_map = {
        'id_type_category': 'id_type_category',
        'id_category': 'id_category',
        'is_main': 'is_main'
    }

    def __init__(self, id_type_category=None, id_category=None, is_main=None):  # noqa: E501
        """EfirDataHubModelsModelsDictionaryCategoryFields - a model defined in Swagger"""  # noqa: E501
        self._id_type_category = None
        self._id_category = None
        self._is_main = None
        self.discriminator = None
        if id_type_category is not None:
            self.id_type_category = id_type_category
        if id_category is not None:
            self.id_category = id_category
        if is_main is not None:
            self.is_main = is_main

    @property
    def id_type_category(self):
        """Gets the id_type_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501

        ID типа категории  # noqa: E501

        :return: The id_type_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :rtype: int
        """
        return self._id_type_category

    @id_type_category.setter
    def id_type_category(self, id_type_category):
        """Sets the id_type_category of this EfirDataHubModelsModelsDictionaryCategoryFields.

        ID типа категории  # noqa: E501

        :param id_type_category: The id_type_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :type: int
        """

        self._id_type_category = id_type_category

    @property
    def id_category(self):
        """Gets the id_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501

        ID категории  # noqa: E501

        :return: The id_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :rtype: int
        """
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        """Sets the id_category of this EfirDataHubModelsModelsDictionaryCategoryFields.

        ID категории  # noqa: E501

        :param id_category: The id_category of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :type: int
        """

        self._id_category = id_category

    @property
    def is_main(self):
        """Gets the is_main of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501

        Признак, что категория является основной  # noqa: E501

        :return: The is_main of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this EfirDataHubModelsModelsDictionaryCategoryFields.

        Признак, что категория является основной  # noqa: E501

        :param is_main: The is_main of this EfirDataHubModelsModelsDictionaryCategoryFields.  # noqa: E501
        :type: bool
        """

        self._is_main = is_main

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
        if issubclass(EfirDataHubModelsModelsDictionaryCategoryFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsDictionaryCategoryFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
