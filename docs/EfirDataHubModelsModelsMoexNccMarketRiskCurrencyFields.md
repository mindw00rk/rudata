# EfirDataHubModelsModelsMoexNccMarketRiskCurrencyFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **datetime** | Дата риска | [optional] 
**fintoolid** | **int** | ID инструмента в базе Интерфакс | [optional] 
**range_id** | **int** | Диапазон | [optional] 
**begin_range** | **int** | Начало диапазона | [optional] 
**end_range** | **int** | Конец диапазона | [optional] 
**risk_fall_rate** | **float** | Ставка риска падения цены | [optional] 
**risk_grow_rate** | **float** | Ставка риска роста цены | [optional] 
**lower_bound** | **float** | Нижняя граница | [optional] 
**central_rate** | **float** | Центральный курс, руб. | [optional] 
**upper_bound** | **float** | Верхняя  граница | [optional] 
**penalty_asset** | **float** | Штрафная ставка за перенос обязательств по активу, % | [optional] 
**penalty_rub** | **float** | Штрафная ставка за перенос обязательств по рублям, % | [optional] 
**to_ensuring** | **bool** | Прием валюты/драг.металла в обеспечение | [optional] 
**ban_short_sale** | **bool** | Запрет коротких продаж | [optional] 
**fix_date** | **datetime** | Дата и время фиксации/ изменения параметров | [optional] 
**assetid2** | **str** | Актив 2 | [optional] 
**discount** | **float** | Начальное значение ставки процентного риска | [optional] 
**repodiscount** | **float** | Ставка РЕПО | [optional] 
**rcl** | **float** | Нижняя граница ценового коридора ценной бумаги | [optional] 
**rch** | **float** | Верхняя граница ценового коридора ценной бумаги | [optional] 
**limit** | **float** | Лимит ликвидности нетто-позиции. | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

