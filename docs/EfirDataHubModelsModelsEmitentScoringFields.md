# EfirDataHubModelsModelsEmitentScoringFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | значение Code из запроса (ИНН или ОГРН) | [optional] 
**fininst_id** | **int** | Идентификатор компании в базе Интерфакс | [optional] 
**inn** | **str** | ИНН | [optional] 
**ogrn** | **str** | ОГРН | [optional] 
**shortname_rus** | **str** | Краткое наименование компании | [optional] 
**model** | **str** | Модель расчета | [optional] 
**source** | **str** | База расчета - РСБУ или МСФО | [optional] 
**last_reported_date** | **datetime** | Дата первого присвоения скоринга | [optional] 
**update_date** | **str** | Дата последнего обновления расчета | [optional] 
**pd** | **float** | Вероятность дефолта в процентах | [optional] 
**pd_pit** | **float** | Вероятность дефолта в процентах, откорректированная на дату вызова | [optional] 
**rating** | **str** | Рейтинг | [optional] 
**rating_ru** | **str** | Рейтинг по национальной шкале | [optional] 
**counterpartyid** | **int** | Идентификатор контрагента | [optional] 
**grade_probabilities** | **AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilities** | Вероятности попадания в грейд | [optional] 
**grade_probabilities_ru** | **AllOfEfirDataHubModelsModelsEmitentScoringFieldsGradeProbabilitiesRu** | Вероятности попадания в грейды по национальной шкале | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

