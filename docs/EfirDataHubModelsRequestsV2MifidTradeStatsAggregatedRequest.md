# EfirDataHubModelsRequestsV2MifidTradeStatsAggregatedRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 100 | [optional] 
**codes** | **list[str]** | Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode);  Максимальное количество элементов: 100 | [optional] 
**actual_on_date** | **datetime** | Дата расчета | [optional] 
**trade_date_start** | **datetime** | Дата начала отрезка отбора фильтров | 
**trade_date_end** | **datetime** | Дата окончания отрезка отбора фильтров | [optional] 
**trade_group_code** | **int** | Код групп сделок для формирования статистик:  1 - Биржевые сделки (основной режим)  12 - Биржевые сделки (основной и прочие режимы)  3 - Внебиржевые сделки  123 - Биржевые и небиржевые сделки   1234 - Биржевые, небиржевые и пока неопределенные сделки | [optional] 
**use_filters** | **bool** | Использовать фильтры для исключения ценовых &#x27;выбросов&#x27; | [optional] 
**use_restored_volumes** | **bool** | Включать сделки с восстановленными объемами. По-умолчанию - true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

