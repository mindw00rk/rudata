# EfirDataHubModelsRequestsV2RUPriceSecuritiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_date** | **datetime** | дата актуальности справочника, если NULL, то выводится справочник, актуальный на текущую дату | [optional] 
**version** | **int** | версия справочника, 1 - старая методика; 2 - новая методика; 0 или NULL - обе методики | [optional] 
**page_num** | **int** | Номер страницы для выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Максимум - 500. | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

