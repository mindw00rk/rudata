# EfirDataHubModelsRequestsV2MoexDividendYieldRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Массив Id инструментов в БД Интерфакс (не более 100).  Если не задан  filter, то обязательный | [optional] 
**filter** | **str** | Строка фильтрации (необязательный, если задан FintoolIds) | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

