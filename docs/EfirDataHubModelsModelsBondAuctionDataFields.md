# EfirDataHubModelsModelsBondAuctionDataFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_fintool** | **int** | Идентификатор облигации | [optional] 
**begdist_date** | **datetime** | Дата начала размещения | [optional] 
**enddist_date** | **datetime** | Дата окончания размещения | [optional] 
**method** | **str** | Способ размещения выпуска | [optional] 
**exch_name** | **str** | Название площадки, на которой происходит размещение | [optional] 
**ask_vol** | **float** | Объем облигаций, предложенных к размещению, штук | [optional] 
**ask_val** | **float** | Объем облигаций, предложенных к размещению, в валюте номинала | [optional] 
**bid_vol** | **float** | Объем спроса на выпуск, штук | [optional] 
**bid_val** | **float** | Объем спроса, в валюте номинала | [optional] 
**min_bid** | **float** | Минимальная цена в заявках на приобретение облигаций | [optional] 
**max_bid** | **float** | Максимальная цена в заявках на приобретение облигаций | [optional] 
**dist_vol** | **float** | Размещенный объем, штук | [optional] 
**dist_val** | **float** | Размещенный объем, в валюте номинала | [optional] 
**waprice** | **float** | Средневзвешенная цена по итогам размещения | [optional] 
**yield_waprice** | **float** | Доходность по средневзвешенной цене | [optional] 
**num_trades** | **int** | Количество сделок при размещении | [optional] 
**beg_bid_date** | **datetime** | Дата начала сбора заявок | [optional] 
**end_bid_date** | **datetime** | Дата окончания сбора заявок | [optional] 
**min_bid_rate** | **float** | Минимальная ставка в поданных заявках | [optional] 
**max_bid_rate** | **float** | Максимальная ставка в поданных заявках | [optional] 
**min_bid_yield** | **float** | Минимальная доходность в поданных заявках | [optional] 
**max_bid_yield** | **float** | Максимальная доходность в поданных заявках | [optional] 
**bid_note** | **str** | Примечание к размещению | [optional] 
**note** | **str** | Примечание общее | [optional] 
**type_operation_name** | **str** | Наименование типа операции | [optional] 
**bid_dates_descr** | **str** | Описание предварительных дат сбора заявок | [optional] 
**counter** | **int** | Общее количество записей в выборке, если указан pageNum &#x3D; 1. Иначе null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

