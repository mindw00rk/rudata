# EfirDataHubModelsRequestsV2ArchiveBondYieldsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss_id** | **int** | Идентификатор инструмента | [optional] 
**isin** | **str** | ISIN | [optional] 
**_date** | **datetime** | Дата запрашиваемых данных | 
**mode** | **int** | Тип возвращаемых данных (к погашению – 1, к оферте – 2, сводные – 3, все – 0) | [optional] 
**fields** | **list[str]** | Список кодовых наименований полей; если не задан, то возвращаются все доступные поля. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

