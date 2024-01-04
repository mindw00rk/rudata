# EfirDataHubModelsRequestsV2SolvencyLicensesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**list[EfirDataHubModelsRequestsV2CounterpartyID]**](EfirDataHubModelsRequestsV2CounterpartyID.md) | Массив идентификаторов контрагента. Необязательный параметр. Если задан, то не более 100 объектов (пар идентификатор, тип идентификатора). | [optional] 
**_date** | **datetime** | Дата расчета. Необязательный параметр. | [optional] 
**filter** | **str** | Строка фильтрации по полям. Необязательный параметр. | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан - не используется, если  меньше 1, то устанавливается в 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если не задан или меньше 1 - устанавливается в 300 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

