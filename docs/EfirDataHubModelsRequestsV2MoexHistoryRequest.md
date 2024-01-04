# EfirDataHubModelsRequestsV2MoexHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | Краткое наименование торговой системы Мосбиржи (англ.). Обязательный параметр. Подсистема MOEX: stock, state, currency и т.д. | [optional] 
**market** | **str** | Краткое наименование рынка Мосбиржи (англ.). Обязательный параметр. Рынок MOEX: index, shares, bonds, ndm и т.д. | [optional] 
**boardid** | **list[str]** | Идентификатор режима торгов Необязательный параметр. Короткое имя режима торгов или группы режимов. Может быть задано нескольких элементов через запятую. | [optional] 
**instruments** | **list[str]** | Массив идентификаторов торгуемых инструментов. Короткие биржевые коды, которые можно получить в сервисе Securities (поле SECID). Например, SBER. | [optional] 
**date_from** | **datetime** | Дата начала периода. | [optional] 
**date_to** | **datetime** | Дата окончания периода. Может совпадать с dateFrom, если требуются данные за один день. | [optional] 
**trading_sessions** | **list[int]** | Перечень номеров торговых сессий для отбора:  - 0 - Утренняя сессия,  - 1 - Основная сессия,  - 2 - Вечерняя сессия,  - 3 - Итоги  Если не задан, то отбор по торговым сессиям не выполняется. | [optional] 
**page_num** | **int** | Номер страницы для выборки. Если не задан или меньше 1, то устанавливается 1 | [optional] 
**page_size** | **int** | Размер страницы выборки. Если более 1000, то устанавливается 1000 | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

