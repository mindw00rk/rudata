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

class EfirDataHubModelsModelsInfoCountryClassificationFields(object):
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
        'country_id': 'int',
        'code_rus': 'str',
        'code_eng': 'str',
        'id_code': 'int',
        'code': 'str',
        'note': 'str',
        'from_date': 'datetime',
        'up_to_date': 'datetime',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'country_id': 'country_id',
        'code_rus': 'code_rus',
        'code_eng': 'code_eng',
        'id_code': 'id_code',
        'code': 'code',
        'note': 'note',
        'from_date': 'from_date',
        'up_to_date': 'up_to_date',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, country_id=None, code_rus=None, code_eng=None, id_code=None, code=None, note=None, from_date=None, up_to_date=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoCountryClassificationFields - a model defined in Swagger"""  # noqa: E501
        self._country_id = None
        self._code_rus = None
        self._code_eng = None
        self._id_code = None
        self._code = None
        self._note = None
        self._from_date = None
        self._up_to_date = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if country_id is not None:
            self.country_id = country_id
        if code_rus is not None:
            self.code_rus = code_rus
        if code_eng is not None:
            self.code_eng = code_eng
        if id_code is not None:
            self.id_code = id_code
        if code is not None:
            self.code = code
        if note is not None:
            self.note = note
        if from_date is not None:
            self.from_date = from_date
        if up_to_date is not None:
            self.up_to_date = up_to_date
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def country_id(self):
        """Gets the country_id of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Идентификатор страны в БД  # noqa: E501

        :return: The country_id of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Идентификатор страны в БД  # noqa: E501

        :param country_id: The country_id of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def code_rus(self):
        """Gets the code_rus of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Код страны (рус)  # noqa: E501

        :return: The code_rus of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._code_rus

    @code_rus.setter
    def code_rus(self, code_rus):
        """Sets the code_rus of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Код страны (рус)  # noqa: E501

        :param code_rus: The code_rus of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: str
        """

        self._code_rus = code_rus

    @property
    def code_eng(self):
        """Gets the code_eng of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Код страны (англ)  # noqa: E501

        :return: The code_eng of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._code_eng

    @code_eng.setter
    def code_eng(self, code_eng):
        """Sets the code_eng of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Код страны (англ)  # noqa: E501

        :param code_eng: The code_eng of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: str
        """

        self._code_eng = code_eng

    @property
    def id_code(self):
        """Gets the id_code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Идентификатор классификатора (значение поля ID объекта Classificator из метода ClassificationCodes)  # noqa: E501

        :return: The id_code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._id_code

    @id_code.setter
    def id_code(self, id_code):
        """Sets the id_code of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Идентификатор классификатора (значение поля ID объекта Classificator из метода ClassificationCodes)  # noqa: E501

        :param id_code: The id_code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: int
        """

        self._id_code = id_code

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Значение классификатора  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Значение классификатора  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def note(self):
        """Gets the note of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Примечание  # noqa: E501

        :return: The note of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Примечание  # noqa: E501

        :param note: The note of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def from_date(self):
        """Gets the from_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Дата начала действия значения классификатора  # noqa: E501

        :return: The from_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Дата начала действия значения классификатора  # noqa: E501

        :param from_date: The from_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def up_to_date(self):
        """Gets the up_to_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Дата окончания действия значения классификатора  # noqa: E501

        :return: The up_to_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: datetime
        """
        return self._up_to_date

    @up_to_date.setter
    def up_to_date(self, up_to_date):
        """Sets the up_to_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Дата окончания действия значения классификатора  # noqa: E501

        :param up_to_date: The up_to_date of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: datetime
        """

        self._up_to_date = up_to_date

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsInfoCountryClassificationFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsInfoCountryClassificationFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsInfoCountryClassificationFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoCountryClassificationFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
