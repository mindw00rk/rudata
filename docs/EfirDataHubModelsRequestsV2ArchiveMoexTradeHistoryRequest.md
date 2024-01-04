# EfirDataHubModelsRequestsV2ArchiveMoexTradeHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | Краткое наименование торговой системы Мосбиржи (англ.). Обязательный параметр. Подсистема MOEX: stock, state, currency и т.д. | 
**market** | **str** | Краткое наименование рынка Мосбиржи (англ.). Обязательный параметр. Рынок MOEX: index, shares, bonds, ndm и т.д. | 
**board_ids** | **list[str]** | Идентификатор режима торгов Необязательный параметр. Короткое имя режима торгов или группы режимов. Может быть задано нескольких элементов через запятую. | [optional] 
**instruments** | **list[str]** | Массив идентификаторов торгуемых инструментов. Короткие биржевые коды, которые можно получить в сервисе Securities (поле SECID). Например, SBER. | [optional] 
**date_from** | **datetime** | dateFrom – Дата начала периода. | 
**date_to** | **datetime** | Дата окончания периода. Интервал запроса данных не может превышать 1 час. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

