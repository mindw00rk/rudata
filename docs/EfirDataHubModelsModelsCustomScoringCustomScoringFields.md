# EfirDataHubModelsModelsCustomScoringCustomScoringFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_id** | **str** | Идентификатор запроса на расчет скоринга | [optional] 
**fininstid** | **int** | Идентификатор эмитента в БД Интерфакс | [optional] 
**inn** | **str** | ИНН эмитента | [optional] 
**ogrn** | **str** | ОГРН эмитента | [optional] 
**source** | **str** | Тип отчетности, по которой сформированы значения: &#x27;rsbu&#x27; или &#x27;ifrs&#x27; | [optional] 
**last_reported_date** | **datetime** | Дата окончания отчетности, по которой был рассчитан расширенный скоринг | [optional] 
**update_date** | **datetime** | Дата расчета расширенного скоринга | [optional] 
**pd** | **float** | Вероятность дефолта в процентах | [optional] 
**pd_pit** | **float** | Вероятность дефолта в процентах, откорректированная на дату вызова | [optional] 
**rating** | **str** | Рейтинг | [optional] 
**rating_ru** | **str** | Рейтинг по национальной шкале | [optional] 
**counterpartyid** | **int** | Идентификатор контрагента | [optional] 
**grade_probabilities** | [**list[EfirDataHubModelsModelsEmitentGradeProbability]**](EfirDataHubModelsModelsEmitentGradeProbability.md) | Массив вероятностей (в процентах) попадания в грейд | [optional] 
**grade_probabilities_ru** | [**list[EfirDataHubModelsModelsEmitentGradeProbabilityRU]**](EfirDataHubModelsModelsEmitentGradeProbabilityRU.md) | Массив вероятностей (в процентах) попадания в грейд по национальной шкале | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

