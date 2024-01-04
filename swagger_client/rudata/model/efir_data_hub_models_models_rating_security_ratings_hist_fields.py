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

class EfirDataHubModelsModelsRatingSecurityRatingsHistFields(object):
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
        'hid': 'int',
        'id_rating': 'int',
        'agency': 'str',
        'code_name': 'str',
        'id_value': 'str',
        'forecast': 'str',
        'change': 'str',
        'date_award': 'datetime',
        'role_id': 'int',
        'role_name': 'str',
        'fintoolid': 'int',
        'fininstid': 'int',
        'isin': 'str'
    }

    attribute_map = {
        'hid': 'hid',
        'id_rating': 'id_rating',
        'agency': 'agency',
        'code_name': 'code_name',
        'id_value': 'id_value',
        'forecast': 'forecast',
        'change': 'change',
        'date_award': 'date_award',
        'role_id': 'role_id',
        'role_name': 'role_name',
        'fintoolid': 'fintoolid',
        'fininstid': 'fininstid',
        'isin': 'isin'
    }

    def __init__(self, hid=None, id_rating=None, agency=None, code_name=None, id_value=None, forecast=None, change=None, date_award=None, role_id=None, role_name=None, fintoolid=None, fininstid=None, isin=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingSecurityRatingsHistFields - a model defined in Swagger"""  # noqa: E501
        self._hid = None
        self._id_rating = None
        self._agency = None
        self._code_name = None
        self._id_value = None
        self._forecast = None
        self._change = None
        self._date_award = None
        self._role_id = None
        self._role_name = None
        self._fintoolid = None
        self._fininstid = None
        self._isin = None
        self.discriminator = None
        if hid is not None:
            self.hid = hid
        if id_rating is not None:
            self.id_rating = id_rating
        if agency is not None:
            self.agency = agency
        if code_name is not None:
            self.code_name = code_name
        if id_value is not None:
            self.id_value = id_value
        if forecast is not None:
            self.forecast = forecast
        if change is not None:
            self.change = change
        if date_award is not None:
            self.date_award = date_award
        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if fintoolid is not None:
            self.fintoolid = fintoolid
        if fininstid is not None:
            self.fininstid = fininstid
        if isin is not None:
            self.isin = isin

    @property
    def hid(self):
        """Gets the hid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Идентификатор рейтинга (устарел, надо использовать id_rating)  # noqa: E501

        :return: The hid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: int
        """
        return self._hid

    @hid.setter
    def hid(self, hid):
        """Sets the hid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Идентификатор рейтинга (устарел, надо использовать id_rating)  # noqa: E501

        :param hid: The hid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: int
        """

        self._hid = hid

    @property
    def id_rating(self):
        """Gets the id_rating of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Идентификатор вида рейтинга  # noqa: E501

        :return: The id_rating of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: int
        """
        return self._id_rating

    @id_rating.setter
    def id_rating(self, id_rating):
        """Sets the id_rating of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Идентификатор вида рейтинга  # noqa: E501

        :param id_rating: The id_rating of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: int
        """

        self._id_rating = id_rating

    @property
    def agency(self):
        """Gets the agency of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Агентство  # noqa: E501

        :return: The agency of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Агентство  # noqa: E501

        :param agency: The agency of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._agency = agency

    @property
    def code_name(self):
        """Gets the code_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Символьный код рейтинга  # noqa: E501

        :return: The code_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        """Sets the code_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Символьный код рейтинга  # noqa: E501

        :param code_name: The code_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._code_name = code_name

    @property
    def id_value(self):
        """Gets the id_value of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Значение рейтинга  # noqa: E501

        :return: The id_value of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        """Sets the id_value of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Значение рейтинга  # noqa: E501

        :param id_value: The id_value of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._id_value = id_value

    @property
    def forecast(self):
        """Gets the forecast of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Прогноз рейтинга  # noqa: E501

        :return: The forecast of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast):
        """Sets the forecast of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Прогноз рейтинга  # noqa: E501

        :param forecast: The forecast of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._forecast = forecast

    @property
    def change(self):
        """Gets the change of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Изменение рейтинга  # noqa: E501

        :return: The change of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Изменение рейтинга  # noqa: E501

        :param change: The change of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._change = change

    @property
    def date_award(self):
        """Gets the date_award of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Дата рейтингового действия  # noqa: E501

        :return: The date_award of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: datetime
        """
        return self._date_award

    @date_award.setter
    def date_award(self, date_award):
        """Sets the date_award of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Дата рейтингового действия  # noqa: E501

        :param date_award: The date_award of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: datetime
        """

        self._date_award = date_award

    @property
    def role_id(self):
        """Gets the role_id of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        0 – рейтинг инструмента  1 – рейтинг эмитента  2 – рейтинг заемщика  3 – рейтинг гаранта или поручителя  # noqa: E501

        :return: The role_id of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        0 – рейтинг инструмента  1 – рейтинг эмитента  2 – рейтинг заемщика  3 – рейтинг гаранта или поручителя  # noqa: E501

        :param role_id: The role_id of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def role_name(self):
        """Gets the role_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Наименование роли  # noqa: E501

        :return: The role_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Наименование роли  # noqa: E501

        :param role_name: The role_name of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def fintoolid(self):
        """Gets the fintoolid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Идентификатор соответствующего организатора в базе Интерфакс  # noqa: E501

        :return: The fintoolid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: int
        """
        return self._fintoolid

    @fintoolid.setter
    def fintoolid(self, fintoolid):
        """Sets the fintoolid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Идентификатор соответствующего организатора в базе Интерфакс  # noqa: E501

        :param fintoolid: The fintoolid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: int
        """

        self._fintoolid = fintoolid

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        Идентификатор выпуска в базе Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        Идентификатор выпуска в базе Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.

        ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsRatingSecurityRatingsHistFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

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
        if issubclass(EfirDataHubModelsModelsRatingSecurityRatingsHistFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingSecurityRatingsHistFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
