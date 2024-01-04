# EfirDataHubModelsRequestsV2MarkingValuesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Массив идентификаторов ценных бумаг в БД Интерфакс, максимальное число элементов 100, необязательный | [optional] 
**filter** | **str** | Cтрока фильтра на выходные значения, необязательная | [optional] 
**date_from** | **datetime** | Дата начала действия классификации (по умолчанию текущая дата) | [optional] 
**date_to** | **datetime** | Дата окончания действия классификации (по умолчанию текущая дата) | [optional] 
**page_num** | **int** | Номер страницы для выборки.  Если не задан или меньше 1, то принимается как 1. | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки.  Если не задан, меньше 1 или больше 1000, то принимается как 1000. | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

