# EfirDataHubModelsModelsRiskCapitalAdequacyFinalizedFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fintool_id** | **int** | Идентификатор финансового инструмента в БД Интерфакс | [optional] 
**isin** | **str** | Код финансового инструмента (ISIN) | [optional] 
**isin144a** | **str** | Дополнительный isin-код выпуска облигаций | [optional] 
**reg_code** | **str** | Регистрационный номер | [optional] 
**nrd_code** | **str** | Код НРД | [optional] 
**_date** | **datetime** | Дата расчета норматива | [optional] 
**reason** | **str** | Обоснование (номер и абзац пункта из нормативного акта, на основании которого определен коэффициент риска creditRiskRatio) | [optional] 
**code** | **str** | Код актива (инструмента) согласно нормативного акта | [optional] 
**rwa** | **str** | Агрегат RWA (Risk-Weighted Assets) | [optional] 
**is_pk** | **bool** | Флаг признака принадлежности актива (инструмента) к ПК- операции с повышенным коэффициентом риска | [optional] 
**credit_risk_ratio** | **float** | Коэффициент риска для взвешивания актива (инструмента) в RWA | [optional] 
**error** | **str** | Текст ошибки в случае возникновения | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

