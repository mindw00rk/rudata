# EfirDataHubModelsModelsRiskCorpInvestClassFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininstid** | **int** | Идентификатор компании в базе Интерфакс | [optional] 
**code** | **str** | Идентификатор компании, заданный во входном параметре  codes (ИНН, ОГРН, LEI) | [optional] 
**inn** | **str** | ИНН компании | [optional] 
**ogrn** | **str** | ОГРН компании | [optional] 
**lei** | **str** | LEI-код компании | [optional] 
**company_name** | **str** | Наименование компании | [optional] 
**dt** | **datetime** | Дата расчета (дата, для которой выполнялся расчет | [optional] 
**update_date** | **datetime** | Дата обновления данных | [optional] 
**issuer_fininstid** | **int** | Идентификатор компании, чьи бумаги попали в котировальный список | [optional] 
**issuer_inn** | **str** | ИНН компании, чьи бумаги попали в котировальный список | [optional] 
**issuer_ogrn** | **str** | ОГРН компании, чьи бумаги попали в котировальный список | [optional] 
**issuer_lei** | **str** | LEI-код компании, чьи бумаги попали в котировальный список | [optional] 
**issuer_name** | **str** | Наименование компании, чьи бумаги попали в котировальный список | [optional] 
**fintoolid** | **int** | Идентификатор бумаги эмитента, попавшей в котировальный список | [optional] 
**isin** | **str** | ISIN бумаги эмитента, попавшей в котировальный список | [optional] 
**fintool_name** | **str** | Наименование бумаги эмитента, попавшей в котировальный список | [optional] 
**investment_grade** | **bool** | Принадлежность к инвестиционному классу (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована. | [optional] 
**corporate_issuer** | **bool** | Принадлежность к корпоративному сектору (true/false/NULL). Значение NULL обозначает что компания не была идентифицирована. | [optional] 
**counter** | **int** | Общее количество записей в выборке | [optional] 
**rn** | **int** | Номер записи в выборке | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

