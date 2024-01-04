# EfirDataHubModelsRequestsV2ScoringCustomScoringMsfoRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор компании - INN или OGRN | 
**id_type** | **str** | Тип идентификатора - INN,OGRN | 
**reports** | [**list[EfirDataHubModelsModelsEmitentMsfoReportFields]**](EfirDataHubModelsModelsEmitentMsfoReportFields.md) | Массив отчётности по структуре ответа метода /v2/Emitent/{code}/MSFOReport(Ext) | 
**sector** | **int** | Id сектора компании из метода /Dictionary/MarketSectors | 
**date_from** | **datetime** | Дата начала периода отчётности | 
**date_to** | **datetime** | Дата конца периода отчётности | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

