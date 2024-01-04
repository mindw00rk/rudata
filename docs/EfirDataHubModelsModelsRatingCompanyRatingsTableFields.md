# EfirDataHubModelsModelsRatingCompanyRatingsTableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_ra** | **str** | Краткое наименование рейтингового действия | [optional] 
**dt** | **datetime** | Дата рейтингового события | [optional] 
**last** | **str** | Значение рейтинга по шкале конкретного рейтингового агентства. Например, «Baaa1» для рейтинга Moody’s. | [optional] 
**last_dt** | **datetime** | Дата последнего события | [optional] 
**change** | **str** | Изменение (подтвержден, понижен, установлен и т.п.) | [optional] 
**forecast** | **str** | Прогноз рейтинга | [optional] 
**advanced** | **str** | Стадии установки рейтинга: На пересмотре, Ожидаемый, Предварительный, Основной | [optional] 
**prev** | **str** | Предыдущее значение рейтинга | [optional] 
**prev_dt** | **datetime** | Дата, когда было присвоено предыдущее значение рейтинга | [optional] 
**id_rating** | **int** | Идентификатор вида рейтинга | [optional] 
**code** | **str** | Символьный код компании | [optional] 
**code_type** | **str** | Тип идентификатора компании | [optional] 
**company_name** | **str** | Наименование компании | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

