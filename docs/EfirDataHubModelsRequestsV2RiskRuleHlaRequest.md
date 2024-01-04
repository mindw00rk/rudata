# EfirDataHubModelsRequestsV2RiskRuleHlaRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_ids** | **list[int]** | Список идентификаторов инструмента в БД Интерфакс | [optional] 
**codes** | **list[str]** | Список кодов инструментов - (ISIN). Используется, если не задан FintoolIds | [optional] 
**_date** | **datetime** | Дата расчета. По-умолчанию - текущая | [optional] 
**source_name** | **str** | Наименование источника данных, по которым рассчитаны значения:  - &#x27;main&#x27; - источник, соответствующий основному торговому инструменту. Приоритет 1.  - &#x27;pcnrd&#x27; - ценовой центр НРД. Приоритет 2.  - &#x27;rudip&#x27; - данные RUDIP/MIFID. Приоритет 3.  - &#x27;moex&#x27; - данные Московской биржи. Приоритет 4.  - Источник не указан - значение с наивысшим приоритетом из существующих на дату. | [optional] 
**page_num** | **int** | Номер страницы для выборки. По-умолчанию - 1. | [optional] 
**page_size** | **int** | Размер страницы выборки. Не более 1000. По-умолчанию - 1000 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

