# EfirDataHubModelsRequestsV2RuDataCalendarRequestEx

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin_ids** | **list[str]** | Список индентификаторов (ISIN, RegCode, NrdCode) | [optional] 
**fintool_ids** | **list[int]** | Список идентификаторов (fintoolId) | [optional] 
**event_types** | **list[str]** | Типы событий(CONV, CALL, CPN, MTY, DIV); | [optional] 
**fields** | **list[str]** | Список требуемых полей (см. метод TimeTableFields) | [optional] 
**filter** | **str** | Дополнительный фильтр | [optional] 
**start_date** | **datetime** | Дата начала интересующего периода | [optional] 
**end_date** | **datetime** | Дата окончания интересующего периода; | [optional] 
**is_show_default** | **bool** | Показывать ли дефолты по событиям. | [optional] 
**sort_desc** | **bool** | Признак сортировки по убыванию времени | [optional] 
**page_num** | **int** | Номер страницы выборки.  Если не задан или меньше 1, то устанавливается в 1 | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки.  Если не задан или меньше 1, то устанавливается в 1000 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

