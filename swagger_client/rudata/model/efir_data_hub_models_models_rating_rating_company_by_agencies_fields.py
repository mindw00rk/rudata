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

class EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields(object):
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
        'fininst_id': 'int',
        'rating_date': 'datetime',
        'rating_level': 'int',
        'rating_id': 'int',
        'rating_agency_id': 'int',
        'rating_value': 'str'
    }

    attribute_map = {
        'fininst_id': 'fininstId',
        'rating_date': 'ratingDate',
        'rating_level': 'ratingLevel',
        'rating_id': 'ratingId',
        'rating_agency_id': 'ratingAgencyId',
        'rating_value': 'ratingValue'
    }

    def __init__(self, fininst_id=None, rating_date=None, rating_level=None, rating_id=None, rating_agency_id=None, rating_value=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields - a model defined in Swagger"""  # noqa: E501
        self._fininst_id = None
        self._rating_date = None
        self._rating_level = None
        self._rating_id = None
        self._rating_agency_id = None
        self._rating_value = None
        self.discriminator = None
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if rating_date is not None:
            self.rating_date = rating_date
        if rating_level is not None:
            self.rating_level = rating_level
        if rating_id is not None:
            self.rating_id = rating_id
        if rating_agency_id is not None:
            self.rating_agency_id = rating_agency_id
        if rating_value is not None:
            self.rating_value = rating_value

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Идентификатор компании базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Идентификатор компании базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def rating_date(self):
        """Gets the rating_date of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Дата присвоения значения лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_date of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: datetime
        """
        return self._rating_date

    @rating_date.setter
    def rating_date(self, rating_date):
        """Sets the rating_date of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Дата присвоения значения лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_date: The rating_date of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: datetime
        """

        self._rating_date = rating_date

    @property
    def rating_level(self):
        """Gets the rating_level of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Уровень рейтинга по итоговой шкале  # noqa: E501

        :return: The rating_level of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_level

    @rating_level.setter
    def rating_level(self, rating_level):
        """Sets the rating_level of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Уровень рейтинга по итоговой шкале  # noqa: E501

        :param rating_level: The rating_level of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: int
        """

        self._rating_level = rating_level

    @property
    def rating_id(self):
        """Gets the rating_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Идентификатор лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id):
        """Sets the rating_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Идентификатор лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_id: The rating_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: int
        """

        self._rating_id = rating_id

    @property
    def rating_agency_id(self):
        """Gets the rating_agency_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Идентификатор агентства, присвоившего лучший рейтинг, или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_agency_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_agency_id

    @rating_agency_id.setter
    def rating_agency_id(self, rating_agency_id):
        """Sets the rating_agency_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Идентификатор агентства, присвоившего лучший рейтинг, или null при отсутствии рейтинга  # noqa: E501

        :param rating_agency_id: The rating_agency_id of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: int
        """

        self._rating_agency_id = rating_agency_id

    @property
    def rating_value(self):
        """Gets the rating_value of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501

        Значение лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :return: The rating_value of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :rtype: str
        """
        return self._rating_value

    @rating_value.setter
    def rating_value(self, rating_value):
        """Sets the rating_value of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.

        Значение лучшего рейтинга или null при отсутствии рейтинга  # noqa: E501

        :param rating_value: The rating_value of this EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields.  # noqa: E501
        :type: str
        """

        self._rating_value = rating_value

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
        if issubclass(EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingRatingCompanyByAgenciesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other