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

class EfirDataHubModelsModelsRatingListCompaniesFields(object):
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
        'name_rus': 'str',
        'name_eng': 'str',
        'search_info': 'str',
        'code_parent': 'str',
        'okpo': 'str',
        'okato_region': 'float',
        'id': 'int',
        'ogrn': 'str',
        'inn': 'str',
        'fininstid': 'int',
        'bic': 'str',
        'swift_bic': 'str',
        'note': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name_rus': 'name_rus',
        'name_eng': 'name_eng',
        'search_info': 'search_info',
        'code_parent': 'code_parent',
        'okpo': 'okpo',
        'okato_region': 'okato_region',
        'id': 'id',
        'ogrn': 'ogrn',
        'inn': 'inn',
        'fininstid': 'fininstid',
        'bic': 'bic',
        'swift_bic': 'swift_bic',
        'note': 'note'
    }

    def __init__(self, code=None, name_rus=None, name_eng=None, search_info=None, code_parent=None, okpo=None, okato_region=None, id=None, ogrn=None, inn=None, fininstid=None, bic=None, swift_bic=None, note=None):  # noqa: E501
        """EfirDataHubModelsModelsRatingListCompaniesFields - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._name_rus = None
        self._name_eng = None
        self._search_info = None
        self._code_parent = None
        self._okpo = None
        self._okato_region = None
        self._id = None
        self._ogrn = None
        self._inn = None
        self._fininstid = None
        self._bic = None
        self._swift_bic = None
        self._note = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if name_rus is not None:
            self.name_rus = name_rus
        if name_eng is not None:
            self.name_eng = name_eng
        if search_info is not None:
            self.search_info = search_info
        if code_parent is not None:
            self.code_parent = code_parent
        if okpo is not None:
            self.okpo = okpo
        if okato_region is not None:
            self.okato_region = okato_region
        if id is not None:
            self.id = id
        if ogrn is not None:
            self.ogrn = ogrn
        if inn is not None:
            self.inn = inn
        if fininstid is not None:
            self.fininstid = fininstid
        if bic is not None:
            self.bic = bic
        if swift_bic is not None:
            self.swift_bic = swift_bic
        if note is not None:
            self.note = note

    @property
    def code(self):
        """Gets the code of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Символьный идентификатор компании  # noqa: E501

        :return: The code of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Символьный идентификатор компании  # noqa: E501

        :param code: The code of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def name_rus(self):
        """Gets the name_rus of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Русское наименование компании  # noqa: E501

        :return: The name_rus of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._name_rus

    @name_rus.setter
    def name_rus(self, name_rus):
        """Sets the name_rus of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Русское наименование компании  # noqa: E501

        :param name_rus: The name_rus of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._name_rus = name_rus

    @property
    def name_eng(self):
        """Gets the name_eng of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Английское наименование компании  # noqa: E501

        :return: The name_eng of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._name_eng

    @name_eng.setter
    def name_eng(self, name_eng):
        """Sets the name_eng of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Английское наименование компании  # noqa: E501

        :param name_eng: The name_eng of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._name_eng = name_eng

    @property
    def search_info(self):
        """Gets the search_info of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Информация для поиска  # noqa: E501

        :return: The search_info of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._search_info

    @search_info.setter
    def search_info(self, search_info):
        """Sets the search_info of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Информация для поиска  # noqa: E501

        :param search_info: The search_info of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._search_info = search_info

    @property
    def code_parent(self):
        """Gets the code_parent of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Символьный идентификатор управляющей компании(для фондов)  # noqa: E501

        :return: The code_parent of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._code_parent

    @code_parent.setter
    def code_parent(self, code_parent):
        """Sets the code_parent of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Символьный идентификатор управляющей компании(для фондов)  # noqa: E501

        :param code_parent: The code_parent of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._code_parent = code_parent

    @property
    def okpo(self):
        """Gets the okpo of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Код ОКПО  # noqa: E501

        :return: The okpo of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._okpo

    @okpo.setter
    def okpo(self, okpo):
        """Sets the okpo of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Код ОКПО  # noqa: E501

        :param okpo: The okpo of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._okpo = okpo

    @property
    def okato_region(self):
        """Gets the okato_region of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Код региона  # noqa: E501

        :return: The okato_region of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: float
        """
        return self._okato_region

    @okato_region.setter
    def okato_region(self, okato_region):
        """Sets the okato_region of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Код региона  # noqa: E501

        :param okato_region: The okato_region of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: float
        """

        self._okato_region = okato_region

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Идентификатор компании в базе ЭФиР  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Идентификатор компании в базе ЭФиР  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Код ОГРН  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Код ОГРН  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        ИНН  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsRatingListCompaniesFields.

        ИНН  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :return: The fininstid of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :param fininstid: The fininstid of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def bic(self):
        """Gets the bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Банковский идентификационный код (БИК)  # noqa: E501

        :return: The bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Банковский идентификационный код (БИК)  # noqa: E501

        :param bic: The bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def swift_bic(self):
        """Gets the swift_bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        SWIFT-код  # noqa: E501

        :return: The swift_bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._swift_bic

    @swift_bic.setter
    def swift_bic(self, swift_bic):
        """Sets the swift_bic of this EfirDataHubModelsModelsRatingListCompaniesFields.

        SWIFT-код  # noqa: E501

        :param swift_bic: The swift_bic of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._swift_bic = swift_bic

    @property
    def note(self):
        """Gets the note of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501

        Примечание  # noqa: E501

        :return: The note of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EfirDataHubModelsModelsRatingListCompaniesFields.

        Примечание  # noqa: E501

        :param note: The note of this EfirDataHubModelsModelsRatingListCompaniesFields.  # noqa: E501
        :type: str
        """

        self._note = note

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
        if issubclass(EfirDataHubModelsModelsRatingListCompaniesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsRatingListCompaniesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
