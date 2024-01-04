# EfirDataHubModelsRequestsV2DictionaryEmitentCategoryValueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_category** | **str** | Строка фильтрации по категории.  Отбираются компании, у которых есть связь с указанной в фильтре категорией | [optional] 
**fininst_ids** | **list[int]** | Список идентификаторов компании. | [optional] 
**codes** | **list[str]** | Список кодов компании (ИНН, ОГРН).  Используется, если не задан fininstIds | [optional] 
**only_emitents_with_category** | **bool** | Отдавать только компании, у которых есть категории | [optional] 
**page_num** | **int** | Номер страницы для выборки.  Если не задан - или меньше 1, то устанавливается в ‘1’ | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки.  Если не задан или меньше 1, то устанавливается в ‘300’ | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

