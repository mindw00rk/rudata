# EfirDataHubModelsModelsEmitentScoringExtHistoryFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | значение Code из запроса (ИНН или ОГРН) | [optional] 
**fininst_id** | **int** | Идентификатор эмитента в БД Интерфакс | [optional] 
**inn** | **str** | ИНН эмитента | [optional] 
**ogrn** | **str** | ОГРН эмитента | [optional] 
**sector** | **str** | Отрасль эмитента | [optional] 
**source** | **str** | Тип отчетности, по которой сформированы значения | [optional] 
**last_reported_date** | **str** | дата окончания отчетности, по которой был рассчитан расширенный скоринг | [optional] 
**update_date** | **datetime** | дата расчета расширенного скоринга | [optional] 
**is_filtered** | **int** | Признак фильтрации по горизонту прогнозирования | [optional] 
**values** | **AllOfEfirDataHubModelsModelsEmitentScoringExtHistoryFieldsValues** | Значения балансов и коэффициентов | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

