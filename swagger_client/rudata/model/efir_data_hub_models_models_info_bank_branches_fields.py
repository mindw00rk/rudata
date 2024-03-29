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

class EfirDataHubModelsModelsInfoBankBranchesFields(object):
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
        'fininstid': 'int',
        'bank_name': 'str',
        'bank_regnum': 'str',
        'branchid': 'int',
        'branch_name': 'str',
        'branch_address': 'str',
        'contactid': 'int',
        'latitude': 'str',
        'longitude': 'str'
    }

    attribute_map = {
        'fininstid': 'fininstid',
        'bank_name': 'bank_name',
        'bank_regnum': 'bank_regnum',
        'branchid': 'branchid',
        'branch_name': 'branch_name',
        'branch_address': 'branch_address',
        'contactid': 'contactid',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, fininstid=None, bank_name=None, bank_regnum=None, branchid=None, branch_name=None, branch_address=None, contactid=None, latitude=None, longitude=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoBankBranchesFields - a model defined in Swagger"""  # noqa: E501
        self._fininstid = None
        self._bank_name = None
        self._bank_regnum = None
        self._branchid = None
        self._branch_name = None
        self._branch_address = None
        self._contactid = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None
        if fininstid is not None:
            self.fininstid = fininstid
        if bank_name is not None:
            self.bank_name = bank_name
        if bank_regnum is not None:
            self.bank_regnum = bank_regnum
        if branchid is not None:
            self.branchid = branchid
        if branch_name is not None:
            self.branch_name = branch_name
        if branch_address is not None:
            self.branch_address = branch_address
        if contactid is not None:
            self.contactid = contactid
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Идентификатор банка в базе Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Идентификатор банка в базе Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def bank_name(self):
        """Gets the bank_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Наименование банка  # noqa: E501

        :return: The bank_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Наименование банка  # noqa: E501

        :param bank_name: The bank_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bank_regnum(self):
        """Gets the bank_regnum of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Регистрационный номер банка (номер лицензии)  # noqa: E501

        :return: The bank_regnum of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._bank_regnum

    @bank_regnum.setter
    def bank_regnum(self, bank_regnum):
        """Sets the bank_regnum of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Регистрационный номер банка (номер лицензии)  # noqa: E501

        :param bank_regnum: The bank_regnum of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._bank_regnum = bank_regnum

    @property
    def branchid(self):
        """Gets the branchid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Идентификатор отделения  # noqa: E501

        :return: The branchid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: int
        """
        return self._branchid

    @branchid.setter
    def branchid(self, branchid):
        """Sets the branchid of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Идентификатор отделения  # noqa: E501

        :param branchid: The branchid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: int
        """

        self._branchid = branchid

    @property
    def branch_name(self):
        """Gets the branch_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Наименование отделения  # noqa: E501

        :return: The branch_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Наименование отделения  # noqa: E501

        :param branch_name: The branch_name of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._branch_name = branch_name

    @property
    def branch_address(self):
        """Gets the branch_address of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Адрес отделения  # noqa: E501

        :return: The branch_address of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._branch_address

    @branch_address.setter
    def branch_address(self, branch_address):
        """Sets the branch_address of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Адрес отделения  # noqa: E501

        :param branch_address: The branch_address of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._branch_address = branch_address

    @property
    def contactid(self):
        """Gets the contactid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Идентификатор группы курсов в рамках банка/отделения  # noqa: E501

        :return: The contactid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: int
        """
        return self._contactid

    @contactid.setter
    def contactid(self, contactid):
        """Sets the contactid of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Идентификатор группы курсов в рамках банка/отделения  # noqa: E501

        :param contactid: The contactid of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: int
        """

        self._contactid = contactid

    @property
    def latitude(self):
        """Gets the latitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Координата отделения – широта  # noqa: E501

        :return: The latitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Координата отделения – широта  # noqa: E501

        :param latitude: The latitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501

        Координата отделения – долгота  # noqa: E501

        :return: The longitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this EfirDataHubModelsModelsInfoBankBranchesFields.

        Координата отделения – долгота  # noqa: E501

        :param longitude: The longitude of this EfirDataHubModelsModelsInfoBankBranchesFields.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

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
        if issubclass(EfirDataHubModelsModelsInfoBankBranchesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoBankBranchesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
