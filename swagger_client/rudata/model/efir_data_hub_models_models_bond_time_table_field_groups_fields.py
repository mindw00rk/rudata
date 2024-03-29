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

class EfirDataHubModelsModelsBondTimeTableFieldGroupsFields(object):
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
        'name': 'str',
        'order_group': 'int',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'order_group': 'order_group',
        'remark': 'remark'
    }

    def __init__(self, id=None, name=None, order_group=None, remark=None):  # noqa: E501
        """EfirDataHubModelsModelsBondTimeTableFieldGroupsFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._order_group = None
        self._remark = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if order_group is not None:
            self.order_group = order_group
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501

        Идентификатор группы  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.

        Идентификатор группы  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501

        Наименование группы, англ.  # noqa: E501

        :return: The name of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.

        Наименование группы, англ.  # noqa: E501

        :param name: The name of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_group(self):
        """Gets the order_group of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501

        Номер по порядку  # noqa: E501

        :return: The order_group of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :rtype: int
        """
        return self._order_group

    @order_group.setter
    def order_group(self, order_group):
        """Sets the order_group of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.

        Номер по порядку  # noqa: E501

        :param order_group: The order_group of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :type: int
        """

        self._order_group = order_group

    @property
    def remark(self):
        """Gets the remark of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501

        Наименование группы, рус.  # noqa: E501

        :return: The remark of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.

        Наименование группы, рус.  # noqa: E501

        :param remark: The remark of this EfirDataHubModelsModelsBondTimeTableFieldGroupsFields.  # noqa: E501
        :type: str
        """

        self._remark = remark

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
        if issubclass(EfirDataHubModelsModelsBondTimeTableFieldGroupsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondTimeTableFieldGroupsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
