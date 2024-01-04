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

class EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest(object):
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
        'date_from': 'datetime',
        'date_to': 'datetime',
        'sort': 'int',
        'filter': 'str',
        'including_gov_org': 'bool',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'sort': 'sort',
        'filter': 'filter',
        'including_gov_org': 'including_gov_org',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, date_from=None, date_to=None, sort=None, filter=None, including_gov_org=None, page_num=None, page_size=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest - a model defined in Swagger"""  # noqa: E501
        self._date_from = None
        self._date_to = None
        self._sort = None
        self._filter = None
        self._including_gov_org = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if sort is not None:
            self.sort = sort
        if filter is not None:
            self.filter = filter
        if including_gov_org is not None:
            self.including_gov_org = including_gov_org
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def date_from(self):
        """Gets the date_from of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Дата начала периода  # noqa: E501

        :return: The date_from of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Дата начала периода  # noqa: E501

        :param date_from: The date_from of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: datetime
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Дата окончания периода  # noqa: E501

        :return: The date_to of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Дата окончания периода  # noqa: E501

        :param date_to: The date_to of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: datetime
        """

        self._date_to = date_to

    @property
    def sort(self):
        """Gets the sort of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Направление сортировки:  0 – от старых к новым  1 – от новых к старым  # noqa: E501

        :return: The sort of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Направление сортировки:  0 – от старых к новым  1 – от новых к старым  # noqa: E501

        :param sort: The sort of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: int
        """

        self._sort = sort

    @property
    def filter(self):
        """Gets the filter of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Строка фильтрации (необязательный)  # noqa: E501

        :return: The filter of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Строка фильтрации (необязательный)  # noqa: E501

        :param filter: The filter of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def including_gov_org(self):
        """Gets the including_gov_org of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Включая рейтинговые действия по правительственным организациям  # noqa: E501

        :return: The including_gov_org of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._including_gov_org

    @including_gov_org.setter
    def including_gov_org(self, including_gov_org):
        """Sets the including_gov_org of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Включая рейтинговые действия по правительственным организациям  # noqa: E501

        :param including_gov_org: The including_gov_org of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: bool
        """

        self._including_gov_org = including_gov_org

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest.  # noqa: E501
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
        if issubclass(EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
