# EfirDataHubModelsModelsRiskCARule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **int** | Тип классификатора. Возможные значения:  0 – гарантированная часть выпуска при фондировании в рублях  1 – негарантированная часть выпуска при фондировании в рублях  2 – гарантированная часть выпуска при фондировании не в рублях  3 – негарантированная часть выпуска при фондировании не в рублях | [optional] 
**rule_type_name** | **str** | “Расшифровка” значения RuleType в стороку:  0 – “GARANT_RUB”  1 – “NOGARANT_RUB”  2 – “GARANT_NOTRUB”  3 – “NOGARANT_NOTRUB | [optional] 
**rule** | **str** | Значение классификатора | [optional] 
**credit_risk_ratio** | **float** | Коэффициент кредитного риска. Может быть NULL. | [optional] 
**risk_group** | **str** | Группа риска | [optional] 
**reason** | **str** | Обоснование (ссылка на абзац из инструкции) | [optional] 
**code** | **str** | Код по инструкции | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

