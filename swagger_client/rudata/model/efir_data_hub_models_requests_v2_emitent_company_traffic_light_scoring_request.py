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

class EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest(object):
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
        'fininst_ids': 'list[int]',
        'codes': 'list[str]',
        'actual_on_date': 'datetime',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'fininst_ids': 'fininstIds',
        'codes': 'codes',
        'actual_on_date': 'actualOnDate',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, fininst_ids=None, codes=None, actual_on_date=None, page_num=None, page_size=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest - a model defined in Swagger"""  # noqa: E501
        self._fininst_ids = None
        self._codes = None
        self._actual_on_date = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None
        if fininst_ids is not None:
            self.fininst_ids = fininst_ids
        if codes is not None:
            self.codes = codes
        if actual_on_date is not None:
            self.actual_on_date = actual_on_date
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def fininst_ids(self):
        """Gets the fininst_ids of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501

        Список идентификаторов эмитентов.  Не более 100 элементов.  Если задан, то Codes не используется.  # noqa: E501

        :return: The fininst_ids of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fininst_ids

    @fininst_ids.setter
    def fininst_ids(self, fininst_ids):
        """Sets the fininst_ids of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.

        Список идентификаторов эмитентов.  Не более 100 элементов.  Если задан, то Codes не используется.  # noqa: E501

        :param fininst_ids: The fininst_ids of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :type: list[int]
        """

        self._fininst_ids = fininst_ids

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501

        Список кодов эмитентов (ИНН, ОГРН или LEI).  Не более 100 элементов.  Если задан FininstIds, то не используется.  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.

        Список кодов эмитентов (ИНН, ОГРН или LEI).  Не более 100 элементов.  Если задан FininstIds, то не используется.  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def actual_on_date(self):
        """Gets the actual_on_date of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501

        Дата, на которую актуальны показатели кредитной оценки.  По умолчанию - текущая дата.  # noqa: E501

        :return: The actual_on_date of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._actual_on_date

    @actual_on_date.setter
    def actual_on_date(self, actual_on_date):
        """Sets the actual_on_date of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.

        Дата, на которую актуальны показатели кредитной оценки.  По умолчанию - текущая дата.  # noqa: E501

        :param actual_on_date: The actual_on_date of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :type: datetime
        """

        self._actual_on_date = actual_on_date

    @property
    def page_num(self):
        """Gets the page_num of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501

        Номер страницы выборки. По-умолчанию - 1  # noqa: E501

        :return: The page_num of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.

        Номер страницы выборки. По-умолчанию - 1  # noqa: E501

        :param page_num: The page_num of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501

        Размер страницы выборки. По-умолчанию - 100.  Максимум - 100.  # noqa: E501

        :return: The page_size of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.

        Размер страницы выборки. По-умолчанию - 100.  Максимум - 100.  # noqa: E501

        :param page_size: The page_size of this EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest.  # noqa: E501
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
        if issubclass(EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2EmitentCompanyTrafficLightScoringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other