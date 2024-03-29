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

class EfirDataHubModelsModelsMoexSecuritiesFields(object):
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
        'id_iss': 'int',
        'secid': 'str',
        'boardid': 'str',
        'board_title': 'str',
        'board_group': 'str',
        'board_group_title': 'str',
        'market': 'str',
        'engine': 'str',
        'short_name': 'str',
        'isin': 'str',
        'cfi_ifx': 'str',
        'cfi_name': 'str',
        'lot_size': 'int',
        'expiration_date': 'datetime',
        'currency': 'str',
        'emitent_code': 'str',
        'emitent_name': 'str',
        'market_sector': 'str',
        'min_price_increment': 'float',
        'fintoolid': 'int',
        'reg_code': 'str',
        'update_date': 'datetime',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'id_iss': 'id_iss',
        'secid': 'secid',
        'boardid': 'boardid',
        'board_title': 'board_title',
        'board_group': 'board_group',
        'board_group_title': 'board_group_title',
        'market': 'market',
        'engine': 'engine',
        'short_name': 'short_name',
        'isin': 'isin',
        'cfi_ifx': 'cfi_ifx',
        'cfi_name': 'cfi_name',
        'lot_size': 'lot_size',
        'expiration_date': 'expiration_date',
        'currency': 'currency',
        'emitent_code': 'emitent_code',
        'emitent_name': 'emitent_name',
        'market_sector': 'market_sector',
        'min_price_increment': 'min_price_increment',
        'fintoolid': 'fintoolid',
        'reg_code': 'reg_code',
        'update_date': 'update_date',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, id_iss=None, secid=None, boardid=None, board_title=None, board_group=None, board_group_title=None, market=None, engine=None, short_name=None, isin=None, cfi_ifx=None, cfi_name=None, lot_size=None, expiration_date=None, currency=None, emitent_code=None, emitent_name=None, market_sector=None, min_price_increment=None, fintoolid=None, reg_code=None, update_date=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsMoexSecuritiesFields - a model defined in Swagger"""  # noqa: E501
        self._id_iss = None
        self._secid = None
        self._boardid = None
        self._board_title = None
        self._board_group = None
        self._board_group_title = None
        self._market = None
        self._engine = None
        self._short_name = None
        self._isin = None
        self._cfi_ifx = None
        self._cfi_name = None
        self._lot_size = None
        self._expiration_date = None
        self._currency = None
        self._emitent_code = None
        self._emitent_name = None
        self._market_sector = None
        self._min_price_increment = None
        self._fintoolid = None
        self._reg_code = None
        self._update_date = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if id_iss is not None:
            self.id_iss = id_iss
        if secid is not None:
            self.secid = secid
        if boardid is not None:
            self.boardid = boardid
        if board_title is not None:
            self.board_title = board_title
        if board_group is not None:
            self.board_group = board_group
        if board_group_title is not None:
            self.board_group_title = board_group_title
        if market is not None:
            self.market = market
        if engine is not None:
            self.engine = engine
        if short_name is not None:
            self.short_name = short_name
        if isin is not None:
            self.isin = isin
        if cfi_ifx is not None:
            self.cfi_ifx = cfi_ifx
        if cfi_name is not None:
            self.cfi_name = cfi_name
        if lot_size is not None:
            self.lot_size = lot_size
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if currency is not None:
            self.currency = currency
        if emitent_code is not None:
            self.emitent_code = emitent_code
        if emitent_name is not None:
            self.emitent_name = emitent_name
        if market_sector is not None:
            self.market_sector = market_sector
        if min_price_increment is not None:
            self.min_price_increment = min_price_increment
        if fintoolid is not None:
            self.fintoolid = fintoolid
        if reg_code is not None:
            self.reg_code = reg_code
        if update_date is not None:
            self.update_date = update_date
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def id_iss(self):
        """Gets the id_iss of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Идентификатор торгового инструмента в базе Интерфакс  # noqa: E501

        :return: The id_iss of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._id_iss

    @id_iss.setter
    def id_iss(self, id_iss):
        """Sets the id_iss of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Идентификатор торгового инструмента в базе Интерфакс  # noqa: E501

        :param id_iss: The id_iss of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._id_iss = id_iss

    @property
    def secid(self):
        """Gets the secid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Торговый код на МБ  # noqa: E501

        :return: The secid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._secid

    @secid.setter
    def secid(self, secid):
        """Sets the secid of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Торговый код на МБ  # noqa: E501

        :param secid: The secid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._secid = secid

    @property
    def boardid(self):
        """Gets the boardid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код режима торгов  # noqa: E501

        :return: The boardid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._boardid

    @boardid.setter
    def boardid(self, boardid):
        """Sets the boardid of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код режима торгов  # noqa: E501

        :param boardid: The boardid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._boardid = boardid

    @property
    def board_title(self):
        """Gets the board_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Наименование режима торгов  # noqa: E501

        :return: The board_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._board_title

    @board_title.setter
    def board_title(self, board_title):
        """Sets the board_title of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Наименование режима торгов  # noqa: E501

        :param board_title: The board_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._board_title = board_title

    @property
    def board_group(self):
        """Gets the board_group of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код группы режимов торгов  # noqa: E501

        :return: The board_group of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._board_group

    @board_group.setter
    def board_group(self, board_group):
        """Sets the board_group of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код группы режимов торгов  # noqa: E501

        :param board_group: The board_group of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._board_group = board_group

    @property
    def board_group_title(self):
        """Gets the board_group_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Наименование группы режимов торгов  # noqa: E501

        :return: The board_group_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._board_group_title

    @board_group_title.setter
    def board_group_title(self, board_group_title):
        """Sets the board_group_title of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Наименование группы режимов торгов  # noqa: E501

        :param board_group_title: The board_group_title of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._board_group_title = board_group_title

    @property
    def market(self):
        """Gets the market of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код рынка  # noqa: E501

        :return: The market of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код рынка  # noqa: E501

        :param market: The market of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._market = market

    @property
    def engine(self):
        """Gets the engine of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код торговой системы  # noqa: E501

        :return: The engine of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код торговой системы  # noqa: E501

        :param engine: The engine of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._engine = engine

    @property
    def short_name(self):
        """Gets the short_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Краткое наименование инструмента  # noqa: E501

        :return: The short_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Краткое наименование инструмента  # noqa: E501

        :param short_name: The short_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsMoexSecuritiesFields.

        ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def cfi_ifx(self):
        """Gets the cfi_ifx of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :return: The cfi_ifx of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._cfi_ifx

    @cfi_ifx.setter
    def cfi_ifx(self, cfi_ifx):
        """Sets the cfi_ifx of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :param cfi_ifx: The cfi_ifx of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._cfi_ifx = cfi_ifx

    @property
    def cfi_name(self):
        """Gets the cfi_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Наименование типа инструмента по классификатору Интерфакс  # noqa: E501

        :return: The cfi_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._cfi_name

    @cfi_name.setter
    def cfi_name(self, cfi_name):
        """Sets the cfi_name of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Наименование типа инструмента по классификатору Интерфакс  # noqa: E501

        :param cfi_name: The cfi_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._cfi_name = cfi_name

    @property
    def lot_size(self):
        """Gets the lot_size of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Размер лота  # noqa: E501

        :return: The lot_size of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Размер лота  # noqa: E501

        :param lot_size: The lot_size of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def expiration_date(self):
        """Gets the expiration_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Дата экспирации  # noqa: E501

        :return: The expiration_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Дата экспирации  # noqa: E501

        :param expiration_date: The expiration_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def currency(self):
        """Gets the currency of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Валюта  # noqa: E501

        :return: The currency of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Валюта  # noqa: E501

        :param currency: The currency of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def emitent_code(self):
        """Gets the emitent_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Код эмитента  # noqa: E501

        :return: The emitent_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._emitent_code

    @emitent_code.setter
    def emitent_code(self, emitent_code):
        """Sets the emitent_code of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Код эмитента  # noqa: E501

        :param emitent_code: The emitent_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._emitent_code = emitent_code

    @property
    def emitent_name(self):
        """Gets the emitent_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Наименование эмитента  # noqa: E501

        :return: The emitent_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._emitent_name

    @emitent_name.setter
    def emitent_name(self, emitent_name):
        """Sets the emitent_name of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Наименование эмитента  # noqa: E501

        :param emitent_name: The emitent_name of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._emitent_name = emitent_name

    @property
    def market_sector(self):
        """Gets the market_sector of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Сектор рынка  # noqa: E501

        :return: The market_sector of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._market_sector

    @market_sector.setter
    def market_sector(self, market_sector):
        """Sets the market_sector of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Сектор рынка  # noqa: E501

        :param market_sector: The market_sector of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._market_sector = market_sector

    @property
    def min_price_increment(self):
        """Gets the min_price_increment of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Минимальный шаг цены  # noqa: E501

        :return: The min_price_increment of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: float
        """
        return self._min_price_increment

    @min_price_increment.setter
    def min_price_increment(self, min_price_increment):
        """Sets the min_price_increment of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Минимальный шаг цены  # noqa: E501

        :param min_price_increment: The min_price_increment of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: float
        """

        self._min_price_increment = min_price_increment

    @property
    def fintoolid(self):
        """Gets the fintoolid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Идентификатор финансового инструмента в базе Интерфакс  # noqa: E501

        :return: The fintoolid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._fintoolid

    @fintoolid.setter
    def fintoolid(self, fintoolid):
        """Sets the fintoolid of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Идентификатор финансового инструмента в базе Интерфакс  # noqa: E501

        :param fintoolid: The fintoolid of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._fintoolid = fintoolid

    @property
    def reg_code(self):
        """Gets the reg_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Регистрационный номер финансового инструмента  # noqa: E501

        :return: The reg_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_code

    @reg_code.setter
    def reg_code(self, reg_code):
        """Sets the reg_code of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Регистрационный номер финансового инструмента  # noqa: E501

        :param reg_code: The reg_code of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: str
        """

        self._reg_code = reg_code

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Дата обновления  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Дата обновления  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsMoexSecuritiesFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsMoexSecuritiesFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsMoexSecuritiesFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsMoexSecuritiesFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
