# EfirDataHubModelsRequestsV2InfoEmitentsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс. | [optional] 
**filter** | **str** | Строка фильтрации. (необязательный) | [optional] 
**inn_as_string** | **bool** | Признак вывода кодов в текстовом виде (необязательный): TRUE – выводить основные коды в текстовом виде (с ведущими нулями) | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

