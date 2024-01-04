# EfirDataHubModelsRequestsV2RatingSecurityRatingsTableRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | Идентификаторы бумаг – ISIN, рег.коды (обязательный). | 
**_date** | **datetime** | Дата, на которую должны быть загружены данные. Если не указана, используется текущая дата. | [optional] 
**filter** | **str** | Строка фильтрации. (необязательный) | [optional] 
**count** | **int** | Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

