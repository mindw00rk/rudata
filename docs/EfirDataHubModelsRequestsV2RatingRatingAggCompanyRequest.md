# EfirDataHubModelsRequestsV2RatingRatingAggCompanyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agg_type** | **str** | Метод агрегации рейтингов нескольких рейтинговых агентств:  - MAX - максимальный из всех агентств.  - MIN - минимальный рейтинг из всех агентств.  - MAX2 - Лучший рейтинг, если агентство единственное, а если больше одного, то лучший рейтинг второго агентства (для всех групп). Отменяет использование PriorityAgency.  - MAX2B - MAX2 применяется только для агрегации рейтингов \&quot;большой тройки\&quot;. Отменяет использование PriorityAgency.  - MAX2R - MAX2 применяется только для агрегации в группе RU. Отменяет использование PriorityAgency.  - MAX2BG - Для государств, правительств (или их частей, например, Минфин), центральных банков или организаций, имеющих право заимствовать от имени государства,  расчет по группе BIG3 производится как MAX2, для остальных применяется MAX. Отменяет использование PriorityAgency. | [optional] [default to 'MAX']
**priority_agency** | **str** | Приоритетное рейтинговое агентство:  - AKRA - АКРА  - RAEX - Эксперт РА  - NCR - НКР  - NRA - НРА  - MDS - Moody’s  - SP - Standard and Poor’s  - FCH - Fitch  - AMB - AM Best | [optional] 
**using_type** | **str** | Приоритет юрисдикции рейтинговых агентств:  - Best - лучший рейтинг среди всех рейтинговых агентств (по умолчанию).  - Jurisdiction - для российских компаний используются рейтинги только российских агентств, для иностранных - только BIG3.  - Rus - для российских компаний используются только рейтинги российских агентств. Для иностранных компаний используются рейтинги российских агентств, а если их нет, то рейтинги \&quot;большой тройки\&quot;.  - Big3 - используются только рейтинги \&quot;большой тройки\&quot;. | [optional] [default to 'Best']
**depth_in_months** | **int** | Глубина поиска в месяцах. Если не указан, не используется. | [optional] 
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс;  Максимальное количество элементов: 100 | 
**_date** | **datetime** | Дата, на которую получаются рейтинги; по умолчанию текущая | [optional] 
**scale_code** | **int** | Идентификатор соотношения шкал. Допустимые значения см. Rating/AggregationScaleRatios. | [optional] [default to 2]
**rating_codes** | **list[str]** | Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName. | [optional] 
**rating_list_name** | **str** | Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists). | [optional] 
**use_freezing** | **bool** | Использовать заморозку рейтингов BIG3 | [optional] [default to False]
**freezing_type** | **AllOfEfirDataHubModelsRequestsV2RatingRatingAggCompanyRequestFreezingType** | Способ заморозки рейтингов при useFreezing&#x3D;true:  - RussianObjects - заморозка рейтингов BIG3 для российских объектов рейтинга (по умолчанию),  - AllObjects - заморозка рейтингов BIG3 для всех объектов рейтинга.  RussianObjects  AllObjects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

