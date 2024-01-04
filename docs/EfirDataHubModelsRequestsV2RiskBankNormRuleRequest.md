# EfirDataHubModelsRequestsV2RiskBankNormRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin** | **str** | ISIN (обязательный) | 
**_date** | **datetime** | Дата (обязательный) | 
**funding** | **bool** | 1 – фондирование в валюте номинала. По умолчанию 0. | [optional] 
**use_frozen_dates** | **bool** | Флаг использвания даты \&quot;заморозки\&quot; рейтингов | [optional] 
**bank_norm_edition** | **str** | Парметры инструкций ЦБ РФ (139-И, 180-И, 180-И/2018, 180-И/2019) | [optional] 
**position_open_date** | **datetime** | Дата открытия (покупки) позиции | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

