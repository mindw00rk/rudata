# EfirDataHubModelsRequestsV2ReportCustomReportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | ID отчётности.  Необязательный.  Если задан - используется этот параметр, иначе - остальные. | [optional] 
**code** | **str** | Один из идентификаторов компании: FininstId, ИНН, ОГРН  Необязательный.  Используется, если не задан Id. | [optional] 
**balance_date** | **datetime** | Дата отчетности.  Необязательный.  Если не задан, то вернётся отчет с самой поздней датой. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

