# EfirDataHubModelsRequestsV2RiskCorpInvestClassRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс, не более 20 шт. | [optional] 
**codes** | **list[str]** | Идентификаторы компаний - ИНН, ОГРН (используются, если не указаны FininstIds). Не более 20 шт. | [optional] 
**_date** | **datetime** | Дата расчета | [optional] 
**actual_date** | **datetime** | Дата актуальности расчета | [optional] 
**filter** | **str** | Строка фильтрации | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

