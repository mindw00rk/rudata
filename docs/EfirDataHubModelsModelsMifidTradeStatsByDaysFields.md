# EfirDataHubModelsModelsMifidTradeStatsByDaysFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | ID инструмента в БД Интерфакс | [optional] 
**tradedatestart** | **datetime** | Дата начала отрезка отбора свойств фильтров | [optional] 
**tradedateend** | **datetime** | Дата окончания отрезка отбора свойств фильтров | [optional] 
**isin** | **str** | ISIN инструмента | [optional] 
**code** | **str** | Код переданный в запросе в массиве Codes | [optional] 
**group_name_rus** | **str** | Имя торговой группы | [optional] 
**group_name_eng** | **str** | Имя торговой группы по-английски | [optional] 
**is_filtered** | **bool** | Признак фильтрованных сделок | [optional] 
**trade_date** | **datetime** | Дата торгов | [optional] 
**update_date** | **datetime** | Дата обновления статистики | [optional] 
**wap** | **float** | Средневзвешенная цена | [optional] 
**median_price** | **float** | Значение, которое PRICE не превышает с вероятностью 0,5 | [optional] 
**price_q025** | **float** | Значение, которое PRICE не превышает с вероятностью 0,25 | [optional] 
**price_q075** | **float** | Значение, которое PRICE не превышает с вероятностью 0,75 | [optional] 
**price_max** | **float** | Максимальная цена сделки | [optional] 
**price_min** | **float** | Минимальная цена сделки | [optional] 
**total_volume** | **float** | Совокупный объем сделок за торговый день (шт) | [optional] 
**total_turnover** | **float** | Общий оборот сделок | [optional] 
**trades_cnt** | **int** | Число сделок за период | [optional] 
**market_price** | **float** | Рыночная цена | [optional] 
**market_price_level** | **int** | Уровень рыночной цены (1-5 или null) | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

