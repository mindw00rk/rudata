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

class EfirDataHubModelsModelsInfoInstrumentsFields(object):
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
        'fintool_id': 'int',
        'name': 'str',
        'shortname_rus': 'str',
        'secname': 'str',
        'isin': 'str',
        'cfi_ifx': 'str',
        'exch': 'int',
        'seccode': 'str',
        'symbol_ts': 'str',
        'code_issuer': 'str',
        'lotsize': 'int',
        'status': 'int',
        'issuer': 'str',
        'sector': 'str',
        'currency': 'str',
        'reg_num': 'str',
        'mat_date': 'datetime',
        'cfi_name': 'str',
        'exchange': 'str',
        'visible': 'str',
        'tool_type': 'str',
        'tool_name': 'str',
        'is_main': 'bool',
        'reg_code': 'str',
        'reg_code_norm': 'str',
        'nrd_code': 'str',
        'nrd_code_norm': 'str',
        'isin2': 'str',
        'isin2_norm': 'str',
        'isin_norm': 'str',
        'trade_site': 'str',
        'board': 'str',
        'update_date': 'datetime',
        'base_asset_fintoolid': 'int',
        'agent_fininstid': 'int',
        'counter': 'int',
        'rn': 'int'
    }

    attribute_map = {
        'id': 'id',
        'fintool_id': 'fintoolId',
        'name': 'name',
        'shortname_rus': 'shortname_rus',
        'secname': 'secname',
        'isin': 'isin',
        'cfi_ifx': 'cfi_ifx',
        'exch': 'exch',
        'seccode': 'seccode',
        'symbol_ts': 'symbol_ts',
        'code_issuer': 'code_issuer',
        'lotsize': 'lotsize',
        'status': 'status',
        'issuer': 'issuer',
        'sector': 'sector',
        'currency': 'currency',
        'reg_num': 'reg_num',
        'mat_date': 'mat_date',
        'cfi_name': 'cfi_name',
        'exchange': 'exchange',
        'visible': 'visible',
        'tool_type': 'tool_type',
        'tool_name': 'tool_name',
        'is_main': 'is_main',
        'reg_code': 'reg_code',
        'reg_code_norm': 'reg_code_norm',
        'nrd_code': 'nrd_code',
        'nrd_code_norm': 'nrd_code_norm',
        'isin2': 'isin2',
        'isin2_norm': 'isin2_norm',
        'isin_norm': 'isin_norm',
        'trade_site': 'trade_site',
        'board': 'board',
        'update_date': 'update_date',
        'base_asset_fintoolid': 'base_asset_fintoolid',
        'agent_fininstid': 'agent_fininstid',
        'counter': 'counter',
        'rn': 'rn'
    }

    def __init__(self, id=None, fintool_id=None, name=None, shortname_rus=None, secname=None, isin=None, cfi_ifx=None, exch=None, seccode=None, symbol_ts=None, code_issuer=None, lotsize=None, status=None, issuer=None, sector=None, currency=None, reg_num=None, mat_date=None, cfi_name=None, exchange=None, visible=None, tool_type=None, tool_name=None, is_main=None, reg_code=None, reg_code_norm=None, nrd_code=None, nrd_code_norm=None, isin2=None, isin2_norm=None, isin_norm=None, trade_site=None, board=None, update_date=None, base_asset_fintoolid=None, agent_fininstid=None, counter=None, rn=None):  # noqa: E501
        """EfirDataHubModelsModelsInfoInstrumentsFields - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fintool_id = None
        self._name = None
        self._shortname_rus = None
        self._secname = None
        self._isin = None
        self._cfi_ifx = None
        self._exch = None
        self._seccode = None
        self._symbol_ts = None
        self._code_issuer = None
        self._lotsize = None
        self._status = None
        self._issuer = None
        self._sector = None
        self._currency = None
        self._reg_num = None
        self._mat_date = None
        self._cfi_name = None
        self._exchange = None
        self._visible = None
        self._tool_type = None
        self._tool_name = None
        self._is_main = None
        self._reg_code = None
        self._reg_code_norm = None
        self._nrd_code = None
        self._nrd_code_norm = None
        self._isin2 = None
        self._isin2_norm = None
        self._isin_norm = None
        self._trade_site = None
        self._board = None
        self._update_date = None
        self._base_asset_fintoolid = None
        self._agent_fininstid = None
        self._counter = None
        self._rn = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if fintool_id is not None:
            self.fintool_id = fintool_id
        if name is not None:
            self.name = name
        if shortname_rus is not None:
            self.shortname_rus = shortname_rus
        if secname is not None:
            self.secname = secname
        if isin is not None:
            self.isin = isin
        if cfi_ifx is not None:
            self.cfi_ifx = cfi_ifx
        if exch is not None:
            self.exch = exch
        if seccode is not None:
            self.seccode = seccode
        if symbol_ts is not None:
            self.symbol_ts = symbol_ts
        if code_issuer is not None:
            self.code_issuer = code_issuer
        if lotsize is not None:
            self.lotsize = lotsize
        if status is not None:
            self.status = status
        if issuer is not None:
            self.issuer = issuer
        if sector is not None:
            self.sector = sector
        if currency is not None:
            self.currency = currency
        if reg_num is not None:
            self.reg_num = reg_num
        if mat_date is not None:
            self.mat_date = mat_date
        if cfi_name is not None:
            self.cfi_name = cfi_name
        if exchange is not None:
            self.exchange = exchange
        if visible is not None:
            self.visible = visible
        if tool_type is not None:
            self.tool_type = tool_type
        if tool_name is not None:
            self.tool_name = tool_name
        if is_main is not None:
            self.is_main = is_main
        if reg_code is not None:
            self.reg_code = reg_code
        if reg_code_norm is not None:
            self.reg_code_norm = reg_code_norm
        if nrd_code is not None:
            self.nrd_code = nrd_code
        if nrd_code_norm is not None:
            self.nrd_code_norm = nrd_code_norm
        if isin2 is not None:
            self.isin2 = isin2
        if isin2_norm is not None:
            self.isin2_norm = isin2_norm
        if isin_norm is not None:
            self.isin_norm = isin_norm
        if trade_site is not None:
            self.trade_site = trade_site
        if board is not None:
            self.board = board
        if update_date is not None:
            self.update_date = update_date
        if base_asset_fintoolid is not None:
            self.base_asset_fintoolid = base_asset_fintoolid
        if agent_fininstid is not None:
            self.agent_fininstid = agent_fininstid
        if counter is not None:
            self.counter = counter
        if rn is not None:
            self.rn = rn

    @property
    def id(self):
        """Gets the id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Идентификатор инструмента (ISS id)  # noqa: E501

        :return: The id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Идентификатор инструмента (ISS id)  # noqa: E501

        :param id: The id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def fintool_id(self):
        """Gets the fintool_id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        FintoolId  # noqa: E501

        :return: The fintool_id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._fintool_id

    @fintool_id.setter
    def fintool_id(self, fintool_id):
        """Sets the fintool_id of this EfirDataHubModelsModelsInfoInstrumentsFields.

        FintoolId  # noqa: E501

        :param fintool_id: The fintool_id of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._fintool_id = fintool_id

    @property
    def name(self):
        """Gets the name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование в ЭФиРе  # noqa: E501

        :return: The name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование в ЭФиРе  # noqa: E501

        :param name: The name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shortname_rus(self):
        """Gets the shortname_rus of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование поля (рус.)  # noqa: E501

        :return: The shortname_rus of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._shortname_rus

    @shortname_rus.setter
    def shortname_rus(self, shortname_rus):
        """Sets the shortname_rus of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование поля (рус.)  # noqa: E501

        :param shortname_rus: The shortname_rus of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._shortname_rus = shortname_rus

    @property
    def secname(self):
        """Gets the secname of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование поля (англ.)  # noqa: E501

        :return: The secname of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._secname

    @secname.setter
    def secname(self, secname):
        """Sets the secname of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование поля (англ.)  # noqa: E501

        :param secname: The secname of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._secname = secname

    @property
    def isin(self):
        """Gets the isin of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this EfirDataHubModelsModelsInfoInstrumentsFields.

        ISIN  # noqa: E501

        :param isin: The isin of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def cfi_ifx(self):
        """Gets the cfi_ifx of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :return: The cfi_ifx of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._cfi_ifx

    @cfi_ifx.setter
    def cfi_ifx(self, cfi_ifx):
        """Sets the cfi_ifx of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Код типа инструмента по классификатору Интерфакс  # noqa: E501

        :param cfi_ifx: The cfi_ifx of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._cfi_ifx = cfi_ifx

    @property
    def exch(self):
        """Gets the exch of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Идентификатор биржи  # noqa: E501

        :return: The exch of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._exch

    @exch.setter
    def exch(self, exch):
        """Sets the exch of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Идентификатор биржи  # noqa: E501

        :param exch: The exch of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._exch = exch

    @property
    def seccode(self):
        """Gets the seccode of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Торговый код  # noqa: E501

        :return: The seccode of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._seccode

    @seccode.setter
    def seccode(self, seccode):
        """Sets the seccode of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Торговый код  # noqa: E501

        :param seccode: The seccode of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._seccode = seccode

    @property
    def symbol_ts(self):
        """Gets the symbol_ts of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Торговое наименование на бирже  # noqa: E501

        :return: The symbol_ts of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._symbol_ts

    @symbol_ts.setter
    def symbol_ts(self, symbol_ts):
        """Sets the symbol_ts of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Торговое наименование на бирже  # noqa: E501

        :param symbol_ts: The symbol_ts of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._symbol_ts = symbol_ts

    @property
    def code_issuer(self):
        """Gets the code_issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Символьный код эмитента  # noqa: E501

        :return: The code_issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._code_issuer

    @code_issuer.setter
    def code_issuer(self, code_issuer):
        """Sets the code_issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Символьный код эмитента  # noqa: E501

        :param code_issuer: The code_issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._code_issuer = code_issuer

    @property
    def lotsize(self):
        """Gets the lotsize of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Размер лота  # noqa: E501

        :return: The lotsize of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._lotsize

    @lotsize.setter
    def lotsize(self, lotsize):
        """Sets the lotsize of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Размер лота  # noqa: E501

        :param lotsize: The lotsize of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._lotsize = lotsize

    @property
    def status(self):
        """Gets the status of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Торговый статус инструмента  # noqa: E501

        :return: The status of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Торговый статус инструмента  # noqa: E501

        :param status: The status of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def issuer(self):
        """Gets the issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование эмитента  # noqa: E501

        :return: The issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование эмитента  # noqa: E501

        :param issuer: The issuer of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def sector(self):
        """Gets the sector of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Отрасль эмитента  # noqa: E501

        :return: The sector of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Отрасль эмитента  # noqa: E501

        :param sector: The sector of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def currency(self):
        """Gets the currency of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Валюта торгов  # noqa: E501

        :return: The currency of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Валюта торгов  # noqa: E501

        :param currency: The currency of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def reg_num(self):
        """Gets the reg_num of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Регистрационный номер инструмента  # noqa: E501

        :return: The reg_num of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_num

    @reg_num.setter
    def reg_num(self, reg_num):
        """Sets the reg_num of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Регистрационный номер инструмента  # noqa: E501

        :param reg_num: The reg_num of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._reg_num = reg_num

    @property
    def mat_date(self):
        """Gets the mat_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Дата погашения/экспирации  # noqa: E501

        :return: The mat_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: datetime
        """
        return self._mat_date

    @mat_date.setter
    def mat_date(self, mat_date):
        """Sets the mat_date of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Дата погашения/экспирации  # noqa: E501

        :param mat_date: The mat_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: datetime
        """

        self._mat_date = mat_date

    @property
    def cfi_name(self):
        """Gets the cfi_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование типа инструмента  # noqa: E501

        :return: The cfi_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._cfi_name

    @cfi_name.setter
    def cfi_name(self, cfi_name):
        """Sets the cfi_name of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование типа инструмента  # noqa: E501

        :param cfi_name: The cfi_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._cfi_name = cfi_name

    @property
    def exchange(self):
        """Gets the exchange of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Биржа/рынок  # noqa: E501

        :return: The exchange of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Биржа/рынок  # noqa: E501

        :param exchange: The exchange of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def visible(self):
        """Gets the visible of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Статус («Видимый», «Архивный»)  # noqa: E501

        :return: The visible of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Статус («Видимый», «Архивный»)  # noqa: E501

        :param visible: The visible of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._visible = visible

    @property
    def tool_type(self):
        """Gets the tool_type of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Код типа инструмента  # noqa: E501

        :return: The tool_type of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Код типа инструмента  # noqa: E501

        :param tool_type: The tool_type of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._tool_type = tool_type

    @property
    def tool_name(self):
        """Gets the tool_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Наименование типа инструмента  # noqa: E501

        :return: The tool_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        """Sets the tool_name of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Наименование типа инструмента  # noqa: E501

        :param tool_name: The tool_name of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._tool_name = tool_name

    @property
    def is_main(self):
        """Gets the is_main of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Основной торговый (или торгуемый) инструмент  # noqa: E501

        :return: The is_main of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Основной торговый (или торгуемый) инструмент  # noqa: E501

        :param is_main: The is_main of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: bool
        """

        self._is_main = is_main

    @property
    def reg_code(self):
        """Gets the reg_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Гос. рег. номер  # noqa: E501

        :return: The reg_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_code

    @reg_code.setter
    def reg_code(self, reg_code):
        """Sets the reg_code of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Гос. рег. номер  # noqa: E501

        :param reg_code: The reg_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._reg_code = reg_code

    @property
    def reg_code_norm(self):
        """Gets the reg_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Гос. рег. номер нормализованное значение  # noqa: E501

        :return: The reg_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._reg_code_norm

    @reg_code_norm.setter
    def reg_code_norm(self, reg_code_norm):
        """Sets the reg_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Гос. рег. номер нормализованное значение  # noqa: E501

        :param reg_code_norm: The reg_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._reg_code_norm = reg_code_norm

    @property
    def nrd_code(self):
        """Gets the nrd_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Рег. номер НРД  # noqa: E501

        :return: The nrd_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._nrd_code

    @nrd_code.setter
    def nrd_code(self, nrd_code):
        """Sets the nrd_code of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Рег. номер НРД  # noqa: E501

        :param nrd_code: The nrd_code of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._nrd_code = nrd_code

    @property
    def nrd_code_norm(self):
        """Gets the nrd_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Рег. номер НРД нормализованное значение  # noqa: E501

        :return: The nrd_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._nrd_code_norm

    @nrd_code_norm.setter
    def nrd_code_norm(self, nrd_code_norm):
        """Sets the nrd_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Рег. номер НРД нормализованное значение  # noqa: E501

        :param nrd_code_norm: The nrd_code_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._nrd_code_norm = nrd_code_norm

    @property
    def isin2(self):
        """Gets the isin2 of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Альтернативный isin  # noqa: E501

        :return: The isin2 of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._isin2

    @isin2.setter
    def isin2(self, isin2):
        """Sets the isin2 of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Альтернативный isin  # noqa: E501

        :param isin2: The isin2 of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._isin2 = isin2

    @property
    def isin2_norm(self):
        """Gets the isin2_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Альтернативный isin нормализованное значение  # noqa: E501

        :return: The isin2_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._isin2_norm

    @isin2_norm.setter
    def isin2_norm(self, isin2_norm):
        """Sets the isin2_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Альтернативный isin нормализованное значение  # noqa: E501

        :param isin2_norm: The isin2_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._isin2_norm = isin2_norm

    @property
    def isin_norm(self):
        """Gets the isin_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        ISIN нормализованное значение  # noqa: E501

        :return: The isin_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._isin_norm

    @isin_norm.setter
    def isin_norm(self, isin_norm):
        """Sets the isin_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.

        ISIN нормализованное значение  # noqa: E501

        :param isin_norm: The isin_norm of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._isin_norm = isin_norm

    @property
    def trade_site(self):
        """Gets the trade_site of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Торговая площадка  # noqa: E501

        :return: The trade_site of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._trade_site

    @trade_site.setter
    def trade_site(self, trade_site):
        """Sets the trade_site of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Торговая площадка  # noqa: E501

        :param trade_site: The trade_site of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._trade_site = trade_site

    @property
    def board(self):
        """Gets the board of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Режим торгов  # noqa: E501

        :return: The board of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: str
        """
        return self._board

    @board.setter
    def board(self, board):
        """Sets the board of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Режим торгов  # noqa: E501

        :param board: The board of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: str
        """

        self._board = board

    @property
    def update_date(self):
        """Gets the update_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Дата обновления  # noqa: E501

        :return: The update_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Дата обновления  # noqa: E501

        :param update_date: The update_date of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: datetime
        """

        self._update_date = update_date

    @property
    def base_asset_fintoolid(self):
        """Gets the base_asset_fintoolid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Идентификатор базового актива в базе Интерфакс  # noqa: E501

        :return: The base_asset_fintoolid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._base_asset_fintoolid

    @base_asset_fintoolid.setter
    def base_asset_fintoolid(self, base_asset_fintoolid):
        """Sets the base_asset_fintoolid of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Идентификатор базового актива в базе Интерфакс  # noqa: E501

        :param base_asset_fintoolid: The base_asset_fintoolid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._base_asset_fintoolid = base_asset_fintoolid

    @property
    def agent_fininstid(self):
        """Gets the agent_fininstid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Идентификатор агента в базе Интерфакс  # noqa: E501

        :return: The agent_fininstid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._agent_fininstid

    @agent_fininstid.setter
    def agent_fininstid(self, agent_fininstid):
        """Sets the agent_fininstid of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Идентификатор агента в базе Интерфакс  # noqa: E501

        :param agent_fininstid: The agent_fininstid of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._agent_fininstid = agent_fininstid

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Общее количество записей в выборке  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Общее количество записей в выборке  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

    @property
    def rn(self):
        """Gets the rn of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501

        Номер записи в выборке  # noqa: E501

        :return: The rn of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
        :rtype: int
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """Sets the rn of this EfirDataHubModelsModelsInfoInstrumentsFields.

        Номер записи в выборке  # noqa: E501

        :param rn: The rn of this EfirDataHubModelsModelsInfoInstrumentsFields.  # noqa: E501
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
        if issubclass(EfirDataHubModelsModelsInfoInstrumentsFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsInfoInstrumentsFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
