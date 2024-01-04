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

class EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest(object):
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
        'actual_date': 'datetime',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'actual_date': 'actualDate',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, actual_date=None, page_num=1, page_size=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest - a model defined in Swagger"""  # noqa: E501
        self._actual_date = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if actual_date is not None:
            self.actual_date = actual_date
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def actual_date(self):
        """Gets the actual_date of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501

        Дата вызова, на которую актуален ответ метода  # noqa: E501

        :return: The actual_date of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_date

    @actual_date.setter
    def actual_date(self, actual_date):
        """Sets the actual_date of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.

        Дата вызова, на которую актуален ответ метода  # noqa: E501

        :param actual_date: The actual_date of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_date = actual_date

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501

        Номер страницы выборки(1 по-умолчанию)  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.

        Номер страницы выборки(1 по-умолчанию)  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501

        Размер страницы выборки(100 по умолчанию). Не более 100.  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.

        Размер страницы выборки(100 по умолчанию). Не более 100.  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2AffiliatesCompanyGroupRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other