# EfirDataHubModelsRequestsV2InfoFintoolFieldsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Строка фильтрации (необязательный).   Для получения полей, доступных для какого-либо из типов инструментов необходимо использовать соответствующее значение фильтра:  - FINTOOL_TYPE&#x3D;&#x27;BOND&#x27; – поля для облигаций  - FINTOOL_TYPE&#x3D;&#x27;SHARE&#x27; – поля для акций  - FINTOOL_TYPE&#x3D;&#x27;DEPO&#x27; – поля для депозитарных расписок  - FINTOOL_TYPE&#x3D;&#x27;FUND&#x27; – поля для фондов  - FINTOOL_TYPE&#x3D;&#x27;MPC&#x27; – поля для ИСУ | [optional] 
**count** | **int** | Макимальное возвращаемое количество записей.  Если для count задано значение 0 или его присвоение отсутствует, то возвращается 1000 записей.  Чтобы получить все записи, надо указать заведомо большее возвращаемое число записей. Например: 1000000. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

