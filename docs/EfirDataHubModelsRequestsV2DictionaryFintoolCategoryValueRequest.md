# EfirDataHubModelsRequestsV2DictionaryFintoolCategoryValueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_category** | **str** | Строка фильтрации по категории.  Отбираются инструменты, у которых есть связь с указанной в фильтре категорией | [optional] 
**fintool_ids** | **list[int]** | Список идентификаторов инструмента (fintoolid) | [optional] 
**codes** | **list[str]** | Список кодов инструмента (ISIN, RegCode, NrdCode).  Используется, если не задан fintoolIds | [optional] 
**only_fintools_with_category** | **bool** | Отдавать только инструменты, у которых есть категории | [optional] 
**page_num** | **int** | Номер страницы для выборки.  Если не задан - или меньше 1, то устанавливается в ‘1’ | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки.  Если не задан или меньше 1, то устанавливается в ‘300’ | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

