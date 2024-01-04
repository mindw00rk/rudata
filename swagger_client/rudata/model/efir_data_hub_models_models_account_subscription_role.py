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

class EfirDataHubModelsModelsAccountSubscriptionRole(object):
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
        'role_id': 'int',
        'user_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'role_id': 'roleId',
        'user_id': 'userId',
        'name': 'name'
    }

    def __init__(self, role_id=None, user_id=None, name=None):  # noqa: E501
        """EfirDataHubModelsModelsAccountSubscriptionRole - a model defined in Swagger"""  # noqa: E501
        self._role_id = None
        self._user_id = None
        self._name = None
        self.discriminator = None
        if role_id is not None:
            self.role_id = role_id
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name

    @property
    def role_id(self):
        """Gets the role_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501


        :return: The role_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this EfirDataHubModelsModelsAccountSubscriptionRole.


        :param role_id: The role_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def user_id(self):
        """Gets the user_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501


        :return: The user_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EfirDataHubModelsModelsAccountSubscriptionRole.


        :param user_id: The user_id of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501


        :return: The name of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EfirDataHubModelsModelsAccountSubscriptionRole.


        :param name: The name of this EfirDataHubModelsModelsAccountSubscriptionRole.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsAccountSubscriptionRole, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsAccountSubscriptionRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other