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

class EfirDataHubModelsModelsBondDefaultsTableFields(object):
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
        'id_fintool': 'str',
        'default_type': 'str',
        'event_type': 'str',
        'id_event': 'int',
        'pay_date': 'datetime',
        'real_pay_date': 'datetime',
        'note': 'str',
        'id': 'int',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'id_fintool': 'id_fintool',
        'default_type': 'default_type',
        'event_type': 'event_type',
        'id_event': 'id_event',
        'pay_date': 'pay_date',
        'real_pay_date': 'real_pay_date',
        'note': 'note',
        'id': 'id',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, id_fintool=None, default_type=None, event_type=None, id_event=None, pay_date=None, real_pay_date=None, note=None, id=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsBondDefaultsTableFields - a model defined in Swagger"""  # noqa: E501
        self._id_fintool = None
        self._default_type = None
        self._event_type = None
        self._id_event = None
        self._pay_date = None
        self._real_pay_date = None
        self._note = None
        self._id = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if id_fintool is not None:
            self.id_fintool = id_fintool
        if default_type is not None:
            self.default_type = default_type
        if event_type is not None:
            self.event_type = event_type
        if id_event is not None:
            self.id_event = id_event
        if pay_date is not None:
            self.pay_date = pay_date
        if real_pay_date is not None:
            self.real_pay_date = real_pay_date
        if note is not None:
            self.note = note
        if id is not None:
            self.id = id
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def id_fintool(self):
        """Gets the id_fintool of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Идентификатор бумаги (ISIN)  # noqa: E501

        :return: The id_fintool of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: str
        """
        return self._id_fintool

    @id_fintool.setter
    def id_fintool(self, id_fintool):
        """Sets the id_fintool of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Идентификатор бумаги (ISIN)  # noqa: E501

        :param id_fintool: The id_fintool of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: str
        """

        self._id_fintool = id_fintool

    @property
    def default_type(self):
        """Gets the default_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Тип дефолта  # noqa: E501

        :return: The default_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: str
        """
        return self._default_type

    @default_type.setter
    def default_type(self, default_type):
        """Sets the default_type of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Тип дефолта  # noqa: E501

        :param default_type: The default_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: str
        """

        self._default_type = default_type

    @property
    def event_type(self):
        """Gets the event_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Тип события, по которому наступил дефолт  # noqa: E501

        :return: The event_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Тип события, по которому наступил дефолт  # noqa: E501

        :param event_type: The event_type of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def id_event(self):
        """Gets the id_event of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Идентификатор события  # noqa: E501

        :return: The id_event of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: int
        """
        return self._id_event

    @id_event.setter
    def id_event(self, id_event):
        """Sets the id_event of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Идентификатор события  # noqa: E501

        :param id_event: The id_event of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: int
        """

        self._id_event = id_event

    @property
    def pay_date(self):
        """Gets the pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Плановая дата выплат  # noqa: E501

        :return: The pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: datetime
        """
        return self._pay_date

    @pay_date.setter
    def pay_date(self, pay_date):
        """Sets the pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Плановая дата выплат  # noqa: E501

        :param pay_date: The pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: datetime
        """

        self._pay_date = pay_date

    @property
    def real_pay_date(self):
        """Gets the real_pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Реальная дата выплат  # noqa: E501

        :return: The real_pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: datetime
        """
        return self._real_pay_date

    @real_pay_date.setter
    def real_pay_date(self, real_pay_date):
        """Sets the real_pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Реальная дата выплат  # noqa: E501

        :param real_pay_date: The real_pay_date of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: datetime
        """

        self._real_pay_date = real_pay_date

    @property
    def note(self):
        """Gets the note of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Комментарий  # noqa: E501

        :return: The note of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Комментарий  # noqa: E501

        :param note: The note of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Идентификатор записи в БД  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Идентификатор записи в БД  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsBondDefaultsTableFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsBondDefaultsTableFields.  # noqa: E501
        :type: int
        """

        self._rn = rn

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
        if issubclass(EfirDataHubModelsModelsBondDefaultsTableFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondDefaultsTableFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
