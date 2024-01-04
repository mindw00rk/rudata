# EfirDataHubModelsRequestsV2ArchiveSnapshotOnExchangesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Идентификаторы инструментов в базе Интерфакс;  Если заданы и Codes и FintoolIds - используется FintoolIds;  Максимальное количество элементов: 20 | [optional] 
**iss_ids** | **list[int]** | Идентификаторы торговых инструментов в БД Интерфакс. Максимум - 20 элементов | [optional] 
**codes** | **list[str]** | Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode). Максимум - 100 элементов | [optional] 
**trade_sites** | **list[int]** | Список торговых площадок. Максимум - 10 элементов | [optional] 
**time_slice** | **str** | Время среза по маске hh:mm | [optional] 
**date_from** | **datetime** | Дата начала периода. | 
**date_to** | **datetime** | Дата окончания периода.   Не более 30 дней от Efir.DataHub.Models.Requests.V2.Archive.SnapshotOnExchangesRequest.DateFrom | 
**fields** | **list[str]** | Список интересующих полей | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

