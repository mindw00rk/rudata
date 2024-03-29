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

class EfirDataHubModelsRequestsV2InfoPager(object):
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
        'page': 'int',
        'size': 'int',
        'sort': 'list[EfirDataHubModelsRequestsV2InfoSort]'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size',
        'sort': 'sort'
    }

    def __init__(self, page=None, size=None, sort=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2InfoPager - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._size = None
        self._sort = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if sort is not None:
            self.sort = sort

    @property
    def page(self):
        """Gets the page of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501

        Номер страницы выборки.  # noqa: E501

        :return: The page of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this EfirDataHubModelsRequestsV2InfoPager.

        Номер страницы выборки.  # noqa: E501

        :param page: The page of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def size(self):
        """Gets the size of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501

        Размер страницы выборки. Не более 1000.  # noqa: E501

        :return: The size of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EfirDataHubModelsRequestsV2InfoPager.

        Размер страницы выборки. Не более 1000.  # noqa: E501

        :param size: The size of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def sort(self):
        """Gets the sort of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501


        :return: The sort of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :rtype: list[EfirDataHubModelsRequestsV2InfoSort]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this EfirDataHubModelsRequestsV2InfoPager.


        :param sort: The sort of this EfirDataHubModelsRequestsV2InfoPager.  # noqa: E501
        :type: list[EfirDataHubModelsRequestsV2InfoSort]
        """

        self._sort = sort

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
        if issubclass(EfirDataHubModelsRequestsV2InfoPager, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2InfoPager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
