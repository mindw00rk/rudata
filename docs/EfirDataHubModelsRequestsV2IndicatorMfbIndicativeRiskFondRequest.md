# EfirDataHubModelsRequestsV2IndicatorMfbIndicativeRiskFondRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Необязательный параметр. Идентификаторы инструмента в БД Интерфакс.  Если не задан FintoolIds и даты периода, то результат содержит все актуальные индикаторы. | [optional] 
**start_date** | **datetime** | Необязательный параметр. Дата начала диапазона дат. | [optional] 
**end_date** | **datetime** | Необязательный параметр. Дата окончания диапазона дат. | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан или меньше 1, то устанавливается в 1. | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1, то устанавливается в 1000. | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

