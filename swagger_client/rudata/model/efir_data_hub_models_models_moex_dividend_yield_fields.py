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

class EfirDataHubModelsModelsMoexDividendYieldFields(object):
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
        'dt': 'datetime',
        'fintool_id': 'int',
        'year': 'int',
        '_yield': 'float',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'dt': 'dt',
        'fintool_id': 'fintoolId',
        'year': 'year',
        '_yield': 'yield',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, dt=None, fintool_id=None, year=None, _yield=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsMoexDividendYieldFields - a model defined in Swagger"""  # noqa: E501
        self._dt = None
        self._fintool_id = None
        self._year = None
        self.__yield = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if dt is not None:
            self.dt = dt
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if year is not None:
            self.year = year
        if _yield is not None:
            self._yield = _yield
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def dt(self):
        """Gets the dt of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Дата величины  # noqa: E501

        :return: The dt of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: datetime
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Дата величины  # noqa: E501

        :param dt: The dt of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :type: datetime
        """

        self._dt = dt

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Идентификатор инструмента  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Идентификатор инструмента  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def year(self):
        """Gets the year of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Год, для которого определена величина доходности  # noqa: E501

        :return: The year of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Год, для которого определена величина доходности  # noqa: E501

        :param year: The year of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def _yield(self):
        """Gets the _yield of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Величина дивидендной доходности  # noqa: E501

        :return: The _yield of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: float
        """
        return self.__yield

    @_yield.setter
    def _yield(self, _yield):
        """Sets the _yield of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Величина дивидендной доходности  # noqa: E501

        :param _yield: The _yield of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :type: float
        """

        self.__yield = _yield

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsMoexDividendYieldFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsMoexDividendYieldFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsMoexDividendYieldFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsMoexDividendYieldFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
