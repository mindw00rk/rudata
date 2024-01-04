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

class EfirDataHubModelsModelsEmitentScoringFields(object):
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
        'shortname_rus': 'str',
        'model': 'str',
        'source': 'str',
        'last_reported_date': 'datetime',
        'update_date': 'str',
        'pd': 'float',
        'pd_pit': 'float',
        'rating': 'str',
        'rating_ru': 'str',
        'counterpartyid': 'int',
        'grade_probabilities': 'AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilities',
        'grade_probabilities_ru': 'AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilitiesRu'
    }

    attribute_map = {
        'code': 'code',
        'fininst_id': 'fininstId',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'shortname_rus': 'shortname_rus',
        'model': 'model',
        'source': 'source',
        'last_reported_date': 'last_reported_date',
        'update_date': 'update_date',
        'pd': 'pd',
        'pd_pit': 'pd_pit',
        'rating': 'rating',
        'rating_ru': 'rating_ru',
        'counterpartyid': 'counterpartyid',
        'grade_probabilities': 'grade_probabilities',
        'grade_probabilities_ru': 'grade_probabilities_ru'
    }

    def __init__(self, code=None, fininst_id=None, inn=None, ogrn=None, shortname_rus=None, model=None, source=None, last_reported_date=None, update_date=None, pd=None, pd_pit=None, rating=None, rating_ru=None, counterpartyid=None, grade_probabilities=None, grade_probabilities_ru=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentScoringFields - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._fininst_id = None
        self._inn = None
        self._ogrn = None
        self._shortname_rus = None
        self._model = None
        self._source = None
        self._last_reported_date = None
        self._update_date = None
        self._pd = None
        self._pd_pit = None
        self._rating = None
        self._rating_ru = None
        self._counterpartyid = None
        self._grade_probabilities = None
        self._grade_probabilities_ru = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if model is not None:
            self.model = model
        if source is not None:
            self.source = source
        if last_reported_date is not None:
            self.last_reported_date = last_reported_date
        if update_date is not None:
            self.update_date = update_date
        if pd is not None:
            self.pd = pd
        if pd_pit is not None:
            self.pd_pit = pd_pit
        if rating is not None:
            self.rating = rating
        if rating_ru is not None:
            self.rating_ru = rating_ru
        if counterpartyid is not None:
            self.counterpartyid = counterpartyid
        if grade_probabilities is not None:
            self.grade_probabilities = grade_probabilities
        if grade_probabilities_ru is not None:
            self.grade_probabilities_ru = grade_probabilities_ru

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        значение Code из запроса (ИНН или ОГРН)  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsEmitentScoringFields.

        значение Code из запроса (ИНН или ОГРН)  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsEmitentScoringFields.

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        ИНН  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentScoringFields.

        ИНН  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        ОГРН  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentScoringFields.

        ОГРН  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Краткое наименование компании  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsEmitentScoringFields.

        Краткое наименование компании  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def model(self):
        """Gets the model of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Модель расчета  # noqa: E501

        :return: The model of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this EfirDataHubModelsModelsEmitentScoringFields.

        Модель расчета  # noqa: E501

        :param model: The model of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def source(self):
        """Gets the source of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        База расчета - РСБУ или МСФО  # noqa: E501

        :return: The source of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EfirDataHubModelsModelsEmitentScoringFields.

        База расчета - РСБУ или МСФО  # noqa: E501

        :param source: The source of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def last_reported_date(self):
        """Gets the last_reported_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Дата первого присвоения скоринга  # noqa: E501

        :return: The last_reported_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: datetime
        """
        return self._last_reported_date

    @last_reported_date.setter
    def last_reported_date(self, last_reported_date):
        """Sets the last_reported_date of this EfirDataHubModelsModelsEmitentScoringFields.

        Дата первого присвоения скоринга  # noqa: E501

        :param last_reported_date: The last_reported_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: datetime
        """

        self._last_reported_date = last_reported_date

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Дата последнего обновления расчета  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsEmitentScoringFields.

        Дата последнего обновления расчета  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

    @property
    def pd(self):
        """Gets the pd of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Вероятность дефолта в процентах  # noqa: E501

        :return: The pd of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: float
        """
        return self._pd

    @pd.setter
    def pd(self, pd):
        """Sets the pd of this EfirDataHubModelsModelsEmitentScoringFields.

        Вероятность дефолта в процентах  # noqa: E501

        :param pd: The pd of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: float
        """

        self._pd = pd

    @property
    def pd_pit(self):
        """Gets the pd_pit of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Вероятность дефолта в процентах, откорректированная на дату вызова  # noqa: E501

        :return: The pd_pit of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: float
        """
        return self._pd_pit

    @pd_pit.setter
    def pd_pit(self, pd_pit):
        """Sets the pd_pit of this EfirDataHubModelsModelsEmitentScoringFields.

        Вероятность дефолта в процентах, откорректированная на дату вызова  # noqa: E501

        :param pd_pit: The pd_pit of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: float
        """

        self._pd_pit = pd_pit

    @property
    def rating(self):
        """Gets the rating of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Рейтинг  # noqa: E501

        :return: The rating of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this EfirDataHubModelsModelsEmitentScoringFields.

        Рейтинг  # noqa: E501

        :param rating: The rating of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._rating = rating

    @property
    def rating_ru(self):
        """Gets the rating_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Рейтинг по национальной шкале  # noqa: E501

        :return: The rating_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: str
        """
        return self._rating_ru

    @rating_ru.setter
    def rating_ru(self, rating_ru):
        """Sets the rating_ru of this EfirDataHubModelsModelsEmitentScoringFields.

        Рейтинг по национальной шкале  # noqa: E501

        :param rating_ru: The rating_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: str
        """

        self._rating_ru = rating_ru

    @property
    def counterpartyid(self):
        """Gets the counterpartyid of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The counterpartyid of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: int
        """
        return self._counterpartyid

    @counterpartyid.setter
    def counterpartyid(self, counterpartyid):
        """Sets the counterpartyid of this EfirDataHubModelsModelsEmitentScoringFields.

        Идентификатор контрагента  # noqa: E501

        :param counterpartyid: The counterpartyid of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: int
        """

        self._counterpartyid = counterpartyid

    @property
    def grade_probabilities(self):
        """Gets the grade_probabilities of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Вероятности попадания в грейд  # noqa: E501

        :return: The grade_probabilities of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilities
        """
        return self._grade_probabilities

    @grade_probabilities.setter
    def grade_probabilities(self, grade_probabilities):
        """Sets the grade_probabilities of this EfirDataHubModelsModelsEmitentScoringFields.

        Вероятности попадания в грейд  # noqa: E501

        :param grade_probabilities: The grade_probabilities of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilities
        """

        self._grade_probabilities = grade_probabilities

    @property
    def grade_probabilities_ru(self):
        """Gets the grade_probabilities_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501

        Вероятности попадания в грейды по национальной шкале  # noqa: E501

        :return: The grade_probabilities_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilitiesRu
        """
        return self._grade_probabilities_ru

    @grade_probabilities_ru.setter
    def grade_probabilities_ru(self, grade_probabilities_ru):
        """Sets the grade_probabilities_ru of this EfirDataHubModelsModelsEmitentScoringFields.

        Вероятности попадания в грейды по национальной шкале  # noqa: E501

        :param grade_probabilities_ru: The grade_probabilities_ru of this EfirDataHubModelsModelsEmitentScoringFields.  # noqa: E501
        :type: AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilitiesRu
        """

        self._grade_probabilities_ru = grade_probabilities_ru

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
        if issubclass(EfirDataHubModelsModelsEmitentScoringFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentScoringFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other