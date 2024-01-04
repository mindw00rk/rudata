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

class EfirDataHubModelsModelsRatingAggregationListFields(object):
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
        'id_list': 'int',
        'id_rating': 'int',
        'id_scale': 'int',
        'code_name': 'str',
        'for_instrument': 'bool',
        'for_company': 'bool',
        'aggregation_type': 'str'
    }

    attribute_map = {
        'id_list': 'id_list',
        'id_rating': 'id_rating',
        'id_scale': 'id_scale',
        'code_name': 'code_name',
        'for_instrument': 'for_instrument',
        'for_company': 'for_company',
        'aggregation_type': 'aggregation_type'
    }

    def __init__(self, id_list=None, id_rating=None, id_scale=None, code_name=None, for_instrument=None, for_company=None, aggregation_type=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingAggregationListFields - a model defined in Swagger"""  # noqa: E501
        self._id_list = None
        self._id_rating = None
        self._id_scale = None
        self._code_name = None
        self._for_instrument = None
        self._for_company = None
        self._aggregation_type = None
        self.discriminator = None
        if id_list is not None:
            self.id_list = id_list
        if id_rating is not None:
            self.id_rating = id_rating
        if id_scale is not None:
            self.id_scale = id_scale
        if code_name is not None:
            self.code_name = code_name
        if for_instrument is not None:
            self.for_instrument = for_instrument
        if for_company is not None:
            self.for_company = for_company
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type

    @property
    def id_list(self):
        """Gets the id_list of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        Идентификатор списка  # noqa: E501

        :return: The id_list of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: int
        """
        return self._id_list

    @id_list.setter
    def id_list(self, id_list):
        """Sets the id_list of this EfirDataHubModelsModelsRatingAggregationListFields.

        Идентификатор списка  # noqa: E501

        :param id_list: The id_list of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: int
        """

        self._id_list = id_list

    @property
    def id_rating(self):
        """Gets the id_rating of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        Идентификатор рейтинга  # noqa: E501

        :return: The id_rating of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: int
        """
        return self._id_rating

    @id_rating.setter
    def id_rating(self, id_rating):
        """Sets the id_rating of this EfirDataHubModelsModelsRatingAggregationListFields.

        Идентификатор рейтинга  # noqa: E501

        :param id_rating: The id_rating of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: int
        """

        self._id_rating = id_rating

    @property
    def id_scale(self):
        """Gets the id_scale of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        Идентификатор рейтинговой шкалы  # noqa: E501

        :return: The id_scale of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: int
        """
        return self._id_scale

    @id_scale.setter
    def id_scale(self, id_scale):
        """Sets the id_scale of this EfirDataHubModelsModelsRatingAggregationListFields.

        Идентификатор рейтинговой шкалы  # noqa: E501

        :param id_scale: The id_scale of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: int
        """

        self._id_scale = id_scale

    @property
    def code_name(self):
        """Gets the code_name of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        Кодовое наименование рейтинга  # noqa: E501

        :return: The code_name of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        """Sets the code_name of this EfirDataHubModelsModelsRatingAggregationListFields.

        Кодовое наименование рейтинга  # noqa: E501

        :param code_name: The code_name of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: str
        """

        self._code_name = code_name

    @property
    def for_instrument(self):
        """Gets the for_instrument of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        true, если рейтинг относится к инструменту  # noqa: E501

        :return: The for_instrument of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: bool
        """
        return self._for_instrument

    @for_instrument.setter
    def for_instrument(self, for_instrument):
        """Sets the for_instrument of this EfirDataHubModelsModelsRatingAggregationListFields.

        true, если рейтинг относится к инструменту  # noqa: E501

        :param for_instrument: The for_instrument of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: bool
        """

        self._for_instrument = for_instrument

    @property
    def for_company(self):
        """Gets the for_company of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        true, если рейтинг относится к компании  # noqa: E501

        :return: The for_company of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: bool
        """
        return self._for_company

    @for_company.setter
    def for_company(self, for_company):
        """Sets the for_company of this EfirDataHubModelsModelsRatingAggregationListFields.

        true, если рейтинг относится к компании  # noqa: E501

        :param for_company: The for_company of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: bool
        """

        self._for_company = for_company

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501

        Тип агрегации. Допустимые значения: RU, BIG3  # noqa: E501

        :return: The aggregation_type of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this EfirDataHubModelsModelsRatingAggregationListFields.

        Тип агрегации. Допустимые значения: RU, BIG3  # noqa: E501

        :param aggregation_type: The aggregation_type of this EfirDataHubModelsModelsRatingAggregationListFields.  # noqa: E501
        :type: str
        """

        self._aggregation_type = aggregation_type

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
        if issubclass(EfirDataHubModelsModelsRatingAggregationListFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingAggregationListFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other