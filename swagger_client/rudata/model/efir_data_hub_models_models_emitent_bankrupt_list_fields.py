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

class EfirDataHubModelsModelsEmitentBankruptListFields(object):
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
        'inn': 'str',
        'ogrn': 'str',
        'full_name': 'str',
        'legal_address': 'str',
        'status': 'str',
        'message_header': 'str',
        'date_of_status': 'datetime',
        'message_id': 'int',
        'quantity_of_cred_intentions': 'float',
        'quantity_of_debt_intentions': 'float',
        'date_of_court_decision': 'datetime',
        'num_of_court_case': 'str',
        'recall_of_license': 'str',
        'date_of_recall': 'datetime',
        'counterpartyid': 'int',
        'update_date': 'datetime',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'fininstid': 'fininstid',
        'inn': 'inn',
        'ogrn': 'ogrn',
        'full_name': 'full_name',
        'legal_address': 'legal_address',
        'status': 'status',
        'message_header': 'message_header',
        'date_of_status': 'date_of_status',
        'message_id': 'message_id',
        'quantity_of_cred_intentions': 'quantity_of_cred_intentions',
        'quantity_of_debt_intentions': 'quantity_of_debt_intentions',
        'date_of_court_decision': 'date_of_court_decision',
        'num_of_court_case': 'num_of_court_case',
        'recall_of_license': 'recall_of_license',
        'date_of_recall': 'date_of_recall',
        'counterpartyid': 'counterpartyid',
        'update_date': 'update_date',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, fininstid=None, inn=None, ogrn=None, full_name=None, legal_address=None, status=None, message_header=None, date_of_status=None, message_id=None, quantity_of_cred_intentions=None, quantity_of_debt_intentions=None, date_of_court_decision=None, num_of_court_case=None, recall_of_license=None, date_of_recall=None, counterpartyid=None, update_date=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsEmitentBankruptListFields - a model defined in Swagger"""  # noqa: E501
        self._fininstid = None
        self._inn = None
        self._ogrn = None
        self._full_name = None
        self._legal_address = None
        self._status = None
        self._message_header = None
        self._date_of_status = None
        self._message_id = None
        self._quantity_of_cred_intentions = None
        self._quantity_of_debt_intentions = None
        self._date_of_court_decision = None
        self._num_of_court_case = None
        self._recall_of_license = None
        self._date_of_recall = None
        self._counterpartyid = None
        self._update_date = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if fininstid is not None:
            self.fininstid = fininstid
        if inn is not None:
            self.inn = inn
        if ogrn is not None:
            self.ogrn = ogrn
        if full_name is not None:
            self.full_name = full_name
        if legal_address is not None:
            self.legal_address = legal_address
        if status is not None:
            self.status = status
        if message_header is not None:
            self.message_header = message_header
        if date_of_status is not None:
            self.date_of_status = date_of_status
        if message_id is not None:
            self.message_id = message_id
        if quantity_of_cred_intentions is not None:
            self.quantity_of_cred_intentions = quantity_of_cred_intentions
        if quantity_of_debt_intentions is not None:
            self.quantity_of_debt_intentions = quantity_of_debt_intentions
        if date_of_court_decision is not None:
            self.date_of_court_decision = date_of_court_decision
        if num_of_court_case is not None:
            self.num_of_court_case = num_of_court_case
        if recall_of_license is not None:
            self.recall_of_license = recall_of_license
        if date_of_recall is not None:
            self.date_of_recall = date_of_recall
        if counterpartyid is not None:
            self.counterpartyid = counterpartyid
        if update_date is not None:
            self.update_date = update_date
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def fininstid(self):
        """Gets the fininstid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501


        :return: The fininstid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: int
        """
        return self._fininstid

    @fininstid.setter
    def fininstid(self, fininstid):
        """Sets the fininstid of this EfirDataHubModelsModelsEmitentBankruptListFields.


        :param fininstid: The fininstid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: int
        """

        self._fininstid = fininstid

    @property
    def inn(self):
        """Gets the inn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        ИНН организации  # noqa: E501

        :return: The inn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._inn

    @inn.setter
    def inn(self, inn):
        """Sets the inn of this EfirDataHubModelsModelsEmitentBankruptListFields.

        ИНН организации  # noqa: E501

        :param inn: The inn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._inn = inn

    @property
    def ogrn(self):
        """Gets the ogrn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        ОГРН организации  # noqa: E501

        :return: The ogrn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._ogrn

    @ogrn.setter
    def ogrn(self, ogrn):
        """Sets the ogrn of this EfirDataHubModelsModelsEmitentBankruptListFields.

        ОГРН организации  # noqa: E501

        :param ogrn: The ogrn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._ogrn = ogrn

    @property
    def full_name(self):
        """Gets the full_name of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Полное наименование организации  # noqa: E501

        :return: The full_name of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Полное наименование организации  # noqa: E501

        :param full_name: The full_name of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def legal_address(self):
        """Gets the legal_address of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Юридический адрес организации  # noqa: E501

        :return: The legal_address of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._legal_address

    @legal_address.setter
    def legal_address(self, legal_address):
        """Sets the legal_address of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Юридический адрес организации  # noqa: E501

        :param legal_address: The legal_address of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._legal_address = legal_address

    @property
    def status(self):
        """Gets the status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Статус организации  # noqa: E501

        :return: The status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Статус организации  # noqa: E501

        :param status: The status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message_header(self):
        """Gets the message_header of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Заголовок сообщения, определившего статус  # noqa: E501

        :return: The message_header of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._message_header

    @message_header.setter
    def message_header(self, message_header):
        """Sets the message_header of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Заголовок сообщения, определившего статус  # noqa: E501

        :param message_header: The message_header of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._message_header = message_header

    @property
    def date_of_status(self):
        """Gets the date_of_status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Дата публикации сообщения, определившего статус  # noqa: E501

        :return: The date_of_status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_status

    @date_of_status.setter
    def date_of_status(self, date_of_status):
        """Sets the date_of_status of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Дата публикации сообщения, определившего статус  # noqa: E501

        :param date_of_status: The date_of_status of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: datetime
        """

        self._date_of_status = date_of_status

    @property
    def message_id(self):
        """Gets the message_id of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        ID сообщения, определившего статус  # noqa: E501

        :return: The message_id of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this EfirDataHubModelsModelsEmitentBankruptListFields.

        ID сообщения, определившего статус  # noqa: E501

        :param message_id: The message_id of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: int
        """

        self._message_id = message_id

    @property
    def quantity_of_cred_intentions(self):
        """Gets the quantity_of_cred_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Количество сообщений о намерении всех кредиторов обратиться в суд  # noqa: E501

        :return: The quantity_of_cred_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: float
        """
        return self._quantity_of_cred_intentions

    @quantity_of_cred_intentions.setter
    def quantity_of_cred_intentions(self, quantity_of_cred_intentions):
        """Sets the quantity_of_cred_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Количество сообщений о намерении всех кредиторов обратиться в суд  # noqa: E501

        :param quantity_of_cred_intentions: The quantity_of_cred_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: float
        """

        self._quantity_of_cred_intentions = quantity_of_cred_intentions

    @property
    def quantity_of_debt_intentions(self):
        """Gets the quantity_of_debt_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Количество сообщений о намерении должника обратиться в суд  # noqa: E501

        :return: The quantity_of_debt_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: float
        """
        return self._quantity_of_debt_intentions

    @quantity_of_debt_intentions.setter
    def quantity_of_debt_intentions(self, quantity_of_debt_intentions):
        """Sets the quantity_of_debt_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Количество сообщений о намерении должника обратиться в суд  # noqa: E501

        :param quantity_of_debt_intentions: The quantity_of_debt_intentions of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: float
        """

        self._quantity_of_debt_intentions = quantity_of_debt_intentions

    @property
    def date_of_court_decision(self):
        """Gets the date_of_court_decision of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Дата вынесения судебного решения  # noqa: E501

        :return: The date_of_court_decision of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_court_decision

    @date_of_court_decision.setter
    def date_of_court_decision(self, date_of_court_decision):
        """Sets the date_of_court_decision of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Дата вынесения судебного решения  # noqa: E501

        :param date_of_court_decision: The date_of_court_decision of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: datetime
        """

        self._date_of_court_decision = date_of_court_decision

    @property
    def num_of_court_case(self):
        """Gets the num_of_court_case of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Номер судебного дела  # noqa: E501

        :return: The num_of_court_case of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._num_of_court_case

    @num_of_court_case.setter
    def num_of_court_case(self, num_of_court_case):
        """Sets the num_of_court_case of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Номер судебного дела  # noqa: E501

        :param num_of_court_case: The num_of_court_case of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._num_of_court_case = num_of_court_case

    @property
    def recall_of_license(self):
        """Gets the recall_of_license of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Признак отзыва лицензии  # noqa: E501

        :return: The recall_of_license of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: str
        """
        return self._recall_of_license

    @recall_of_license.setter
    def recall_of_license(self, recall_of_license):
        """Sets the recall_of_license of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Признак отзыва лицензии  # noqa: E501

        :param recall_of_license: The recall_of_license of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: str
        """

        self._recall_of_license = recall_of_license

    @property
    def date_of_recall(self):
        """Gets the date_of_recall of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Дата отзыва лицензии  # noqa: E501

        :return: The date_of_recall of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_recall

    @date_of_recall.setter
    def date_of_recall(self, date_of_recall):
        """Sets the date_of_recall of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Дата отзыва лицензии  # noqa: E501

        :param date_of_recall: The date_of_recall of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: datetime
        """

        self._date_of_recall = date_of_recall

    @property
    def counterpartyid(self):
        """Gets the counterpartyid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Идентификатор контрагента  # noqa: E501

        :return: The counterpartyid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: int
        """
        return self._counterpartyid

    @counterpartyid.setter
    def counterpartyid(self, counterpartyid):
        """Sets the counterpartyid of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Идентификатор контрагента  # noqa: E501

        :param counterpartyid: The counterpartyid of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: int
        """

        self._counterpartyid = counterpartyid

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Дата добавления или обновления записи компании  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Дата добавления или обновления записи компании  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsEmitentBankruptListFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsEmitentBankruptListFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsEmitentBankruptListFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsEmitentBankruptListFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
