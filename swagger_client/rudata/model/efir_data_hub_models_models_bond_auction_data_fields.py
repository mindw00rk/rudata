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

class EfirDataHubModelsModelsBondAuctionDataFields(object):
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
        'id_fintool': 'int',
        'begdist_date': 'datetime',
        'enddist_date': 'datetime',
        'method': 'str',
        'exch_name': 'str',
        'ask_vol': 'float',
        'ask_val': 'float',
        'bid_vol': 'float',
        'bid_val': 'float',
        'min_bid': 'float',
        'max_bid': 'float',
        'dist_vol': 'float',
        'dist_val': 'float',
        'waprice': 'float',
        'yield_waprice': 'float',
        'num_trades': 'int',
        'beg_bid_date': 'datetime',
        'end_bid_date': 'datetime',
        'min_bid_rate': 'float',
        'max_bid_rate': 'float',
        'min_bid_yield': 'float',
        'max_bid_yield': 'float',
        'bid_note': 'str',
        'note': 'str',
        'type_operation_name': 'str',
        'bid_dates_descr': 'str',
        'counter': 'int'
    }

    attribute_map = {
        'id_fintool': 'id_fintool',
        'begdist_date': 'begdist_date',
        'enddist_date': 'enddist_date',
        'method': 'method',
        'exch_name': 'exch_name',
        'ask_vol': 'ask_vol',
        'ask_val': 'ask_val',
        'bid_vol': 'bid_vol',
        'bid_val': 'bid_val',
        'min_bid': 'min_bid',
        'max_bid': 'max_bid',
        'dist_vol': 'dist_vol',
        'dist_val': 'dist_val',
        'waprice': 'waprice',
        'yield_waprice': 'yield_waprice',
        'num_trades': 'num_trades',
        'beg_bid_date': 'beg_bid_date',
        'end_bid_date': 'end_bid_date',
        'min_bid_rate': 'min_bid_rate',
        'max_bid_rate': 'max_bid_rate',
        'min_bid_yield': 'min_bid_yield',
        'max_bid_yield': 'max_bid_yield',
        'bid_note': 'bid_note',
        'note': 'note',
        'type_operation_name': 'type_operation_name',
        'bid_dates_descr': 'bid_dates_descr',
        'counter': 'counter'
    }

    def __init__(self, id_fintool=None, begdist_date=None, enddist_date=None, method=None, exch_name=None, ask_vol=None, ask_val=None, bid_vol=None, bid_val=None, min_bid=None, max_bid=None, dist_vol=None, dist_val=None, waprice=None, yield_waprice=None, num_trades=None, beg_bid_date=None, end_bid_date=None, min_bid_rate=None, max_bid_rate=None, min_bid_yield=None, max_bid_yield=None, bid_note=None, note=None, type_operation_name=None, bid_dates_descr=None, counter=None):  # noqa: E501
        """EfirDataHubModelsModelsBondAuctionDataFields - a model defined in Swagger"""  # noqa: E501
        self._id_fintool = None
        self._begdist_date = None
        self._enddist_date = None
        self._method = None
        self._exch_name = None
        self._ask_vol = None
        self._ask_val = None
        self._bid_vol = None
        self._bid_val = None
        self._min_bid = None
        self._max_bid = None
        self._dist_vol = None
        self._dist_val = None
        self._waprice = None
        self._yield_waprice = None
        self._num_trades = None
        self._beg_bid_date = None
        self._end_bid_date = None
        self._min_bid_rate = None
        self._max_bid_rate = None
        self._min_bid_yield = None
        self._max_bid_yield = None
        self._bid_note = None
        self._note = None
        self._type_operation_name = None
        self._bid_dates_descr = None
        self._counter = None
        self.discriminator = None
        if id_fintool is not None:
            self.id_fintool = id_fintool
        if begdist_date is not None:
            self.begdist_date = begdist_date
        if enddist_date is not None:
            self.enddist_date = enddist_date
        if method is not None:
            self.method = method
        if exch_name is not None:
            self.exch_name = exch_name
        if ask_vol is not None:
            self.ask_vol = ask_vol
        if ask_val is not None:
            self.ask_val = ask_val
        if bid_vol is not None:
            self.bid_vol = bid_vol
        if bid_val is not None:
            self.bid_val = bid_val
        if min_bid is not None:
            self.min_bid = min_bid
        if max_bid is not None:
            self.max_bid = max_bid
        if dist_vol is not None:
            self.dist_vol = dist_vol
        if dist_val is not None:
            self.dist_val = dist_val
        if waprice is not None:
            self.waprice = waprice
        if yield_waprice is not None:
            self.yield_waprice = yield_waprice
        if num_trades is not None:
            self.num_trades = num_trades
        if beg_bid_date is not None:
            self.beg_bid_date = beg_bid_date
        if end_bid_date is not None:
            self.end_bid_date = end_bid_date
        if min_bid_rate is not None:
            self.min_bid_rate = min_bid_rate
        if max_bid_rate is not None:
            self.max_bid_rate = max_bid_rate
        if min_bid_yield is not None:
            self.min_bid_yield = min_bid_yield
        if max_bid_yield is not None:
            self.max_bid_yield = max_bid_yield
        if bid_note is not None:
            self.bid_note = bid_note
        if note is not None:
            self.note = note
        if type_operation_name is not None:
            self.type_operation_name = type_operation_name
        if bid_dates_descr is not None:
            self.bid_dates_descr = bid_dates_descr
        if counter is not None:
            self.counter = counter

    @property
    def id_fintool(self):
        """Gets the id_fintool of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Идентификатор облигации  # noqa: E501

        :return: The id_fintool of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: int
        """
        return self._id_fintool

    @id_fintool.setter
    def id_fintool(self, id_fintool):
        """Sets the id_fintool of this EfirDataHubModelsModelsBondAuctionDataFields.

        Идентификатор облигации  # noqa: E501

        :param id_fintool: The id_fintool of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: int
        """

        self._id_fintool = id_fintool

    @property
    def begdist_date(self):
        """Gets the begdist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Дата начала размещения  # noqa: E501

        :return: The begdist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._begdist_date

    @begdist_date.setter
    def begdist_date(self, begdist_date):
        """Sets the begdist_date of this EfirDataHubModelsModelsBondAuctionDataFields.

        Дата начала размещения  # noqa: E501

        :param begdist_date: The begdist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: datetime
        """

        self._begdist_date = begdist_date

    @property
    def enddist_date(self):
        """Gets the enddist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Дата окончания размещения  # noqa: E501

        :return: The enddist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._enddist_date

    @enddist_date.setter
    def enddist_date(self, enddist_date):
        """Sets the enddist_date of this EfirDataHubModelsModelsBondAuctionDataFields.

        Дата окончания размещения  # noqa: E501

        :param enddist_date: The enddist_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: datetime
        """

        self._enddist_date = enddist_date

    @property
    def method(self):
        """Gets the method of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Способ размещения выпуска  # noqa: E501

        :return: The method of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this EfirDataHubModelsModelsBondAuctionDataFields.

        Способ размещения выпуска  # noqa: E501

        :param method: The method of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def exch_name(self):
        """Gets the exch_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Название площадки, на которой происходит размещение  # noqa: E501

        :return: The exch_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._exch_name

    @exch_name.setter
    def exch_name(self, exch_name):
        """Sets the exch_name of this EfirDataHubModelsModelsBondAuctionDataFields.

        Название площадки, на которой происходит размещение  # noqa: E501

        :param exch_name: The exch_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._exch_name = exch_name

    @property
    def ask_vol(self):
        """Gets the ask_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Объем облигаций, предложенных к размещению, штук  # noqa: E501

        :return: The ask_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._ask_vol

    @ask_vol.setter
    def ask_vol(self, ask_vol):
        """Sets the ask_vol of this EfirDataHubModelsModelsBondAuctionDataFields.

        Объем облигаций, предложенных к размещению, штук  # noqa: E501

        :param ask_vol: The ask_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._ask_vol = ask_vol

    @property
    def ask_val(self):
        """Gets the ask_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Объем облигаций, предложенных к размещению, в валюте номинала  # noqa: E501

        :return: The ask_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._ask_val

    @ask_val.setter
    def ask_val(self, ask_val):
        """Sets the ask_val of this EfirDataHubModelsModelsBondAuctionDataFields.

        Объем облигаций, предложенных к размещению, в валюте номинала  # noqa: E501

        :param ask_val: The ask_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._ask_val = ask_val

    @property
    def bid_vol(self):
        """Gets the bid_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Объем спроса на выпуск, штук  # noqa: E501

        :return: The bid_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._bid_vol

    @bid_vol.setter
    def bid_vol(self, bid_vol):
        """Sets the bid_vol of this EfirDataHubModelsModelsBondAuctionDataFields.

        Объем спроса на выпуск, штук  # noqa: E501

        :param bid_vol: The bid_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._bid_vol = bid_vol

    @property
    def bid_val(self):
        """Gets the bid_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Объем спроса, в валюте номинала  # noqa: E501

        :return: The bid_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._bid_val

    @bid_val.setter
    def bid_val(self, bid_val):
        """Sets the bid_val of this EfirDataHubModelsModelsBondAuctionDataFields.

        Объем спроса, в валюте номинала  # noqa: E501

        :param bid_val: The bid_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._bid_val = bid_val

    @property
    def min_bid(self):
        """Gets the min_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Минимальная цена в заявках на приобретение облигаций  # noqa: E501

        :return: The min_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._min_bid

    @min_bid.setter
    def min_bid(self, min_bid):
        """Sets the min_bid of this EfirDataHubModelsModelsBondAuctionDataFields.

        Минимальная цена в заявках на приобретение облигаций  # noqa: E501

        :param min_bid: The min_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._min_bid = min_bid

    @property
    def max_bid(self):
        """Gets the max_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Максимальная цена в заявках на приобретение облигаций  # noqa: E501

        :return: The max_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._max_bid

    @max_bid.setter
    def max_bid(self, max_bid):
        """Sets the max_bid of this EfirDataHubModelsModelsBondAuctionDataFields.

        Максимальная цена в заявках на приобретение облигаций  # noqa: E501

        :param max_bid: The max_bid of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._max_bid = max_bid

    @property
    def dist_vol(self):
        """Gets the dist_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Размещенный объем, штук  # noqa: E501

        :return: The dist_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._dist_vol

    @dist_vol.setter
    def dist_vol(self, dist_vol):
        """Sets the dist_vol of this EfirDataHubModelsModelsBondAuctionDataFields.

        Размещенный объем, штук  # noqa: E501

        :param dist_vol: The dist_vol of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._dist_vol = dist_vol

    @property
    def dist_val(self):
        """Gets the dist_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Размещенный объем, в валюте номинала  # noqa: E501

        :return: The dist_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._dist_val

    @dist_val.setter
    def dist_val(self, dist_val):
        """Sets the dist_val of this EfirDataHubModelsModelsBondAuctionDataFields.

        Размещенный объем, в валюте номинала  # noqa: E501

        :param dist_val: The dist_val of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._dist_val = dist_val

    @property
    def waprice(self):
        """Gets the waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Средневзвешенная цена по итогам размещения  # noqa: E501

        :return: The waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._waprice

    @waprice.setter
    def waprice(self, waprice):
        """Sets the waprice of this EfirDataHubModelsModelsBondAuctionDataFields.

        Средневзвешенная цена по итогам размещения  # noqa: E501

        :param waprice: The waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._waprice = waprice

    @property
    def yield_waprice(self):
        """Gets the yield_waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Доходность по средневзвешенной цене  # noqa: E501

        :return: The yield_waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._yield_waprice

    @yield_waprice.setter
    def yield_waprice(self, yield_waprice):
        """Sets the yield_waprice of this EfirDataHubModelsModelsBondAuctionDataFields.

        Доходность по средневзвешенной цене  # noqa: E501

        :param yield_waprice: The yield_waprice of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._yield_waprice = yield_waprice

    @property
    def num_trades(self):
        """Gets the num_trades of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Количество сделок при размещении  # noqa: E501

        :return: The num_trades of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: int
        """
        return self._num_trades

    @num_trades.setter
    def num_trades(self, num_trades):
        """Sets the num_trades of this EfirDataHubModelsModelsBondAuctionDataFields.

        Количество сделок при размещении  # noqa: E501

        :param num_trades: The num_trades of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: int
        """

        self._num_trades = num_trades

    @property
    def beg_bid_date(self):
        """Gets the beg_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Дата начала сбора заявок  # noqa: E501

        :return: The beg_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._beg_bid_date

    @beg_bid_date.setter
    def beg_bid_date(self, beg_bid_date):
        """Sets the beg_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.

        Дата начала сбора заявок  # noqa: E501

        :param beg_bid_date: The beg_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: datetime
        """

        self._beg_bid_date = beg_bid_date

    @property
    def end_bid_date(self):
        """Gets the end_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Дата окончания сбора заявок  # noqa: E501

        :return: The end_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: datetime
        """
        return self._end_bid_date

    @end_bid_date.setter
    def end_bid_date(self, end_bid_date):
        """Sets the end_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.

        Дата окончания сбора заявок  # noqa: E501

        :param end_bid_date: The end_bid_date of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: datetime
        """

        self._end_bid_date = end_bid_date

    @property
    def min_bid_rate(self):
        """Gets the min_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Минимальная ставка в поданных заявках  # noqa: E501

        :return: The min_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._min_bid_rate

    @min_bid_rate.setter
    def min_bid_rate(self, min_bid_rate):
        """Sets the min_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.

        Минимальная ставка в поданных заявках  # noqa: E501

        :param min_bid_rate: The min_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._min_bid_rate = min_bid_rate

    @property
    def max_bid_rate(self):
        """Gets the max_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Максимальная ставка в поданных заявках  # noqa: E501

        :return: The max_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._max_bid_rate

    @max_bid_rate.setter
    def max_bid_rate(self, max_bid_rate):
        """Sets the max_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.

        Максимальная ставка в поданных заявках  # noqa: E501

        :param max_bid_rate: The max_bid_rate of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._max_bid_rate = max_bid_rate

    @property
    def min_bid_yield(self):
        """Gets the min_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Минимальная доходность в поданных заявках  # noqa: E501

        :return: The min_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._min_bid_yield

    @min_bid_yield.setter
    def min_bid_yield(self, min_bid_yield):
        """Sets the min_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.

        Минимальная доходность в поданных заявках  # noqa: E501

        :param min_bid_yield: The min_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._min_bid_yield = min_bid_yield

    @property
    def max_bid_yield(self):
        """Gets the max_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Максимальная доходность в поданных заявках  # noqa: E501

        :return: The max_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: float
        """
        return self._max_bid_yield

    @max_bid_yield.setter
    def max_bid_yield(self, max_bid_yield):
        """Sets the max_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.

        Максимальная доходность в поданных заявках  # noqa: E501

        :param max_bid_yield: The max_bid_yield of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: float
        """

        self._max_bid_yield = max_bid_yield

    @property
    def bid_note(self):
        """Gets the bid_note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Примечание к размещению  # noqa: E501

        :return: The bid_note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._bid_note

    @bid_note.setter
    def bid_note(self, bid_note):
        """Sets the bid_note of this EfirDataHubModelsModelsBondAuctionDataFields.

        Примечание к размещению  # noqa: E501

        :param bid_note: The bid_note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._bid_note = bid_note

    @property
    def note(self):
        """Gets the note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Примечание общее  # noqa: E501

        :return: The note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EfirDataHubModelsModelsBondAuctionDataFields.

        Примечание общее  # noqa: E501

        :param note: The note of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def type_operation_name(self):
        """Gets the type_operation_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Наименование типа операции  # noqa: E501

        :return: The type_operation_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._type_operation_name

    @type_operation_name.setter
    def type_operation_name(self, type_operation_name):
        """Sets the type_operation_name of this EfirDataHubModelsModelsBondAuctionDataFields.

        Наименование типа операции  # noqa: E501

        :param type_operation_name: The type_operation_name of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._type_operation_name = type_operation_name

    @property
    def bid_dates_descr(self):
        """Gets the bid_dates_descr of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Описание предварительных дат сбора заявок  # noqa: E501

        :return: The bid_dates_descr of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: str
        """
        return self._bid_dates_descr

    @bid_dates_descr.setter
    def bid_dates_descr(self, bid_dates_descr):
        """Sets the bid_dates_descr of this EfirDataHubModelsModelsBondAuctionDataFields.

        Описание предварительных дат сбора заявок  # noqa: E501

        :param bid_dates_descr: The bid_dates_descr of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: str
        """

        self._bid_dates_descr = bid_dates_descr

    @property
    def counter(self):
        """Gets the counter of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501

        Общее количество записей в выборке, если указан pageNum = 1. Иначе null.  # noqa: E501

        :return: The counter of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :rtype: int
        """
        return self._counter

    @counter.setter
    def counter(self, counter):
        """Sets the counter of this EfirDataHubModelsModelsBondAuctionDataFields.

        Общее количество записей в выборке, если указан pageNum = 1. Иначе null.  # noqa: E501

        :param counter: The counter of this EfirDataHubModelsModelsBondAuctionDataFields.  # noqa: E501
        :type: int
        """

        self._counter = counter

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
        if issubclass(EfirDataHubModelsModelsBondAuctionDataFields, dict):
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
        if not isinstance(other, EfirDataHubModelsModelsBondAuctionDataFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
