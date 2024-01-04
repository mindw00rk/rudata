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

class EfirDataHubModelsModelsRatingListRatingsFields(object):
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
        'id': 'int',
        'rating_id': 'int',
        'code_name': 'str',
        'agency': 'str',
        'fullname_rus': 'str',
        'fullname_eng': 'str',
        'for_instrument': 'int',
        'for_company': 'int',
        'agency_eng': 'str',
        'official_name': 'str',
        'is_credit': 'int',
        'term_type': 'str',
        'term_type_name': 'str',
        'currency_type': 'str',
        'currency_type_name': 'str',
        'scale_type': 'str',
        'scale_type_name': 'str',
        'is_archive': 'int',
        'is_accred_br': 'int',
        'doc_511p': 'str',
        'doc_421p': 'str',
        'doc_180i': 'str',
        'agency_id': 'int',
        'used_in_agg': 'bool',
        'scale_id': 'int',
        'aggregation_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rating_id': 'rating_id',
        'code_name': 'code_name',
        'agency': 'agency',
        'fullname_rus': 'fullname_rus',
        'fullname_eng': 'fullname_eng',
        'for_instrument': 'for_instrument',
        'for_company': 'for_company',
        'agency_eng': 'agency_eng',
        'official_name': 'official_name',
        'is_credit': 'is_credit',
        'term_type': 'term_type',
        'term_type_name': 'term_type_name',
        'currency_type': 'currency_type',
        'currency_type_name': 'currency_type_name',
        'scale_type': 'scale_type',
        'scale_type_name': 'scale_type_name',
        'is_archive': 'is_archive',
        'is_accred_br': 'is_accred_br',
        'doc_511p': 'doc_511p',
        'doc_421p': 'doc_421p',
        'doc_180i': 'doc_180i',
        'agency_id': 'agency_id',
        'used_in_agg': 'usedInAgg',
        'scale_id': 'scale_id',
        'aggregation_type': 'aggregation_type'
    }

    def __init__(self, id=None, rating_id=None, code_name=None, agency=None, fullname_rus=None, fullname_eng=None, for_instrument=None, for_company=None, agency_eng=None, official_name=None, is_credit=None, term_type=None, term_type_name=None, currency_type=None, currency_type_name=None, scale_type=None, scale_type_name=None, is_archive=None, is_accred_br=None, doc_511p=None, doc_421p=None, doc_180i=None, agency_id=None, used_in_agg=None, scale_id=None, aggregation_type=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingListRatingsFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._rating_id = None
        self._code_name = None
        self._agency = None
        self._fullname_rus = None
        self._fullname_eng = None
        self._for_instrument = None
        self._for_company = None
        self._agency_eng = None
        self._official_name = None
        self._is_credit = None
        self._term_type = None
        self._term_type_name = None
        self._currency_type = None
        self._currency_type_name = None
        self._scale_type = None
        self._scale_type_name = None
        self._is_archive = None
        self._is_accred_br = None
        self._doc_511p = None
        self._doc_421p = None
        self._doc_180i = None
        self._agency_id = None
        self._used_in_agg = None
        self._scale_id = None
        self._aggregation_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if rating_id is not None:
            self.rating_id = rating_id
        if code_name is not None:
            self.code_name = code_name
        if agency is not None:
            self.agency = agency
        if fullname_rus is not None:
            self.fullname_rus = fullname_rus
        if fullname_eng is not None:
            self.fullname_eng = fullname_eng
        if for_instrument is not None:
            self.for_instrument = for_instrument
        if for_company is not None:
            self.for_company = for_company
        if agency_eng is not None:
            self.agency_eng = agency_eng
        if official_name is not None:
            self.official_name = official_name
        if is_credit is not None:
            self.is_credit = is_credit
        if term_type is not None:
            self.term_type = term_type
        if term_type_name is not None:
            self.term_type_name = term_type_name
        if currency_type is not None:
            self.currency_type = currency_type
        if currency_type_name is not None:
            self.currency_type_name = currency_type_name
        if scale_type is not None:
            self.scale_type = scale_type
        if scale_type_name is not None:
            self.scale_type_name = scale_type_name
        if is_archive is not None:
            self.is_archive = is_archive
        if is_accred_br is not None:
            self.is_accred_br = is_accred_br
        if doc_511p is not None:
            self.doc_511p = doc_511p
        if doc_421p is not None:
            self.doc_421p = doc_421p
        if doc_180i is not None:
            self.doc_180i = doc_180i
        if agency_id is not None:
            self.agency_id = agency_id
        if used_in_agg is not None:
            self.used_in_agg = used_in_agg
        if scale_id is not None:
            self.scale_id = scale_id
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор рейтинга (устарел, надо использовать rating_id)  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор рейтинга (устарел, надо использовать rating_id)  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rating_id(self):
        """Gets the rating_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор вида рейтинга  # noqa: E501

        :return: The rating_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id):
        """Sets the rating_id of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор вида рейтинга  # noqa: E501

        :param rating_id: The rating_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._rating_id = rating_id

    @property
    def code_name(self):
        """Gets the code_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Символьный код рейтинга  # noqa: E501

        :return: The code_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._code_name

    @code_name.setter
    def code_name(self, code_name):
        """Sets the code_name of this EfirDataHubModelsModelsRatingListRatingsFields.

        Символьный код рейтинга  # noqa: E501

        :param code_name: The code_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._code_name = code_name

    @property
    def agency(self):
        """Gets the agency of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Рейтинговое агентство (рус)  # noqa: E501

        :return: The agency of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this EfirDataHubModelsModelsRatingListRatingsFields.

        Рейтинговое агентство (рус)  # noqa: E501

        :param agency: The agency of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._agency = agency

    @property
    def fullname_rus(self):
        """Gets the fullname_rus of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Русское наименование рейтинга  # noqa: E501

        :return: The fullname_rus of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_rus

    @fullname_rus.setter
    def fullname_rus(self, fullname_rus):
        """Sets the fullname_rus of this EfirDataHubModelsModelsRatingListRatingsFields.

        Русское наименование рейтинга  # noqa: E501

        :param fullname_rus: The fullname_rus of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._fullname_rus = fullname_rus

    @property
    def fullname_eng(self):
        """Gets the fullname_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Английское наименование рейтинга  # noqa: E501

        :return: The fullname_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._fullname_eng

    @fullname_eng.setter
    def fullname_eng(self, fullname_eng):
        """Sets the fullname_eng of this EfirDataHubModelsModelsRatingListRatingsFields.

        Английское наименование рейтинга  # noqa: E501

        :param fullname_eng: The fullname_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._fullname_eng = fullname_eng

    @property
    def for_instrument(self):
        """Gets the for_instrument of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        = 1, если рейтинг относится к инструменту  # noqa: E501

        :return: The for_instrument of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._for_instrument

    @for_instrument.setter
    def for_instrument(self, for_instrument):
        """Sets the for_instrument of this EfirDataHubModelsModelsRatingListRatingsFields.

        = 1, если рейтинг относится к инструменту  # noqa: E501

        :param for_instrument: The for_instrument of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._for_instrument = for_instrument

    @property
    def for_company(self):
        """Gets the for_company of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        = 1, если рейтинг относится к эмитенту  # noqa: E501

        :return: The for_company of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._for_company

    @for_company.setter
    def for_company(self, for_company):
        """Sets the for_company of this EfirDataHubModelsModelsRatingListRatingsFields.

        = 1, если рейтинг относится к эмитенту  # noqa: E501

        :param for_company: The for_company of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._for_company = for_company

    @property
    def agency_eng(self):
        """Gets the agency_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Рейтинговое агентство (анг)  # noqa: E501

        :return: The agency_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._agency_eng

    @agency_eng.setter
    def agency_eng(self, agency_eng):
        """Sets the agency_eng of this EfirDataHubModelsModelsRatingListRatingsFields.

        Рейтинговое агентство (анг)  # noqa: E501

        :param agency_eng: The agency_eng of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._agency_eng = agency_eng

    @property
    def official_name(self):
        """Gets the official_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Официальное наименование рейтинга  # noqa: E501

        :return: The official_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._official_name

    @official_name.setter
    def official_name(self, official_name):
        """Sets the official_name of this EfirDataHubModelsModelsRatingListRatingsFields.

        Официальное наименование рейтинга  # noqa: E501

        :param official_name: The official_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._official_name = official_name

    @property
    def is_credit(self):
        """Gets the is_credit of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        = 1 для кредитных рейтингов  # noqa: E501

        :return: The is_credit of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._is_credit

    @is_credit.setter
    def is_credit(self, is_credit):
        """Sets the is_credit of this EfirDataHubModelsModelsRatingListRatingsFields.

        = 1 для кредитных рейтингов  # noqa: E501

        :param is_credit: The is_credit of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._is_credit = is_credit

    @property
    def term_type(self):
        """Gets the term_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор типа срочности  # noqa: E501

        :return: The term_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._term_type

    @term_type.setter
    def term_type(self, term_type):
        """Sets the term_type of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор типа срочности  # noqa: E501

        :param term_type: The term_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._term_type = term_type

    @property
    def term_type_name(self):
        """Gets the term_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Наименование типа срочности  # noqa: E501

        :return: The term_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._term_type_name

    @term_type_name.setter
    def term_type_name(self, term_type_name):
        """Sets the term_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.

        Наименование типа срочности  # noqa: E501

        :param term_type_name: The term_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._term_type_name = term_type_name

    @property
    def currency_type(self):
        """Gets the currency_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор типа валюты  # noqa: E501

        :return: The currency_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._currency_type

    @currency_type.setter
    def currency_type(self, currency_type):
        """Sets the currency_type of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор типа валюты  # noqa: E501

        :param currency_type: The currency_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._currency_type = currency_type

    @property
    def currency_type_name(self):
        """Gets the currency_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Наименование типа валюты  # noqa: E501

        :return: The currency_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._currency_type_name

    @currency_type_name.setter
    def currency_type_name(self, currency_type_name):
        """Sets the currency_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.

        Наименование типа валюты  # noqa: E501

        :param currency_type_name: The currency_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._currency_type_name = currency_type_name

    @property
    def scale_type(self):
        """Gets the scale_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор типа шкалы  # noqa: E501

        :return: The scale_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type):
        """Sets the scale_type of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор типа шкалы  # noqa: E501

        :param scale_type: The scale_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._scale_type = scale_type

    @property
    def scale_type_name(self):
        """Gets the scale_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Наименование типа шкалы  # noqa: E501

        :return: The scale_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._scale_type_name

    @scale_type_name.setter
    def scale_type_name(self, scale_type_name):
        """Sets the scale_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.

        Наименование типа шкалы  # noqa: E501

        :param scale_type_name: The scale_type_name of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._scale_type_name = scale_type_name

    @property
    def is_archive(self):
        """Gets the is_archive of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        = 1 для архивных (не используемых на текущий момент) рейтингов  # noqa: E501

        :return: The is_archive of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._is_archive

    @is_archive.setter
    def is_archive(self, is_archive):
        """Sets the is_archive of this EfirDataHubModelsModelsRatingListRatingsFields.

        = 1 для архивных (не используемых на текущий момент) рейтингов  # noqa: E501

        :param is_archive: The is_archive of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._is_archive = is_archive

    @property
    def is_accred_br(self):
        """Gets the is_accred_br of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Аккредитация Банка России  # noqa: E501

        :return: The is_accred_br of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._is_accred_br

    @is_accred_br.setter
    def is_accred_br(self, is_accred_br):
        """Sets the is_accred_br of this EfirDataHubModelsModelsRatingListRatingsFields.

        Аккредитация Банка России  # noqa: E501

        :param is_accred_br: The is_accred_br of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._is_accred_br = is_accred_br

    @property
    def doc_511p(self):
        """Gets the doc_511p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        511-П  # noqa: E501

        :return: The doc_511p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._doc_511p

    @doc_511p.setter
    def doc_511p(self, doc_511p):
        """Sets the doc_511p of this EfirDataHubModelsModelsRatingListRatingsFields.

        511-П  # noqa: E501

        :param doc_511p: The doc_511p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._doc_511p = doc_511p

    @property
    def doc_421p(self):
        """Gets the doc_421p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        421-П  # noqa: E501

        :return: The doc_421p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._doc_421p

    @doc_421p.setter
    def doc_421p(self, doc_421p):
        """Sets the doc_421p of this EfirDataHubModelsModelsRatingListRatingsFields.

        421-П  # noqa: E501

        :param doc_421p: The doc_421p of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._doc_421p = doc_421p

    @property
    def doc_180i(self):
        """Gets the doc_180i of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        180-И  # noqa: E501

        :return: The doc_180i of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._doc_180i

    @doc_180i.setter
    def doc_180i(self, doc_180i):
        """Sets the doc_180i of this EfirDataHubModelsModelsRatingListRatingsFields.

        180-И  # noqa: E501

        :param doc_180i: The doc_180i of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._doc_180i = doc_180i

    @property
    def agency_id(self):
        """Gets the agency_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор агентства  # noqa: E501

        :return: The agency_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор агентства  # noqa: E501

        :param agency_id: The agency_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._agency_id = agency_id

    @property
    def used_in_agg(self):
        """Gets the used_in_agg of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Флаг участия в расчёте агрегированных рейтингов.  # noqa: E501

        :return: The used_in_agg of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: bool
        """
        return self._used_in_agg

    @used_in_agg.setter
    def used_in_agg(self, used_in_agg):
        """Sets the used_in_agg of this EfirDataHubModelsModelsRatingListRatingsFields.

        Флаг участия в расчёте агрегированных рейтингов.  # noqa: E501

        :param used_in_agg: The used_in_agg of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: bool
        """

        self._used_in_agg = used_in_agg

    @property
    def scale_id(self):
        """Gets the scale_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Идентификатор шкалы  # noqa: E501

        :return: The scale_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: int
        """
        return self._scale_id

    @scale_id.setter
    def scale_id(self, scale_id):
        """Sets the scale_id of this EfirDataHubModelsModelsRatingListRatingsFields.

        Идентификатор шкалы  # noqa: E501

        :param scale_id: The scale_id of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: int
        """

        self._scale_id = scale_id

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501

        Тип агрегации ('RU' или 'BIG3')  # noqa: E501

        :return: The aggregation_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this EfirDataHubModelsModelsRatingListRatingsFields.

        Тип агрегации ('RU' или 'BIG3')  # noqa: E501

        :param aggregation_type: The aggregation_type of this EfirDataHubModelsModelsRatingListRatingsFields.  # noqa: E501
        :type: str
        """

        self._aggregation_type = aggregation_type

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
        if issubclass(EfirDataHubModelsModelsRatingListRatingsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingListRatingsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
