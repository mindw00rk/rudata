# EfirDataHubModelsRequestsV2RiskCapitalAdequacyParamsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор инструмента – ISIN (обязательный) | 
**_date** | **datetime** | Дата расчета (обязательный) | 
**use_frozen_dates** | **bool** | Флаг заморозки рейтингов (необязательный) | [optional] 
**cbr_instructions** | [**list[EfirDataHubModelsRequestsV2NameValuePair]**](EfirDataHubModelsRequestsV2NameValuePair.md) | Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \&quot;Положение о порядке расчета показателя краткосрочной ликвидности\&quot;  - marketRiskEdition - для положений \&quot;О порядке расчета кредитными организациями величины рыночного риска\&quot;  - bankNormEdition - для положений \&quot;Об обязательных нормативах банков\&quot; | [optional] 
**position_open_date** | **datetime** | Дата открытия (покупки) позиции | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

