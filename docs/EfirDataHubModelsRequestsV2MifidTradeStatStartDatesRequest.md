# EfirDataHubModelsRequestsV2MifidTradeStatStartDatesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Идентификатор финансового инструмента в базе Интерфакс (не более 100) | [optional] 
**codes** | **list[str]** | Иные идентификаторы облигации (ISIN, RegCode, NRDCode; не более 100). | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

