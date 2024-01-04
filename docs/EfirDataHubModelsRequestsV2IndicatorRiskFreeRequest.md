# EfirDataHubModelsRequestsV2IndicatorRiskFreeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_date** | **datetime** | Дата, на которую возвращаются точки кривой. | 
**curve_code** | **str** | Код кривой. Возможные значения:  - MOEX.RUB.ZCYC - Кривая бескупонной доходности Мосбиржи в рублях;  - UST.USD.DYCR - Дневные ставки кривой доходности US Treasuries;  - ECB.EUR.ZCYC - Дневные ставки кривой доходности ЕЦБ;  - CCDC.CNY.ZCYC - Дневные ставки кривой бескупонной доходности КИТАЙ; | 
**num_decimals** | **int** | Число знаков после запятой, до которых необходимо округлять значения доходности (поле rate).  Возможные значения - от 0 до 6 включительно.  По умолчанию 4. | [optional] [default to 4]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

