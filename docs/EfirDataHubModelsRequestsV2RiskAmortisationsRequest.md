# EfirDataHubModelsRequestsV2RiskAmortisationsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isin** | **str** | ISIN (обязательный) | 
**current_only** | **bool** | Использовать только будущие амортизации или все | [optional] 
**offer_enable** | **bool** | Использовать оферты | [optional] 
**_date** | **datetime** | Дата расчета | [optional] 
**group_by_periods** | **bool** | Группировать амортизации по периодам отчетности по рискам | [optional] 
**edition** | **str** | Редакция инструкции ЦБ | [optional] 
**parts_as_pct** | **bool** | Значения погашаемых долей: true - в %, false - в долях (% * 0.01) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

