# EfirDataHubModelsModelsReportCustomRsbuReportFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | Идентификатор отчётности | [optional] 
**fininst_id** | **int** | Идентификатор организации в базе Интерфакс | [optional] 
**inn** | **str** | ИНН | [optional] 
**ogrn** | **str** | ОГРН | [optional] 
**sector** | **int** | Id сектора организации, см. метод /Dictionary/MarketSectors | [optional] 
**period_begin** | **datetime** | Дата начала отчетного периода | [optional] 
**period_end** | **datetime** | Дата окончания отчетного периода | [optional] 
**period_name** | **str** | Наименование отчетного периода | [optional] 
**edition_id** | **int** | Версия отчёта | [optional] 
**status** | **int** | Статус отчета:  - 1 - в очереди,  - 2 - в процессе,  - 3 - готово,  - 4 - ошибка расчета  - 5 - отсутствует отчетность по компании | [optional] 
**power** | **float** | Множитель | [optional] 
**counterpartyid** | **int** | Идентификатор контрагента | [optional] 
**rows** | [**list[EfirDataHubModelsModelsReportCustomRsbuReportRow]**](EfirDataHubModelsModelsReportCustomRsbuReportRow.md) | Значения строк | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

