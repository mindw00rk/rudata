# EfirDataHubModelsModelsBondCalculateBondFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_offer** | **bool** | Тип расчета: 1 – расчет к оферте; 0 – расчет к погашению. | [optional] 
**offer_id** | **int** | Номер оферты для которой производится расчет | [optional] 
**price_pct** | **float** | Чистая цена в % от номинала | [optional] 
**accrint_pct** | **float** | НКД в % от номинала | [optional] 
**fullprice_pct** | **float** | Полная цена в % от номинала | [optional] 
**facevalcur** | **str** | Валюта номинала | [optional] 
**price** | **float** | Чистая цена в валюте номинала | [optional] 
**accrint** | **float** | НКД в валюте номинала | [optional] 
**fullprice** | **float** | Полная цена в валюте номинала | [optional] 
**cfaceval** | **float** | Номинал | [optional] 
**_date** | **datetime** | Дата соответствующей оферты/погашения | [optional] 
**_yield** | **float** | Доходность по последней сделке, % | [optional] 
**dur** | **int** | Дюрация по Маколею, дней | [optional] 
**durmd** | **float** | Дюрация модифицированная, % | [optional] 
**convx** | **float** | Выпуклость | [optional] 
**pvbp** | **float** | PVBP | [optional] 
**cyield** | **float** | Доходность текущая по последней цене, % | [optional] 
**syield** | **float** | Доходность простая по последней цене, % | [optional] 
**accrint_at_date** | **float** | НКД на дату Efir.DataHub.Models.Models.Bond.CalculateBondFields.date | [optional] 
**faceval_at_date** | **float** | Остаточный номинал на дату Efir.DataHub.Models.Models.Bond.CalculateBondFields.date | [optional] 
**error** | **str** | Описание ошибок расчета | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

