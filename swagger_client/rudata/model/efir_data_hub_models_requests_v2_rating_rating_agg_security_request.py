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

class EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest(object):
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
        'agg_type': 'str',
        'priority_agency': 'str',
        'using_type': 'str',
        'depth_in_months': 'int',
        'scale_ratio_id': 'int',
        'fintool_ids': 'list[int]',
        '_date': 'datetime',
        'rating_codes': 'list[str]',
        'rating_list_name': 'str',
        'use_freezing': 'bool',
        'freezing_type': 'AllOfEfirDataHubModelsRequestsV2RatingRatingAggSecurityRequestFreezingType'
    }

    attribute_map = {
        'agg_type': 'aggType',
        'priority_agency': 'priorityAgency',
        'using_type': 'usingType',
        'depth_in_months': 'depthInMonths',
        'scale_ratio_id': 'scaleRatioId',
        'fintool_ids': 'fintoolIds',
        '_date': 'date',
        'rating_codes': 'ratingCodes',
        'rating_list_name': 'ratingListName',
        'use_freezing': 'useFreezing',
        'freezing_type': 'freezingType'
    }

    def __init__(self, agg_type='MAX', priority_agency=None, using_type='Best', depth_in_months=None, scale_ratio_id=2, fintool_ids=None, _date=None, rating_codes=None, rating_list_name=None, use_freezing=False, freezing_type=None):  # noqa: E501
        """EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest - a model defined in Swagger"""  # noqa: E501
        self._agg_type = None
        self._priority_agency = None
        self._using_type = None
        self._depth_in_months = None
        self._scale_ratio_id = None
        self._fintool_ids = None
        self.__date = None
        self._rating_codes = None
        self._rating_list_name = None
        self._use_freezing = None
        self._freezing_type = None
        self.discriminator = None
        if agg_type is not None:
            self.agg_type = agg_type
        if priority_agency is not None:
            self.priority_agency = priority_agency
        if using_type is not None:
            self.using_type = using_type
        if depth_in_months is not None:
            self.depth_in_months = depth_in_months
        if scale_ratio_id is not None:
            self.scale_ratio_id = scale_ratio_id
        self.fintool_ids = fintool_ids
        if _date is not None:
            self._date = _date
        if rating_codes is not None:
            self.rating_codes = rating_codes
        if rating_list_name is not None:
            self.rating_list_name = rating_list_name
        if use_freezing is not None:
            self.use_freezing = use_freezing
        if freezing_type is not None:
            self.freezing_type = freezing_type

    @property
    def agg_type(self):
        """Gets the agg_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Метод агрегации рейтингов нескольких рейтинговых агентств:  - MAX - максимальный из всех агентств.  - MIN - минимальный рейтинг из всех агентств.  - MAX2 - Лучший рейтинг, если агентство единственное, а если больше одного, то лучший рейтинг второго агентства (для всех групп). Отменяет использование PriorityAgency.  - MAX2B - MAX2 применяется только для агрегации рейтингов \"большой тройки\". Отменяет использование PriorityAgency.  - MAX2R - MAX2 применяется только для агрегации в группе RU. Отменяет использование PriorityAgency.  - MAX2BG - MAX2BG - Для облигаций, которые относятся к госсектору (типы = гос, еврогос), расчет по группе BIG3 производится как MAX2, а для остальных будет применяться MAX. Отменяет использование PriorityAgency.  # noqa: E501

        :return: The agg_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: str
        """
        return self._agg_type

    @agg_type.setter
    def agg_type(self, agg_type):
        """Sets the agg_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Метод агрегации рейтингов нескольких рейтинговых агентств:  - MAX - максимальный из всех агентств.  - MIN - минимальный рейтинг из всех агентств.  - MAX2 - Лучший рейтинг, если агентство единственное, а если больше одного, то лучший рейтинг второго агентства (для всех групп). Отменяет использование PriorityAgency.  - MAX2B - MAX2 применяется только для агрегации рейтингов \"большой тройки\". Отменяет использование PriorityAgency.  - MAX2R - MAX2 применяется только для агрегации в группе RU. Отменяет использование PriorityAgency.  - MAX2BG - MAX2BG - Для облигаций, которые относятся к госсектору (типы = гос, еврогос), расчет по группе BIG3 производится как MAX2, а для остальных будет применяться MAX. Отменяет использование PriorityAgency.  # noqa: E501

        :param agg_type: The agg_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: str
        """

        self._agg_type = agg_type

    @property
    def priority_agency(self):
        """Gets the priority_agency of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Приоритетное рейтинговое агентство:  - AKRA - АКРА  - RAEX - Эксперт РА  - NCR - НКР  - NRA - НРА  - MDS - Moody’s  - SP - Standard and Poor’s  - FCH - Fitch  - AMB - AM Best  # noqa: E501

        :return: The priority_agency of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority_agency

    @priority_agency.setter
    def priority_agency(self, priority_agency):
        """Sets the priority_agency of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Приоритетное рейтинговое агентство:  - AKRA - АКРА  - RAEX - Эксперт РА  - NCR - НКР  - NRA - НРА  - MDS - Moody’s  - SP - Standard and Poor’s  - FCH - Fitch  - AMB - AM Best  # noqa: E501

        :param priority_agency: The priority_agency of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: str
        """

        self._priority_agency = priority_agency

    @property
    def using_type(self):
        """Gets the using_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Приоритет юрисдикции рейтинговых агентств:  - Best - лучший рейтинг среди всех рейтинговых агентств (по умолчанию).  - Jurisdiction - для российских инструментов используются рейтинги только российских агентств, для иностранных - только BIG3.  - Rus - для российских инструментов используются только рейтинги российских агентств, для иностранных инструментов используются рейтинги российских агентств, а если их нет, то рейтинги \"большой тройки\".  - Big3 - используются только рейтинги \"большой тройки\".  # noqa: E501

        :return: The using_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: str
        """
        return self._using_type

    @using_type.setter
    def using_type(self, using_type):
        """Sets the using_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Приоритет юрисдикции рейтинговых агентств:  - Best - лучший рейтинг среди всех рейтинговых агентств (по умолчанию).  - Jurisdiction - для российских инструментов используются рейтинги только российских агентств, для иностранных - только BIG3.  - Rus - для российских инструментов используются только рейтинги российских агентств, для иностранных инструментов используются рейтинги российских агентств, а если их нет, то рейтинги \"большой тройки\".  - Big3 - используются только рейтинги \"большой тройки\".  # noqa: E501

        :param using_type: The using_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: str
        """

        self._using_type = using_type

    @property
    def depth_in_months(self):
        """Gets the depth_in_months of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Глубина поиска в месяцах. Если не указан, не используется.  # noqa: E501

        :return: The depth_in_months of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: int
        """
        return self._depth_in_months

    @depth_in_months.setter
    def depth_in_months(self, depth_in_months):
        """Sets the depth_in_months of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Глубина поиска в месяцах. Если не указан, не используется.  # noqa: E501

        :param depth_in_months: The depth_in_months of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: int
        """

        self._depth_in_months = depth_in_months

    @property
    def scale_ratio_id(self):
        """Gets the scale_ratio_id of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Идентификатор соотношения шкал. Допустимые значения см. Rating/AggregationScaleRatios.  # noqa: E501

        :return: The scale_ratio_id of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: int
        """
        return self._scale_ratio_id

    @scale_ratio_id.setter
    def scale_ratio_id(self, scale_ratio_id):
        """Sets the scale_ratio_id of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Идентификатор соотношения шкал. Допустимые значения см. Rating/AggregationScaleRatios.  # noqa: E501

        :param scale_ratio_id: The scale_ratio_id of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: int
        """

        self._scale_ratio_id = scale_ratio_id

    @property
    def fintool_ids(self):
        """Gets the fintool_ids of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Идентификаторы инструментов в базе Интерфакс;  Максимальное количество элементов: 100  # noqa: E501

        :return: The fintool_ids of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._fintool_ids

    @fintool_ids.setter
    def fintool_ids(self, fintool_ids):
        """Sets the fintool_ids of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Идентификаторы инструментов в базе Интерфакс;  Максимальное количество элементов: 100  # noqa: E501

        :param fintool_ids: The fintool_ids of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: list[int]
        """
        if fintool_ids is None:
            raise ValueError("Invalid value for `fintool_ids`, must not be `None`")  # noqa: E501

        self._fintool_ids = fintool_ids

    @property
    def _date(self):
        """Gets the _date of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Дата, на которую получаются рейтинги; по умолчанию текущая  # noqa: E501

        :return: The _date of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Дата, на которую получаются рейтинги; по умолчанию текущая  # noqa: E501

        :param _date: The _date of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def rating_codes(self):
        """Gets the rating_codes of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName.  # noqa: E501

        :return: The rating_codes of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._rating_codes

    @rating_codes.setter
    def rating_codes(self, rating_codes):
        """Sets the rating_codes of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName.  # noqa: E501

        :param rating_codes: The rating_codes of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: list[str]
        """

        self._rating_codes = rating_codes

    @property
    def rating_list_name(self):
        """Gets the rating_list_name of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists).  # noqa: E501

        :return: The rating_list_name of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: str
        """
        return self._rating_list_name

    @rating_list_name.setter
    def rating_list_name(self, rating_list_name):
        """Sets the rating_list_name of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists).  # noqa: E501

        :param rating_list_name: The rating_list_name of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: str
        """

        self._rating_list_name = rating_list_name

    @property
    def use_freezing(self):
        """Gets the use_freezing of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Использовать заморозку рейтингов BIG3  # noqa: E501

        :return: The use_freezing of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_freezing

    @use_freezing.setter
    def use_freezing(self, use_freezing):
        """Sets the use_freezing of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Использовать заморозку рейтингов BIG3  # noqa: E501

        :param use_freezing: The use_freezing of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: bool
        """

        self._use_freezing = use_freezing

    @property
    def freezing_type(self):
        """Gets the freezing_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501

        Способ заморозки рейтингов при useFreezing=true:  - RussianObjects - заморозка рейтингов BIG3 для российских объектов рейтинга (по умолчанию),  - AllObjects - заморозка рейтингов BIG3 для всех объектов рейтинга.  RussianObjects  AllObjects  # noqa: E501

        :return: The freezing_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :rtype: AllOfEfirDataHubModelsRequestsV2RatingRatingAggSecurityRequestFreezingType
        """
        return self._freezing_type

    @freezing_type.setter
    def freezing_type(self, freezing_type):
        """Sets the freezing_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.

        Способ заморозки рейтингов при useFreezing=true:  - RussianObjects - заморозка рейтингов BIG3 для российских объектов рейтинга (по умолчанию),  - AllObjects - заморозка рейтингов BIG3 для всех объектов рейтинга.  RussianObjects  AllObjects  # noqa: E501

        :param freezing_type: The freezing_type of this EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest.  # noqa: E501
        :type: AllOfEfirDataHubModelsRequestsV2RatingRatingAggSecurityRequestFreezingType
        """

        self._freezing_type = freezing_type

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
        if issubclass(EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest, dict):
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
        if not isinstance(other, EfirDataHubModelsRequestsV2RatingRatingAggSecurityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other