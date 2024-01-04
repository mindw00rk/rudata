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

class EfirDataHubModelsModelsRatingAggregationScaleMappingFields(object):
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
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, id=None, code=None, name=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingAggregationScaleMappingFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._code = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501

        Идентификатор соотношения  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.

        Идентификатор соотношения  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501

        Код соотношения  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.

        Код соотношения  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501

        Наименование соотношения  # noqa: E501

        :return: The name of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.

        Наименование соотношения  # noqa: E501

        :param name: The name of this EfirDataHubModelsModelsRatingAggregationScaleMappingFields.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(EfirDataHubModelsModelsRatingAggregationScaleMappingFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingAggregationScaleMappingFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other