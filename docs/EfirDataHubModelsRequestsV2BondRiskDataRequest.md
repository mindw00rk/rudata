# EfirDataHubModelsRequestsV2BondRiskDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calc_date** | **datetime** | Дата расчета риска (обязательный). | 
**filter** | **str** | Строка фильтрации (необязательный). Для получения данных по конкретному выпуску необходимо использовать фильтр по id_fintool. | [optional] 
**count** | **int** | Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

