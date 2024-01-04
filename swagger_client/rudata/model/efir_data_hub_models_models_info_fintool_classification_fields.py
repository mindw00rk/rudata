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

class EfirDataHubModelsModelsInfoFintoolClassificationFields(object):
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
        'fintoolid': 'int',
        'isin': 'str',
        'reg_code': 'str',
        'fininstid': 'int',
        'inn': 'str',
        'okpo': 'str',
        'sparkid': 'int',
        'id_code': 'int',
        'code': 'str',
        'from_date': 'str',
        'up_to_date': 'datetime',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fintoolid': 'fintoolid',
        'isin': 'isin',
        'reg_code': 'reg_code',
        'fininstid': 'fininstid',
        'inn': 'inn',
        'okpo': 'okpo',
        'sparkid': 'sparkid',
        'id_code': 'id_code',
        'code': 'code',
        'from_date': 'from_date',
        'up_to_date': 'up_to_date',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fintoolid=None, isin=None, reg_code=None, fininstid=None, inn=None, okpo=None, sparkid=None, id_code=None, code=None, from_date=None, up_to_date=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoFintoolClassificationFields - a model defined in Swagger"""  # noqa: E501
        self._fintoolid = None
        self._isin = None
        self._reg_code = None
        self._fininstid = None
        self._inn = None
        self._okpo = None
        self._sparkid = None
        self._id_code = None
        self._code = None
        self._from_date = None
        self._up_to_date = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fintoolid is not None:
            self.fintoolid = fintoolid
        if isin is not None:
            self.isin = isin
        if reg_code is not None:
            self.reg_code = reg_code
        if fininstid is not None:
            self.fininstid = fininstid
        if inn is not None:
            self.inn = inn
        if okpo is not None:
            self.okpo = okpo
        if sparkid is not None:
            self.sparkid = sparkid
        if id_code is not None:
            self.id_code = id_code
        if code is not None:
            self.code = code
        if from_date is not None:
            self.from_date = from_date
        if up_to_date is not None:
            self.up_to_date = up_to_date
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fintoolid(self):
        """Gets the fintoolid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ID финансового инструмента в БД интерфакс  # noqa: E501

        :return: The fintoolid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._fintoolid

    @fintoolid.setter
    def fintoolid(self, fintoolid):
        """Sets the fintoolid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ID финансового инструмента в БД интерфакс  # noqa: E501

        :param fintoolid: The fintoolid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: int
        """

        self._fintoolid = fintoolid

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def reg_code(self):
        """Gets the reg_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Регистрационный номер  # noqa: E501

        :return: The reg_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_code

    @reg_code.setter
    def reg_code(self, reg_code):
        """Sets the reg_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Регистрационный номер  # noqa: E501

        :param reg_code: The reg_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._reg_code = reg_code

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ID эмитента в БД Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ID эмитента в БД Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ИНН  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ИНН  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def okpo(self):
        """Gets the okpo of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ОКПО  # noqa: E501

        :return: The okpo of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._okpo

    @okpo.setter
    def okpo(self, okpo):
        """Sets the okpo of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ОКПО  # noqa: E501

        :param okpo: The okpo of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._okpo = okpo

    @property
    def sparkid(self):
        """Gets the sparkid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        ID эмитента в БД СПАРК  # noqa: E501

        :return: The sparkid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._sparkid

    @sparkid.setter
    def sparkid(self, sparkid):
        """Sets the sparkid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        ID эмитента в БД СПАРК  # noqa: E501

        :param sparkid: The sparkid of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: int
        """

        self._sparkid = sparkid

    @property
    def id_code(self):
        """Gets the id_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Идентификатор классификатора (значение поля ID объекта Classificator из метода /Info/ClassificationCodes)  # noqa: E501

        :return: The id_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._id_code

    @id_code.setter
    def id_code(self, id_code):
        """Sets the id_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Идентификатор классификатора (значение поля ID объекта Classificator из метода /Info/ClassificationCodes)  # noqa: E501

        :param id_code: The id_code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: int
        """

        self._id_code = id_code

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Код классификатора  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Код классификатора  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def from_date(self):
        """Gets the from_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Дата начала действия значения классификатора  # noqa: E501

        :return: The from_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Дата начала действия значения классификатора  # noqa: E501

        :param from_date: The from_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: str
        """

        self._from_date = from_date

    @property
    def up_to_date(self):
        """Gets the up_to_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Дата окончания действия значения классификатора.  # noqa: E501

        :return: The up_to_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: datetime
        """
        return self._up_to_date

    @up_to_date.setter
    def up_to_date(self, up_to_date):
        """Sets the up_to_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Дата окончания действия значения классификатора.  # noqa: E501

        :param up_to_date: The up_to_date of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: datetime
        """

        self._up_to_date = up_to_date

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsInfoFintoolClassificationFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsInfoFintoolClassificationFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoFintoolClassificationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other