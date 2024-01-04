# EfirDataHubModelsRequestsV2RUPriceGetHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | (Необязательный) Список идентификаторов инструментов (любой из ISIN, регистрационный номер, код НРД, FintoolID)  Ограничение – если ids не задан, то возвратятся данные максимум за один месяц (от dateFrom до dateFrom + 1 месяц). | [optional] 
**fields** | **list[str]** | (Необязательный) Список кодов необходимых полей (см. метод HistoryColumns, CODENAME). Если не задано, то вернутся все поля. | [optional] 
**date_from** | **datetime** | Дата начала периода | [optional] 
**date_to** | **datetime** | Дата окончания периода. Может совпадать с dateFrom, если требуются данные за один день. | [optional] 
**version** | **AllOfEfirDataHubModelsRequestsV2RUPriceGetHistoryRequestVersion** | Версия методики: 0 - Обе методики; 1 - Методика НФА (старая); 2, null или не указан - Методика ЦЦ НРД (новая);  0 &#x3D; All  1 &#x3D; NFA  2 &#x3D; NRD | [optional] 
**page_num** | **int** | Номер страницы для выборки. По умолчанию - 1. | [optional] 
**page_size** | **int** | Размер страницы выборки. Максимум - 1000 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

