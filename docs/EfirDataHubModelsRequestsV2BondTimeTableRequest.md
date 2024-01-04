# EfirDataHubModelsRequestsV2BondTimeTableRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | Список идентификаторов (ISIN) | [optional] 
**event_types** | **list[str]** | Типы событий(CONV, CALL, CPN, MTY); | [optional] 
**fields** | **list[str]** | Список требуемых полей (см. метод TimeTableFields) | [optional] 
**start_date** | **datetime** | Дата начала интересующего периода | [optional] 
**end_date** | **datetime** | Дата окончания интересующего периода; | [optional] 
**is_show_default** | **bool** | Показывать ли дефолты по событиям. | [optional] 
**page_num** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 100]
**sort_desc** | **bool** | Признак сортировки по убыванию времени | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

