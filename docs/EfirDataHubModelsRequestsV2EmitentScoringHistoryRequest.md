# EfirDataHubModelsRequestsV2EmitentScoringHistoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс (не более 20) | [optional] 
**codes** | **list[str]** | Коды компаний -ИНН или ОГРН, не более 20 кодов. Указать, если не указаны FinistIds | [optional] 
**actual_on_date** | **datetime** | Дата на которую актуальны скоринги. По умолчанию - текущая дата | [optional] 
**model** | **AllOfEfirDataHubModelsRequestsV2EmitentScoringHistoryRequestModel** | Модель расчета. 0 – invlogit  0 &#x3D; Invlogit | [optional] 
**source** | **AllOfEfirDataHubModelsRequestsV2EmitentScoringHistoryRequestSource** | Тип отчетности: 0 - РСБУ, 1 – МСФО  0 &#x3D; RSBU  1 &#x3D; IFRS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

