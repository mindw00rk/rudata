# EfirDataHubModelsRequestsV2RiskMarketRiskDataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **list[str]** | Список идентификаторов (ISIN, регистрационный номер) | 
**calc_date** | **datetime** | Дата расчета | 
**offer_enable** | **bool** | Учитывать оферты | [optional] 
**use_frozen_dates** | **bool** | Использовать даты рейтингов | [optional] 
**edition** | **str** | Редакция инструкции ЦБ («387-П» или «511-П») | [optional] 
**b_b_country** | **str** | Двухбуквенный код страны филиала банка (Alfa-2), например, KZ, по умолчанию &#x3D; RU | [optional] 
**cbr_instructions** | [**list[EfirDataHubModelsRequestsV2NameValuePair]**](EfirDataHubModelsRequestsV2NameValuePair.md) | Параметры инструкций ЦБ РФ:  - vlaEdition - для положений \&quot;Положение о порядке расчета показателя краткосрочной ликвидности\&quot;  - marketRiskEdition - для положений \&quot;О порядке расчета кредитными организациями величины рыночного риска\&quot;  - bankNormEdition - для положений \&quot;Об обязательных нормативах банков\&quot; | [optional] 
**position_open_date** | **datetime** | Дата открытия (покупки) позиции | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

