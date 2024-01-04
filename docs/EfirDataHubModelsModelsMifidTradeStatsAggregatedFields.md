# EfirDataHubModelsModelsMifidTradeStatsAggregatedFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор финансового инструмента в базе Интерфакс | [optional] 
**tradedatestart** | **datetime** | Дата начала отбора сделок | [optional] 
**tradedateend** | **datetime** | Дата окончания отбора сделок | [optional] 
**is_filtered** | **bool** | Признак фильтрации сделок | [optional] 
**isin** | **str** | ISIN | [optional] 
**code** | **str** | Код переданный в параметре Codes | [optional] 
**group_name_rus** | **str** | Наименование группы сделок - Рус | [optional] 
**group_name_eng** | **str** | Наименование группы сделок - Англ | [optional] 
**update_date** | **datetime** | Дата обновления статистики | [optional] 
**total_turnover** | **float** | Общий оборот сделок | [optional] 
**total_volume** | **float** | Общий объем сделок | [optional] 
**wap** | **float** | Средневзвешенная цена сделок периода | [optional] 
**median_price** | **float** | Значение, которое PRICE не превышает с вероятностью 0,5 | [optional] 
**price_q025** | **float** | Значение, которое PRICE не превышает с вероятностью 0,25 | [optional] 
**price_q075** | **float** | Значение, которое PRICE не превышает с вероятностью 0,75 | [optional] 
**price_max** | **float** | Максимальная цена для сделок периода | [optional] 
**price_min** | **float** | Минимальная цена для сделок периода | [optional] 
**trades_cnt** | **int** | Число сделок за период | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

