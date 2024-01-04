# EfirDataHubModelsRequestsV2RatingRatingsHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** | Дата начала периода | [optional] 
**date_to** | **datetime** | Дата окончания периода | [optional] 
**sort** | **int** | Направление сортировки:  0 – от старых к новым  1 – от новых к старым | [optional] 
**filter** | **str** | Строка фильтрации (необязательный) | [optional] 
**including_gov_org** | **bool** | Включая рейтинговые действия по правительственным организациям | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

