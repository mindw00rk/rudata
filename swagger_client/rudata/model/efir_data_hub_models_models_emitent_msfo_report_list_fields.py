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

class EfirDataHubModelsModelsEmitentMsfoReportListFields(object):
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
        'id': 'int',
        'fininst_id': 'int',
        'inn': 'int',
        'inn_as_string': 'str',
        'ogrn': 'int',
        'ogrn_as_string': 'str',
        'period_date': 'datetime',
        'period_name': 'str',
        'source_link': 'str',
        'counterpartyid': 'int'
    }

    attribute_map = {
        'id': 'id',
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'inn_as_string': 'inn_as_string',
        'ogrn': 'ogrn',
        'ogrn_as_string': 'ogrn_as_string',
        'period_date': 'period_date',
        'period_name': 'period_name',
        'source_link': 'source_link',
        'counterpartyid': 'counterpartyid'
    }

    def __init__(self, id=None, fininst_id=None, inn=None, inn_as_string=None, ogrn=None, ogrn_as_string=None, period_date=None, period_name=None, source_link=None, counterpartyid=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentMsfoReportListFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fininst_id = None
        self._inn = None
        self._inn_as_string = None
        self._ogrn = None
        self._ogrn_as_string = None
        self._period_date = None
        self._period_name = None
        self._source_link = None
        self._counterpartyid = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if inn_as_string is not None:
            self.inn_as_string = inn_as_string
        if ogrn is not None:
            self.ogrn = ogrn
        if ogrn_as_string is not None:
            self.ogrn_as_string = ogrn_as_string
        if period_date is not None:
            self.period_date = period_date
        if period_name is not None:
            self.period_name = period_name
        if source_link is not None:
            self.source_link = source_link
        if counterpartyid is not None:
            self.counterpartyid = counterpartyid

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Идентификатор отчетности  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Идентификатор отчетности  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Идентификатор организации в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Идентификатор организации в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        ИНН в виде числа  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        ИНН в виде числа  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: int
        """

        self._inn = inn

    @property
    def inn_as_string(self):
        """Gets the inn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        ИНН в строковом формате, с сохранением ведущих нулей  # noqa: E501

        :return: The inn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._inn_as_string

    @inn_as_string.setter
    def inn_as_string(self, inn_as_string):
        """Sets the inn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        ИНН в строковом формате, с сохранением ведущих нулей  # noqa: E501

        :param inn_as_string: The inn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: str
        """

        self._inn_as_string = inn_as_string

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        ОГРН в виде числа  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        ОГРН в виде числа  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: int
        """

        self._ogrn = ogrn

    @property
    def ogrn_as_string(self):
        """Gets the ogrn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        ОГРН в строковом формате, с сохранением ведущих нулей  # noqa: E501

        :return: The ogrn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn_as_string

    @ogrn_as_string.setter
    def ogrn_as_string(self, ogrn_as_string):
        """Sets the ogrn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        ОГРН в строковом формате, с сохранением ведущих нулей  # noqa: E501

        :param ogrn_as_string: The ogrn_as_string of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: str
        """

        self._ogrn_as_string = ogrn_as_string

    @property
    def period_date(self):
        """Gets the period_date of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Дата окончания отчетного периода  # noqa: E501

        :return: The period_date of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._period_date

    @period_date.setter
    def period_date(self, period_date):
        """Sets the period_date of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Дата окончания отчетного периода  # noqa: E501

        :param period_date: The period_date of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: datetime
        """

        self._period_date = period_date

    @property
    def period_name(self):
        """Gets the period_name of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Наименование отчетного периода  # noqa: E501

        :return: The period_name of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._period_name

    @period_name.setter
    def period_name(self, period_name):
        """Sets the period_name of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Наименование отчетного периода  # noqa: E501

        :param period_name: The period_name of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: str
        """

        self._period_name = period_name

    @property
    def source_link(self):
        """Gets the source_link of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Ссылка на исходную отчетность  # noqa: E501

        :return: The source_link of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._source_link

    @source_link.setter
    def source_link(self, source_link):
        """Sets the source_link of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Ссылка на исходную отчетность  # noqa: E501

        :param source_link: The source_link of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: str
        """

        self._source_link = source_link

    @property
    def counterpartyid(self):
        """Gets the counterpartyid of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The counterpartyid of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._counterpartyid

    @counterpartyid.setter
    def counterpartyid(self, counterpartyid):
        """Sets the counterpartyid of this EfirDataHubModelsModelsEmitentMsfoReportListFields.

        Идентификатор контрагента  # noqa: E501

        :param counterpartyid: The counterpartyid of this EfirDataHubModelsModelsEmitentMsfoReportListFields.  # noqa: E501
        :type: int
        """

        self._counterpartyid = counterpartyid

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
        if issubclass(EfirDataHubModelsModelsEmitentMsfoReportListFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentMsfoReportListFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
