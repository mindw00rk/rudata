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

class EfirDataHubModelsModelsRiskCorpInvestClassFields(object):
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
        'fininstid': 'int',
        'code': 'str',
        'inn': 'str',
        'ogrn': 'str',
        'lei': 'str',
        'company_name': 'str',
        'dt': 'datetime',
        'update_date': 'datetime',
        'issuer_fininstid': 'int',
        'issuer_inn': 'str',
        'issuer_ogrn': 'str',
        'issuer_lei': 'str',
        'issuer_name': 'str',
        'fintoolid': 'int',
        'isin': 'str',
        'fintool_name': 'str',
        'investment_grade': 'bool',
        'corporate_issuer': 'bool',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fininstid': 'fininstid',
        'code': 'code',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'lei': 'lei',
        'company_name': 'company_name',
        'dt': 'dt',
        'update_date': 'update_date',
        'issuer_fininstid': 'issuer_fininstid',
        'issuer_inn': 'issuer_inn',
        'issuer_ogrn': 'issuer_ogrn',
        'issuer_lei': 'issuer_lei',
        'issuer_name': 'issuer_name',
        'fintoolid': 'fintoolid',
        'isin': 'isin',
        'fintool_name': 'fintool_name',
        'investment_grade': 'investment_grade',
        'corporate_issuer': 'corporate_issuer',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fininstid=None, code=None, inn=None, ogrn=None, lei=None, company_name=None, dt=None, update_date=None, issuer_fininstid=None, issuer_inn=None, issuer_ogrn=None, issuer_lei=None, issuer_name=None, fintoolid=None, isin=None, fintool_name=None, investment_grade=None, corporate_issuer=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsRiskCorpInvestClassFields - a model defined in Swagger"""  # noqa: E501
        self._fininstid = None
        self._code = None
        self._inn = None
        self._ogrn = None
        self._lei = None
        self._company_name = None
        self._dt = None
        self._update_date = None
        self._issuer_fininstid = None
        self._issuer_inn = None
        self._issuer_ogrn = None
        self._issuer_lei = None
        self._issuer_name = None
        self._fintoolid = None
        self._isin = None
        self._fintool_name = None
        self._investment_grade = None
        self._corporate_issuer = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fininstid is not None:
            self.fininstid = fininstid
        if code is not None:
            self.code = code
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if lei is not None:
            self.lei = lei
        if company_name is not None:
            self.company_name = company_name
        if dt is not None:
            self.dt = dt
        if update_date is not None:
            self.update_date = update_date
        if issuer_fininstid is not None:
            self.issuer_fininstid = issuer_fininstid
        if issuer_inn is not None:
            self.issuer_inn = issuer_inn
        if issuer_ogrn is not None:
            self.issuer_ogrn = issuer_ogrn
        if issuer_lei is not None:
            self.issuer_lei = issuer_lei
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if fintoolid is not None:
            self.fintoolid = fintoolid
        if isin is not None:
            self.isin = isin
        if fintool_name is not None:
            self.fintool_name = fintool_name
        if investment_grade is not None:
            self.investment_grade = investment_grade
        if corporate_issuer is not None:
            self.corporate_issuer = corporate_issuer
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Идентификатор компании, заданный во входном параметре  codes (ИНН, ОГРН, LEI)  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Идентификатор компании, заданный во входном параметре  codes (ИНН, ОГРН, LEI)  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        ИНН компании  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        ИНН компании  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        ОГРН компании  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        ОГРН компании  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def lei(self):
        """Gets the lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        LEI-код компании  # noqa: E501

        :return: The lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._lei

    @lei.setter
    def lei(self, lei):
        """Sets the lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        LEI-код компании  # noqa: E501

        :param lei: The lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._lei = lei

    @property
    def company_name(self):
        """Gets the company_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Наименование компании  # noqa: E501

        :return: The company_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Наименование компании  # noqa: E501

        :param company_name: The company_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def dt(self):
        """Gets the dt of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Дата расчета (дата, для которой выполнялся расчет  # noqa: E501

        :return: The dt of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: datetime
        """
        return self._dt

    @dt.setter
    def dt(self, dt):
        """Sets the dt of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Дата расчета (дата, для которой выполнялся расчет  # noqa: E501

        :param dt: The dt of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: datetime
        """

        self._dt = dt

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Дата обновления данных  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Дата обновления данных  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def issuer_fininstid(self):
        """Gets the issuer_fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Идентификатор компании, чьи бумаги попали в котировальный список  # noqa: E501

        :return: The issuer_fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: int
        """
        return self._issuer_fininstid

    @issuer_fininstid.setter
    def issuer_fininstid(self, issuer_fininstid):
        """Sets the issuer_fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Идентификатор компании, чьи бумаги попали в котировальный список  # noqa: E501

        :param issuer_fininstid: The issuer_fininstid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: int
        """

        self._issuer_fininstid = issuer_fininstid

    @property
    def issuer_inn(self):
        """Gets the issuer_inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        ИНН компании, чьи бумаги попали в котировальный список  # noqa: E501

        :return: The issuer_inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer_inn

    @issuer_inn.setter
    def issuer_inn(self, issuer_inn):
        """Sets the issuer_inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        ИНН компании, чьи бумаги попали в котировальный список  # noqa: E501

        :param issuer_inn: The issuer_inn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._issuer_inn = issuer_inn

    @property
    def issuer_ogrn(self):
        """Gets the issuer_ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        ОГРН компании, чьи бумаги попали в котировальный список  # noqa: E501

        :return: The issuer_ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer_ogrn

    @issuer_ogrn.setter
    def issuer_ogrn(self, issuer_ogrn):
        """Sets the issuer_ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        ОГРН компании, чьи бумаги попали в котировальный список  # noqa: E501

        :param issuer_ogrn: The issuer_ogrn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._issuer_ogrn = issuer_ogrn

    @property
    def issuer_lei(self):
        """Gets the issuer_lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        LEI-код компании, чьи бумаги попали в котировальный список  # noqa: E501

        :return: The issuer_lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer_lei

    @issuer_lei.setter
    def issuer_lei(self, issuer_lei):
        """Sets the issuer_lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        LEI-код компании, чьи бумаги попали в котировальный список  # noqa: E501

        :param issuer_lei: The issuer_lei of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._issuer_lei = issuer_lei

    @property
    def issuer_name(self):
        """Gets the issuer_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Наименование компании, чьи бумаги попали в котировальный список  # noqa: E501

        :return: The issuer_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Наименование компании, чьи бумаги попали в котировальный список  # noqa: E501

        :param issuer_name: The issuer_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._issuer_name = issuer_name

    @property
    def fintoolid(self):
        """Gets the fintoolid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Идентификатор бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :return: The fintoolid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: int
        """
        return self._fintoolid

    @fintoolid.setter
    def fintoolid(self, fintoolid):
        """Sets the fintoolid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Идентификатор бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :param fintoolid: The fintoolid of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: int
        """

        self._fintoolid = fintoolid

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        ISIN бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        ISIN бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def fintool_name(self):
        """Gets the fintool_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Наименование бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :return: The fintool_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: str
        """
        return self._fintool_name

    @fintool_name.setter
    def fintool_name(self, fintool_name):
        """Sets the fintool_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Наименование бумаги эмитента, попавшей в котировальный список  # noqa: E501

        :param fintool_name: The fintool_name of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: str
        """

        self._fintool_name = fintool_name

    @property
    def investment_grade(self):
        """Gets the investment_grade of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Принадлежность к инвестиционному классу (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована.  # noqa: E501

        :return: The investment_grade of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: bool
        """
        return self._investment_grade

    @investment_grade.setter
    def investment_grade(self, investment_grade):
        """Sets the investment_grade of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Принадлежность к инвестиционному классу (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована.  # noqa: E501

        :param investment_grade: The investment_grade of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: bool
        """

        self._investment_grade = investment_grade

    @property
    def corporate_issuer(self):
        """Gets the corporate_issuer of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Принадлежность к корпоративному сектору (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована.  # noqa: E501

        :return: The corporate_issuer of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: bool
        """
        return self._corporate_issuer

    @corporate_issuer.setter
    def corporate_issuer(self, corporate_issuer):
        """Sets the corporate_issuer of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Принадлежность к корпоративному сектору (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована.  # noqa: E501

        :param corporate_issuer: The corporate_issuer of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: bool
        """

        self._corporate_issuer = corporate_issuer

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsRiskCorpInvestClassFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsRiskCorpInvestClassFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRiskCorpInvestClassFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other