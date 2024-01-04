# EfirDataHubModelsRequestsV2EmitentMultipliersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Список идентификаторов организации в базе Интерфакс.  Обязательный. Не более 100 элементов. | 
**start_date** | **datetime** | Дата начала периода. По-умолчанию - текущая дата | [optional] 
**end_date** | **datetime** | Дата окончания периода. По-умолчанию - текущая дата. Период не более 30 дней. | [optional] 
**fields** | **list[str]** | Список мультипликаторов. Необязательный.  Допускаются только значения code из метода MultipliersList | [optional] 
**only_unique_values** | **bool** | Выводить значения мультипликаторов только в дни их расчёта. По-умолчанию - false | [optional] 
**page_num** | **int** | Номер страницы выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Максимум 1000. По-умолчанию 100 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

