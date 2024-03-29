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

class EfirDataHubModelsModelsReportCustomReportListFields(object):
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
        'report_id': 'str',
        'fininst_id': 'int',
        'inn': 'str',
        'ogrn': 'str',
        'period_date': 'datetime',
        'period_name': 'str',
        'counterpartyid': 'int',
        'status': 'int',
        'update_date': 'datetime',
        'counter': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'period_date': 'period_date',
        'period_name': 'period_name',
        'counterpartyid': 'counterpartyid',
        'status': 'status',
        'update_date': 'update_date',
        'counter': 'counter'
    }

    def __init__(self, report_id=None, fininst_id=None, inn=None, ogrn=None, period_date=None, period_name=None, counterpartyid=None, status=None, update_date=None, counter=None):  # noqa: E501
        """EfirDataHubModelsModelsReportCustomReportListFields - a model defined in Swagger"""  # noqa: E501
        self._report_id = None
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._period_date = None
        self._period_name = None
        self._counterpartyid = None
        self._status = None
        self._update_date = None
        self._counter = None
        self.discriminator = None
        if report_id is not None:
            self.report_id = report_id
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if period_date is not None:
            self.period_date = period_date
        if period_name is not None:
            self.period_name = period_name
        if counterpartyid is not None:
            self.counterpartyid = counterpartyid
        if status is not None:
            self.status = status
        if update_date is not None:
            self.update_date = update_date
        if counter is not None:
            self.counter = counter

    @property
    def report_id(self):
        """Gets the report_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Идентификатор отчета  # noqa: E501

        :return: The report_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this EfirDataHubModelsModelsReportCustomReportListFields.

        Идентификатор отчета  # noqa: E501

        :param report_id: The report_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Идентификатор организации в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsReportCustomReportListFields.

        Идентификатор организации в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        ИНН  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsReportCustomReportListFields.

        ИНН  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        ОГРН  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsReportCustomReportListFields.

        ОГРН  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def period_date(self):
        """Gets the period_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Дата окончания отчетного периода  # noqa: E501

        :return: The period_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._period_date

    @period_date.setter
    def period_date(self, period_date):
        """Sets the period_date of this EfirDataHubModelsModelsReportCustomReportListFields.

        Дата окончания отчетного периода  # noqa: E501

        :param period_date: The period_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: datetime
        """

        self._period_date = period_date

    @property
    def period_name(self):
        """Gets the period_name of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Наименование отчетного периода  # noqa: E501

        :return: The period_name of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: str
        """
        return self._period_name

    @period_name.setter
    def period_name(self, period_name):
        """Sets the period_name of this EfirDataHubModelsModelsReportCustomReportListFields.

        Наименование отчетного периода  # noqa: E501

        :param period_name: The period_name of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: str
        """

        self._period_name = period_name

    @property
    def counterpartyid(self):
        """Gets the counterpartyid of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The counterpartyid of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._counterpartyid

    @counterpartyid.setter
    def counterpartyid(self, counterpartyid):
        """Sets the counterpartyid of this EfirDataHubModelsModelsReportCustomReportListFields.

        Идентификатор контрагента  # noqa: E501

        :param counterpartyid: The counterpartyid of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: int
        """

        self._counterpartyid = counterpartyid

    @property
    def status(self):
        """Gets the status of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Статус отчета:  - 1 - в очереди,  - 2 - в процессе,  - 3 - готово,  - 4 - ошибка расчета  - 5 - отсутствует отчетность по компании  # noqa: E501

        :return: The status of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EfirDataHubModelsModelsReportCustomReportListFields.

        Статус отчета:  - 1 - в очереди,  - 2 - в процессе,  - 3 - готово,  - 4 - ошибка расчета  - 5 - отсутствует отчетность по компании  # noqa: E501

        :param status: The status of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Дата обновления отчета  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsReportCustomReportListFields.

        Дата обновления отчета  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsReportCustomReportListFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsReportCustomReportListFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

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
        if issubclass(EfirDataHubModelsModelsReportCustomReportListFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsReportCustomReportListFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
