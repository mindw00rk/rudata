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

class BondCalculatorAccruedInterestModelsAccruedInterestRecord(object):
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
        'fintool_id': 'int',
        'shift_days': 'int',
        'shift_type_source': 'AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordShiftTypeSource',
        'type_currency': 'str',
        '_date': 'datetime',
        'accrued_interest': 'float',
        'accrued_interest_pct': 'float',
        'current_face_value': 'float',
        'current_face_value_pct': 'float',
        'calculation_type': 'AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordCalculationType',
        'error': 'str',
        'face_value_currency': 'str',
        'accrued_interest_currency': 'str',
        'face_value_last_known_date': 'datetime'
    }

    attribute_map = {
        'fintool_id': 'fintoolId',
        'shift_days': 'shiftDays',
        'shift_type_source': 'shiftTypeSource',
        'type_currency': 'typeCurrency',
        '_date': 'date',
        'accrued_interest': 'accruedInterest',
        'accrued_interest_pct': 'accruedInterestPct',
        'current_face_value': 'currentFaceValue',
        'current_face_value_pct': 'currentFaceValuePct',
        'calculation_type': 'calculationType',
        'error': 'error',
        'face_value_currency': 'faceValueCurrency',
        'accrued_interest_currency': 'accruedInterestCurrency',
        'face_value_last_known_date': 'faceValueLastKnownDate'
    }

    def __init__(self, fintool_id=None, shift_days=None, shift_type_source=None, type_currency=None, _date=None, accrued_interest=None, accrued_interest_pct=None, current_face_value=None, current_face_value_pct=None, calculation_type=None, error=None, face_value_currency=None, accrued_interest_currency=None, face_value_last_known_date=None):  # noqa: E501
        """BondCalculatorAccruedInterestModelsAccruedInterestRecord - a model defined in Swagger"""  # noqa: E501
        self._fintool_id = None
        self._shift_days = None
        self._shift_type_source = None
        self._type_currency = None
        self.__date = None
        self._accrued_interest = None
        self._accrued_interest_pct = None
        self._current_face_value = None
        self._current_face_value_pct = None
        self._calculation_type = None
        self._error = None
        self._face_value_currency = None
        self._accrued_interest_currency = None
        self._face_value_last_known_date = None
        self.discriminator = None
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if shift_days is not None:
            self.shift_days = shift_days
        if shift_type_source is not None:
            self.shift_type_source = shift_type_source
        if type_currency is not None:
            self.type_currency = type_currency
        if _date is not None:
            self._date = _date
        if accrued_interest is not None:
            self.accrued_interest = accrued_interest
        if accrued_interest_pct is not None:
            self.accrued_interest_pct = accrued_interest_pct
        if current_face_value is not None:
            self.current_face_value = current_face_value
        if current_face_value_pct is not None:
            self.current_face_value_pct = current_face_value_pct
        if calculation_type is not None:
            self.calculation_type = calculation_type
        if error is not None:
            self.error = error
        if face_value_currency is not None:
            self.face_value_currency = face_value_currency
        if accrued_interest_currency is not None:
            self.accrued_interest_currency = accrued_interest_currency
        if face_value_last_known_date is not None:
            self.face_value_last_known_date = face_value_last_known_date

    @property
    def fintool_id(self):
        """Gets the fintool_id of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :return: The fintool_id of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Идентификатор инструмента в базе Интерфакс  # noqa: E501

        :param fintool_id: The fintool_id of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def shift_days(self):
        """Gets the shift_days of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Число дней смещения  # noqa: E501

        :return: The shift_days of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: int
        """
        return self._shift_days

    @shift_days.setter
    def shift_days(self, shift_days):
        """Sets the shift_days of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Число дней смещения  # noqa: E501

        :param shift_days: The shift_days of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: int
        """

        self._shift_days = shift_days

    @property
    def shift_type_source(self):
        """Gets the shift_type_source of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Тип календаря:  - calendar - календарные дни;  - workdays - рабочие дни.  0 = Calendar  1 = Workdays  # noqa: E501

        :return: The shift_type_source of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordShiftTypeSource
        """
        return self._shift_type_source

    @shift_type_source.setter
    def shift_type_source(self, shift_type_source):
        """Sets the shift_type_source of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Тип календаря:  - calendar - календарные дни;  - workdays - рабочие дни.  0 = Calendar  1 = Workdays  # noqa: E501

        :param shift_type_source: The shift_type_source of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordShiftTypeSource
        """

        self._shift_type_source = shift_type_source

    @property
    def type_currency(self):
        """Gets the type_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Код или источник валюты:  - facevalue - используется календарь страны выпуска;  - jurisdiction - используется календарь страны-эмитента валюты номинала инструмента;  - 3-буквенный код валюты ОКВ.  # noqa: E501

        :return: The type_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._type_currency

    @type_currency.setter
    def type_currency(self, type_currency):
        """Sets the type_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Код или источник валюты:  - facevalue - используется календарь страны выпуска;  - jurisdiction - используется календарь страны-эмитента валюты номинала инструмента;  - 3-буквенный код валюты ОКВ.  # noqa: E501

        :param type_currency: The type_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: str
        """

        self._type_currency = type_currency

    @property
    def _date(self):
        """Gets the _date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Дата, на которую рассчитаны показатели  # noqa: E501

        :return: The _date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Дата, на которую рассчитаны показатели  # noqa: E501

        :param _date: The _date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def accrued_interest(self):
        """Gets the accrued_interest of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        НКД в валюте номинала  # noqa: E501

        :return: The accrued_interest of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: float
        """
        return self._accrued_interest

    @accrued_interest.setter
    def accrued_interest(self, accrued_interest):
        """Sets the accrued_interest of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        НКД в валюте номинала  # noqa: E501

        :param accrued_interest: The accrued_interest of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: float
        """

        self._accrued_interest = accrued_interest

    @property
    def accrued_interest_pct(self):
        """Gets the accrued_interest_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        НКД в процентах от номинала  # noqa: E501

        :return: The accrued_interest_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: float
        """
        return self._accrued_interest_pct

    @accrued_interest_pct.setter
    def accrued_interest_pct(self, accrued_interest_pct):
        """Sets the accrued_interest_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        НКД в процентах от номинала  # noqa: E501

        :param accrued_interest_pct: The accrued_interest_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: float
        """

        self._accrued_interest_pct = accrued_interest_pct

    @property
    def current_face_value(self):
        """Gets the current_face_value of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Текущий номинал в валюте номинала  # noqa: E501

        :return: The current_face_value of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: float
        """
        return self._current_face_value

    @current_face_value.setter
    def current_face_value(self, current_face_value):
        """Sets the current_face_value of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Текущий номинал в валюте номинала  # noqa: E501

        :param current_face_value: The current_face_value of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: float
        """

        self._current_face_value = current_face_value

    @property
    def current_face_value_pct(self):
        """Gets the current_face_value_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Текущий номинал в процентах от номинала  # noqa: E501

        :return: The current_face_value_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: float
        """
        return self._current_face_value_pct

    @current_face_value_pct.setter
    def current_face_value_pct(self, current_face_value_pct):
        """Sets the current_face_value_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Текущий номинал в процентах от номинала  # noqa: E501

        :param current_face_value_pct: The current_face_value_pct of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: float
        """

        self._current_face_value_pct = current_face_value_pct

    @property
    def calculation_type(self):
        """Gets the calculation_type of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Способ вычисления НКД:  - typical - типовой случай;  - null - при ошибке.  0 = Typical  # noqa: E501

        :return: The calculation_type of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordCalculationType
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Способ вычисления НКД:  - typical - типовой случай;  - null - при ошибке.  0 = Typical  # noqa: E501

        :param calculation_type: The calculation_type of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: AllOfBondCalculatorAccruedInterestModelsAccruedInterestRecordCalculationType
        """

        self._calculation_type = calculation_type

    @property
    def error(self):
        """Gets the error of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Текст ошибки при наличии, в остальных случаях null.  # noqa: E501

        :return: The error of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Текст ошибки при наличии, в остальных случаях null.  # noqa: E501

        :param error: The error of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def face_value_currency(self):
        """Gets the face_value_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Код валюты номинала по ОКВ  # noqa: E501

        :return: The face_value_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._face_value_currency

    @face_value_currency.setter
    def face_value_currency(self, face_value_currency):
        """Sets the face_value_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Код валюты номинала по ОКВ  # noqa: E501

        :param face_value_currency: The face_value_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: str
        """

        self._face_value_currency = face_value_currency

    @property
    def accrued_interest_currency(self):
        """Gets the accrued_interest_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501

        Код валюты НКД (купонной выплаты) по ОКВ  # noqa: E501

        :return: The accrued_interest_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._accrued_interest_currency

    @accrued_interest_currency.setter
    def accrued_interest_currency(self, accrued_interest_currency):
        """Sets the accrued_interest_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.

        Код валюты НКД (купонной выплаты) по ОКВ  # noqa: E501

        :param accrued_interest_currency: The accrued_interest_currency of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: str
        """

        self._accrued_interest_currency = accrued_interest_currency

    @property
    def face_value_last_known_date(self):
        """Gets the face_value_last_known_date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501


        :return: The face_value_last_known_date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._face_value_last_known_date

    @face_value_last_known_date.setter
    def face_value_last_known_date(self, face_value_last_known_date):
        """Sets the face_value_last_known_date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.


        :param face_value_last_known_date: The face_value_last_known_date of this BondCalculatorAccruedInterestModelsAccruedInterestRecord.  # noqa: E501
        :type: datetime
        """

        self._face_value_last_known_date = face_value_last_known_date

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
        if issubclass(BondCalculatorAccruedInterestModelsAccruedInterestRecord, dict):
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
        if not isinstance(other, BondCalculatorAccruedInterestModelsAccruedInterestRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
