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

class EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields(object):
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
        'group_id': 'int',
        'group_update_date': 'datetime',
        'member_sparkid': 'int',
        'member_fininstid': 'int',
        'member_inn': 'str',
        'group_short_name': 'str',
        'member_counterpartyid': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_update_date': 'group_update_date',
        'member_sparkid': 'member_sparkid',
        'member_fininstid': 'member_fininstid',
        'member_inn': 'member_inn',
        'group_short_name': 'group_short_name',
        'member_counterpartyid': 'member_counterpartyid'
    }

    def __init__(self, group_id=None, group_update_date=None, member_sparkid=None, member_fininstid=None, member_inn=None, group_short_name=None, member_counterpartyid=None):  # noqa: E501
        """EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._group_update_date = None
        self._member_sparkid = None
        self._member_fininstid = None
        self._member_inn = None
        self._group_short_name = None
        self._member_counterpartyid = None
        self.discriminator = None
        if group_id is not None:
            self.group_id = group_id
        if group_update_date is not None:
            self.group_update_date = group_update_date
        if member_sparkid is not None:
            self.member_sparkid = member_sparkid
        if member_fininstid is not None:
            self.member_fininstid = member_fininstid
        if member_inn is not None:
            self.member_inn = member_inn
        if group_short_name is not None:
            self.group_short_name = group_short_name
        if member_counterpartyid is not None:
            self.member_counterpartyid = member_counterpartyid

    @property
    def group_id(self):
        """Gets the group_id of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Идентификатор группы компаний  # noqa: E501

        :return: The group_id of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Идентификатор группы компаний  # noqa: E501

        :param group_id: The group_id of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def group_update_date(self):
        """Gets the group_update_date of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Дата обновления описания групп компаний  # noqa: E501

        :return: The group_update_date of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: datetime
        """
        return self._group_update_date

    @group_update_date.setter
    def group_update_date(self, group_update_date):
        """Sets the group_update_date of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Дата обновления описания групп компаний  # noqa: E501

        :param group_update_date: The group_update_date of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: datetime
        """

        self._group_update_date = group_update_date

    @property
    def member_sparkid(self):
        """Gets the member_sparkid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Идентификатор СПАРК компании группы  # noqa: E501

        :return: The member_sparkid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: int
        """
        return self._member_sparkid

    @member_sparkid.setter
    def member_sparkid(self, member_sparkid):
        """Sets the member_sparkid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Идентификатор СПАРК компании группы  # noqa: E501

        :param member_sparkid: The member_sparkid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: int
        """

        self._member_sparkid = member_sparkid

    @property
    def member_fininstid(self):
        """Gets the member_fininstid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Идентификатор в БД Эфир компании группы  # noqa: E501

        :return: The member_fininstid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: int
        """
        return self._member_fininstid

    @member_fininstid.setter
    def member_fininstid(self, member_fininstid):
        """Sets the member_fininstid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Идентификатор в БД Эфир компании группы  # noqa: E501

        :param member_fininstid: The member_fininstid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: int
        """

        self._member_fininstid = member_fininstid

    @property
    def member_inn(self):
        """Gets the member_inn of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        ИНН компании группы  # noqa: E501

        :return: The member_inn of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: str
        """
        return self._member_inn

    @member_inn.setter
    def member_inn(self, member_inn):
        """Sets the member_inn of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        ИНН компании группы  # noqa: E501

        :param member_inn: The member_inn of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: str
        """

        self._member_inn = member_inn

    @property
    def group_short_name(self):
        """Gets the group_short_name of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Наименование компании группы  # noqa: E501

        :return: The group_short_name of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: str
        """
        return self._group_short_name

    @group_short_name.setter
    def group_short_name(self, group_short_name):
        """Sets the group_short_name of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Наименование компании группы  # noqa: E501

        :param group_short_name: The group_short_name of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: str
        """

        self._group_short_name = group_short_name

    @property
    def member_counterpartyid(self):
        """Gets the member_counterpartyid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The member_counterpartyid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :rtype: int
        """
        return self._member_counterpartyid

    @member_counterpartyid.setter
    def member_counterpartyid(self, member_counterpartyid):
        """Sets the member_counterpartyid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.

        Идентификатор контрагента  # noqa: E501

        :param member_counterpartyid: The member_counterpartyid of this EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields.  # noqa: E501
        :type: int
        """

        self._member_counterpartyid = member_counterpartyid

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
        if issubclass(EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRuDataCompanyGroupsMembersFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other