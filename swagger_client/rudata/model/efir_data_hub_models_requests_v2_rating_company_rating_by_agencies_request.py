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

class EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest(object):
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
        '_date': 'datetime',
        'agg_type': 'str',
        'rating_codes': 'list[str]',
        'rating_list_name': 'str'
    }

    attribute_map = {
        'fininst_ids': 'fininstIds',
        '_date': 'date',
        'agg_type': 'aggType',
        'rating_codes': 'ratingCodes',
        'rating_list_name': 'ratingListName'
    }

    def __init__(self, fininst_ids=None, _date=None, agg_type='MAX', rating_codes=None, rating_list_name=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest - a model defined in Swagger"""  # noqa: E501
        self._fininst_ids = None
        self.__date = None
        self._agg_type = None
        self._rating_codes = None
        self._rating_list_name = None
        self.discriminator = None
        self.fininst_ids = fininst_ids
        if _date is not None:
            self._date = _date
        if agg_type is not None:
            self.agg_type = agg_type
        if rating_codes is not None:
            self.rating_codes = rating_codes
        if rating_list_name is not None:
            self.rating_list_name = rating_list_name

    @property
    def fininst_ids(self):
        """Gets the fininst_ids of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501

        Идентификаторы компаний в базе Интерфакс;  Максимальное количество элементов: 100  # noqa: E501

        :return: The fininst_ids of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fininst_ids

    @fininst_ids.setter
    def fininst_ids(self, fininst_ids):
        """Sets the fininst_ids of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.

        Идентификаторы компаний в базе Интерфакс;  Максимальное количество элементов: 100  # noqa: E501

        :param fininst_ids: The fininst_ids of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :type: list[int]
        """
        if fininst_ids is None:
            raise ValueError("Invalid value for `fininst_ids`, must not be `None`")  # noqa: E501

        self._fininst_ids = fininst_ids

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501

        Дата, на которую получаются рейтинги; по умолчанию текущая  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.

        Дата, на которую получаются рейтинги; по умолчанию текущая  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def agg_type(self):
        """Gets the agg_type of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501

        Метод агрегации рейтингов:  - MAX - максимальный (по умолчанию);  - MIN - минимальный.  # noqa: E501

        :return: The agg_type of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :rtype: str
        """
        return self._agg_type

    @agg_type.setter
    def agg_type(self, agg_type):
        """Sets the agg_type of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.

        Метод агрегации рейтингов:  - MAX - максимальный (по умолчанию);  - MIN - минимальный.  # noqa: E501

        :param agg_type: The agg_type of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :type: str
        """

        self._agg_type = agg_type

    @property
    def rating_codes(self):
        """Gets the rating_codes of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501

        Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName.  # noqa: E501

        :return: The rating_codes of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._rating_codes

    @rating_codes.setter
    def rating_codes(self, rating_codes):
        """Sets the rating_codes of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.

        Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName.  # noqa: E501

        :param rating_codes: The rating_codes of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :type: list[str]
        """

        self._rating_codes = rating_codes

    @property
    def rating_list_name(self):
        """Gets the rating_list_name of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501

        Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists).  # noqa: E501

        :return: The rating_list_name of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :rtype: str
        """
        return self._rating_list_name

    @rating_list_name.setter
    def rating_list_name(self, rating_list_name):
        """Sets the rating_list_name of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.

        Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists).  # noqa: E501

        :param rating_list_name: The rating_list_name of this EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest.  # noqa: E501
        :type: str
        """

        self._rating_list_name = rating_list_name

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
        if issubclass(EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RatingCompanyRatingByAgenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other