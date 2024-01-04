# EfirDataHubModelsRequestsV2EmitentScoringExtHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс (не более 20) | [optional] 
**codes** | **list[str]** | Коды компаний -ИНН или ОГРН, не более 20 кодов. Указать, если не указаны FinistIds | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны скоринги. По умолчаню - текущая дата | [optional] 
**source** | **AllOfEfirDataHubModelsRequestsV2EmitentScoringExtHistoryRequestSource** | Тип отчетности: 0 - РСБУ, 1 – МСФО  0 &#x3D; RSBU  1 &#x3D; IFRS | [optional] 
**is_filtered** | **bool** | Признак фильтрации значений балансов и коэффициентов на момент окончания отчетности | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

