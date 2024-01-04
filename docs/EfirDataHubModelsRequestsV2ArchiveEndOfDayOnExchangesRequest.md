# EfirDataHubModelsRequestsV2ArchiveEndOfDayOnExchangesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss_ids** | **list[int]** | Идентификаторы торговых инструментов в БД Интерфакс.  Должен быть задан один из трех списков: IssIds, FintoolIds, Codes.  Максимальное количество элементов: 20 | [optional] 
**codes** | **list[str]** | Идентификаторы инструментов: ISIN или регистрационный номер (RegCode) или код НРД (NRDCode).  Должен быть задан один из трех списков: IssIds, FintoolIds, Codes.  Максимальное количество элементов: 20 | [optional] 
**fintool_ids** | **list[int]** | Числовые идентификаторы в базе Интерфакс; если заданы и Codes и FintoolIds - используется FintoolIds;  Должен быть задан один из трех списков: IssIds, FintoolIds, Codes.  Максимальное количество элементов: 20 | [optional] 
**trade_sites** | **list[int]** | Список торговых площадок, ID из справочника «Торговые площадки»; | [optional] 
**board_ids** | **list[str]** | Список boardID для MOEX | [optional] 
**date_from** | **datetime** | Дата начала периода. По умолчанию - вчера. | [optional] 
**date_to** | **datetime** | Дата окончания периода. По умолчанию - вчера. | [optional] 
**fields** | **list[str]** | Обязательный, список кодовых наименований полей, колонка name из выходной таблицы метода /Info/Fields; | 
**official** | **bool** | Флаг официальных итогов | [optional] 
**use_default_trade_site** | **bool** | Возвращать данные только по основному инструменту.  Используется, если не задан IssIds или TradeSites. | [optional] 
**page_num** | **int** | Номер страницы для выборки | [optional] [default to 1]
**page_size** | **int** | Размер страницы выборки. Максимум - 100. | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

