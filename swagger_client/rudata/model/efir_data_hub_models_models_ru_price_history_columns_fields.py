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

class EfirDataHubModelsModelsRUPriceHistoryColumnsFields(object):
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
        'id_group': 'int',
        'codename': 'str',
        'shortname_rus': 'str',
        'fullname_rus': 'str',
        'shortname_nrd': 'str',
        'field_remark': 'str',
        'sort_order': 'int',
        'shortname_eng': 'str',
        'fullname_eng': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_group': 'id_group',
        'codename': 'codename',
        'shortname_rus': 'shortname_rus',
        'fullname_rus': 'fullname_rus',
        'shortname_nrd': 'shortname_nrd',
        'field_remark': 'field_remark',
        'sort_order': 'sort_order',
        'shortname_eng': 'shortname_eng',
        'fullname_eng': 'fullname_eng'
    }

    def __init__(self, id=None, id_group=None, codename=None, shortname_rus=None, fullname_rus=None, shortname_nrd=None, field_remark=None, sort_order=None, shortname_eng=None, fullname_eng=None):  # noqa: E501
        """EfirDataHubModelsModelsRUPriceHistoryColumnsFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_group = None
        self._codename = None
        self._shortname_rus = None
        self._fullname_rus = None
        self._shortname_nrd = None
        self._field_remark = None
        self._sort_order = None
        self._shortname_eng = None
        self._fullname_eng = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_group is not None:
            self.id_group = id_group
        if codename is not None:
            self.codename = codename
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus
        if shortname_nrd is not None:
            self.shortname_nrd = shortname_nrd
        if field_remark is not None:
            self.field_remark = field_remark
        if sort_order is not None:
            self.sort_order = sort_order
        if shortname_eng is not None:
            self.shortname_eng = shortname_eng
        if fullname_eng is not None:
            self.fullname_eng = fullname_eng

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Идентификатор поля  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Идентификатор поля  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_group(self):
        """Gets the id_group of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Идентификатор группы  # noqa: E501

        :return: The id_group of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: int
        """
        return self._id_group

    @id_group.setter
    def id_group(self, id_group):
        """Sets the id_group of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Идентификатор группы  # noqa: E501

        :param id_group: The id_group of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: int
        """

        self._id_group = id_group

    @property
    def codename(self):
        """Gets the codename of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Символьный код поля  # noqa: E501

        :return: The codename of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._codename

    @codename.setter
    def codename(self, codename):
        """Sets the codename of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Символьный код поля  # noqa: E501

        :param codename: The codename of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._codename = codename

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Короткое имя на русском  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Короткое имя на русском  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Полное название на русском  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Полное название на русском  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

    @property
    def shortname_nrd(self):
        """Gets the shortname_nrd of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Наименование поля в НРД  # noqa: E501

        :return: The shortname_nrd of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_nrd

    @shortname_nrd.setter
    def shortname_nrd(self, shortname_nrd):
        """Sets the shortname_nrd of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Наименование поля в НРД  # noqa: E501

        :param shortname_nrd: The shortname_nrd of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._shortname_nrd = shortname_nrd

    @property
    def field_remark(self):
        """Gets the field_remark of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Примечание (ссылка на методику)  # noqa: E501

        :return: The field_remark of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._field_remark

    @field_remark.setter
    def field_remark(self, field_remark):
        """Sets the field_remark of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Примечание (ссылка на методику)  # noqa: E501

        :param field_remark: The field_remark of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._field_remark = field_remark

    @property
    def sort_order(self):
        """Gets the sort_order of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Порядок сортировки (для удобства UI)  # noqa: E501

        :return: The sort_order of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Порядок сортировки (для удобства UI)  # noqa: E501

        :param sort_order: The sort_order of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def shortname_eng(self):
        """Gets the shortname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Короткое имя на английском  # noqa: E501

        :return: The shortname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_eng

    @shortname_eng.setter
    def shortname_eng(self, shortname_eng):
        """Sets the shortname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Короткое имя на английском  # noqa: E501

        :param shortname_eng: The shortname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._shortname_eng = shortname_eng

    @property
    def fullname_eng(self):
        """Gets the fullname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501

        Полное название на английском  # noqa: E501

        :return: The fullname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_eng

    @fullname_eng.setter
    def fullname_eng(self, fullname_eng):
        """Sets the fullname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.

        Полное название на английском  # noqa: E501

        :param fullname_eng: The fullname_eng of this EfirDataHubModelsModelsRUPriceHistoryColumnsFields.  # noqa: E501
        :type: str
        """

        self._fullname_eng = fullname_eng

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
        if issubclass(EfirDataHubModelsModelsRUPriceHistoryColumnsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRUPriceHistoryColumnsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
