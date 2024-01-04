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

class EfirDataHubModelsModelsInfoClassificationFields(object):
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
        'fintooltype': 'str',
        'securitytype': 'str',
        'securitykind': 'str',
        'fullname_rus': 'str',
        'count': 'int'
    }

    attribute_map = {
        'fintooltype': 'fintooltype',
        'securitytype': 'securitytype',
        'securitykind': 'securitykind',
        'fullname_rus': 'fullname_rus',
        'count': 'count'
    }

    def __init__(self, fintooltype=None, securitytype=None, securitykind=None, fullname_rus=None, count=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoClassificationFields - a model defined in Swagger"""  # noqa: E501
        self._fintooltype = None
        self._securitytype = None
        self._securitykind = None
        self._fullname_rus = None
        self._count = None
        self.discriminator = None
        if fintooltype is not None:
            self.fintooltype = fintooltype
        if securitytype is not None:
            self.securitytype = securitytype
        if securitykind is not None:
            self.securitykind = securitykind
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus
        if count is not None:
            self.count = count

    @property
    def fintooltype(self):
        """Gets the fintooltype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501

        Тип финансового инструмента (наименование).  # noqa: E501

        :return: The fintooltype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._fintooltype

    @fintooltype.setter
    def fintooltype(self, fintooltype):
        """Sets the fintooltype of this EfirDataHubModelsModelsInfoClassificationFields.

        Тип финансового инструмента (наименование).  # noqa: E501

        :param fintooltype: The fintooltype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :type: str
        """

        self._fintooltype = fintooltype

    @property
    def securitytype(self):
        """Gets the securitytype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501

        Тип выпуска/расписки/фонда  # noqa: E501

        :return: The securitytype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._securitytype

    @securitytype.setter
    def securitytype(self, securitytype):
        """Sets the securitytype of this EfirDataHubModelsModelsInfoClassificationFields.

        Тип выпуска/расписки/фонда  # noqa: E501

        :param securitytype: The securitytype of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :type: str
        """

        self._securitytype = securitytype

    @property
    def securitykind(self):
        """Gets the securitykind of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501

        Вид выпуска/спонсируемость/тип инвестиций  # noqa: E501

        :return: The securitykind of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._securitykind

    @securitykind.setter
    def securitykind(self, securitykind):
        """Sets the securitykind of this EfirDataHubModelsModelsInfoClassificationFields.

        Вид выпуска/спонсируемость/тип инвестиций  # noqa: E501

        :param securitykind: The securitykind of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :type: str
        """

        self._securitykind = securitykind

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501

        Наименование типа выпуска/расписки/фонда  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsInfoClassificationFields.

        Наименование типа выпуска/расписки/фонда  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

    @property
    def count(self):
        """Gets the count of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501

        Количество финансовых инструментов, соответствующих данной классификации  # noqa: E501

        :return: The count of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EfirDataHubModelsModelsInfoClassificationFields.

        Количество финансовых инструментов, соответствующих данной классификации  # noqa: E501

        :param count: The count of this EfirDataHubModelsModelsInfoClassificationFields.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(EfirDataHubModelsModelsInfoClassificationFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoClassificationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
