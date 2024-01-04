# EfirDataHubModelsModelsRUPriceSecuritiesFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_date** | **str** | Дата актуальности справочника | [optional] 
**version** | **int** | Версия справочника, 1 - старая методика; 2 - новая методика; | [optional] 
**fintoolid** | **int** | Идентификатор выпуска бумаги | [optional] 
**isin** | **str** | ISIN инструмента | [optional] 
**regcode** | **str** | Регистрационный код | [optional] 
**nrd_code** | **str** | Код инструмента в НРД | [optional] 
**shortname_rus** | **str** | Краткое наименование выпуска | [optional] 
**issueruid** | **int** | УИН оператора в БД Интерфакс (fininstid) | [optional] 
**borroweruid** | **int** | УИН реального заемщика (эмитента) в БД Интерфакс (fininstid) | [optional] 
**id_iss** | **int** | Идентификатор торгового инструмента в базе Интерфакс (для version&#x3D;1) | [optional] 
**beg_date** | **datetime** | Первая дата итогов торгов | [optional] 
**end_date** | **datetime** | Последняя дата итогов торгов | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

