# EfirDataHubModelsRequestsV2ScoringCustomScoringRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_id** | **str** | Идентификатор запроса на расчет пользовательского скоринга. Необязательный. | [optional] 
**codes** | **list[str]** | Коды компаний ИНН или ОГРН, не более 20 кодов. Необязательный. | [optional] 
**actual_on_date** | **datetime** | Дата, на которую актуальны скоринги (вернется последний пользовательский скоринг за указанную дату).  По умолчанию - текущая дата. | [optional] 
**source** | **AllOfEfirDataHubModelsRequestsV2ScoringCustomScoringRequestSource** | Тип отчетности: 0 - РСБУ, 1 – МСФО.  Если не задан, то будет получена наиболее актуальная на дату запись без учета типа отчетности.  0 &#x3D; RSBU  1 &#x3D; IFRS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

