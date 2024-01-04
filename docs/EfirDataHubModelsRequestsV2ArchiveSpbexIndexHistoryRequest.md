# EfirDataHubModelsRequestsV2ArchiveSpbexIndexHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss_ids** | **list[int]** | Идентификаторы торговых инструментов в БД Интерфакс. Если заданы, FintoolIds и Codes игнорируются  Максимальное количество элементов: 20 | [optional] 
**codes** | **list[str]** | Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode);  Максимальное количество элементов: 20 | [optional] 
**fintool_ids** | **list[int]** | Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 20 | [optional] 
**date_from** | **datetime** | Дата начала интересующего периода | [optional] 
**date_to** | **datetime** | Дата окончания интересующего периода | [optional] 
**page_num** | **int** | Номер страницы для выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Максимум - 100 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

