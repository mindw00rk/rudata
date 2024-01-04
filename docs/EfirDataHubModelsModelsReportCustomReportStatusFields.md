# EfirDataHubModelsModelsReportCustomReportStatusFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_id** | **str** | Идентификатор запроса пакета компаний | [optional] 
**dt** | **datetime** | дата и время запроса | [optional] 
**user_id** | **int** | ID пользователя | [optional] 
**fininst_id** | **int** | ID компании | [optional] 
**inn** | **str** | ИНН компании | [optional] 
**ogrn** | **str** | ОГРН  компании | [optional] 
**extended** | **bool** | true - расширенный скоринг, false - базовый | [optional] 
**source** | **AllOfEfirDataHubModelsModelsReportCustomReportStatusFieldsSource** | База расчета &#x27;RSBU&#x27;- 0 или &#x27;IFRS&#x27; -1  0 &#x3D; RSBU  1 &#x3D; IFRS | [optional] 
**status** | **AllOfEfirDataHubModelsModelsReportCustomReportStatusFieldsStatus** | Статус отчета:  - 1 - в очереди,  - 2 - в процессе,  - 3 - готово,  - 4 - ошибка расчета  - 5 - отсутствует отчетность по компании  1 &#x3D; Queued  2 &#x3D; Processing  3 &#x3D; Ready  4 &#x3D; Error  5 &#x3D; NoReports | [optional] 
**counter** | **int** | Общее количество записей в выборке, если указан pageNum &#x3D; 1. Иначе &#x3D; null | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

