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

class EfirDataHubModelsRequestsV2SolvencyLicensesRequest(object):
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
        'ids': 'list[EfirDataHubModelsRequestsV2CounterpartyID]',
        '_date': 'datetime',
        'filter': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        '_date': 'date',
        'filter': 'filter',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, ids=None, _date=None, filter=None, page_num=None, page_size=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2SolvencyLicensesRequest - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self.__date = None
        self._filter = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids
        if _date is not None:
            self._date = _date
        if filter is not None:
            self.filter = filter
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def ids(self):
        """Gets the ids of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501

        Массив идентификаторов контрагента. Необязательный параметр. Если задан, то не более 100 объектов (пар идентификатор, тип идентификатора).  # noqa: E501

        :return: The ids of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :rtype: list[EfirDataHubModelsRequestsV2CounterpartyID]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.

        Массив идентификаторов контрагента. Необязательный параметр. Если задан, то не более 100 объектов (пар идентификатор, тип идентификатора).  # noqa: E501

        :param ids: The ids of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :type: list[EfirDataHubModelsRequestsV2CounterpartyID]
        """

        self._ids = ids

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501

        Дата расчета. Необязательный параметр.  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.

        Дата расчета. Необязательный параметр.  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def filter(self):
        """Gets the filter of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501

        Строка фильтрации по полям. Необязательный параметр.  # noqa: E501

        :return: The filter of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.

        Строка фильтрации по полям. Необязательный параметр.  # noqa: E501

        :param filter: The filter of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.

        Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.

        Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2SolvencyLicensesRequest.  # noqa: E501
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
        if issubclass(EfirDataHubModelsRequestsV2SolvencyLicensesRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2SolvencyLicensesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
