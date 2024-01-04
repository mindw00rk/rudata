# EfirDataHubModelsRequestsV2RatingSecurityRatingByAgenciesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс;  Максимальное количество элементов: 100 | 
**_date** | **datetime** | Дата, на которую получаются рейтинги; по умолчанию текущая | [optional] 
**agg_type** | **str** | Метод агрегации рейтингов:  - MAX - максимальный (по умолчанию);  - MIN - минимальный. | [optional] [default to 'MAX']
**rating_codes** | **list[str]** | Коды рейтингов, участвующих в агрегации. Игнорируется, если указан RatingListName. | [optional] 
**rating_list_name** | **str** | Имя списка рейтингов, см. Rating/AggregationLists. Если не указан,  используется список Стандартный (см. /Rating/AggregationLists). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

