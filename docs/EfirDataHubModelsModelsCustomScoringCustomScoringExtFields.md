# EfirDataHubModelsModelsCustomScoringCustomScoringExtFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_id** | **str** | Идентификатор запроса на расчет скоринга | [optional] 
**fininstid** | **int** | Идентификатор эмитента в БД Интерфакс | [optional] 
**inn** | **str** | ИНН эмитента | [optional] 
**ogrn** | **str** | ОГРН эмитента | [optional] 
**sector** | **str** | Отрасль эмитента | [optional] 
**source** | **str** | Тип отчетности, по которой сформированы значения | [optional] 
**last_reported_date** | **datetime** | дата окончания отчетности, по которой был рассчитан расширенный скоринг | [optional] 
**update_date** | **datetime** | дата расчета расширенного скоринга | [optional] 
**pd** | **float** | Вероятность дефолта в процентах | [optional] 
**pd_pit** | **float** | Вероятность дефолта в процентах, откорректированная на дату вызова | [optional] 
**rating** | **str** | Рейтинг | [optional] 
**rating_ru** | **str** | Рейтинг по национальной шкале | [optional] 
**counterpartyid** | **int** | Идентификатор контрагента | [optional] 
**transformed** | [**list[EfirDataHubModelsModelsEmitentScoringExtTransformed]**](EfirDataHubModelsModelsEmitentScoringExtTransformed.md) | Трансформированные коэффициенты (вероятности в %) | [optional] 
**forecasts** | [**list[EfirDataHubModelsModelsEmitentScoringExtForecast]**](EfirDataHubModelsModelsEmitentScoringExtForecast.md) | Прогнозы | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

