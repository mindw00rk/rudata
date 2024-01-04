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

class EfirDataHubModelsModelsRiskVarMatrixElement(object):
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
        'model_id': 'int',
        '_date': 'datetime',
        'first': 'str',
        'first_type': 'int',
        'second': 'str',
        'second_type': 'int',
        'em_acov': 'float',
        'cor': 'float'
    }

    attribute_map = {
        'model_id': 'modelId',
        '_date': 'date',
        'first': 'first',
        'first_type': 'firstType',
        'second': 'second',
        'second_type': 'secondType',
        'em_acov': 'emAcov',
        'cor': 'cor'
    }

    def __init__(self, model_id=None, _date=None, first=None, first_type=None, second=None, second_type=None, em_acov=None, cor=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskVarMatrixElement - a model defined in Swagger"""  # noqa: E501
        self._model_id = None
        self.__date = None
        self._first = None
        self._first_type = None
        self._second = None
        self._second_type = None
        self._em_acov = None
        self._cor = None
        self.discriminator = None
        if model_id is not None:
            self.model_id = model_id
        if _date is not None:
            self._date = _date
        if first is not None:
            self.first = first
        if first_type is not None:
            self.first_type = first_type
        if second is not None:
            self.second = second
        if second_type is not None:
            self.second_type = second_type
        if em_acov is not None:
            self.em_acov = em_acov
        if cor is not None:
            self.cor = cor

    @property
    def model_id(self):
        """Gets the model_id of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Идентификотор модели расчета  # noqa: E501

        :return: The model_id of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Идентификотор модели расчета  # noqa: E501

        :param model_id: The model_id of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: int
        """

        self._model_id = model_id

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Дата расчета  # noqa: E501

        :return: The _date of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Дата расчета  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def first(self):
        """Gets the first of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Имя фактора риска первого столбца/колонки матрицы  # noqa: E501

        :return: The first of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Имя фактора риска первого столбца/колонки матрицы  # noqa: E501

        :param first: The first of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def first_type(self):
        """Gets the first_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Тип фактора риска первого столбца/колонки матрицы:   0 – облигации  1 – валюты   2 - акции  # noqa: E501

        :return: The first_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._first_type

    @first_type.setter
    def first_type(self, first_type):
        """Sets the first_type of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Тип фактора риска первого столбца/колонки матрицы:   0 – облигации  1 – валюты   2 - акции  # noqa: E501

        :param first_type: The first_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: int
        """

        self._first_type = first_type

    @property
    def second(self):
        """Gets the second of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Имя фактора риска второго столбца/колонки матрицы  # noqa: E501

        :return: The second of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: str
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Имя фактора риска второго столбца/колонки матрицы  # noqa: E501

        :param second: The second of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: str
        """

        self._second = second

    @property
    def second_type(self):
        """Gets the second_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Тип фактора риска второго столбца/колонки матрицы  # noqa: E501

        :return: The second_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: int
        """
        return self._second_type

    @second_type.setter
    def second_type(self, second_type):
        """Sets the second_type of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Тип фактора риска второго столбца/колонки матрицы  # noqa: E501

        :param second_type: The second_type of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: int
        """

        self._second_type = second_type

    @property
    def em_acov(self):
        """Gets the em_acov of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Значение ковариации факторов риска  # noqa: E501

        :return: The em_acov of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: float
        """
        return self._em_acov

    @em_acov.setter
    def em_acov(self, em_acov):
        """Sets the em_acov of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Значение ковариации факторов риска  # noqa: E501

        :param em_acov: The em_acov of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: float
        """

        self._em_acov = em_acov

    @property
    def cor(self):
        """Gets the cor of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501

        Значение корреляции факторов риска  # noqa: E501

        :return: The cor of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :rtype: float
        """
        return self._cor

    @cor.setter
    def cor(self, cor):
        """Sets the cor of this EfirDataHubModelsModelsRiskVarMatrixElement.

        Значение корреляции факторов риска  # noqa: E501

        :param cor: The cor of this EfirDataHubModelsModelsRiskVarMatrixElement.  # noqa: E501
        :type: float
        """

        self._cor = cor

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
        if issubclass(EfirDataHubModelsModelsRiskVarMatrixElement, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskVarMatrixElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
