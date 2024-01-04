# EfirDataHubModelsModelsRiskCapitalAdequacyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_doc** | **int** | Идентификатор инструкции, действующей на дату расчета | [optional] 
**doc_short_name** | **str** | Краткое наименование инструкции (например, «139-И») | [optional] 
**repo_discount** | **float** | Дисконт для расчета риска по операциям РЕПО | [optional] 
**rules** | [**list[EfirDataHubModelsModelsRiskCARule]**](EfirDataHubModelsModelsRiskCARule.md) | Mассив объектов класса CARule | [optional] 
**error** | **str** | Текст ошибки, если она произошла | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

