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

class EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase(object):
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
        'parent_sparkid': 'int',
        'parent_fininstid': 'int',
        'parent_inn': 'str',
        'parent_ishead': 'bool',
        'child_sparkid': 'int',
        'child_fininstid': 'int',
        'child_inn': 'str',
        'child_ismanaged': 'bool',
        'chainlink_num': 'int',
        'parent_counterpartyid': 'int',
        'child_counterpartyid': 'int'
    }

    attribute_map = {
        'parent_sparkid': 'parent_sparkid',
        'parent_fininstid': 'parent_fininstid',
        'parent_inn': 'parent_inn',
        'parent_ishead': 'parent_ishead',
        'child_sparkid': 'child_sparkid',
        'child_fininstid': 'child_fininstid',
        'child_inn': 'child_inn',
        'child_ismanaged': 'child_ismanaged',
        'chainlink_num': 'chainlink_num',
        'parent_counterpartyid': 'parent_counterpartyid',
        'child_counterpartyid': 'child_counterpartyid'
    }

    def __init__(self, parent_sparkid=None, parent_fininstid=None, parent_inn=None, parent_ishead=None, child_sparkid=None, child_fininstid=None, child_inn=None, child_ismanaged=None, chainlink_num=None, parent_counterpartyid=None, child_counterpartyid=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase - a model defined in Swagger"""  # noqa: E501
        self._parent_sparkid = None
        self._parent_fininstid = None
        self._parent_inn = None
        self._parent_ishead = None
        self._child_sparkid = None
        self._child_fininstid = None
        self._child_inn = None
        self._child_ismanaged = None
        self._chainlink_num = None
        self._parent_counterpartyid = None
        self._child_counterpartyid = None
        self.discriminator = None
        if parent_sparkid is not None:
            self.parent_sparkid = parent_sparkid
        if parent_fininstid is not None:
            self.parent_fininstid = parent_fininstid
        if parent_inn is not None:
            self.parent_inn = parent_inn
        if parent_ishead is not None:
            self.parent_ishead = parent_ishead
        if child_sparkid is not None:
            self.child_sparkid = child_sparkid
        if child_fininstid is not None:
            self.child_fininstid = child_fininstid
        if child_inn is not None:
            self.child_inn = child_inn
        if child_ismanaged is not None:
            self.child_ismanaged = child_ismanaged
        if chainlink_num is not None:
            self.chainlink_num = chainlink_num
        if parent_counterpartyid is not None:
            self.parent_counterpartyid = parent_counterpartyid
        if child_counterpartyid is not None:
            self.child_counterpartyid = child_counterpartyid

    @property
    def parent_sparkid(self):
        """Gets the parent_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор СПАРК родительской компании  # noqa: E501

        :return: The parent_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._parent_sparkid

    @parent_sparkid.setter
    def parent_sparkid(self, parent_sparkid):
        """Sets the parent_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор СПАРК родительской компании  # noqa: E501

        :param parent_sparkid: The parent_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._parent_sparkid = parent_sparkid

    @property
    def parent_fininstid(self):
        """Gets the parent_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор Интерфакс родительской компании  # noqa: E501

        :return: The parent_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._parent_fininstid

    @parent_fininstid.setter
    def parent_fininstid(self, parent_fininstid):
        """Sets the parent_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор Интерфакс родительской компании  # noqa: E501

        :param parent_fininstid: The parent_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._parent_fininstid = parent_fininstid

    @property
    def parent_inn(self):
        """Gets the parent_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        ИНН родительской компании  # noqa: E501

        :return: The parent_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: str
        """
        return self._parent_inn

    @parent_inn.setter
    def parent_inn(self, parent_inn):
        """Sets the parent_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        ИНН родительской компании  # noqa: E501

        :param parent_inn: The parent_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: str
        """

        self._parent_inn = parent_inn

    @property
    def parent_ishead(self):
        """Gets the parent_ishead of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Признак головной компании для родительской компании  # noqa: E501

        :return: The parent_ishead of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: bool
        """
        return self._parent_ishead

    @parent_ishead.setter
    def parent_ishead(self, parent_ishead):
        """Sets the parent_ishead of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Признак головной компании для родительской компании  # noqa: E501

        :param parent_ishead: The parent_ishead of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: bool
        """

        self._parent_ishead = parent_ishead

    @property
    def child_sparkid(self):
        """Gets the child_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор СПАРК дочерней компании  # noqa: E501

        :return: The child_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._child_sparkid

    @child_sparkid.setter
    def child_sparkid(self, child_sparkid):
        """Sets the child_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор СПАРК дочерней компании  # noqa: E501

        :param child_sparkid: The child_sparkid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._child_sparkid = child_sparkid

    @property
    def child_fininstid(self):
        """Gets the child_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор Интерфакс дочерней компании  # noqa: E501

        :return: The child_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._child_fininstid

    @child_fininstid.setter
    def child_fininstid(self, child_fininstid):
        """Sets the child_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор Интерфакс дочерней компании  # noqa: E501

        :param child_fininstid: The child_fininstid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._child_fininstid = child_fininstid

    @property
    def child_inn(self):
        """Gets the child_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        ИНН дочерней компании  # noqa: E501

        :return: The child_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: str
        """
        return self._child_inn

    @child_inn.setter
    def child_inn(self, child_inn):
        """Sets the child_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        ИНН дочерней компании  # noqa: E501

        :param child_inn: The child_inn of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: str
        """

        self._child_inn = child_inn

    @property
    def child_ismanaged(self):
        """Gets the child_ismanaged of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Флаг управления дочерней компанией  # noqa: E501

        :return: The child_ismanaged of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: bool
        """
        return self._child_ismanaged

    @child_ismanaged.setter
    def child_ismanaged(self, child_ismanaged):
        """Sets the child_ismanaged of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Флаг управления дочерней компанией  # noqa: E501

        :param child_ismanaged: The child_ismanaged of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: bool
        """

        self._child_ismanaged = child_ismanaged

    @property
    def chainlink_num(self):
        """Gets the chainlink_num of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Порядковый номер звена цепочки (снизу наверх)  # noqa: E501

        :return: The chainlink_num of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._chainlink_num

    @chainlink_num.setter
    def chainlink_num(self, chainlink_num):
        """Sets the chainlink_num of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Порядковый номер звена цепочки (снизу наверх)  # noqa: E501

        :param chainlink_num: The chainlink_num of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._chainlink_num = chainlink_num

    @property
    def parent_counterpartyid(self):
        """Gets the parent_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор контрагента родительской компании  # noqa: E501

        :return: The parent_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._parent_counterpartyid

    @parent_counterpartyid.setter
    def parent_counterpartyid(self, parent_counterpartyid):
        """Sets the parent_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор контрагента родительской компании  # noqa: E501

        :param parent_counterpartyid: The parent_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._parent_counterpartyid = parent_counterpartyid

    @property
    def child_counterpartyid(self):
        """Gets the child_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501

        Идентификатор контрагента дочерней компании  # noqa: E501

        :return: The child_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :rtype: int
        """
        return self._child_counterpartyid

    @child_counterpartyid.setter
    def child_counterpartyid(self, child_counterpartyid):
        """Sets the child_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.

        Идентификатор контрагента дочерней компании  # noqa: E501

        :param child_counterpartyid: The child_counterpartyid of this EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase.  # noqa: E501
        :type: int
        """

        self._child_counterpartyid = child_counterpartyid

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
        if issubclass(EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentCompanyGroupChainLinkBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other