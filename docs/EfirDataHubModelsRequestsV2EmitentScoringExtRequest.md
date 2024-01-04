# EfirDataHubModelsRequestsV2EmitentScoringExtRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fininst_ids** | **list[int]** | Идентификаторы компаний в базе Интерфакс (не более 20) | [optional] 
**codes** | **list[str]** | Коды компаний -ИНН или ОГРН, не более 20 кодов. Указать, если не указаны FinistIds | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны скоринги. По умолчаню - текущая дата | [optional] 
**non_expired_only** | **bool** | Флаг возврата только тех скорингов, которые по дате окончания отчетности отстоят от даты запроса не более чем на 400 дней.  По-умолчанию - true | [optional] 
**source** | **AllOfEfirDataHubModelsRequestsV2EmitentScoringExtRequestSource** | Тип отчетности: 0 - РСБУ, 1 – МСФО. Если не задан, то будет получена наиболее актуальная на дату запись без учета типа отчетности.  0 &#x3D; RSBU  1 &#x3D; IFRS | [optional] 
**sector** | **int** | Сектор | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

