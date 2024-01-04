# EfirDataHubModelsRequestsV2RuDataCalendarV2Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Список идентификаторов (fintoolId)  Максимум 100 элементов. | [optional] 
**event_types** | **list[str]** | Типы событий(CONV, CALL, CPN, MTY, DIV, DFLT).  Если не указаны, то выбираются все типы. | [optional] 
**fields** | **list[str]** | Список требуемых полей (см. метод TimeTableFields) | [optional] 
**filter** | **str** | Дополнительный фильтр | [optional] 
**start_date** | **datetime** | Дата начала интересующего периода | [optional] 
**end_date** | **datetime** | Дата окончания интересующего периода; | [optional] 
**is_show_default** | **bool** | Показывать ли дефолты по событиям. По-умолчанию - True. | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Максимум 1000.  Если не задан, устанавливается 1000. | [optional] 
**sort_desc** | **bool** | Признак сортировки по убыванию времени | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

