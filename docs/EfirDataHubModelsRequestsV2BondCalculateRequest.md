# EfirDataHubModelsRequestsV2BondCalculateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_close_register** | **bool** |  | [optional] 
**is_percent** | **bool** |  | [optional] 
**id** | **int** | issId облигации | 
**_date** | **datetime** | Дата расчета | 
**value** | **float** | Цена (в % от номинала) или доходность (в % годовых) | 
**value_type** | **AllOfEfirDataHubModelsRequestsV2BondCalculateRequestValueType** | Тип значения value:  - 0 – чистая цена;  - 1 – полная цена;  - 2 – доходность к погашению;  - 3 – доходность к оферте.  0 &#x3D; NetPricePrc  1 &#x3D; GrossPricePrc  2 &#x3D; YieldToMaturity  3 &#x3D; YieldToOffer  10 &#x3D; NetPriceMoneyPrc  11 &#x3D; GrossPriceMoneyPrc | [optional] 
**rate_new** | **float** | Значение ставки для неизвестных купонов. Если не задано, то используется ставка последнего известного купона. | [optional] 
**fields** | **list[str]** | Список требуемых полей | [optional] 
**periods** | **AllOfEfirDataHubModelsRequestsV2BondCalculateRequestPeriods** | Определяет периоды расчёта, т.е. набор возвращаемых данных:   - 0 – до погашения и ближайшей оферты;  - 1 – сводные значения;  - 2 – до погашения;  - 3 – до погашения и всех оставшихся оферт.  0 &#x3D; MaturityAndOffer  1 &#x3D; Consolidated  2 &#x3D; Maturity  3 &#x3D; MaturityAndAllOffers | [optional] 
**commission** | **float** | Optional commission | [optional] 
**members** | **list[str]** | Строковой массив, возвращаемых в ответе, объектов:  \&quot;CalculateBond\&quot;,\&quot;FaceValue\&quot;. Если не указан, то все. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

