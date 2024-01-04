# EfirDataHubModelsModelsMoexFuturesFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_iss** | **int** | Числовой идентификатор инструмента в БД ЭФИР | [optional] 
**secid** | **str** | Краткий торговый код ПФИ на Мосбирже | [optional] 
**boardid** | **str** | Идентификатор режима торгов | [optional] 
**board_title** | **str** | Полное наименование режима торгов | [optional] 
**board_group** | **str** | Краткое наименование группы режимов торгов Мосбиржи (англ.) | [optional] 
**board_group_title** | **str** | Краткое наименование группы режимов торгов Мосбиржи (рус.) | [optional] 
**market** | **str** | Краткое наименование рынка Мосбиржи (англ.) | [optional] 
**engine** | **str** | Краткое наименование торговой системы Мосбиржи (англ.) | [optional] 
**short_name** | **str** | Краткое русское наименование ПФИ на Мосбирже | [optional] 
**isin** | **str** | Международный идентификационный код инструмента ISIN | [optional] 
**cfi_ifx** | **str** | Идентификационный код типа инструмента в БД Интерфакс | [optional] 
**cfi_name** | **str** | Расшифровка идентификационного кода типа инструмента | [optional] 
**lot_size** | **int** | Размер лота в штуках | [optional] 
**expiration_date** | **datetime** | Дата погашения ценной бумаги | [optional] 
**currency** | **str** | Код валюты торгов | [optional] 
**emitent_code** | **str** | Код эмитента (акции - Мосбиржа и НП РТС, остальные - Интерфакс) | [optional] 
**emitent_name** | **str** | Наименование эмитента из БД Интерфакс | [optional] 
**market_sector** | **str** | Сектор рынка эмитента | [optional] 
**ba_id_iss** | **int** | Числовой идентификатор базового актива фьючерсного контракта в БД ЭФИР | [optional] 
**ba_secid** | **str** | Краткий торговый код базового актива фьючерсного контракта на Мосбирже | [optional] 
**ba_currency** | **int** | Код валюты торгов для базового актива фьючерсного контракта | [optional] 
**ba_coeff** | **float** | Коэффициент инструмента БА описывает количество единиц базового актива в одном фьючерсе | [optional] 
**ba_min_step** | **float** | Минимальный шаг цены в валюте торгов | [optional] 
**ba_min_step_price** | **float** | Стоимость шага цены | [optional] 
**ba_lot_size** | **int** | Размер лота в штуках | [optional] 
**ba_trade_currency** | **int** | Код валюты торгов для базового актива фьючерсного контракта | [optional] 
**secid_full** | **str** | Полный код фьючерса | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

