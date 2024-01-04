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

class EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest(object):
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
        'fintool_ids': 'list[int]',
        'iss_ids': 'list[int]',
        'codes': 'list[str]',
        'trade_sites': 'list[int]',
        'time_slice': 'str',
        'date_from': 'datetime',
        'date_to': 'datetime',
        'fields': 'list[str]'
    }

    attribute_map = {
        'fintool_ids': 'fintoolIds',
        'iss_ids': 'issIds',
        'codes': 'codes',
        'trade_sites': 'tradeSites',
        'time_slice': 'timeSlice',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'fields': 'fields'
    }

    def __init__(self, fintool_ids=None, iss_ids=None, codes=None, trade_sites=None, time_slice=None, date_from=None, date_to=None, fields=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest - a model defined in Swagger"""  # noqa: E501
        self._fintool_ids = None
        self._iss_ids = None
        self._codes = None
        self._trade_sites = None
        self._time_slice = None
        self._date_from = None
        self._date_to = None
        self._fields = None
        self.discriminator = None
        if fintool_ids is not None:
            self.fintool_ids = fintool_ids
        if iss_ids is not None:
            self.iss_ids = iss_ids
        if codes is not None:
            self.codes = codes
        if trade_sites is not None:
            self.trade_sites = trade_sites
        if time_slice is not None:
            self.time_slice = time_slice
        self.date_from = date_from
        self.date_to = date_to
        if fields is not None:
            self.fields = fields

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Идентификаторы инструментов в базе Интерфакс;  Если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 20  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Идентификаторы инструментов в базе Интерфакс;  Если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 20  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: list[int]
        """

        self._fintool_ids = fintool_ids

    @property
    def iss_ids(self):
        """Gets the iss_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Идентификаторы торговых инструментов в БД Интерфакс. Максимум - 20 элементов  # noqa: E501

        :return: The iss_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._iss_ids

    @iss_ids.setter
    def iss_ids(self, iss_ids):
        """Sets the iss_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Идентификаторы торговых инструментов в БД Интерфакс. Максимум - 20 элементов  # noqa: E501

        :param iss_ids: The iss_ids of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: list[int]
        """

        self._iss_ids = iss_ids

    @property
    def codes(self):
        """Gets the codes of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode). Максимум - 100 элементов  # noqa: E501

        :return: The codes of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode). Максимум - 100 элементов  # noqa: E501

        :param codes: The codes of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: list[str]
        """

        self._codes = codes

    @property
    def trade_sites(self):
        """Gets the trade_sites of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Список торговых площадок. Максимум - 10 элементов  # noqa: E501

        :return: The trade_sites of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._trade_sites

    @trade_sites.setter
    def trade_sites(self, trade_sites):
        """Sets the trade_sites of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Список торговых площадок. Максимум - 10 элементов  # noqa: E501

        :param trade_sites: The trade_sites of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: list[int]
        """

        self._trade_sites = trade_sites

    @property
    def time_slice(self):
        """Gets the time_slice of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Время среза по маске hh:mm  # noqa: E501

        :return: The time_slice of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_slice

    @time_slice.setter
    def time_slice(self, time_slice):
        """Sets the time_slice of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Время среза по маске hh:mm  # noqa: E501

        :param time_slice: The time_slice of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: str
        """

        self._time_slice = time_slice

    @property
    def date_from(self):
        """Gets the date_from of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Дата начала периода.  # noqa: E501

        :return: The date_from of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Дата начала периода.  # noqa: E501

        :param date_from: The date_from of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: datetime
        """
        if date_from is None:
            raise ValueError("Invalid value for `date_from`, must not be `None`")  # noqa: E501

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Дата окончания периода.   Не более 30 дней от Efir.DataHub.Models.Requests.V2.Archive.SnapshotOnExchangesRequest.DateFrom  # noqa: E501

        :return: The date_to of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Дата окончания периода.   Не более 30 дней от Efir.DataHub.Models.Requests.V2.Archive.SnapshotOnExchangesRequest.DateFrom  # noqa: E501

        :param date_to: The date_to of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: datetime
        """
        if date_to is None:
            raise ValueError("Invalid value for `date_to`, must not be `None`")  # noqa: E501

        self._date_to = date_to

    @property
    def fields(self):
        """Gets the fields of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501

        Список интересующих полей  # noqa: E501

        :return: The fields of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.

        Список интересующих полей  # noqa: E501

        :param fields: The fields of this EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

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
        if issubclass(EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
