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

class EfirDataHubModelsModelsEmitentScoringExtHistoryFields(object):
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
        'code': 'str',
        'fininst_id': 'int',
        'inn': 'str',
        'ogrn': 'str',
        'sector': 'str',
        'source': 'str',
        'last_reported_date': 'str',
        'update_date': 'datetime',
        'is_filtered': 'int',
        'values': 'AllOfEfirDataHubModelsModelsEmitentScoringExtHistoryFieldsValues'
    }

    attribute_map = {
        'code': 'code',
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'sector': 'sector',
        'source': 'source',
        'last_reported_date': 'last_reported_date',
        'update_date': 'update_date',
        'is_filtered': 'is_filtered',
        'values': 'values'
    }

    def __init__(self, code=None, fininst_id=None, inn=None, ogrn=None, sector=None, source=None, last_reported_date=None, update_date=None, is_filtered=None, values=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentScoringExtHistoryFields - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._sector = None
        self._source = None
        self._last_reported_date = None
        self._update_date = None
        self._is_filtered = None
        self._values = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if sector is not None:
            self.sector = sector
        if source is not None:
            self.source = source
        if last_reported_date is not None:
            self.last_reported_date = last_reported_date
        if update_date is not None:
            self.update_date = update_date
        if is_filtered is not None:
            self.is_filtered = is_filtered
        if values is not None:
            self.values = values

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        значение Code из запроса (ИНН или ОГРН)  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        значение Code из запроса (ИНН или ОГРН)  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        Идентификатор эмитента в БД Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        Идентификатор эмитента в БД Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        ИНН эмитента  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        ИНН эмитента  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        ОГРН эмитента  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        ОГРН эмитента  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def sector(self):
        """Gets the sector of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        Отрасль эмитента  # noqa: E501

        :return: The sector of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        Отрасль эмитента  # noqa: E501

        :param sector: The sector of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        Тип отчетности, по которой сформированы значения  # noqa: E501

        :return: The source of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        Тип отчетности, по которой сформированы значения  # noqa: E501

        :param source: The source of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def last_reported_date(self):
        """Gets the last_reported_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        дата окончания отчетности, по которой был рассчитан расширенный скоринг  # noqa: E501

        :return: The last_reported_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: str
        """
        return self._last_reported_date

    @last_reported_date.setter
    def last_reported_date(self, last_reported_date):
        """Sets the last_reported_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        дата окончания отчетности, по которой был рассчитан расширенный скоринг  # noqa: E501

        :param last_reported_date: The last_reported_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: str
        """

        self._last_reported_date = last_reported_date

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        дата расчета расширенного скоринга  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        дата расчета расширенного скоринга  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def is_filtered(self):
        """Gets the is_filtered of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        Признак фильтрации по горизонту прогнозирования  # noqa: E501

        :return: The is_filtered of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: int
        """
        return self._is_filtered

    @is_filtered.setter
    def is_filtered(self, is_filtered):
        """Sets the is_filtered of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        Признак фильтрации по горизонту прогнозирования  # noqa: E501

        :param is_filtered: The is_filtered of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: int
        """

        self._is_filtered = is_filtered

    @property
    def values(self):
        """Gets the values of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501

        Значения балансов и коэффициентов  # noqa: E501

        :return: The values of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsModelsEmitentScoringExtHistoryFieldsValues
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.

        Значения балансов и коэффициентов  # noqa: E501

        :param values: The values of this EfirDataHubModelsModelsEmitentScoringExtHistoryFields.  # noqa: E501
        :type: AllOfEfirDataHubModelsModelsEmitentScoringExtHistoryFieldsValues
        """

        self._values = values

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
        if issubclass(EfirDataHubModelsModelsEmitentScoringExtHistoryFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentScoringExtHistoryFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
