# EfirDataHubModelsRequestsV2BondCalculateBondMultiRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **datetime** | Дата расчёта | 
**items** | [**list[EfirDataHubModelsRequestsV2BondCalculateBondMultiRequestItem]**](EfirDataHubModelsRequestsV2BondCalculateBondMultiRequestItem.md) | Список инструментов с параметрами | 
**fields** | **list[str]** | Список требуемых полей | [optional] 
**periods** | **AllOfEfirDataHubModelsRequestsV2BondCalculateBondMultiRequestPeriods** | Определяет периоды расчёта, т.е. набор возвращаемых данных:   0 - до погашения и ближайшей оферты  1- сводные значения  2 – до погашения  3 – до погашения и всех оставшихся оферт  0 &#x3D; MaturityAndOffer  1 &#x3D; Consolidated  2 &#x3D; Maturity  3 &#x3D; MaturityAndAllOffers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

