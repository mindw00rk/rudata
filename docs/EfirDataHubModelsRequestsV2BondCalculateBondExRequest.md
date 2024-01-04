# EfirDataHubModelsRequestsV2BondCalculateBondExRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор облигации (ISIN, RegCode, NRDCode, FintoolID, TradeCode) | 
**_date** | **datetime** | Дата расчета | 
**value** | **float** | Цена (в % от номинала) или доходность (в % годовых) | 
**value_type** | **AllOfEfirDataHubModelsRequestsV2BondCalculateBondExRequestValueType** | Тип значения value:  - 0 – чистая цена;  - 1 – полная цена;  - 2 – доходность к погашению;  - 3 – доходность к оферте;  - 10 – чистая цена в валюте номинала;  - 11 – полная цена в валюте номинала.  0 &#x3D; NetPricePrc  1 &#x3D; GrossPricePrc  2 &#x3D; YieldToMaturity  3 &#x3D; YieldToOffer  10 &#x3D; NetPriceMoneyPrc  11 &#x3D; GrossPriceMoneyPrc | [optional] 
**fields** | **list[str]** | Список требуемых полей | [optional] 
**periods** | **AllOfEfirDataHubModelsRequestsV2BondCalculateBondExRequestPeriods** | Определяет периоды расчёта, т.е. набор возвращаемых данных:   - 0 – до погашения и ближайшей оферты;  - 1 – сводные значения;  - 2 – до погашения;  - 3 – до погашения и всех оставшихся оферт.  0 &#x3D; MaturityAndOffer  1 &#x3D; Consolidated  2 &#x3D; Maturity  3 &#x3D; MaturityAndAllOffers | [optional] 
**coupon_forecast** | **str** | Пользовательские значения доходности для неизвестных купонов. Разделитель «;». | [optional] 
**coupon_binding** | **str** | Даты пользовательских купонов, заданных в параметре couponForecast. Разделитель «;». | [optional] 
**use_pay_date** | **bool** | Use PayDate as event date instead of the end of period | [optional] 
**is_close_register** | **bool** | Use date of registry closing | [optional] 
**tax_model** | **int** | Use specific taxation model | [optional] 
**commission** | **float** | Optional commission | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

