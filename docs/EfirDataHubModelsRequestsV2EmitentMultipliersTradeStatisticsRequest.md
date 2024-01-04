# EfirDataHubModelsRequestsV2EmitentMultipliersTradeStatisticsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Список идентификаторов организации в базе Интерфакс. Не более 100 элементов. | 
**start_date** | **datetime** | Дата начала периода. По-умолчанию, текущая | [optional] 
**end_date** | **datetime** | Дата окончания периода. По-умолчанию, текущая.  Период не более 30 дней | [optional] 
**page_num** | **int** | Номер страницы выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. По-умолчанию 100 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

