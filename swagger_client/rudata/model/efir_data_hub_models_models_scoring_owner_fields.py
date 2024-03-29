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

class EfirDataHubModelsModelsScoringOwnerFields(object):
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
        'company_shortname': 'str',
        'company_sparkid': 'int',
        'company_inn': 'str',
        'company_ogrn': 'str',
        'graph': 'list[EfirDataHubModelsModelsScoringGraph]',
        'owners': 'list[EfirDataHubModelsModelsScoringOwner]'
    }

    attribute_map = {
        'company_shortname': 'company_shortname',
        'company_sparkid': 'company_sparkid',
        'company_inn': 'company_inn',
        'company_ogrn': 'company_ogrn',
        'graph': 'graph',
        'owners': 'owners'
    }

    def __init__(self, company_shortname=None, company_sparkid=None, company_inn=None, company_ogrn=None, graph=None, owners=None):  # noqa: E501
        """EfirDataHubModelsModelsScoringOwnerFields - a model defined in Swagger"""  # noqa: E501
        self._company_shortname = None
        self._company_sparkid = None
        self._company_inn = None
        self._company_ogrn = None
        self._graph = None
        self._owners = None
        self.discriminator = None
        if company_shortname is not None:
            self.company_shortname = company_shortname
        if company_sparkid is not None:
            self.company_sparkid = company_sparkid
        if company_inn is not None:
            self.company_inn = company_inn
        if company_ogrn is not None:
            self.company_ogrn = company_ogrn
        if graph is not None:
            self.graph = graph
        if owners is not None:
            self.owners = owners

    @property
    def company_shortname(self):
        """Gets the company_shortname of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        Краткое имя компании  # noqa: E501

        :return: The company_shortname of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: str
        """
        return self._company_shortname

    @company_shortname.setter
    def company_shortname(self, company_shortname):
        """Sets the company_shortname of this EfirDataHubModelsModelsScoringOwnerFields.

        Краткое имя компании  # noqa: E501

        :param company_shortname: The company_shortname of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: str
        """

        self._company_shortname = company_shortname

    @property
    def company_sparkid(self):
        """Gets the company_sparkid of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        Идентификатор компании в СПАРК  # noqa: E501

        :return: The company_sparkid of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: int
        """
        return self._company_sparkid

    @company_sparkid.setter
    def company_sparkid(self, company_sparkid):
        """Sets the company_sparkid of this EfirDataHubModelsModelsScoringOwnerFields.

        Идентификатор компании в СПАРК  # noqa: E501

        :param company_sparkid: The company_sparkid of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: int
        """

        self._company_sparkid = company_sparkid

    @property
    def company_inn(self):
        """Gets the company_inn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        ИНН  # noqa: E501

        :return: The company_inn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: str
        """
        return self._company_inn

    @company_inn.setter
    def company_inn(self, company_inn):
        """Sets the company_inn of this EfirDataHubModelsModelsScoringOwnerFields.

        ИНН  # noqa: E501

        :param company_inn: The company_inn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: str
        """

        self._company_inn = company_inn

    @property
    def company_ogrn(self):
        """Gets the company_ogrn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        ОГРН  # noqa: E501

        :return: The company_ogrn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: str
        """
        return self._company_ogrn

    @company_ogrn.setter
    def company_ogrn(self, company_ogrn):
        """Sets the company_ogrn of this EfirDataHubModelsModelsScoringOwnerFields.

        ОГРН  # noqa: E501

        :param company_ogrn: The company_ogrn of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: str
        """

        self._company_ogrn = company_ogrn

    @property
    def graph(self):
        """Gets the graph of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        Полный граф владения компанией  # noqa: E501

        :return: The graph of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsScoringGraph]
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this EfirDataHubModelsModelsScoringOwnerFields.

        Полный граф владения компанией  # noqa: E501

        :param graph: The graph of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: list[EfirDataHubModelsModelsScoringGraph]
        """

        self._graph = graph

    @property
    def owners(self):
        """Gets the owners of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501

        Массив описаний владельцев компании  # noqa: E501

        :return: The owners of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :rtype: list[EfirDataHubModelsModelsScoringOwner]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this EfirDataHubModelsModelsScoringOwnerFields.

        Массив описаний владельцев компании  # noqa: E501

        :param owners: The owners of this EfirDataHubModelsModelsScoringOwnerFields.  # noqa: E501
        :type: list[EfirDataHubModelsModelsScoringOwner]
        """

        self._owners = owners

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
        if issubclass(EfirDataHubModelsModelsScoringOwnerFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsScoringOwnerFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
