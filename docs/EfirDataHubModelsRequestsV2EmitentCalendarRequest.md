# EfirDataHubModelsRequestsV2EmitentCalendarRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Список идентификаторов компании в БД Интерфакс. Не более 100 элементов | [optional] 
**date_from** | **datetime** | Дата начала периода событий календаря. По-умолчанию - текущая дата. | [optional] 
**date_to** | **datetime** | Дата окончания периода событий календаря. По-умолчанию - текущая дата. | [optional] 
**filter** | **str** | Фильтр по полям выборки | [optional] 
**page_num** | **int** | Номер страницы выборки (По-умолчанию 1) | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки, не более 100 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

