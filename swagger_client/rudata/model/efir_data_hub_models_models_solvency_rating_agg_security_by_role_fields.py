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

class EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields(object):
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
        'role_code': 'str',
        'surety_fininst_id': 'int',
        'surety_aggregated_rating_level': 'int',
        'surety_rating_code': 'str',
        'surety_rating_id': 'int',
        'surety_rating_agency_id': 'int',
        'surety_rating_scale_id': 'int',
        'surety_rating_value': 'str',
        'surety_rating_date': 'datetime'
    }

    attribute_map = {
        'fintool_id': 'fintoolId',
        'role_code': 'roleCode',
        'surety_fininst_id': 'suretyFininstId',
        'surety_aggregated_rating_level': 'suretyAggregatedRatingLevel',
        'surety_rating_code': 'suretyRatingCode',
        'surety_rating_id': 'suretyRatingId',
        'surety_rating_agency_id': 'suretyRatingAgencyId',
        'surety_rating_scale_id': 'suretyRatingScaleId',
        'surety_rating_value': 'suretyRatingValue',
        'surety_rating_date': 'suretyRatingDate'
    }

    def __init__(self, fintool_id=None, role_code=None, surety_fininst_id=None, surety_aggregated_rating_level=None, surety_rating_code=None, surety_rating_id=None, surety_rating_agency_id=None, surety_rating_scale_id=None, surety_rating_value=None, surety_rating_date=None):  # noqa: E501
        """EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields - a model defined in Swagger"""  # noqa: E501
        self._fintool_id = None
        self._role_code = None
        self._surety_fininst_id = None
        self._surety_aggregated_rating_level = None
        self._surety_rating_code = None
        self._surety_rating_id = None
        self._surety_rating_agency_id = None
        self._surety_rating_scale_id = None
        self._surety_rating_value = None
        self._surety_rating_date = None
        self.discriminator = None
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if role_code is not None:
            self.role_code = role_code
        if surety_fininst_id is not None:
            self.surety_fininst_id = surety_fininst_id
        if surety_aggregated_rating_level is not None:
            self.surety_aggregated_rating_level = surety_aggregated_rating_level
        if surety_rating_code is not None:
            self.surety_rating_code = surety_rating_code
        if surety_rating_id is not None:
            self.surety_rating_id = surety_rating_id
        if surety_rating_agency_id is not None:
            self.surety_rating_agency_id = surety_rating_agency_id
        if surety_rating_scale_id is not None:
            self.surety_rating_scale_id = surety_rating_scale_id
        if surety_rating_value is not None:
            self.surety_rating_value = surety_rating_value
        if surety_rating_date is not None:
            self.surety_rating_date = surety_rating_date

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def role_code(self):
        """Gets the role_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Код роли (всегда surety - гарант/поручитель)  # noqa: E501

        :return: The role_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: str
        """
        return self._role_code

    @role_code.setter
    def role_code(self, role_code):
        """Sets the role_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Код роли (всегда surety - гарант/поручитель)  # noqa: E501

        :param role_code: The role_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: str
        """

        self._role_code = role_code

    @property
    def surety_fininst_id(self):
        """Gets the surety_fininst_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Идентификатор гаранта/поручителя в базе Интерфакс  # noqa: E501

        :return: The surety_fininst_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._surety_fininst_id

    @surety_fininst_id.setter
    def surety_fininst_id(self, surety_fininst_id):
        """Sets the surety_fininst_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Идентификатор гаранта/поручителя в базе Интерфакс  # noqa: E501

        :param surety_fininst_id: The surety_fininst_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._surety_fininst_id = surety_fininst_id

    @property
    def surety_aggregated_rating_level(self):
        """Gets the surety_aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Уровень рейтинга гаранта/поручителя по итоговой шкале  # noqa: E501

        :return: The surety_aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._surety_aggregated_rating_level

    @surety_aggregated_rating_level.setter
    def surety_aggregated_rating_level(self, surety_aggregated_rating_level):
        """Sets the surety_aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Уровень рейтинга гаранта/поручителя по итоговой шкале  # noqa: E501

        :param surety_aggregated_rating_level: The surety_aggregated_rating_level of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._surety_aggregated_rating_level = surety_aggregated_rating_level

    @property
    def surety_rating_code(self):
        """Gets the surety_rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Код лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: str
        """
        return self._surety_rating_code

    @surety_rating_code.setter
    def surety_rating_code(self, surety_rating_code):
        """Sets the surety_rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Код лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_code: The surety_rating_code of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: str
        """

        self._surety_rating_code = surety_rating_code

    @property
    def surety_rating_id(self):
        """Gets the surety_rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Идентификатор лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._surety_rating_id

    @surety_rating_id.setter
    def surety_rating_id(self, surety_rating_id):
        """Sets the surety_rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Идентификатор лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_id: The surety_rating_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._surety_rating_id = surety_rating_id

    @property
    def surety_rating_agency_id(self):
        """Gets the surety_rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Идентификатор агентства, присвоившего лучший рейтинг гаранта/поручителя, или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._surety_rating_agency_id

    @surety_rating_agency_id.setter
    def surety_rating_agency_id(self, surety_rating_agency_id):
        """Sets the surety_rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Идентификатор агентства, присвоившего лучший рейтинг гаранта/поручителя, или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_agency_id: The surety_rating_agency_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._surety_rating_agency_id = surety_rating_agency_id

    @property
    def surety_rating_scale_id(self):
        """Gets the surety_rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Идентификатор шкалы лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: int
        """
        return self._surety_rating_scale_id

    @surety_rating_scale_id.setter
    def surety_rating_scale_id(self, surety_rating_scale_id):
        """Sets the surety_rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Идентификатор шкалы лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_scale_id: The surety_rating_scale_id of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: int
        """

        self._surety_rating_scale_id = surety_rating_scale_id

    @property
    def surety_rating_value(self):
        """Gets the surety_rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Значение лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: str
        """
        return self._surety_rating_value

    @surety_rating_value.setter
    def surety_rating_value(self, surety_rating_value):
        """Sets the surety_rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Значение лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_value: The surety_rating_value of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: str
        """

        self._surety_rating_value = surety_rating_value

    @property
    def surety_rating_date(self):
        """Gets the surety_rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501

        Дата присвоения значения лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :return: The surety_rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :rtype: datetime
        """
        return self._surety_rating_date

    @surety_rating_date.setter
    def surety_rating_date(self, surety_rating_date):
        """Sets the surety_rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.

        Дата присвоения значения лучшего рейтинга гаранта/поручителя или null при отсутствии рейтинга  # noqa: E501

        :param surety_rating_date: The surety_rating_date of this EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields.  # noqa: E501
        :type: datetime
        """

        self._surety_rating_date = surety_rating_date

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
        if issubclass(EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsSolvencyRatingAggSecurityByRoleFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other