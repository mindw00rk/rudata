# EfirDataHubModelsRequestsV2BondCalculateBondMultiRequestItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор/код инструмента | [optional] 
**value** | **float** | Цена или доходность инструмента | [optional] 
**value_type** | **AllOfEfirDataHubModelsRequestsV2BondCalculateBondMultiRequestItemValueType** | Тип значения value: 0 – чистая цена; 1 – полная цена; 2 – доходность к погашению; 3 – доходность к оферте;  10 - чистая цена в валюте номинала;  11 - полная цена в валюте номинала  0 &#x3D; NetPricePrc  1 &#x3D; GrossPricePrc  2 &#x3D; YieldToMaturity  3 &#x3D; YieldToOffer  10 &#x3D; NetPriceMoneyPrc  11 &#x3D; GrossPriceMoneyPrc | [optional] 
**coupon_forecasts** | [**list[EfirDataHubModelsRequestsV2BondCalculateBondMultiForecast]**](EfirDataHubModelsRequestsV2BondCalculateBondMultiForecast.md) | Пользовательские значения для неизвестных купонов | [optional] 
**use_pay_date** | **bool** | Признак необходимости использовать дату фактического платежа вместо даты окончания купона. Опционально. | [optional] 
**is_close_register** | **bool** | Расчёт НКД вести не на дату окончания купона, а на дату фиксации реестра получателей. Опционально. | [optional] 
**tax_model** | **int** | Номер модели налогообложения. Опционально. | [optional] 
**commission** | **float** | Размер комиссии, а если не задан, то считаем равным 0. Опционально. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

