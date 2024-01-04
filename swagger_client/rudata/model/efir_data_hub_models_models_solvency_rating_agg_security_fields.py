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

class EfirDataHubModelsModelsSolvencyRatingAggSecurityFields(object):
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
        'fintool_id': 'int',
        'aggregated_rating_level': 'int',
        'rating_code': 'str',
        'rating_id': 'int',
        'rating_agency_id': 'int',
        'rating_scale_id': 'int',
        'rating_value': 'str',
        'rating_date': 'datetime'
    }

    attribute_map = {
        'fintool_id': 'fintoolId',
        'aggregated_rating_level': 'aggregatedRatingLevel',
        'rating_code': 'ratingCode',
        'rating_id': 'ratingId',
        'rating_agency_id': 'ratingAgencyId',
        'rating_scale_id': 'ratingScaleId',
        'rating_value': 'ratingValue',
        'rating_date': 'ratingDate'
    }

    def __init__(self, fintool_id=None, aggregated_rating_level=None, rating_code=None, rating_id=None, rating_agency_id=None, rating_scale_id=None, rating_value=None, rating_date=None):  # noqa: E501
        """EfirDataHubModelsModelsSolvencyRatingAggSecurityFields - a model defined in Swagger"""  # noqa: E501
        self._fintool_id = None
        self._aggregated_rating_level = None
        self._rating_code = None
        self._rating_id = None
        self._rating_agency_id = None
        self._rating_scale_id = None
        self._rating_value = None
        self._rating_date = None
        self.discriminator = None
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if aggregated_rating_level is not None:
            self.aggregated_rating_level = aggregated_rating_level
        if rating_code is not None:
            self.rating_code = rating_code
        if rating_id is not None:
            self.rating_id = rating_id
        if rating_agency_id is not None:
            self.rating_agency_id = rating_agency_id
        if rating_scale_id is not None:
            self.rating_scale_id = rating_scale_id
        if rating_value is not None:
            self.rating_value = rating_value
        if rating_date is not None:
            self.rating_date = rating_date

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def aggregated_rating_level(self):
        """Gets the aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Уровень рейтинга по итоговой шкале  # noqa: E501

        :return: The aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: int
        """
        return self._aggregated_rating_level

    @aggregated_rating_level.setter
    def aggregated_rating_level(self, aggregated_rating_level):
        """Sets the aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Уровень рейтинга по итоговой шкале  # noqa: E501

        :param aggregated_rating_level: The aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: int
        """

        self._aggregated_rating_level = aggregated_rating_level

    @property
    def rating_code(self):
        """Gets the rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Код лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: str
        """
        return self._rating_code

    @rating_code.setter
    def rating_code(self, rating_code):
        """Sets the rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Код лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_code: The rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: str
        """

        self._rating_code = rating_code

    @property
    def rating_id(self):
        """Gets the rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Идентификатор лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id):
        """Sets the rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Идентификатор лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_id: The rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: int
        """

        self._rating_id = rating_id

    @property
    def rating_agency_id(self):
        """Gets the rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Идентификатор агентства, присвоившего лучший рейтинг, или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_agency_id

    @rating_agency_id.setter
    def rating_agency_id(self, rating_agency_id):
        """Sets the rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Идентификатор агентства, присвоившего лучший рейтинг, или null при отсутствии рейтинга  # noqa: E501

        :param rating_agency_id: The rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: int
        """

        self._rating_agency_id = rating_agency_id

    @property
    def rating_scale_id(self):
        """Gets the rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Идентификатор шкалы лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_scale_id

    @rating_scale_id.setter
    def rating_scale_id(self, rating_scale_id):
        """Sets the rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Идентификатор шкалы лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_scale_id: The rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: int
        """

        self._rating_scale_id = rating_scale_id

    @property
    def rating_value(self):
        """Gets the rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Значение лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: str
        """
        return self._rating_value

    @rating_value.setter
    def rating_value(self, rating_value):
        """Sets the rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Значение лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_value: The rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: str
        """

        self._rating_value = rating_value

    @property
    def rating_date(self):
        """Gets the rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501

        Дата присвоения значения лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :rtype: datetime
        """
        return self._rating_date

    @rating_date.setter
    def rating_date(self, rating_date):
        """Sets the rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.

        Дата присвоения значения лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_date: The rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityFields.  # noqa: E501
        :type: datetime
        """

        self._rating_date = rating_date

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
        if issubclass(EfirDataHubModelsModelsSolvencyRatingAggSecurityFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsSolvencyRatingAggSecurityFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
