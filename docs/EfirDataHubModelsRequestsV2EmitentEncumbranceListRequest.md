# EfirDataHubModelsRequestsV2EmitentEncumbranceListRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Список id компаний в базе Интерфакс (не более 100). Необязательный. | [optional] 
**codes** | **list[str]** | Список ИНН или ОГРН организации (не более 100). Необязательный.  Используется, если на задан список FininstIds. | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны данные об обременении имущества. По умолчанию - текущая дата | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

