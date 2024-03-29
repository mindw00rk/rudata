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

class EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest(object):
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
        'iss_id': 'int',
        'isin': 'str',
        '_date': 'datetime',
        'date_type': 'str',
        'fields': 'list[str]',
        'official': 'bool',
        'trade_site': 'str'
    }

    attribute_map = {
        'iss_id': 'issId',
        'isin': 'isin',
        '_date': 'date',
        'date_type': 'dateType',
        'fields': 'fields',
        'official': 'official',
        'trade_site': 'tradeSite'
    }

    def __init__(self, iss_id=None, isin=None, _date=None, date_type=None, fields=None, official=None, trade_site=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest - a model defined in Swagger"""  # noqa: E501
        self._iss_id = None
        self._isin = None
        self.__date = None
        self._date_type = None
        self._fields = None
        self._official = None
        self._trade_site = None
        self.discriminator = None
        if iss_id is not None:
            self.iss_id = iss_id
        if isin is not None:
            self.isin = isin
        self._date = _date
        if date_type is not None:
            self.date_type = date_type
        if fields is not None:
            self.fields = fields
        if official is not None:
            self.official = official
        if trade_site is not None:
            self.trade_site = trade_site

    @property
    def iss_id(self):
        """Gets the iss_id of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Идентификатор инструмента. Должен быть задан этот параметр или isin.  # noqa: E501

        :return: The iss_id of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: int
        """
        return self._iss_id

    @iss_id.setter
    def iss_id(self, iss_id):
        """Sets the iss_id of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Идентификатор инструмента. Должен быть задан этот параметр или isin.  # noqa: E501

        :param iss_id: The iss_id of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: int
        """

        self._iss_id = iss_id

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        ISIN инструмента. Должен быть задан этот параметр или issId.  # noqa: E501

        :return: The isin of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        ISIN инструмента. Должен быть задан этот параметр или issId.  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Дата запрашиваемых данных  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Дата запрашиваемых данных  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def date_type(self):
        """Gets the date_type of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Тип возвращаемых данных:  - ACTUAL – строго на указанную дату(умолчание)  - LAST_TRADE_DATE – на ближайшую окончившуюся торговую сессию (максимальная протяжка LAST_TRADE_DATE - 12 месяцев)  - LAST_SESSION_DATE - данные на ближайшую предшествующую дату, когда по инструменту проводились торги. Независимо от совершенных сделок  # noqa: E501

        :return: The date_type of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_type

    @date_type.setter
    def date_type(self, date_type):
        """Sets the date_type of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Тип возвращаемых данных:  - ACTUAL – строго на указанную дату(умолчание)  - LAST_TRADE_DATE – на ближайшую окончившуюся торговую сессию (максимальная протяжка LAST_TRADE_DATE - 12 месяцев)  - LAST_SESSION_DATE - данные на ближайшую предшествующую дату, когда по инструменту проводились торги. Независимо от совершенных сделок  # noqa: E501

        :param date_type: The date_type of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: str
        """

        self._date_type = date_type

    @property
    def fields(self):
        """Gets the fields of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Список кодовых наименований полей, колонка name из выходной таблицы метода /Info/Fields.   По умолчанию выводятся все доступные поля.  # noqa: E501

        :return: The fields of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Список кодовых наименований полей, колонка name из выходной таблицы метода /Info/Fields.   По умолчанию выводятся все доступные поля.  # noqa: E501

        :param fields: The fields of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def official(self):
        """Gets the official of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Запрос официальных итогов:  - true – запрашивать официальные итоги   - false – запрашивать неофициальные итоги  # noqa: E501

        :return: The official of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: bool
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Запрос официальных итогов:  - true – запрашивать официальные итоги   - false – запрашивать неофициальные итоги  # noqa: E501

        :param official: The official of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: bool
        """

        self._official = official

    @property
    def trade_site(self):
        """Gets the trade_site of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501

        Идентификатор торговой площадки/источника, возвращаемый методом /Info/Exchange_tree.  # noqa: E501

        :return: The trade_site of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :rtype: str
        """
        return self._trade_site

    @trade_site.setter
    def trade_site(self, trade_site):
        """Sets the trade_site of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.

        Идентификатор торговой площадки/источника, возвращаемый методом /Info/Exchange_tree.  # noqa: E501

        :param trade_site: The trade_site of this EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest.  # noqa: E501
        :type: str
        """

        self._trade_site = trade_site

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
        if issubclass(EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
