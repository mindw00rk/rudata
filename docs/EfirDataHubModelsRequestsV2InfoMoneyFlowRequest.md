# EfirDataHubModelsRequestsV2InfoMoneyFlowRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор инструмента. ISIN, RegCode, NRDCode, FintoolId. | 
**date1** | **datetime** | Дата начала интервала времени. | 
**date2** | **datetime** | Дата окончания интервала времени. | 
**use_offer** | **bool** | 1 – исходя из продажи облигации в ближайшую оферту | [optional] 
**use_forecast** | **bool** | 1 – исходя из предполагаемых дивидендов | [optional] 
**coupon_forecasts** | [**list[EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast]**](EfirDataHubModelsRequestsV2InfoMoneyFlowRequestForecast.md) | Пользовательские данные для описания неизвестных купонов. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

