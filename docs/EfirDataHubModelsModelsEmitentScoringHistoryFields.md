# EfirDataHubModelsModelsEmitentScoringHistoryFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Значение Code из запроса (ИНН или ОГРН) | [optional] 
**fininst_id** | **int** | Идентификатор компании в БД Интерфакс | [optional] 
**model** | **str** | Модель расчета | [optional] 
**source** | **str** | База расчета - РСБУ или МСФО | [optional] 
**last_reported_date** | **datetime** | Дата окончания отчетности, по которой был рассчитан скоринг | [optional] 
**update_date** | **str** | Дата расчета скоринга | [optional] 
**pd** | **float** | Вероятность дефолта в процентах | [optional] 
**pd_pit** | **float** | Вероятность дефолта в процентах, откорректированная на дату вызова | [optional] 
**rating** | **str** | Рейтинг | [optional] 
**rating_ru** | **str** | Рейтинг по национальной шкале | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

