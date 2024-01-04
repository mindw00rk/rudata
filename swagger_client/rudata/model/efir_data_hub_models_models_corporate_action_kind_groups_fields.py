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

class EfirDataHubModelsModelsCorporateActionKindGroupsFields(object):
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
        'code': 'str',
        'name_rus': 'str',
        'name_eng': 'str',
        'order_group': 'int'
    }

    attribute_map = {
        'code': 'code',
        'name_rus': 'name_rus',
        'name_eng': 'name_eng',
        'order_group': 'order_group'
    }

    def __init__(self, code=None, name_rus=None, name_eng=None, order_group=None):  # noqa: E501
        """EfirDataHubModelsModelsCorporateActionKindGroupsFields - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name_rus = None
        self._name_eng = None
        self._order_group = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name_rus is not None:
            self.name_rus = name_rus
        if name_eng is not None:
            self.name_eng = name_eng
        if order_group is not None:
            self.order_group = order_group

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501

        Символьный идентификатор группы  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.

        Символьный идентификатор группы  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name_rus(self):
        """Gets the name_rus of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501

        Наименование группы (рус.)  # noqa: E501

        :return: The name_rus of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :rtype: str
        """
        return self._name_rus

    @name_rus.setter
    def name_rus(self, name_rus):
        """Sets the name_rus of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.

        Наименование группы (рус.)  # noqa: E501

        :param name_rus: The name_rus of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :type: str
        """

        self._name_rus = name_rus

    @property
    def name_eng(self):
        """Gets the name_eng of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501

        Наименование группы (англ.)  # noqa: E501

        :return: The name_eng of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :rtype: str
        """
        return self._name_eng

    @name_eng.setter
    def name_eng(self, name_eng):
        """Sets the name_eng of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.

        Наименование группы (англ.)  # noqa: E501

        :param name_eng: The name_eng of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :type: str
        """

        self._name_eng = name_eng

    @property
    def order_group(self):
        """Gets the order_group of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501

        Порядковый номер группы  # noqa: E501

        :return: The order_group of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :rtype: int
        """
        return self._order_group

    @order_group.setter
    def order_group(self, order_group):
        """Sets the order_group of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.

        Порядковый номер группы  # noqa: E501

        :param order_group: The order_group of this EfirDataHubModelsModelsCorporateActionKindGroupsFields.  # noqa: E501
        :type: int
        """

        self._order_group = order_group

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
        if issubclass(EfirDataHubModelsModelsCorporateActionKindGroupsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsCorporateActionKindGroupsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
