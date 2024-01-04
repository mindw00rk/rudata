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

class EfirDataHubModelsModelsInfoEnumValuesFields(object):
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
        'val': 'str',
        'fullname_rus': 'str',
        'val_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'val': 'val',
        'fullname_rus': 'fullname_rus',
        'val_id': 'val_id'
    }

    def __init__(self, id=None, val=None, fullname_rus=None, val_id=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoEnumValuesFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._val = None
        self._fullname_rus = None
        self._val_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if val is not None:
            self.val = val
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus
        if val_id is not None:
            self.val_id = val_id

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501

        Идентификатор значения  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsInfoEnumValuesFields.

        Идентификатор значения  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def val(self):
        """Gets the val of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501

        Значение  # noqa: E501

        :return: The val of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val):
        """Sets the val of this EfirDataHubModelsModelsInfoEnumValuesFields.

        Значение  # noqa: E501

        :param val: The val of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :type: str
        """

        self._val = val

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501

        Наименование значения  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsInfoEnumValuesFields.

        Наименование значения  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

    @property
    def val_id(self):
        """Gets the val_id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501

        Идентификатор значения по классификатору Интерфакс  # noqa: E501

        :return: The val_id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :rtype: int
        """
        return self._val_id

    @val_id.setter
    def val_id(self, val_id):
        """Sets the val_id of this EfirDataHubModelsModelsInfoEnumValuesFields.

        Идентификатор значения по классификатору Интерфакс  # noqa: E501

        :param val_id: The val_id of this EfirDataHubModelsModelsInfoEnumValuesFields.  # noqa: E501
        :type: int
        """

        self._val_id = val_id

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
        if issubclass(EfirDataHubModelsModelsInfoEnumValuesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoEnumValuesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other