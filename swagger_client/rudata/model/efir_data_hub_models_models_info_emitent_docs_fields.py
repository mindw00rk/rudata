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

class EfirDataHubModelsModelsInfoEmitentDocsFields(object):
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
        'fininst_id': 'int',
        'link_number': 'int',
        'doc_type': 'str',
        'link': 'str',
        'caption': 'str',
        'doc_type_id': 'int',
        'link_type': 'str',
        'link_type_id': 'int',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fininst_id': 'fininstId',
        'link_number': 'linkNumber',
        'doc_type': 'docType',
        'link': 'link',
        'caption': 'caption',
        'doc_type_id': 'docTypeId',
        'link_type': 'linkType',
        'link_type_id': 'linkTypeId',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fininst_id=None, link_number=None, doc_type=None, link=None, caption=None, doc_type_id=None, link_type=None, link_type_id=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoEmitentDocsFields - a model defined in Swagger"""  # noqa: E501
        self._fininst_id = None
        self._link_number = None
        self._doc_type = None
        self._link = None
        self._caption = None
        self._doc_type_id = None
        self._link_type = None
        self._link_type_id = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fininst_id is not None:
            self.fininst_id = fininst_id
        if link_number is not None:
            self.link_number = link_number
        if doc_type is not None:
            self.doc_type = doc_type
        if link is not None:
            self.link = link
        if caption is not None:
            self.caption = caption
        if doc_type_id is not None:
            self.doc_type_id = doc_type_id
        if link_type is not None:
            self.link_type = link_type
        if link_type_id is not None:
            self.link_type_id = link_type_id
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fininst_id(self):
        """Gets the fininst_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :return: The fininst_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._fininst_id

    @fininst_id.setter
    def fininst_id(self, fininst_id):
        """Sets the fininst_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Идентификатор компании в базе Интерфакс  # noqa: E501

        :param fininst_id: The fininst_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: int
        """

        self._fininst_id = fininst_id

    @property
    def link_number(self):
        """Gets the link_number of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Идентификатор записи в рамках одной компании  # noqa: E501

        :return: The link_number of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._link_number

    @link_number.setter
    def link_number(self, link_number):
        """Sets the link_number of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Идентификатор записи в рамках одной компании  # noqa: E501

        :param link_number: The link_number of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: int
        """

        self._link_number = link_number

    @property
    def doc_type(self):
        """Gets the doc_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        docType - string - тип документа/ссылки; Возможные типы:  - 'Web ссылки'  - 'Файлы'  - 'Логотип (ссылка)'  - 'Логотип (файл)'  # noqa: E501

        :return: The doc_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        docType - string - тип документа/ссылки; Возможные типы:  - 'Web ссылки'  - 'Файлы'  - 'Логотип (ссылка)'  - 'Логотип (файл)'  # noqa: E501

        :param doc_type: The doc_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: str
        """

        self._doc_type = doc_type

    @property
    def link(self):
        """Gets the link of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Ссылка на документ  # noqa: E501

        :return: The link of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Ссылка на документ  # noqa: E501

        :param link: The link of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def caption(self):
        """Gets the caption of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Название документа  # noqa: E501

        :return: The caption of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Название документа  # noqa: E501

        :param caption: The caption of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def doc_type_id(self):
        """Gets the doc_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Идентификатор типа документа  # noqa: E501

        :return: The doc_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._doc_type_id

    @doc_type_id.setter
    def doc_type_id(self, doc_type_id):
        """Sets the doc_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Идентификатор типа документа  # noqa: E501

        :param doc_type_id: The doc_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: int
        """

        self._doc_type_id = doc_type_id

    @property
    def link_type(self):
        """Gets the link_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Тип ссылки  # noqa: E501

        :return: The link_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Тип ссылки  # noqa: E501

        :param link_type: The link_type of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: str
        """

        self._link_type = link_type

    @property
    def link_type_id(self):
        """Gets the link_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Идентификатор типа ссылки  # noqa: E501

        :return: The link_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._link_type_id

    @link_type_id.setter
    def link_type_id(self, link_type_id):
        """Sets the link_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Идентификатор типа ссылки  # noqa: E501

        :param link_type_id: The link_type_id of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: int
        """

        self._link_type_id = link_type_id

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsInfoEmitentDocsFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsInfoEmitentDocsFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsInfoEmitentDocsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoEmitentDocsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other