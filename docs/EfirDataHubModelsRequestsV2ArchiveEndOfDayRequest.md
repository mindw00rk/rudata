# EfirDataHubModelsRequestsV2ArchiveEndOfDayRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iss_id** | **int** | Идентификатор инструмента. Должен быть задан этот параметр или isin. | [optional] 
**isin** | **str** | ISIN инструмента. Должен быть задан этот параметр или issId. | [optional] 
**_date** | **datetime** | Дата запрашиваемых данных | 
**date_type** | **str** | Тип возвращаемых данных:  - ACTUAL – строго на указанную дату(умолчание)  - LAST_TRADE_DATE – на ближайшую окончившуюся торговую сессию (максимальная протяжка LAST_TRADE_DATE - 12 месяцев)  - LAST_SESSION_DATE - данные на ближайшую предшествующую дату, когда по инструменту проводились торги. Независимо от совершенных сделок | [optional] 
**fields** | **list[str]** | Список кодовых наименований полей, колонка name из выходной таблицы метода /Info/Fields.   По умолчанию выводятся все доступные поля. | [optional] 
**official** | **bool** | Запрос официальных итогов:  - true – запрашивать официальные итоги   - false – запрашивать неофициальные итоги | [optional] 
**trade_site** | **str** | Идентификатор торговой площадки/источника, возвращаемый методом /Info/Exchange_tree. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

